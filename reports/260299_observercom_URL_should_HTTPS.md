# observer.com URL should HTTPS

## Report Details
- **Report ID**: 260299
- **URL**: https://hackerone.com/reports/260299
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-15T12:07:23.223Z
- **Disclosed**: 2017-09-14T21:09:28.853Z

## Reporter
- **Username**: bf7e43565d8cf54de3bc5a7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
#Summary

This is just for the awareness to use HTTPS everywhere, even for outgoing links - where it's possible.
Treat this report with some salt, not as in hashes.

#Navigate to:

       https://www.legalrobot-uat.com/press/

Example page (In the lower part where you find the observer.com Link):

observer redirect to HTTPS after click, but cookie is sent on the network before that.

See my attached photo. {F212950}

Related Issue : #1093

Thanks!


## Attachments
- ob.png
