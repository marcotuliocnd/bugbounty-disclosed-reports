# Missing Rate Limitation at /apps/upload_app/ 

## Report Details
- **Report ID**: 416906
- **URL**: https://hackerone.com/reports/416906
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-10-01T14:11:18.837Z
- **Disclosed**: 2018-10-07T10:52:01.487Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
##Summary##
I discovered that one is able to create **unlimited** number of apps via `/apps/upload_app/ `. 

**PS: I feel this is within the scope of your program and you want to know about it. If otherwise, I'll be happy to close this.**

## Steps To Reproduce:

  1. Login and go to https://chaturbate.com/apps/upload_app/
  1. Fill the form
  1. Enable a proxy interception tool (e.g Burp Suite)
  1. Click Save
  1. Send the `POST` request made to  `/apps/upload_app/` to intruder
  1. Set 100 or more custom inputs and Start attack
  1. I was able to create many apps without limitation and I've had to pause because of your policy on rate limits

## Supporting Material/References:
{F353746}

## Impact

Create unlimited apps

## Attachments
- Screen_Shot_2018-10-01_at_3.09.02_PM.png
