# kh_put_iv SEGFAULT - mruby 1.2.0

## Report Details
- **Report ID**: 217610
- **URL**: https://hackerone.com/reports/217610
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-01T07:14:38.590Z
- **Disclosed**: 2017-04-13T22:45:37.586Z

## Reporter
- **Username**: ilsani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
mruby v. 1.2.0 crashes in `kh_put_iv` function in `variable.c` file with a crafted input. I'm examining the bug in order to better understand the root cause of the issue.

Test platform:
Linux 4.2.0-1 SMP Debian 4.2.3-2 x86_64

Stacktrace:
```
Program terminated with signal SIGSEGV, Segmentation fault.
#0  0x000000000045329c in kh_put_iv (mrb=0x2744c10, h=0x2f2f3a7370747468, key=671, ret=0x0)
    at /home/msani/wrk/security/code-review/shopify/mruby/src/mruby/src/variable.c:292
292     KHASH_DEFINE(iv, mrb_sym, mrb_value, TRUE, kh_int_hash_func, kh_int_hash_equal)
(gdb) backtrace 
#0  0x000000000045329c in kh_put_iv (mrb=0x2744c10, h=0x2f2f3a7370747468, key=671, ret=0x0)
    at /home/msani/wrk/security/code-review/shopify/mruby/src/mruby/src/variable.c:292
#1  0x0000000000459117 in iv_put (mrb=0x2744c10, t=0x2f2f3a7370747468, sym=671, val=...)
    at /home/msani/wrk/security/code-review/shopify/mruby/src/mruby/src/variable.c:310
#2  mrb_mod_cv_set (mrb=<optimized out>, c=<optimized out>, sym=<optimized out>, v=...)
    at /home/msani/wrk/security/code-review/shopify/mruby/src/mruby/src/variable.c:838
#3  0x000000000050e1e1 in mrb_vm_exec (mrb=<optimized out>, proc=<optimized out>, pc=<optimized out>)
    at /home/msani/wrk/security/code-review/shopify/mruby/src/mruby/src/vm.c:979
#4  0x000000000051f5bb in mrb_vm_run (proc=0x2746ef0, self=..., stack_keep=8, mrb=<optimized out>)
    at /home/msani/wrk/security/code-review/shopify/mruby/src/mruby/src/vm.c:823
#5  mrb_top_run (mrb=0x2744c10, proc=0x2746ef0, self=..., stack_keep=<optimized out>)
    at /home/msani/wrk/security/code-review/shopify/mruby/src/mruby/src/vm.c:2614
#6  0x00000000004d4f93 in mrb_load_exec (mrb=0x2744c10, p=<optimized out>, c=0x0)
    at /home/msani/wrk/security/code-review/shopify/mruby/src/mruby/mrbgems/mruby-compiler/core/parse.y:5760
#7  0x0000000000400c85 in main () at runtest.c:23
(gdb) exploitable 
__main__:99: UserWarning: GDB v7.11 may not support required Python API
Description: Possible stack corruption
Short description: PossibleStackCorruption (7/22)
Hash: 5696db2f9fc8b1e9b330173ee7ddc787.2627e5d3f14472e2e24f2d46a9038356
Exploitability Classification: EXPLOITABLE
Explanation: GDB generated an error while unwinding the stack and/or the stack contained return addresses that were not mapped in the inferior's process address space and/or the stack pointer is pointing to a location outside the default stack region. These conditions likely indicate stack corruption, which is generally considered exploitable.
Other tags: AccessViolation (21/22)

```

Attachment [1] is the crafted input.

## Attachments
- input.txt
