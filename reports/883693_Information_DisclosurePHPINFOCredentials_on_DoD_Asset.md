# Information Disclosure(PHPINFO/Credentials) on DoD Asset

## Report Details
- **Report ID**: 883693
- **URL**: https://hackerone.com/reports/883693
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-27T14:45:20.010Z
- **Disclosed**: 2021-03-11T20:41:03.457Z

## Reporter
- **Username**: atbabers
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A DoD leaks credentials on a phpinfo() page.

**Description:**
https://███ publicly displays a phpinfo() page that leaks system information and credentials.

## Impact
The impact is medium not only due to information leakage of numerous different details such as system information but also the leakage of domain credentials.
USERDOMAIN	███████
USERNAME	██████
█████████PASSWORD']	████████

## Step-by-step Reproduction Instructions

1. Visit: https://████/████
2. Information Disclosed

## Suggested Mitigation/Remediation Actions
████████ BAT  suggests removing the ███ page or requiring authentication before making it accessible.

## Impact

The impact is medium not only due to information leakage of numerous different details such as system information but also the leakage of domain credentials.

## Attachments
No attachments
