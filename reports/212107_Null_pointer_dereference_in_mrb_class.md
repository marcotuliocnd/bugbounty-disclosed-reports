# Null pointer dereference in mrb_class

## Report Details
- **Report ID**: 212107
- **URL**: https://hackerone.com/reports/212107
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-10T00:58:59.157Z
- **Disclosed**: 2017-03-14T21:12:28.984Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The following code demonstrates a segfault in mruby and mruby-engine:

    module A module A
    ensure
        module A module A module A module A
        ensure
            module A module A module A module A module A module A
               a 
            ensure
                module A
                    yield
                end
            end end end end end end
        end end end end
    end end

The mruby crash is due to a null pointer dereference in `mrb_class` (class.h:50):

    49│   default:
    50├>    return mrb_obj_ptr(v)->c;
    51│   }

(gdb) print mrb_obj_ptr(v)
$1 = (struct RObject *) 0x0
(gdb) print v
$2 = {value = {f = 0, p = 0x0, i = 0, sym = 0}, tt = 49}

The sandbox crash happens during a call to KHASH_DEFINE (class.c:19). Examining the assembly suggests the crash happens when trying to dereference the rsi register:

(gdb) x/i $rip
=> 0x7ffff402f490 <kh_get_mt>:  mov    eax,DWORD PTR [rsi]
(gdb) p $rsi
$4 = 32

Examining mruby with Valgrind shows two invalid reads on the following line (vm.c:1867):

    if (mrb_nil_p(stack[m1+r+m2])) {
    
Valgrind output:

    ==11371== Invalid read of size 4
    ==11371==    at 0x41FCEB: mrb_vm_exec (vm.c:1867)
    ==11371==    by 0x41B684: mrb_vm_run (vm.c:822)
    ==11371==    by 0x42386C: mrb_run (vm.c:2570)
    ==11371==    by 0x419D40: ecall (vm.c:314)
    ==11371==    by 0x41EEF2: mrb_vm_exec (vm.c:1651)
    ==11371==    by 0x41B684: mrb_vm_run (vm.c:822)
    ==11371==    by 0x42386C: mrb_run (vm.c:2570)
    ==11371==    by 0x419D40: ecall (vm.c:314)
    ==11371==    by 0x41CAD1: mrb_vm_exec (vm.c:1132)
    ==11371==    by 0x41B684: mrb_vm_run (vm.c:822)
    ==11371==    by 0x42386C: mrb_run (vm.c:2570)
    ==11371==    by 0x419D40: ecall (vm.c:314)
    ==11371==  Address 0x56271f8 is 8 bytes after a block of size 16 alloc'd
    ==11371==    at 0x4C2AB80: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    ==11371==    by 0x4C2CF1F: realloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    ==11371==    by 0x40F300: mrb_default_allocf (state.c:60)
    ==11371==    by 0x428156: mrb_realloc_simple (gc.c:201)
    ==11371==    by 0x4281D8: mrb_realloc (gc.c:215)
    ==11371==    by 0x4282A4: mrb_malloc (gc.c:236)
    ==11371==    by 0x419A8A: mrb_env_unshare (vm.c:259)
    ==11371==    by 0x419B33: cipop (vm.c:278)
    ==11371==    by 0x41ED8E: mrb_vm_exec (vm.c:1624)
    ==11371==    by 0x41B684: mrb_vm_run (vm.c:822)
    ==11371==    by 0x42386C: mrb_run (vm.c:2570)
    ==11371==    by 0x419D40: ecall (vm.c:314)
    ==11371== 
    ==11371== Invalid read of size 4
    ==11371==    at 0x41FD1B: mrb_vm_exec (vm.c:1867)
    ==11371==    by 0x41B684: mrb_vm_run (vm.c:822)
    ==11371==    by 0x42386C: mrb_run (vm.c:2570)
    ==11371==    by 0x419D40: ecall (vm.c:314)
    ==11371==    by 0x41EEF2: mrb_vm_exec (vm.c:1651)
    ==11371==    by 0x41B684: mrb_vm_run (vm.c:822)
    ==11371==    by 0x42386C: mrb_run (vm.c:2570)
    ==11371==    by 0x419D40: ecall (vm.c:314)
    ==11371==    by 0x41CAD1: mrb_vm_exec (vm.c:1132)
    ==11371==    by 0x41B684: mrb_vm_run (vm.c:822)
    ==11371==    by 0x42386C: mrb_run (vm.c:2570)
    ==11371==    by 0x419D40: ecall (vm.c:314)
    ==11371==  Address 0x56271f0 is 0 bytes after a block of size 16 alloc'd
    ==11371==    at 0x4C2AB80: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    ==11371==    by 0x4C2CF1F: realloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    ==11371==    by 0x40F300: mrb_default_allocf (state.c:60)
    ==11371==    by 0x428156: mrb_realloc_simple (gc.c:201)
    ==11371==    by 0x4281D8: mrb_realloc (gc.c:215)
    ==11371==    by 0x4282A4: mrb_malloc (gc.c:236)
    ==11371==    by 0x419A8A: mrb_env_unshare (vm.c:259)
    ==11371==    by 0x419B33: cipop (vm.c:278)
    ==11371==    by 0x41ED8E: mrb_vm_exec (vm.c:1624)
    ==11371==    by 0x41B684: mrb_vm_run (vm.c:822)
    ==11371==    by 0x42386C: mrb_run (vm.c:2570)
    ==11371==    by 0x419D40: ecall (vm.c:314)
    ==11371== 
    trace:
	    [15] crash_input:9
	    [14] crash_input:8
	    [12] crash_input:5
	    [11] crash_input:5
	    [10] crash_input:5
	    [9] crash_input:5
	    [8] crash_input:5
	    [6] crash_input:3
	    [5] crash_input:3
	    [4] crash_input:3
	    [3] crash_input:3
	    [1] crash_input:1
	    [0] crash_input:1
    LocalJumpError: unexpected yield
    ==11371== 
    ==11371== HEAP SUMMARY:
    ==11371==     in use at exit: 0 bytes in 0 blocks
    ==11371==   total heap usage: 4,735 allocs, 4,735 frees, 872,977 bytes allocated
    ==11371== 
    ==11371== All heap blocks were freed -- no leaks are possible
    ==11371== 
    ==11371== For counts of detected and suppressed errors, rerun with: -v
    ==11371== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 0 from 0)

    
As `m1`, `r` and `m2` are all 0 during the invalid reads, it seems `stack` is pointing beyond allocated memory. Note that running with Valgrind appears to change the behaviour of the program: it does not result in a segfault, raising a LocalJumpError instead.

We are still examining the bug and hope to provide a fix soon.

Test platform:
Linux Mint 17.3 (Cinnamon 64-bit), built with gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3)

mruby-engine SHA: 09be20e67888b20bebf9b0588bc3cbec7f55325f
mruby/mruby submodule SHA: 63dbed00946afda34178a479cfa38fa78d620a00

Thank you,
Dinko Galetic
Denis Kasak



## Attachments
No attachments
