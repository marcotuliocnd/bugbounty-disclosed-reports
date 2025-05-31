# [www.stripo.email] You can override the speed limit by adding the X-Forwarded-For header.

## Report Details
- **Report ID**: 855013
- **URL**: https://hackerone.com/reports/855013
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-21T12:41:29.813Z
- **Disclosed**: 2020-04-23T08:44:00.659Z

## Reporter
- **Username**: what_web
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
###Summary
In *https://stripo.email/template-order* I think you have implemented rate limiting via 429 status code for too many requests, but in reality it is not. An attacker could bypass the 429 speed limit by adding an X-Forwarded-For header.

###Steps To Reproduce
1. Go to the *https://stripo.email/template-order* page
2. fill in the random content and Click the Order Template grab the packet.
3. Automate the request by adding the X-Forwarded-For header.

###Proof of Concept
The first photo bypasses the speed limit by adding an X-Forwarded-For header.
{F797676}

The second figure shows the 429 status code playing due to the speed limit if the X-Forwarded-For header is not added.
{F797677}

###Fix
Fix this bug by changing the way the server handles X-Forwarded-For headers

## Impact

Override speed limit

## Attachments
- testc1.PNG
- testc2.PNG
