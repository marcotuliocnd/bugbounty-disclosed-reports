# Open redirect while disconnecting Email

## Report Details
- **Report ID**: 238117
- **URL**: https://hackerone.com/reports/238117
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-08T17:12:28.261Z
- **Disclosed**: 2017-06-08T19:10:55.468Z

## Reporter
- **Username**: atruba
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi team, 
there is a open redirect end point when any account owner disconnect email accounts. He is redirected to some other domain.

Vulnerable URL

https://demo.weblate.org/accounts/disconnect/email/2354/?next=http://google.com
POC

Steps:
Go to authentication tab.
Disconnect Email account and capture the request.
Now, after next= write https://evil.com.
You are redirected to evil.com

Thanks,

## Attachments
No attachments
