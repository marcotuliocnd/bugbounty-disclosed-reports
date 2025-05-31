#  SharePoint Web Services Exposed to Anonymous Access

## Report Details
- **Report ID**: 920401
- **URL**: https://hackerone.com/reports/920401
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-10T03:54:27.682Z
- **Disclosed**: 2020-11-24T13:51:29.920Z

## Reporter
- **Username**: balisong
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
The SharePoint configuration for this particular site allows any user to access the spdisco.aspx on the web server which discloses the location of of all SharePoint's web service endpoints. The URLs are: 
██████████
███

## Impact

An adversary may utilize the exposed information about the web services to mount specific attacks against this SharePoint site. It may allow the attacker to communicate with the web service to further identify potential weaknesses and further compromise the system.

## Attachments
No attachments
