# No Rate On Add Suggest

## Report Details
- **Report ID**: 481654
- **URL**: https://hackerone.com/reports/481654
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-17T23:13:57.902Z
- **Disclosed**: 2019-01-22T13:59:29.029Z

## Reporter
- **Username**: elmahdi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
###Hello
###Description : 
####I have found that there is no limit in the number of requests in place of adding suggest, which may exploit the vulnerability of the attacker to send a large number of suggestions, for example, send a million suggest may lead to cause a problem to the server

###Steps To Reproduce : 
####1. Go To https://hosted.weblate.org/translate/andors-trail/game-content/ar/?checksum=c4ddb61773f5e641#suggestions add And Fill in fields
####2.Click On Add
####3.And intercept The Request With Proxy ( Burp )
####4.And Send The Request To Inturder
####5.And Go to Payloads and Select In The Payload type > Numbers ...
####6.Click On Start Attack
###POC : 
{F408287}
{F408288}

###Remediation : 
####1. limit the functionality to x attempts in a predefined period before blocking the account 
####2. set up a captcha to prevent robots

## Impact

####An attacker could cause a problem for the server

## Attachments
- Capture.PNG
- Capture.PNG
