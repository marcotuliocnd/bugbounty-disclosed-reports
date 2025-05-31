# Information Disclosure FrontPage Configuration Information /_vti_inf.html in https://www.mtn.co.za/

## Report Details
- **Report ID**: 761617
- **URL**: https://hackerone.com/reports/761617
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-19T11:03:44.896Z
- **Disclosed**: 2020-04-03T11:57:50.369Z

## Reporter
- **Username**: miguel_santareno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hi there i found a information disclosure Microsoft FrontPage configuration in the subdomain https://www.mtn.co.za/ that allows me to see version number and scripting paths off sharepoint using firefox.

POC:
Go to the following url:
https://www.mtn.co.za/_vti_inf.html and you will see a blank page.

blank.jpg

Then just go to view-source:https://www.mtn.co.za/_vti_inf.html all you will be able to see the FrontPage Configuration Information:

<!-- FrontPage Configuration Information 
FPVersion="15.00.0.000"
FPShtmlScriptUrl="_vti_bin/shtml.dll/_vti_rpc"
FPAuthorScriptUrl="_vti_bin/_vti_aut/author.dll"
FPAdminScriptUrl="_vti_bin/_vti_adm/admin.dll"
TPScriptUrl="_vti_bin/owssvr.dll"
-->


sharepoint.jpg

Remediation:
Remove the /_vti_inf.html file from the web server or restrict access to this file.

Example:
For more detailed information please check the References section first link.

References:
https://fortiguard.com/encyclopedia/ips/103284772
https://blogs.msdn.microsoft.com/fabdulwahab/2015/08/15/security-protecting-sharepoint-server-applications/

Best Regards Miguel Santareno

## Impact

Attackers can know the version and scripting paths information of Sharepoint FrontPage Configuration.

## Attachments
- blank.png
- sharepoint.png
