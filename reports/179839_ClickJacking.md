# ClickJacking 

## Report Details
- **Report ID**: 179839
- **URL**: https://hackerone.com/reports/179839
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-11-03T06:39:58.967Z
- **Disclosed**: 2017-11-09T20:07:47.394Z

## Reporter
- **Username**: jessepinkman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
hi there i have found a clickjacking vulnerability in your site
in the index (home page): https://www.yelp.com/
Clickjacking, also known as a "UI redress attack", is when an attacker uses multiple transparent or opaque layers to trick a user into clicking on a button or link on another page when they were intending to click on the the top level page. Thus, the attacker is "hijacking" clicks meant for their page and routing them to another page, most likely owned by another application, domain, or both.

Using a similar technique, keystrokes can also be hijacked. With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email or bank account, but are instead typing into an invisible frame controlled by the attacker. 
PoC:
<html>
   <head>
     <title>test yelp</title>
   </head>
   <body>
     <p> yelp.com is vulnerable to clickjacking!</p>
     <iframe src="https://www.yelp.com" width="500" height="500"></iframe>
   </body>
</html>

Regards.


## Attachments
No attachments
