# Memory corrouption in mrb_gc_mark

## Report Details
- **Report ID**: 208363
- **URL**: https://hackerone.com/reports/208363
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-23T07:15:38.002Z
- **Disclosed**: 2017-04-17T02:42:13.361Z

## Reporter
- **Username**: minhrau
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The memory corruption in mrb_gc_mark function can lead to code execution or at least DoS on mruby.

PoC attached.

### Crash debug

>mr@minhrau ~ $ ./mrubylatest/mruby/build/bench/bin/mruby ./mruby/fuzz03/crashes/mrb_gc_mark.rb
>Reading symbols from ./mrubylatest/mruby/build/bench/bin/mruby...done.
>(gdb) r ./mruby/fuzz03/crashes/mrb_gc_mark.rb
>Starting program: /home/minhrau/mrubylatest/mruby/build/bench/bin/mruby ./mruby/fuzz03/crashes/mrb_gc_mark.rb
>{:r=>["h1MuXist", "kenea", "mini[g", "\377\377\365"]}
>
>---snip---
>
>Program received signal SIGSEGV, Segmentation fault.
>mrb_gc_mark (obj=0x4b563330305c3035, mrb=0x69f010) at /home/minhrau/mrubylatest/mruby/src/gc.c:696
>696   if (!is_white(obj)) return;
>(gdb) p obj
>$1 = (struct RBasic *) 0x4b563330305c3035
>(gdb) x/i $rip
>=> 0x4185fe <incremental_gc+78>:    movzbl 0x1(%rax),%edx
>(gdb) i r
>rax            0x4b563330305c3035   5428582682904506421
>rbx            0x7422a0 7611040
>rcx            0x0  0
>rdx            0xffffffffffffffff   -1
>rsi            0x69f0e8 6942952
>rdi            0x69f010 6942736
>rbp            0xffffffffffffffff   0xffffffffffffffff
>rsp            0x7fffffffdc90   0x7fffffffdc90
>r8             0x4  4
>r9             0x6b2660 7022176
>r10            0x6b2650 7022160
>r11            0x7ffff73ea760   140737341466464
>r12            0x69f010 6942736
>r13            0x69f0e8 6942952
>r14            0x0  0
>r15            0x69f010 6942736
>rip            0x4185fe 0x4185fe <incremental_gc+78>
>eflags         0x10206  [ PF IF RF ]
>cs             0x33 51
>ss             0x2b 43
>ds             0x0  0
>es             0x0  0
>fs             0x0  0
>gs             0x0  0
>(gdb) 

### Backtrace

>(gdb) bt
>   #0  mrb_gc_mark (obj=0x4b563330305c3035, mrb=0x69f010) at /home/minhrau/mrubylatest/mruby/src/gc.c:696
>   #1  gc_mark_children (gc=0x69f0e8, obj=<optimized out>, mrb=0x69f010) at /home/minhrau/mrubylatest/mruby/src/gc.c:600
>   #2  gc_gray_mark (obj=<optimized out>, gc=0x69f0e8, mrb=0x69f010) at /home/minhrau/mrubylatest/mruby/src/gc.c:887
>   #3  incremental_marking_phase (limit=<optimized out>, gc=<optimized out>, mrb=<optimized out>) at /home/minhrau/mrubylatest/mruby/src/gc.c:982
>   #4  incremental_gc (mrb=mrb@entry=0x69f010, gc=gc@entry=0x69f0e8, limit=limit@entry=18446744073709551615) at /home/minhrau/mrubylatest/mruby/src/gc.c:1086
>   #5  0x000000000041988a in incremental_gc (limit=18446744073709551615, gc=0x69f0e8, mrb=0x69f010) at /home/minhrau/mrubylatest/mruby/src/gc.c:1081
>   #6  incremental_gc_until (to_state=<optimized out>, gc=<optimized out>, mrb=<optimized out>) at /home/minhrau/mrubylatest/mruby/src/gc.c:1111
>   #7  mrb_incremental_gc (mrb=mrb@entry=0x69f010) at /home/minhrau/mrubylatest/mruby/src/gc.c:1162
>   #8  0x0000000000419dc0 in mrb_obj_alloc (mrb=mrb@entry=0x69f010, ttype=ttype@entry=MRB_TT_STRING, cls=0x6a94e0) at /home/minhrau/mrubylatest/mruby/src/gc.c:507
>   #9  0x0000000000424841 in str_new (p=0x0, len=0, mrb=0x69f010) at /home/minhrau/mrubylatest/mruby/src/string.c:59
>   #10 mrb_str_dup (mrb=mrb@entry=0x69f010, str=...) at /home/minhrau/mrubylatest/mruby/src/string.c:1069
>   #11 0x00000000004439c3 in mrb_vm_exec (mrb=mrb@entry=0x69f010, proc=<optimized out>, proc@entry=0x6e4fa0, pc=<optimized out>) at /home/minhrau/mrubylatest/mruby/src/vm.c:2317
>   #12 0x0000000000446e35 in mrb_vm_run (mrb=0x69f010, proc=0x6e4fa0, self=..., stack_keep=<optimized out>) at /home/minhrau/mrubylatest/mruby/src/vm.c:815
>   #13 0x0000000000449331 in mrb_top_run (mrb=mrb@entry=0x69f010, proc=proc@entry=0x6e4fa0, self=..., stack_keep=stack_keep@entry=0) at /home/minhrau/mrubylatest/mruby/src/vm.c:2569
>   #14 0x000000000043f87c in mrb_load_exec (mrb=mrb@entry=0x69f010, p=p@entry=0x6eb9c0, c=c@entry=0x6ea860) at /home/minhrau/mrubylatest/mruby/mrbgems/mruby-compiler/core/parse.y:5755
>   #15 0x00000000004415d5 in mrb_load_file_cxt (mrb=mrb@entry=0x69f010, f=0x6eb590, c=c@entry=0x6ea860) at /home/minhrau/mrubylatest/mruby/mrbgems/mruby-compiler/core/parse.y:5764
>   #16 0x00000000004020a5 in main (argc=<optimized out>, argv=<optimized out>) at /home/minhrau/mrubylatest/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232



## Attachments
- mrb_gc_mark.rb
