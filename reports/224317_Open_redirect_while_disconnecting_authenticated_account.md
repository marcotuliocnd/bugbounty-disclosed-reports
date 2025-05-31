# Open redirect while disconnecting authenticated account

## Report Details
- **Report ID**: 224317
- **URL**: https://hackerone.com/reports/224317
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-27T12:45:43.745Z
- **Disclosed**: 2017-06-08T16:43:46.455Z

## Reporter
- **Username**: gsecure
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi team, 
there is a open redirect end point when any account owner disconnect authenticated accounts say
google. He is redirected to some other domain.

Vulnerable URL
---
[demo.weblate.org/accounts/disconnect/google-oauth2/2335/?next=](demo.weblate.org/accounts/disconnect/google-oauth2/2335/?next=)

POC 
1. Go to authentication tab.
2. Disconnect Google account and capture the request.
3. Now, after next= write https://evil.com.
4. You are redirected to evil.com

video POC is attached.

Best Regards
Gurwinder

## Attachments
- weblate1
