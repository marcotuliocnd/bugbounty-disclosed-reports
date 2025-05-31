# Clickjacking misconfiguration bug

## Report Details
- **Report ID**: 1176104
- **URL**: https://hackerone.com/reports/1176104
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-04-27T02:33:56.055Z
- **Disclosed**: 2021-06-18T14:48:19.451Z

## Reporter
- **Username**: ridoykhan0x1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hi team,

While performing security testing  of your website i have found the vulnerability called Clickjacking.

Many URLS are in scope and vulnerable to Clickjacking.

What is Clickjacking ?

Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.

This vulnerability affects Web Server.

Steps to Reproduce / POC

Vulnerable Urls:https://docs.sifchain.finance

Put every above url one by one in the code of iframe, which  is given below

<!DOCTYPE HTML>

<html lang="en-US">

<head>

<meta charset="UTF-8">

<title>I Frame</title>

</head>

<body>

<h3>clickjacking vulnerability</h3>

<iframe src="https://docs.sifchain.finance"height="550px" width="700px"></iframe>

</body>

</html>

By nil chowdhury

niloychowdhury129@gmail.com

Notice that site is visible in the Iframe

POC is in the attachments. Thanks, waiting for your response.

Reference links: Below are the links which will help you to understand more about this issue including the remediation
https://hackerone.com/reports/8724
https://hackerone.com/reports/289246
https://hackerone.com/reports/1027192
https://hackerone.com/reports/405342
https://hackerone.com/reports/591432

## Impact

Using a similar technique, keystrokes can also be hijacked. With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email or bank account, but are instead typing into an invisible frame controlled by the attackers 

## Attachments
- Screenshot_2021-04-27-08-28-09-231_com.android.chrome.jpg
