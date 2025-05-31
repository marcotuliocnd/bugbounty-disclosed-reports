# imagecropauto out-of-bounds access

## Report Details
- **Report ID**: 178144
- **URL**: https://hackerone.com/reports/178144
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-26T02:40:46.968Z
- **Disclosed**: 2019-10-13T18:21:47.487Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information

Upstream Bug
---
https://bugs.php.net/bug.php?id=72494


Summary
---
imagecropauto on IMG_CROP_THRESHOLD mode causes arbitrary read access and possible leak of information. The function imagecropauto doesn't check valid colors for non-truecolor images. This causes that gdImageRed/Green/Blue/Alpha macros read beyond that 255 allowed values, when it troes match colors inside the gdColorMatch function.

Details
---
color is only checked to be positive:

```
https://github.com/php/php-src/blob/master/ext/gd/gd.c#L4591


PHP_FUNCTION(imagecropauto)
{
...
		case GD_CROP_THRESHOLD:
			if (color < 0) {
				php_error_docref(NULL, E_WARNING, "Color argument missing with threshold mode");
				RETURN_FALSE;
			}
			im_crop = gdImageCropThreshold(im, color, (float) threshold);
			break;
...
```

color is passed to gdColorMatch:

```
https://github.com/php/php-src/blob/master/ext/gd/libgd/gd_crop.c#L227

gdImagePtr gdImageCropThreshold(gdImagePtr im, const unsigned int color, const float threshold)
{
...
	match = 1;
	for (y = 0; match && y < height; y++) {
		for (x = 0; match && x < width; x++) {
			match = (gdColorMatch(im, color, gdImageGetPixel(im, x,y), threshold)) > 0;
		}
	}
...
```

col1 (color) is now used with the gdImageRed/gdImageGreen/gdImageBlue/gdImageAlpha macros.


```
https://github.com/php/php-src/blob/master/ext/gd/libgd/gd_crop.c#L344

static int gdColorMatch(gdImagePtr im, int col1, int col2, float threshold)
{
	const int dr = gdImageRed(im, col1) - gdImageRed(im, col2);
	const int dg = gdImageGreen(im, col1) - gdImageGreen(im, col2);
	const int db = gdImageBlue(im, col1) - gdImageBlue(im, col2);
	const int da = gdImageAlpha(im, col1) - gdImageAlpha(im, col2);
	const double dist = sqrt(dr * dr + dg * dg + db * db + da * da);
	const double dist_perc = sqrt(dist / (255^2 + 255^2 + 255^2));
	return (dist_perc <= threshold);
	//return (100.0 * dist / 195075) < threshold;
}
```

In these macros it is used as an index (c) for the red/green/blue/alpha arrays, we are able to read beyond the 255 items on these arrays.

```
https://github.com/php/php-src/blob/master/ext/gd/libgd/gd.h#L730

#define gdImageColorsTotal(im) ((im)->colorsTotal)
#define gdImageRed(im, c) ((im)->trueColor ? gdTrueColorGetRed(c) : \
	(im)->red[(c)])
#define gdImageGreen(im, c) ((im)->trueColor ? gdTrueColorGetGreen(c) : \
	(im)->green[(c)])
#define gdImageBlue(im, c) ((im)->trueColor ? gdTrueColorGetBlue(c) : \
	(im)->blue[(c)])
#define gdImageAlpha(im, c) ((im)->trueColor ? gdTrueColorGetAlpha(c) : \
	(im)->alpha[(c)])
```

GDB output:
```
 gdb -q --args /home/user/php/php-70/sapi/cli/php -n poc.php
No symbol table is loaded.  Use the "file" command.
Breakpoint 1 (__asan_report_error) pending.
Reading symbols from /home/user/php/php-70/sapi/cli/php...done.
gdb-peda$ b gd_crop.c:350
Breakpoint 2 at 0x8190002: file /home/user/php/php-70/ext/gd/libgd/gd_crop.c, line 350.
gdb-peda$ r
Starting program: /home/user/php/php-70/sapi/cli/php -n poc.php
[----------------------------------registers-----------------------------------]
EAX: 0x0
EBX: 0x8b47000 --> 0x8b46db8 --> 0x1
ECX: 0x60c
EDX: 0x0
ESI: 0xf5a14020 --> 0xf5a7a118 --> 0x84b92de (<ZEND_DO_ICALL_SPEC_HANDLER>:     push   ebp)
EDI: 0xf5a7a118 --> 0x84b92de (<ZEND_DO_ICALL_SPEC_HANDLER>:    push   ebp)
EBP: 0xffff9f18 --> 0xffff9f78 --> 0xffff9fd8 --> 0xffffa008 --> 0xffffa028 --> 0xffffa068 (--> ...)
ESP: 0xffff9ee0 --> 0x4
EIP: 0x8190002 (<gdColorMatch+366>:     mov    eax,DWORD PTR [ebp-0x28])
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x818fffb <gdColorMatch+359>:        sub    edx,eax
   0x818fffd <gdColorMatch+361>:        mov    eax,edx
   0x818ffff <gdColorMatch+363>:        mov    DWORD PTR [ebp-0x1c],eax
=> 0x8190002 <gdColorMatch+366>:        mov    eax,DWORD PTR [ebp-0x28]
   0x8190005 <gdColorMatch+369>:        imul   eax,DWORD PTR [ebp-0x28]
   0x8190009 <gdColorMatch+373>:        mov    edx,eax
   0x819000b <gdColorMatch+375>:        mov    eax,DWORD PTR [ebp-0x24]
   0x819000e <gdColorMatch+378>:        imul   eax,DWORD PTR [ebp-0x24]
[------------------------------------stack-------------------------------------]
0000| 0xffff9ee0 --> 0x4
0004| 0xffff9ee4 --> 0x1
0008| 0xffff9ee8 --> 0x4
0012| 0xffff9eec --> 0x0
0016| 0xffff9ef0 --> 0x0
0020| 0xffff9ef4 --> 0x0
0024| 0xffff9ef8 --> 0x0
0028| 0xffff9efc --> 0x0
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, gdColorMatch (im=0xf5a6c000, col1=0x539, col2=0x0, threshold=0) at /home/user/php/php-70/ext/gd/libgd/gd_crop.c:350
350             const double dist = sqrt(dr * dr + dg * dg + db * db + da * da);
gdb-peda$ p/d col1
$1 = 1337
gdb-peda$ p &im->red
$4 = (int (*)[256]) 0xf5a6c010  ## im->red bottom limit

gdb-peda$ p &im->red[255]
$6 = (int *) 0xf5a6c40c         ## im->red top limit
       
gdb-peda$ p &im->red[col1]
$3 = (int *) 0xf5a6d4f4         ## Out of bounds

```

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=1d69028d2f15216d128b5a6e606f763ef09d4991
```

Fixed for PHP 5.6.25, PHP 7.0.10
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php#7.0.10


## Attachments
No attachments
