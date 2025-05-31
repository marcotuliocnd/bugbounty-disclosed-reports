# Single Sing On - Clickjacking

## Report Details
- **Report ID**: 299009
- **URL**: https://hackerone.com/reports/299009
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-18T05:11:32.852Z
- **Disclosed**: 2018-02-21T15:27:13.238Z

## Reporter
- **Username**: r0p3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
**Description:** 
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on.
**Browsers Verified In:**
Any

**Steps To Reproduce:** 
Create HTML file containg following code:
` <iframe src="https://sso.semrush.com/"></iframe> `
Execute the HTML file & you will see Single Sing On login page present trough the iframe.


**Supporting Material/References:**

## Impact

Revealing confidential information(credentials) AND/OR taking control of their computer/account while clicking on seemingly innocuous web pages.

## Attachments
- SSO_clickjacking.png
