# XSS on www.██████ alerts and a number of other pages

## Report Details
- **Report ID**: 450315
- **URL**: https://hackerone.com/reports/450315
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-27T08:08:02.043Z
- **Disclosed**: 2019-12-02T19:10:17.263Z

## Reporter
- **Username**: d0nut
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:** If an action on ███████ results in an error, an error dialog is shown. This 
dialog, in certain scenarios, is vulnerable to stored XSS due to a lack of sanitization.

**Description:** In this specific example, I'll be using a GET endpoint that attempts to delete alerts based on an ID supplied. If the ID does not belong to the user, an error is displayed containing the ID. This ID is not sanitized when displayed in the error dialog.

Example PoC: `https://www.██████████/alerts/delete/id/1234<img+src+onerror%3d'alert(1)'>`

The previous PoC appears to be reflected but it is actually stored. Here's a PoC to prove that: `https://████████pythonanywhere.com/poc/xss/dod/4rspEdWG1tqA2pQ4bY4C`

## Impact
XSS

## Step-by-step Reproduction Instructions

1. Trick victim to visiting attacker.com
2. Attacker.com makes a GET request to `https://www.████/alerts/delete/id/1234<img+src+onerror%3d'<PAYLOAD>'>`
3. Redirect victim to `https://www.██████████/alerts/` or similar (like `https://www.████████/member/options`)

## Product, Version, and Configuration (If applicable)
https://www.█████

## Suggested Mitigation/Remediation Actions
Sanitization of the error message.

## Impact

XSS

## Attachments
No attachments
