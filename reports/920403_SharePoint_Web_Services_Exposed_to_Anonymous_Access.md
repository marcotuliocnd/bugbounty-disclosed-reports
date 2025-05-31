#  SharePoint Web Services Exposed to Anonymous Access

## Report Details
- **Report ID**: 920403
- **URL**: https://hackerone.com/reports/920403
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-10T04:04:55.473Z
- **Disclosed**: 2020-11-24T13:52:18.982Z

## Reporter
- **Username**: balisong
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Summary:
Any unauthenticated/anonymous users are able to access the SharePoint Web Services (.wsdl files) for the ██████████ website.

Description:
The SharePoint installation for this particular site allows any user to access the spdisco.aspx on the web server which discloses the location of of all SharePoint's web service endpoints. The URLs are: 
█████████
█████
████████
██████████
████

Suggested Mitigation/Remediation Actions:
Disable anonymous access to spdisco.aspx

## Impact

An adversary may utilize the exposed information about the web services to mount specific attacks against this SharePoint site. It may allow the attacker to communicate with the web service to further identify potential weaknesses and further compromise the system.

## Attachments
No attachments
