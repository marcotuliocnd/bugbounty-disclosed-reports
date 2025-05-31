# CSRF Account Deletion on ███ Website

## Report Details
- **Report ID**: 840285
- **URL**: https://hackerone.com/reports/840285
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-05T00:58:26.478Z
- **Disclosed**: 2020-07-09T04:23:40.660Z

## Reporter
- **Username**: notdeghost
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

A CSRF vulnerability against the [███████](████) allows attackers to delete user accounts. 

## Impact

Users who visit a malicious website could find their ████████ account deleted. 

## Step-by-step Reproduction Instructions

1. Create and login to a new account on the [██████](███████)
2. Open the provided HTML file and press the "POC" button. Note that the POC button is used only to make testing easier, and is not necessary in an actual attack scenario. 
3. Refresh the page on the ███ website. You should find that you have been logged out, and are unable to sign back into your account. 

██████

## Product, Version, and Configuration (If applicable)

**Website**: [███████](██████████)

## Suggested Mitigation/Remediation Actions

Enforce proper CSRF control on the ██████, for example with Google captcha (which is already implemented through much of the site).

## Impact

Users who visit a malicious website could find their account deleted.

## Attachments
No attachments
