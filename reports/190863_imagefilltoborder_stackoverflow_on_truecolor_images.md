# imagefilltoborder stackoverflow on truecolor images

## Report Details
- **Report ID**: 190863
- **URL**: https://hackerone.com/reports/190863
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-13T16:26:04.962Z
- **Disclosed**: 2017-02-07T17:56:30.880Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
https://bugs.php.net/bug.php?id=72696

Summary
--
Invalid color causes stack exhaustion by recursive call to function gdImageFillToBorder when the image used is truecolor. This was tested on a 64 bits platform.

GDB debugging
--
```
gdb -q --args /home/operac/php-70-sinasan/sapi/cli/php -n poc.php
Reading symbols from /home/operac/php-70-sinasan/sapi/cli/php...done.
(gdb) b gd.c:1851
Breakpoint 1 at 0x54a354: gd.c:1851. (2 locations)
(gdb) b gd.c:1834
Breakpoint 2 at 0x54a287: gd.c:1834. (2 locations)
(gdb) r
Starting program: /home/operac/php-70-sinasan/sapi/cli/php -n poc.php

Breakpoint 1, php_gd_gdImageFillToBorder (im=0x7ffff2c77000, x=0, y=0, border=1, color=-2) at /home/operac/php-70-sinasan/ext/gd/libgd/gd.c:1851
1851                                            gdImageFillToBorder(im, i, y + 1, border, color);
(gdb) c
Continuing.

Breakpoint 2, php_gd_gdImageFillToBorder (im=0x7ffff2c77000, x=0, y=1, border=1, color=-2) at /home/operac/php-70-sinasan/ext/gd/libgd/gd.c:1834
1834                                            gdImageFillToBorder(im, i, y - 1, border, color);
(gdb) c
Continuing.

Breakpoint 1, php_gd_gdImageFillToBorder (im=0x7ffff2c77000, x=0, y=0, border=1, color=-2) at /home/operac/php-70-sinasan/ext/gd/libgd/gd.c:1851
1851                                            gdImageFillToBorder(im, i, y + 1, border, color);
(gdb) c
Continuing.

Breakpoint 2, php_gd_gdImageFillToBorder (im=0x7ffff2c77000, x=0, y=1, border=1, color=-2) at /home/operac/php-70-sinasan/ext/gd/libgd/gd.c:1834
1834                                            gdImageFillToBorder(im, i, y - 1, border, color);
(gdb) p/x color
$1 = 0xfffffffe

```

Patch
--
```
https://github.com/php/php-src/commit/863d37ea66d5c960db08d6f4a2cbd2518f0f80d1
```

Fixed for PHP 5.6.28
--

## Attachments
No attachments
