# Password reset token not expiring

## Report Details
- **Report ID**: 170161
- **URL**: https://hackerone.com/reports/170161
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-18T05:58:14.333Z
- **Disclosed**: 2017-11-09T19:53:16.088Z

## Reporter
- **Username**: hk755a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Hello Yelp,
Old unused Password reset tokens are not expiring on yelp.com after the issuance of a new token.

EXPLANATION:

Suppose at 09:00 hrs I used password reset options of yelp and got a token on my email.Lets call it token_01. But i did not use it.
And at 09:04 hrs I used again the password reset option and got a new token,which is token_02.
Now generally after the issuance of token_02,the previous unused token should expire.But in case of yelp its not happening.Both the tokens are remaining usable at the same time.

ATTACK SCENARIO:

Suppose I am an attacker and I got access to the recovery email option of your yelp account.I logged in to your recovery email (suppose that is user@gmail.com).Then I used the forget password option of your yelp email.I will get one password reset token.
I noted the token and then deleted the email from user@gmail.com.
In the meantime you understood that someone got access to your gmail account.Then you reset the password of your user@gmail.com so that any one cant hack again your yelp account.
Now its time for my exploitation.
I will use my token which is live even after your issuance of new token.and I will hack into your yelp account.

MITIGATION:

All password reset tokens should automatically expire after the issuance of new ones.

## Attachments
No attachments
