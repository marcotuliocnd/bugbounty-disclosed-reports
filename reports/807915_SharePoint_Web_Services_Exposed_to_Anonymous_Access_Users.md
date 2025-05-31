#  SharePoint Web Services Exposed to Anonymous Access Users

## Report Details
- **Report ID**: 807915
- **URL**: https://hackerone.com/reports/807915
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-01T02:24:56.186Z
- **Disclosed**: 2020-07-14T17:17:58.499Z

## Reporter
- **Username**: balisong
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Any unauthenticated/anonymous users are able to access the SharePoint Web Services (.wsdl files) for the █████ Initiative website.

**Description:**
The SharePoint installation for this particular site allows any user to access the spdisco.aspx on the web server which discloses the location of of all SharePoint's web service endpoints. The URL is: https://█████/██████/_vti_bin/spdisco.aspx

## Impact
An adversary may utilize the exposed information about the web services to mount specific attacks against this SharePoint site. It may allow the attacker to communicate with the web service to further identify potential weaknesses and further compromise the system.

## Step-by-step Reproduction Instructions

1. Navigate to https://███████/██████████/_vti_bin/spdisco.aspx

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions
Disable anonymous access to spdisco.aspx

## Impact

An adversary may utilize the exposed information about the web services to mount specific attacks against this SharePoint site. It may allow the attacker to communicate with the web service to further identify potential weaknesses and further compromise the system.

## Attachments
No attachments
