# Password token validation in https://wakatime.com/

## Report Details
- **Report ID**: 244614
- **URL**: https://hackerone.com/reports/244614
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-30T03:11:56.800Z
- **Disclosed**: 2017-07-24T02:38:16.440Z

## Reporter
- **Username**: silv3rpoision
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi team,

I noticed that when requesting multiple reset links at https://wakatime.com/reset_password/ all tokens are valid and can be used.

In numerous applications the following policy is adopted as an additional security measure:

keep valid only that token with shorter lifetime (last requested)
or

invalidate all reset links generated after successful use of one of these tokens
Please check it.

Steps to reproduce:
1.Go to password reset page and request two times for pass reset token
2.Then go to your email and visit first pass reset link
3.Then you will realize that it is not getting expired .

Browser/OS: 
Chroem latest linux

Attack scenario:
There is not a immediate thereat to this but it is implemented for best practice and for secure design principle.

## Attachments
No attachments
