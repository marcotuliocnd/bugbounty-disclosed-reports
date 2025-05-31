#  Legal | Application is Missing CSP(Content Security Policy) Header 

## Report Details
- **Report ID**: 163676
- **URL**: https://hackerone.com/reports/163676
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-26T22:14:47.426Z
- **Disclosed**: 2016-08-31T06:12:39.693Z

## Reporter
- **Username**: sadhu16
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
-Content Security Policy Header used to allow only source code to execute in the application from the domain mentioned in its list. By using this we can restrict code to execute which is written in application either by developer or by Hacker

-Since application contains no such header i am going to  inject an image from third party domain which is not of application domain

<img src="https://s-media-cache-ak0.pinimg.com/564x/ab/2d/bd/ab2dbda0c6c11455527c0dd34d5f5bf6.jpg" height="500" width="500"/>

third party domain
https://s-media-cache-ak0.pinimg.com/564x/ab/2d/bd/ab2dbda0c6c11455527c0dd34d5f5bf6.jpg

Refer-https://www.owasp.org/index.php/Content_Security_Policy_Cheat_Sheet

## Attachments
- csp_exploit.wmv
