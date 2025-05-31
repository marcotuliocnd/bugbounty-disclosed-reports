# clickjacking to Semrush auth login

## Report Details
- **Report ID**: 318295
- **URL**: https://hackerone.com/reports/318295
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-02-21T17:57:55.777Z
- **Disclosed**: 2018-03-13T14:25:36.732Z

## Reporter
- **Username**: karrrtik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
Description:
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on. this attack could be perform to semrush auth user because its direct popup for geo.semrush.com login.

Steps To Reproduce:
Create HTML file containg following code:
<iframe src="https://geo.semrush.com/"></iframe>
Execute the HTML file & you will see Single Sing On login page present trough the iframe.

## Impact

Revealing confidential information(credentials) AND/OR taking control of their computer/account while clicking on seemingly innocuous web pages.

The hacker selected the **UI Redressing (Clickjacking)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://geo.semrush.com/

**Can a victim be tricked into unknowingly initiating a specific action?**
Yes

**What specific action can the user be tricked into?**
semrush auth login could be hack

## Attachments
- geo.semrush.png
