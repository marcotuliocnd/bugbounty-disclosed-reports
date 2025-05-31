# Information Disclosure Microsoft IIS Server service.cnf in a mtn website

## Report Details
- **Report ID**: 767066
- **URL**: https://hackerone.com/reports/767066
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-02T09:34:18.586Z
- **Disclosed**: 2020-04-03T11:58:12.770Z

## Reporter
- **Username**: miguel_santareno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hi there i found a information disclosure Microsoft IIS Server service.cnf file in the website https://www.mtn.co.za/ using firefox.

In the following steps i will demonstrate how to reproduce the vulnerability.

POC:
1ºGo to the following url:
https://www.mtn.co.za/_vti_pvt/service.cnf

you will see:
vti_encoding:SR|utf8-nl
vti_extenderversion:SR|15.0.0.5179

service.jpg

Remediation:
Remove the service.cnf file from the web server or restrict access to this file.

Example:
For more detailed information please check the References section first link.

References:
https://www.acunetix.com/vulnerabilities/web/vulnerability/microsoft-iis-server-service-cnf-file-found/
https://blogs.msdn.microsoft.com/fabdulwahab/2015/08/15/security-protecting-sharepoint-server-applications/

Best Regards Miguel Santareno

## Impact

Attackers can read /_vti_pvt/service.cnf and gather more information about the system

## Attachments
- service.png
