# Out-Of-Bounds Read in timelib_meridian()

## Report Details
- **Report ID**: 283644
- **URL**: https://hackerone.com/reports/283644
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-28T00:16:57.759Z
- **Disclosed**: 2019-10-14T04:38:08.877Z

## Reporter
- **Username**: xixabangm4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Description
While deserializing an invalid dateTime value, wddx_deserialize() would result in a heap out-of-bounds read in timelib_meridian(). As wddx_deserialize() is exposed to network data, and sometimes echo the results back to client, this issue could potentially allow remote peeking of the process memory. It should also affect other PHP APIs that make use of timelib_meridian().
This issue is similar to but is a separate issue of CVE-2017-11145, it is related to the "back of" and "front of" directives in the timelib format.

Details can be found at: https://bugs.php.net/bug.php?id=75055

Impact
Affects both PHP 5 before 5.6.32 (ChangeLog http://www.php.net/ChangeLog-5.php#5.6.32) and PHP 7 before 7.1.11 (ChangeLog http://www.php.net/ChangeLog-7.php#7.1.11).
Resolved PHP bug report, will update the pending CVE.



## Attachments
No attachments
