# Clickjacking: X-Frame-Options header missing

## Report Details
- **Report ID**: 163646
- **URL**: https://hackerone.com/reports/163646
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-26T19:59:55.903Z
- **Disclosed**: 2016-08-29T07:41:34.649Z

## Reporter
- **Username**: sadhu16
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.

This vulnerability affects Web Server.

POC

Here are th steps to reproduce the vulnerability

1.open notepad and paste the following code

<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="https://www.legalrobot.com/swag/" width="500" height="500"></iframe>
   </body>
</html>
2.save it as <anyname>.html eg cj.html
3.and just simply open that in browser

As far as i know this data is enough to prove that your site is vulberable to Clickjacking..
according to OWASP its more than enough..
https://www.owasp.org/index.php/Testing_for_Clickjacking_(OWASP-CS-004)

Solution

https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet
check this out..here is the solution for that...

Please also find the attached screenshots (one of response & one of  attack being exploited in browser )



## Attachments
- cj1.png
- cj1response.png
