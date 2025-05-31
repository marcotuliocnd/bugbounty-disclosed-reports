# Clickjacking wordcamp.org

## Report Details
- **Report ID**: 230581
- **URL**: https://hackerone.com/reports/230581
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-22T05:52:59.310Z
- **Disclosed**: 2017-06-24T18:24:56.135Z

## Reporter
- **Username**: hasanexpert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hello Security,
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.
The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
This vulnerability affects Web Server.
IMPACT:
An attacker can host this domain in other evil site by using iframe and if a user fill the given filed it can directly redirect as logs to attacker and after its redirect to your web server.. its lead to steal user information too and use that host site as phishing of your site its CSRF and Clickjacking
POC:
1.Open URL :https://www.blockchain.com/
2.put the url in the below code of iframe
<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>i Frame</title>
</head>
<body>
<h3>This is clickjacking vulnerable</h3>
<iframe src="https://www.blockchain.com/" frameborder="2 px" height="500px" width="500px"></iframe>
</body>
</html>

3.Observe that site is getting displayed in Iframe

Impact:
By using Clickjacking technique, an attacker hijack's click's
meant for one page and route them to another page, most likely
for another application, domain, or both.

Remediation:
Frame busting technique is the better framing protection
technique.
Sending the proper X-Frame-Options HTTP response headers
that instruct the browser to not allow framing from other
domains

## Attachments
- Clickjackin.jpg
