# Information Disclosure FrontPage Configuration Information

## Report Details
- **Report ID**: 2180018
- **URL**: https://hackerone.com/reports/2180018
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-09-25T17:08:26.117Z
- **Disclosed**: 2023-10-20T17:14:08.467Z

## Reporter
- **Username**: gu4rdianbyte
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi there i found a information disclosure Microsoft FrontPage configuration in the subdomain ██████████hat allows me to see version number and scripting paths off sharepoint using firefox.

POC:
Go to the following url:
https://███████/_vti_inf.html
and you will see the code

<!-- FrontPage Configuration Information 
FPVersion="16.00.0.000"
FPShtmlScriptUrl="_vti_bin/shtml.dll/_vti_rpc"
FPAuthorScriptUrl="_vti_bin/_vti_aut/author.dll"
FPAdminScriptUrl="_vti_bin/_vti_adm/admin.dll"
TPScriptUrl="_vti_bin/owssvr.dll"
-->
██████████

For more detailed information please check the References section first link.

## References
https://fortiguard.com/encyclopedia/ips/103284772
https://blogs.msdn.microsoft.com/fabdulwahab/2015/08/15/security-protecting-sharepoint-server-applications/

## Impact

Attackers can know the version and scripting paths information of Sharepoint FrontPage Configuration.

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Just follow the URL provided

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
