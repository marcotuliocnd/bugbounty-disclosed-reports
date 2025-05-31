# Information disclosure (No rate limting in forgot password & other login)

## Report Details
- **Report ID**: 91343
- **URL**: https://hackerone.com/reports/91343
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-09-30T23:59:00.486Z
- **Disclosed**: 2018-04-14T08:47:26.902Z

## Reporter
- **Username**: protector47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Hi there,
I noticed a small information leak which allows an attacker to check whether an email address is associated with an account.If your account is not associated with website then an error will become raise that **"That username or email was not found."**
You should always return a status message like: **"If your email exists in our database, you'll receive a reset link"**. That way an attacker cannot distinguish between the two cases.
Also you should add rate limiting :)

Thanks,

## Attachments
No attachments
