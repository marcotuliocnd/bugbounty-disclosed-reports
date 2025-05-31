# Content spoofing on error pages or text injection

## Report Details
- **Report ID**: 474688
- **URL**: https://hackerone.com/reports/474688
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-04T15:36:29.541Z
- **Disclosed**: 2019-01-08T20:04:04.794Z

## Reporter
- **Username**: drosofraymaybe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cfptime

## Vulnerability Information
###Poc:

[https://www.cfptime.org/%20is%20not%20available%20anymore%20,%20pls%20go%20to%20WWW.EVIL.COM%20because%20this%20site](https://www.cfptime.org/%20is%20not%20available%20anymore%20,%20pls%20go%20to%20WWW.EVIL.COM%20because%20this%20site).

###Steps to reproduce:

1: Just browse this target on any browser 
2: Target: http://www.cfptime.org/
3: add any content after For example: this is not available anymore pls check WWW.EVIL.COM because this site
4: Now browser reflect the content or text .

###Fix :
Use Predefined 404 page , with fixed error content 
It can be fixed by adding the following to the web server config:
ErrorDocument 404 "File not found."

## Impact

Application allows users to inject any content on the 404 not found webpage
The issue is not critical , as it is only possible to inject plain text, no links or active content, to the error page.

## Attachments
- Capture.PNG
