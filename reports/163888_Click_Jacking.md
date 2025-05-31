# Click Jacking

## Report Details
- **Report ID**: 163888
- **URL**: https://hackerone.com/reports/163888
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-27T20:33:16.256Z
- **Disclosed**: 2016-08-29T16:37:33.194Z

## Reporter
- **Username**: muhaddix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hey **legalRobot!** I have found **Click Jacking type** of Vulnerability in your Website

Now The Question is What is **Click Jacking.**
**Click Jacking** (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

How to Produce Click Jacking in your Website,
**Steps to Produce this Issue:-**
1) Create new .Html file. (I also send this file to you)
2) Copy & Paste this code in Html & save it
`<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="https://www.legalrobot.com/" width="500" 
height="500"></iframe>
   </body>
</html>`
 3) Open that html file and you are seeing your website content opening in other frame.

**Fix:** Use a proper X-Frame to your website, So other domains can not use your website content, Mostly Spammers & Attackers can use this technique. (See My Example File too)

Get More Help From Owasp guides:
https://www.owasp.org/index.php?title=Testing_for_Clickjacking_(OTG-CLIENT-009)&setlang=en
https://www.owasp.org/index.php/Clickjacking
https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet

Glad to be, If you fix this Click Jacking flaw in your website,
Thanks! Regards: Muhammad Muhaddis (Cyber Security Researcher)

## Attachments
- Click_Jacking_Example.html
- Click_Jacking.html
