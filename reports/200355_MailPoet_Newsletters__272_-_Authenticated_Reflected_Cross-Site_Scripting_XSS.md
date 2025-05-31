# MailPoet Newsletters <= 2.7.2 - Authenticated Reflected Cross-Site Scripting (XSS)

## Report Details
- **Report ID**: 200355
- **URL**: https://hackerone.com/reports/200355
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-01-22T14:42:55.144Z
- **Disclosed**: 2017-06-17T17:58:38.886Z

## Reporter
- **Username**: madrobot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hello __Team__

__Abstract__:-
A Cross-Site Scripting vulnerability was found in the MailPoet Newsletters plugin. This issue allows an attacker to perform a wide variety of actions, such as stealing Administrators' session tokens, or performing arbitrary actions on their behalf. In order to exploit this issue, the attacker has to lure/force a logged on WordPress Administrator into opening a URL provided by an attacker.

__Introduction__:-
The MailPoet Newsletters plugin allows a WordPress administrator to create newsletters, automated emails, post notifications and autoresponders. A Cross-Site Scripting vulnerability was found in the MailPoet Newsletters plugin. This issue allows an attacker to perform a wide variety of actions, such as stealing Administrators' session tokens, or performing arbitrary actions on their behalf. In order to exploit this issue, the attacker has to lure/force a logged on WordPress Administrator into opening a URL provided by an attacker.

__Proof of concept__:-
Have an authenticated admin visit the URL:-

https://business-blog.zomato.com//?wysija-page=1&controller=subscribers&action=wysija_outter&encodedForm=eyJmb3JtIjoiUHduIiwiYWZ0ZXJfd2lkZ2V0IjoiPHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4ifQ==
The encodedForm parameter is the base64 encoded string:
{"form":"Pwn","after_widget":"<script>alert('XSS)</script>"}

A pop-up box should appear, meaning the JavaScript contained in the request_id request parameter was executed by the browser.

{F154227}

__Fix__:-
This issue is resolved in MailPoet Newsletters version 2.7.3.

__Regards__,
Santhosh

## Attachments
- zomato_xss.png
