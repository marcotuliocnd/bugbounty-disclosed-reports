# Clickjacking: X-Frame Header Missing

## Report Details
- **Report ID**: 168358
- **URL**: https://hackerone.com/reports/168358
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-14T16:27:14.287Z
- **Disclosed**: 2017-11-09T20:08:58.295Z

## Reporter
- **Username**: vaxo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

CODE:
<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="http://yelp.com" width="500" height="500"></iframe>
   </body>
</html>


For More :  https://www.owasp.org/index.php/Testing_for_Clickjacking_(OWASP-CS-004) 

Proof attatched !

## Attachments
- Screenshot_from_2016-09-14_22-10-39.png
