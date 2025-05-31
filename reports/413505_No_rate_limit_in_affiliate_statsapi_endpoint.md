# No rate limit in affiliate statsapi endpoint

## Report Details
- **Report ID**: 413505
- **URL**: https://hackerone.com/reports/413505
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-24T19:11:43.656Z
- **Disclosed**: 2018-10-19T17:41:26.170Z

## Reporter
- **Username**: maximus-decimus-meridius
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
##Brute force at affiliate statsapi##


## Steps To Reproduce:

  1. The affiliate stats api link is vulnerable to brute force

 https:// chaturbate.com/affiliates/apistats/?username=hackeronetestchat&token=**vulnerable**
I've used my profile and and my token to check brute force

The correct token returned with 200 ok status

## Impact

An attacker could view the  affiliates stats of an user

## Attachments
- chaturbate.PNG
