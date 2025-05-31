# Invalid memory write caused by incorrect upper bound in array_copy

## Report Details
- **Report ID**: 185899
- **URL**: https://hackerone.com/reports/185899
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-28T00:31:39.611Z
- **Disclosed**: 2016-12-18T13:23:23.939Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Ok, here is a weird one!

It only crashes in mruby, and can't be made to crash in mruby-engine as max memory possible to extend to is 256M which this requires more.

The file is:

```
values = [3,5,8]
test = [1,6]
results,= [1.2]
values.each do |value|
  case value
    when *test
      results << value
    when *test*= results <<=value
  end
end
```

```
$ ./dev/bin/mruby crash.rb
Segmentation fault: 11
```

```
$ lldb ./dev/bin/mruby crash.rb
(lldb) target create "./dev/bin/mruby"
Current executable set to './dev/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash.rb"
(lldb) r
Process 93838 launched: './dev/bin/mruby' (x86_64)
Process 93838 stopped
* thread #1: tid = 0x78effc5, 0x000000010000222d mruby`array_copy + 61, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x16f000000)
    frame #0: 0x000000010000222d mruby`array_copy + 61
mruby`array_copy:
->  0x10000222d <+61>: movq   %rdx, (%rax)
    0x100002230 <+64>: movq   0x8(%rcx), %rcx
    0x100002234 <+68>: movq   %rcx, 0x8(%rax)
    0x100002238 <+72>: movl   -0x18(%rbp), %eax
(lldb) bt
* thread #1: tid = 0x78effc5, 0x000000010000222d mruby`array_copy + 61, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x16f000000)
  * frame #0: 0x000000010000222d mruby`array_copy + 61
    frame #1: 0x0000000100004437 mruby`mrb_ary_times + 295
    frame #2: 0x000000010003fc13 mruby`mrb_vm_exec + 6739
    frame #3: 0x000000010003e1a7 mruby`mrb_vm_run + 135
    frame #4: 0x0000000100046604 mruby`mrb_top_run + 100
    frame #5: 0x0000000100071adf mruby`load_exec + 1183
    frame #6: 0x0000000100071623 mruby`mrb_load_file_cxt + 67
    frame #7: 0x00000001000017d8 mruby`main + 904
    frame #8: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb) register read
General Purpose Registers:
       rax = 0x000000016f000000
       rbx = 0x0000000000000000
       rcx = 0x000000010082a600
       rdx = 0x0000000000000001
       rdi = 0x000000016eff6800
       rsi = 0x0000000100820e00
       rbp = 0x00007fff5fbfc9d0
       rsp = 0x00007fff5fbfc9d0
        r8 = 0x0000000100110000
        r9 = 0x0000000000000003
       r10 = 0x0000000000000000
       r11 = 0x0000000000000246
       r12 = 0x0000000000000000
       r13 = 0x0000000000000000
       r14 = 0x0000000000000000
       r15 = 0x0000000000000000
       rip = 0x000000010000222d  mruby`array_copy + 61
    rflags = 0x0000000000010206
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000

(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

A lldb process that we have symbols compiled in:

```
$ lldb ./mruby/bin/mruby crash.rb
(lldb) target create "./mruby/bin/mruby"
Current executable set to './mruby/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash.rb"
(lldb) r
Process 30719 launched: './mruby/bin/mruby' (x86_64)
Process 30719 stopped
* thread #1: tid = 0x78f948b, 0x0000000100001c5d mruby`array_copy(dst=0x000000016e7f6800, src=0x0000000101825c00, size=5184) + 61 at array.c:74, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x16e800000)
    frame #0: 0x0000000100001c5d mruby`array_copy(dst=0x000000016e7f6800, src=0x0000000101825c00, size=5184) + 61 at array.c:74
   71     mrb_int i;
   72
   73     for (i = 0; i < size; i++) {
-> 74       dst[i] = src[i];
   75     }
   76   }
   77
(lldb) up
frame #1: 0x0000000100003e67 mruby`mrb_ary_times(mrb=0x0000000100300390, self=mrb_value @ 0x00007fff5fbfca10) + 295 at array.c:350
   347    a2 = ary_new_capa(mrb, a1->len * times);
   348    ptr = a2->ptr;
   349    while (times--) {
-> 350      array_copy(ptr, a1->ptr, a1->len);
   351      ptr += a1->len;
   352      a2->len += a1->len;
   353    }
