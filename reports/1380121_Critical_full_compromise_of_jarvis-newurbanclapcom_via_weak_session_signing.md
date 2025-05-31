# Critical full compromise of jarvis-new.urbanclap.com via weak session signing

## Report Details
- **Report ID**: 1380121
- **URL**: https://hackerone.com/reports/1380121
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-10-25T11:50:21.616Z
- **Disclosed**: 2022-01-30T20:03:00.574Z

## Reporter
- **Username**: ian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: urbancompany

## Vulnerability Information
## Summary
Hi there, I discovered that jarvis-new.urbanclap.com uses a weak Flask session key. Because Flask sessions are signed with a static secret, if this secret is known to an attacker then they can modify the session state. In this case, we can modify the Redash `user_id` for the session and log in as any user. **This results in a full compromise of the instance.** I have attached a screenshot showing that I logged into `█████████@urbancompany.com` and have full admin permissions:

██████████
████
██████████
███████

## How to fix
Change the `REDASH_COOKIE_SECRET` and `REDASH_SECRET_KEY` to a random value immediately.

## PoC
For simplicity, it is easiest to forge a password reset link for Redash. We can do this with a bit of Python. To get the reset link for user ID 1, we simply run:
```
>>> from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
>>> serializer = URLSafeTimedSerializer("███")
>>> serializer.dumps(str("1"))
'███'
```

Then, we can browse to `https://jarvis-new.urbanclap.com/reset/█████` and choose a new password for user ID 1. This then logs us into their account.

## Impact

Since this is connected to all of your databases, this is likely a significant leak of PII and other sensitive information. This is easily a critical issue.

## Attachments
No attachments
