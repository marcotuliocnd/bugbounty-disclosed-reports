# Clickjacking - https://mercantile.wordpress.org/

## Report Details
- **Report ID**: 258283
- **URL**: https://hackerone.com/reports/258283
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-09T15:05:27.500Z
- **Disclosed**: 2017-08-28T17:11:41.615Z

## Reporter
- **Username**: giantfire
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hi team,

While performing security testing of your website i have found the vulnerability called Clickjacking.

What is Clickjacking ?
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.
The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
This vulnerability affects Web Server.

>> Steps to Reproduce / POC
1. Please Open URL: https://mercantile.wordpress.org/
2. Put the url in the code of iframe, which is given below

<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I Frame</title>
</head>
<body>
<h3>clickjacking vulnerability</h3>
<iframe src="https://mercantile.wordpress.org/" frameborder="5 px" height="550px" width="700px"></iframe>
</body>
</html>

3. Notice that site is visible in the Iframe

POC is in the attachments. Thanks, waiting for your response.

Regards
giantfire

## Attachments
- wordpress.PNG
