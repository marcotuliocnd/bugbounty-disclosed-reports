# Use after free with assign by ref to overloaded objects

## Report Details
- **Report ID**: 123119
- **URL**: https://hackerone.com/reports/123119
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-15T00:11:58.915Z
- **Disclosed**: 2019-10-04T16:03:39.688Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Reported: 2015-07-15 16:30 UTC
Fixed: 2015-07-21 14:20 UTC

Bug Report:
https://bugs.php.net/bug.php?id=70083

Fixed in PHP 5.6:
http://git.php.net/?p=php-src.git;a=commitdiff;h=f57cb13c566613eec0e1c2f6d96d18565436a9b7

Fixed in 7:
http://git.php.net/?p=php-src.git;a=commit;h=0af07333520f65def3a72f31effa38c907e962f9

This bug may also affect PHP 5.0.4, 5.0.5, 5.1.0-5.1.6, 5.4.0-5.5.26 (based on 3v4l.org responses), triggered by this unminimized test case which wasn't included in the original bug report:

```
<?php

class wpq {
    private $unrenced;

    public function __get($name) {
        return $this;
    }
}
 function ret_assoc() {
    return array('Roo' => 'bar');
}

$wpq = new wpq;
$wpq->interesting =& ret_assoc();
$x +@$wpq->interesting;
printf("%s\n", $x);
```

## Attachments
No attachments
