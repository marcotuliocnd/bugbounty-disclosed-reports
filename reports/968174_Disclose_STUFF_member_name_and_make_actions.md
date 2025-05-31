# Disclose STUFF member name and make actions.

## Report Details
- **Report ID**: 968174
- **URL**: https://hackerone.com/reports/968174
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-08-27T00:04:04.982Z
- **Disclosed**: 2022-05-14T14:34:50.371Z

## Reporter
- **Username**: zambo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Shopify Security Team!

 Bug Summary:
=============

Based on the report #968165, this also can retrieve the STUFF member name and can send messages using his name.

 Reproduction steps:
=============
  - install shopify chat applications.

Start Exploit #1 : 
=============
+ Go to targeted store : 
+ Start a chat using the app with the store support.
+ Click on _I need an update on my order_.
+ fill out the Order ID and Email. ( fill the info randomly if you want to), the respond comes with message "in order to provide you with ....".
+  I intercept the the post request, and inject changes in the request, 
+ In this exploit allowed the attacker to send messages like a team member (bot)

{F965084}

Example : i changed text element  to " Hello customer hahaha "

Result : 
========

poc from shopify ping application ( STUFF side )

{F965081}


 Start Exploit #2 : 
=============
+ Go to targeted store : 
+ Start a chat using the app with the store support.
+ As soon as you get the answer.
+ I intercept the message request, i found the STUFF member name and ID.

{F965077}

{F965078}

## Impact

Can retrive STUFF info,  not allowed !

## Attachments
- Screen_Shot_2020-08-26_at_23.19.50.png
- Screen_Shot_2020-08-26_at_23.40.13.png
- processed.jpeg
- Screen_Shot_2020-08-26_at_23.25.59.png
