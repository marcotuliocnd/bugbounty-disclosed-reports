# Arbitrary File Upload in Logo & Log in image Theming setting.

## Report Details
- **Report ID**: 155690
- **URL**: https://hackerone.com/reports/155690
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-31T21:57:59.882Z
- **Disclosed**: 2016-10-05T12:34:55.184Z

## Reporter
- **Username**: bastianwelfrid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi team

First I think this vulnerability doesn't fall at your bug bounty program but this is a bad design that should fix right now cause if an attacker get admin access he still can upload a malicious file in client server side.

I saw that Logo & Log in image allow to upload other files type example *.html and it'll execute in client server.
Other case,I created an html code and saved it as image file,server still executed it as html file.
The Logo & Log in image will upload it into ../data/themedinstancelogo & ../data/themedbackgroundlogo

Good news,I tried to upload an php file but server executed that file as text.

PoC:
Upload an html file through logo upload and Log in image and you will see that file will execute.

http://example.com/nextcloud/data/themedinstancelogo
http://example.com/nextcloud/data/themedbackgroundlogo

Regards,


## Attachments
- nc.png
