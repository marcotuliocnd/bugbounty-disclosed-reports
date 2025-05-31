# Uninitialized read in gdImageCreateFromXbm

## Report Details
- **Report ID**: 623588
- **URL**: https://hackerone.com/reports/623588
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-21T02:53:16.633Z
- **Disclosed**: 2020-10-10T02:16:30.335Z

## Reporter
- **Username**: chamal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This bug is present in gdImageCreateFromXbm method of ext/gd/libgd/gd_xbm.c file.
This method contains below mentioned lines.
```c
...
unsigned int b;
...
sscanf(h, "%x", &b);
		for (bit = 1; bit <= max_bit; bit = bit << 1) {
			gdImageSetPixel(im, x++, y, (b & bit) ? 1 : 0);
...
```

So when sscanf method is not able to read a hex value, "b" variable will contain uninitialized data.
Bug Report : https://bugs.php.net/bug.php?id=77973
PHP Version : 7.1.29
CVE-ID : [2019-11038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11038)

## Impact

Uninitialized data may leak data from stack memory.

## Attachments
No attachments
