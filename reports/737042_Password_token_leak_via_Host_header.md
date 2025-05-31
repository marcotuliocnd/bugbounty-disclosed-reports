# Password token leak via Host header

## Report Details
- **Report ID**: 737042
- **URL**: https://hackerone.com/reports/737042
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-13T18:56:19.002Z
- **Disclosed**: 2019-12-19T13:01:38.710Z

## Reporter
- **Username**: aishkendle
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
#Password token leak via Host header
--------------

##Vulnerability Description:
Token will be leaked by the Server to that third party site and that token can be used by third parties to reset the password and take over the account & directly login in your account

##Steps To Reproduce:

1) Send reset password link to your email address.
2)Now go to email, turn burp suite intercept on and click on reset password link. Check for the requests having the token in referrer and host as third party website. And copy the link
3)Now turn intercept off and reset the password.(with that link)
4)Now reset the password.

#POC:
Images Uploaded

## Impact

#Impact

It allows the person who has control of particular site to change the user's password (CSRF attack), because this person knows reset password token of the user.

## Attachments
- Screenshot_from_2019-11-14_00-22-22.png
- Screenshot_from_2019-11-14_00-21-53.png
- Screenshot_from_2019-11-14_00-22-37.png
