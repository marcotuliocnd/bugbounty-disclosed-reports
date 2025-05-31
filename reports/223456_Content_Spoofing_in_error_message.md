# Content Spoofing in error message

## Report Details
- **Report ID**: 223456
- **URL**: https://hackerone.com/reports/223456
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T14:07:20.853Z
- **Disclosed**: 2017-05-17T14:28:51.708Z

## Reporter
- **Username**: codertom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi Weblate,

   I found a content spoofing

###Steps to reproduce
1. Go to https://hosted.weblate.org/translate/debian-reference/translations/fr/?type=Sorry for the inconvenience we where having some trouble in our system because of some hackers, please don't log in for you to make safe of your credential or just go to this updated website: http://evil.weblade.org/attack.php and no other than website

As you could now see your application tells a user something wrong with your application that would degrade the reputation of your application in some way.

Thanks,
Tom


## Attachments
No attachments