(lldb) p times
(mrb_int) $0 = 51781
(lldb) bt
* thread #1: tid = 0x78f948b, 0x0000000100001c5d mruby`array_copy(dst=0x000000016e7f6800, src=0x0000000101825c00, size=5184) + 61 at array.c:74, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x16e800000)
    frame #0: 0x0000000100001c5d mruby`array_copy(dst=0x000000016e7f6800, src=0x0000000101825c00, size=5184) + 61 at array.c:74
  * frame #1: 0x0000000100003e67 mruby`mrb_ary_times(mrb=0x0000000100300390, self=mrb_value @ 0x00007fff5fbfca10) + 295 at array.c:350
    frame #2: 0x000000010003f643 mruby`mrb_vm_exec(mrb=0x0000000100300390, proc=0x0000000101004df0, pc=0x000000010060f530) + 6739 at vm.c:1165
    frame #3: 0x000000010003dbd7 mruby`mrb_vm_run(mrb=0x0000000100300390, proc=0x0000000101004e80, self=mrb_value @ 0x00007fff5fbfd6b0, stack_keep=0) + 135 at vm.c:766
    frame #4: 0x0000000100046034 mruby`mrb_top_run(mrb=0x0000000100300390, proc=0x0000000101004e80, self=mrb_value @ 0x00007fff5fbfd720, stack_keep=0) + 100 at vm.c:2458
    frame #5: 0x000000010007150f mruby`load_exec(mrb=0x0000000100300390, p=0x0000000101811420, c=0x000000010060ed90) + 1183 at parse.y:5747
    frame #6: 0x0000000100071053 mruby`mrb_load_file_cxt(mrb=0x0000000100300390, f=0x00007fff7cda6050, c=0x000000010060ed90) + 67 at parse.y:5756
    frame #7: 0x0000000100001208 mruby`main(argc=2, argv=0x00007fff5fbfdb40) + 904 at mruby.c:226
    frame #8: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

So this is showing that we are trying to write to `0x16e800000`, which is within the bounds of the allocation. I added the following patch temporarily to further debug:

```
diff --git a/src/array.c b/src/array.c
index 106353c..a880c61 100644
--- a/src/array.c
+++ b/src/array.c
@@ -346,6 +346,7 @@ mrb_ary_times(mrb_state *mrb, mrb_value self)
   }
   a2 = ary_new_capa(mrb, a1->len * times);
   ptr = a2->ptr;
+  printf("ptr = %p, ptr + len*times = %p\n", ptr, ptr + a1->len * times);
   while (times--) {
     array_copy(ptr, a1->ptr, a1->len);
     ptr += a1->len;

```

which gives the output of `ptr = 0x106aee000, ptr + len*times = 0x2732ee000` just before the segfault, which clearly shows that the allocation includes the address it is failing on.

So here is where I get lost, as I was confused why realloc didn't fail when it couldn't allocate the memory... BUT I figured out what was wrong. When checking possible size, we are using the `ARY_MAX_SIZE` macro, which is set to either `SIZE_MAX / sizeof(mrb_value)` or `MRB_INT_MAX`, whichever is smallest. Now you can see here that one divides by the size of `mrb_value`, and one doesn't. On my system (64bit), the MRB_INT_MAX is smaller, so it is using that. I suggest the following patch to fix this, by dividing that by the size of `mrb_value` as well. 

```
diff --git a/src/array.c b/src/array.c
index 106353c..ed2b346 100644
--- a/src/array.c
+++ b/src/array.c
@@ -14,7 +14,8 @@
 #define ARY_DEFAULT_LEN   4
 #define ARY_SHRINK_RATIO  5 /* must be larger than 2 */
 #define ARY_C_MAX_SIZE (SIZE_MAX / sizeof(mrb_value))
-#define ARY_MAX_SIZE ((ARY_C_MAX_SIZE < (size_t)MRB_INT_MAX) ? (mrb_int)ARY_C_MAX_SIZE : MRB_INT_MAX-1)
+#define ARY_INT_MAX_SIZE ((size_t)MRB_INT_MAX / sizeof(mrb_value))
+#define ARY_MAX_SIZE ((ARY_C_MAX_SIZE < ARY_INT_MAX_SIZE) ? (mrb_int)ARY_C_MAX_SIZE : (mrb_int)ARY_INT_MAX_SIZE)
 
 static struct RArray*
 ary_new_capa(mrb_state *mrb, mrb_int capa)
```

Applying this patch no longer crashes, and instead complains that the array size is too big.

```
trace:
        [0] crash.rb:8:in Object.call
        [1] /Users/<snip>/mruby-engine/mruby/mrblib/array.rb:17:in Array.each
        [2] crash.rb:4
crash.rb:8: array size too big (ArgumentError)
```

Cheers,

Hugh

## Attachments
No attachments
