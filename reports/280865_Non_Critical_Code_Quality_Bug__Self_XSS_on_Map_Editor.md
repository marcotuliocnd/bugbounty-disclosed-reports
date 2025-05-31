# Non Critical Code Quality Bug / Self XSS on Map Editor

## Report Details
- **Report ID**: 280865
- **URL**: https://hackerone.com/reports/280865
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-20T06:22:02.275Z
- **Disclosed**: 2017-12-12T16:22:20.785Z

## Reporter
- **Username**: mksecurity
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Hi Team,

I've found non-critical XSS on map editor. It is not for bounty just for code quality.

This is my url:

https://infogram.com/app/#edit/c024c717-31c2-4c31-8491-1cc9534e9adb

When i added map on form then edit Country name and replace with "<script>alert(1);</script>" it is executed. 

Attached screenshots. 


## Attachments
- infogram2.PNG
- infogram1.PNG
