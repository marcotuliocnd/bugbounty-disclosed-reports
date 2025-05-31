# Website PHP source code returned in javascript

## Report Details
- **Report ID**: 1794462
- **URL**: https://hackerone.com/reports/1794462
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-06T04:51:12.654Z
- **Disclosed**: 2023-04-10T12:46:08.650Z

## Reporter
- **Username**: mdfarhanchowdhuryhasin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Source code disclosure:
----------------------------------



Summary:
--------------------

Severity             : Low
Confidence      : Tentative
Host                      : https://nextcloud.com
Path                       : /wp-content/themes/theme-package/dist/js/main.js


Issue detail:
------------------------------------
The application appears to disclose some server-side source code written in PHP.

Issue background:
---------------------------------------

Source code intended to be kept server-side can sometimes end up being disclosed to users. Such code may contain sensitive information such as database passwords and secret keys, which may help malicious users formulate attacks against the application.



Issue remediation:
---------------------------------

Server-side source code is normally disclosed to clients as a result of typographical errors in scripts or because of misconfiguration, such as failing to grant executable permissions to a script or directory. Review the cause of the code disclosure and prevent it from happening.


References:
--------------------------------------

Web Security Academy: Information disclosure

Vulnerability classifications:
------------------------------------------

    CWE-18: Source Code
    CWE-200: Information Exposure
    CWE-388: Error Handling
    CWE-540: Information Exposure Through Source Code
    CWE-541: Information Exposure Through Include Source Code
    CWE-615: Information Exposure Through Comments
    CAPEC-37: Retrieve Embedded Sensitive Data

## Impact

Source code intended to be kept server-side can sometimes end up being disclosed to users. Such code may contain sensitive information such as database passwords and secret keys, which may help malicious users formulate attacks against the application.

## Attachments
- Screenshot_2022-12-06_104011.png
- Screenshot_2022-12-06_104127.png
- Screenshot_2022-12-06_104213.png
- Screenshot_2022-12-06_104237.png
- Screenshot_2022-12-06_104303.png
