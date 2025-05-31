# Reflected XSS on https://█████████html?url

## Report Details
- **Report ID**: 1071524
- **URL**: https://hackerone.com/reports/1071524
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-04T20:44:42.814Z
- **Disclosed**: 2021-01-25T19:52:15.659Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Vulnerable Website URL or Application:
https://███████html?url=javascript:alert("nagli")

##Description of Security Issue: (please limit to one site/app per submission)
Reflected XSS due to no input validation

█████████

##Remediation
Sanitize the input on the that parameter

##Best Regards
nagli

## Impact

Executing Javascript on behalf of the victim

## Attachments
No attachments
