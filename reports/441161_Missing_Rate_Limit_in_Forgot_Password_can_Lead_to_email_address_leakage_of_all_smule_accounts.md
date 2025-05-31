# Missing Rate Limit in Forgot Password can Lead to email address leakage of all smule accounts

## Report Details
- **Report ID**: 441161
- **URL**: https://hackerone.com/reports/441161
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-15T10:55:59.936Z
- **Disclosed**: 2019-05-13T15:32:49.080Z

## Reporter
- **Username**: dhakal_ananda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: smule

## Vulnerability Information
Hello Smule,

I have found a vulnerability by which an attacker can get access of all the gmail accounts associated with Smule. The forgot password parameter can be brute forced through which an attacker can get the email address.

##Steps to Reproduce

> Enter your email address and for the forgot password parameter.
> Capture the request in the proxy.
> Brute for the parameter using different email address.
> Check the different request and see the response.

The right email and the wrong email will have different response and request length. Hence, the attack is successful.

## Impact

The impact is obvious here. As you can see, the vulnerability is about the email address leakage of the smule accounts. The email address leakage of the account is said to be prohibited. The confidential data of the Smule application can be leaked.

###Mitigation

Add rate limit on the application.
Use CAPTCHA verification if many request is sent.

## Attachments
No attachments
