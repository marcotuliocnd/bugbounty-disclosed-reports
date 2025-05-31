# Missing DMARC on weblate.org

## Report Details
- **Report ID**: 223545
- **URL**: https://hackerone.com/reports/223545
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T18:55:03.356Z
- **Disclosed**: 2017-05-17T14:23:30.854Z

## Reporter
- **Username**: khalidamin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
##Summary
Email spoofing is possible due to missing SPF/Dmarc Records.
Similar to this report submitted to Hackerone itself: https://hackerone.com/reports/575

##Steps to reproduce:
1- Go to https://emkei.cz ( A Fake Mailer )
2- Set the from to parameter as noreply@weblate.org or any other name, and send it.
3- The email is sent with any content you'd like to add as the message.

Thanks.

## Attachments
- Screenshot_(137).png
