# Click Jacking Nextcloud

## Report Details
- **Report ID**: 347782
- **URL**: https://hackerone.com/reports/347782
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-05-05T15:38:23.376Z
- **Disclosed**: 2019-07-01T10:02:23.776Z

## Reporter
- **Username**: enz0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello Security,
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.
The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
This vulnerability affects Web Server.
IMPACT:
An attacker can host this domain in other evil site by using iframe and if a user fill the given filed it can directly redirect as logs to attacker and after its redirect to your web server.. its lead to steal user information too and use that host site as phishing of your site its CSRF and Clickjacking

POC:
1. open https://portal.nextcloud.com/login.php or https://nextcloud.com
2. Put the url in the below code of iframe
<html>
<body>
<iframe 
sandbox="allow-modals allow-scripts allow-forms allow-popups allow-same-origin"
src="https://portal.nextcloud.com/login.php" width=600 height=400>
</iframe>
</body>
</html>
3.Observe that site is getting displayed in Iframe

## Impact

By using Clickjacking technique, an attacker hijack's click's
meant for one page and route them to another page, most likely
for another application, domain, or both.

The hacker selected the **UI Redressing (Clickjacking)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://portal.nextcloud.com/login.php

**Can a victim be tricked into unknowingly initiating a specific action?**
Yes

**What specific action can the user be tricked into?**
This is the nexcloud login page, it can trick user login or forgot password function

## Attachments
- poc.png
