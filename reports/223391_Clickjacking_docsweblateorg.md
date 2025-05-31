# Clickjacking docs.weblate.org

## Report Details
- **Report ID**: 223391
- **URL**: https://hackerone.com/reports/223391
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T11:22:11.904Z
- **Disclosed**: 2017-06-05T12:45:32.666Z

## Reporter
- **Username**: akbarparambil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.

This vulnerability affects Web Server.

POC

Here are th steps to reproduce the vulnerability

1.save the below file as anything.html and run it u can see its vulnerable to clickjacking

<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="http://docs.weblate.org" width="500" height="500"></iframe>
   </body>
</html>

As far as i know this data is enough to prove that your site is vulberable to Clickjacking..
according to OWASP its more than enough..
https://www.owasp.org/index.php/Testing_for_Clickjacking_(OWASP-CS-004)

Solution

https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet



## Attachments
- Screenshot_from_2017-04-24_16-45-10.png
