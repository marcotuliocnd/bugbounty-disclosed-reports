# Illegal write/read access caused by gdImageAALine overflow

## Report Details
- **Report ID**: 182420
- **URL**: https://hackerone.com/reports/182420
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-16T02:24:22.263Z
- **Disclosed**: 2019-10-31T06:16:01.317Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
https://bugs.php.net/bug.php?id=72482

Summary
---
Ilegal write/read access at gdImageSetAAPixelColor caused by gdImageAALine overflow.
gdImageAALine tries to clip the limit values and fails because an integer overflow occurs while calculating the new line limits.

PHP 5 is affected, but my debugging is done on PHP 7.

One of the integer overflows happens here:

1314   x2 -= ((im->sy - y2) * (x1 - x2)) / (y2 - y1);
gdb-peda$ p ((im->sy - y2) * (x1 - x2)) / (y2 - y1)   ## (a * b) / c  fails
$8 = 0x0
gdb-peda$ p (im->sy - y2) * ((x1 - x2) / (y2 - y1))   ## a * (b / c)   works
$9 = 0x40000c10

The illegal write access happens while trying to set this pixels to draw the line in gdImageSetAAPixelColor:

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=b25009fc2c97c6b5a93b3fc5f6a5b221b62f1273
https://gist.github.com/anonymous/873314feb4f89bd8336711333299f748
```

Fixed for PHP 5.6.28, PHP 7.0.13
--
http://php.net/ChangeLog-5.php#5.6.28
http://php.net/ChangeLog-7.php#7.0.13

## Attachments
No attachments
