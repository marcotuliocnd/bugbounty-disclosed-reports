# Invalid memory access in `mrb_str_format`

## Report Details
- **Report ID**: 191328
- **URL**: https://hackerone.com/reports/191328
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-12-15T07:52:31.565Z
- **Disclosed**: 2017-01-11T17:52:03.585Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Only affects `mruby` because `mruby-engine` doesn't have sprintf. I should have filed this last friday before I went to the pub, so missed out on higher bounties. Oh well!

Crash file is:

```
sprintf("%1$*c", 0)
```

Crash is:

```
$ lldb ./bin/mruby ../crash.rb
(lldb) target create "./bin/mruby"
Current executable set to './bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "../crash.rb"
(lldb) r
Process 69381 launched: './bin/mruby' (x86_64)
Process 69381 stopped
* thread #1: tid = 0x1d8935, 0x00007fff9969ec49 libsystem_platform.dylib`_platform_bzero$VARIANT$Haswell + 41, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x100700000)
    frame #0: 0x00007fff9969ec49 libsystem_platform.dylib`_platform_bzero$VARIANT$Haswell + 41
libsystem_platform.dylib`_platform_bzero$VARIANT$Haswell:
->  0x7fff9969ec49 <+41>: rep
    0x7fff9969ec4a <+42>: stosb  %al, %es:(%rdi)
    0x7fff9969ec4b <+43>: movq   %rdx, %rax
    0x7fff9969ec4e <+46>: popq   %rbp
(lldb) up
frame #1: 0x00007fff96fbfa6b libsystem_c.dylib`__memset_chk + 22
libsystem_c.dylib`__memset_chk:
    0x7fff96fbfa6b <+22>: movq   %rbx, %rax
    0x7fff96fbfa6e <+25>: addq   $0x8, %rsp
    0x7fff96fbfa72 <+29>: popq   %rbx
    0x7fff96fbfa73 <+30>: popq   %rbp
(lldb) up
frame #2: 0x000000010004a155 mruby`mrb_str_format(mrb=0x0000000100300390, argc=2, argv=0x000000010100f020, fmt=mrb_value @ 0x00007fff5fbfc800) + 11829 at sprintf.c:693
   690            FILL(' ', width-1);
   691          }
   692          else {
-> 693            FILL(' ', width-1);
   694            CHECK(n);
   695            memcpy(buf+blen, c, n);
   696            blen += n;
(lldb) p width
(mrb_int) $0 = 0
(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

Happens you have a positional width parameter passed to sprintf, with an argument of 0. 

A patch to fix is:

```
diff --git a/mrbgems/mruby-sprintf/src/sprintf.c b/mrbgems/mruby-sprintf/src/sprintf.c
index 696d093..8ed8b92 100644
--- a/mrbgems/mruby-sprintf/src/sprintf.c
+++ b/mrbgems/mruby-sprintf/src/sprintf.c
@@ -618,8 +618,8 @@ retry:
 
       case '*':
         CHECK_FOR_WIDTH(flags);
-        flags |= FWIDTH;
         GETASTER(width);
+        flags |= FWIDTH;
         if (width < 0) {
           flags |= FMINUS;
           width = -width;
```

Cheers,

Hugh

## Attachments
No attachments
