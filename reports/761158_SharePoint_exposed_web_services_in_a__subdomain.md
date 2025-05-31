# SharePoint exposed web services in a  subdomain

## Report Details
- **Report ID**: 761158
- **URL**: https://hackerone.com/reports/761158
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-18T17:46:39.674Z
- **Disclosed**: 2020-05-16T13:06:35.089Z

## Reporter
- **Username**: miguel_santareno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hi there
I found a subdomain that is sharepoint configuration is poorly implemented
Because of improper configuration an anonymous user can access to the SharePoint Web Services.

POC:
Go to the following url:
https://www.mtn.co.za/_vti_bin/lists.asmx?WSDL

services.jpg

Remediation
Restrict access to this page.

References:
https://www.acunetix.com/vulnerabilities/web/vulnerability/sharepoint-exposed-web-services/
https://blogs.msdn.microsoft.com/fabdulwahab/2015/08/15/security-protecting-sharepoint-server-applications/

Best Regards Miguel Santareno

## Impact

Attackers can know the full structure off the application.

## Attachments
- services.png
