# Session Hijacking leads to full control of account by attacker

## Report Details
- **Report ID**: 1201396
- **URL**: https://hackerone.com/reports/1201396
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-18T18:22:42.839Z
- **Disclosed**: 2021-06-24T16:05:20.979Z

## Reporter
- **Username**: sampritdas
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
Hi Team ,

I am Samprit Das MCEH (Metaxone Certified Ethical Hacker) and a Security Researcher I just checked your website and got a critical vulnerability please read the report carefully.

Description:-
The Session Hijacking attack consists of the exploitation of the web session control mechanism, which is normally managed for a session token.
Because http communication uses many different TCP connections, the web server needs a method to recognize every user’s connections.
The most useful method depends on a token that the Web Server sends to the client browser after a successful client authentication.
A session token is normally composed of a string of variable width and it could be used in different ways, like in the URL, in the header of the http requisition as a cookie, in other parts of the header of the http request, or yet in the body of the http requisition.
The Session Hijacking attack compromises the session token by stealing or predicting a valid session token to gain unauthorized access to the Web Server.

Step to reproduce:-

1) Login to application with firefox and press CTRL+Shift+I
2) You will see developer tool will open
3) Now go to Storage copy the value of the name field connect.sid
4) Now Open New private window on firefox and press CTRL+Shift+I
5) Again developer mode will open on private window
6) Then again go to Storage and in connect.sid value change the value of new private window with firefox one
7) After that press Enter and reload the Website Boom account will open due to session hijacking

Video POC :- https://drive.google.com/file/d/1sw0or6Q0yTNLEWfezEqwfSNZoIcGOQ06/view?usp=sharing

Reference:-

https://hackerone.com/reports/745324
https://owasp.org/www-community/attacks/Session_hijacking_attack
https://hackerone.com/reports/167460

## Impact

For this vulnerability attacker don't need any user credentials to login on an account what he will do, he will capture connect.sid value/token
with any sniffing tools like Wireshark etc after getting session value/token he can easily login to account by developer tools as we can seen in POC video
by this way account can be controlled by attacker and for this vulnerability it can also be impact full for xss attack
if a attacker got xss vulnerability on your website he can chain the vulnerability with this attack

Thank you,
Samprit Das

## Attachments
No attachments
