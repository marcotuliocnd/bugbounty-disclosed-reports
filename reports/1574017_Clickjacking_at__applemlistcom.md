# Clickjacking at  app.lemlist.com

## Report Details
- **Report ID**: 1574017
- **URL**: https://hackerone.com/reports/1574017
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-05-18T01:43:11.809Z
- **Disclosed**: 2022-05-20T15:04:22.692Z

## Reporter
- **Username**: scriptsavvy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lemlist

## Vulnerability Information
Hi team,

While performing security testing of your website i have found the vulnerability called Clickjacking.
Many URLS are in scope and vulnerable to Clickjacking.

What is Clickjacking ?

Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
This vulnerability affects Web Server.


Vulnerable Urls:
=============

https://app.lemlist.com

Put every above url one by one in the code of iframe, which is given below
```javascript
<html lang="tr-TR">
<kafa>
<meta karakter kümesi="UTF-8">
<title>Çerçeve Yapıyorum</title>
</head>
<body>
<h3>clickjacking güvenlik açığı</h3>
<iframe src="https://app.lemlist.com/teams/tea_sgYr5dZr478x4FQ9K/settings/user/usr_Z3GZ4DDHLLyLyZHj5/users" height="550px" width="700px"></iframe>
</body>
</html>
```

## Impact

Using a similar technique, keystrokes can also be hijacked. With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email or bank account, but are instead typing into an invisible frame controlled by the attacker.

## Attachments
- Ekran_g_r_nt_s__2022-05-18_044120.png
- index.html
