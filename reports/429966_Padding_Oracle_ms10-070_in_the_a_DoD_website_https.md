# Padding Oracle ms10-070 in the a DoD website (https://██████/)

## Report Details
- **Report ID**: 429966
- **URL**: https://hackerone.com/reports/429966
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-28T15:20:54.764Z
- **Disclosed**: 2020-05-14T17:38:18.499Z

## Reporter
- **Username**: miguel_santareno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi there i found a Padding Oracle ms10-070 in the following website:
https://█████████/

In the following steps i will demonstrate how to reproduce the vulnerability.

POC:
1ºGo to the following url:
https://████/

you will see in the source code off the page something like "WebResource.axd?d="

webresource.jpg

2ºOpen the link and Copy the value from WebResource.axd?d= to &t=636681459604795562
██████████████

value.jpg

Next step i use a script that i found in this github that allows me to test if the application is vulnerable or not.
https://github.com/inquisb/miscellaneous/blob/master/ms10-070_check.py

clone the script to your machine and then copy the value and paste.
Output from the script:
./ms10-070 ████████████

padding.jpg

Example:
For more detailed information please check the References section first link.

Remediation and References:
https://docs.microsoft.com/en-us/security-updates/securitybulletins/2010/ms10-070
https://blogs.msdn.microsoft.com/fabdulwahab/2015/08/15/security-protecting-sharepoint-server-applications/

Best Regards Miguel Santareno

## Impact

Given control of data and a padding oracle, an attacker can wholly decrypt said data. This is possible without any knowledge of the key material.

## Attachments
No attachments
