# Password Change not notified when changed from settings

## Report Details
- **Report ID**: 242846
- **URL**: https://hackerone.com/reports/242846
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-24T08:34:18.654Z
- **Disclosed**: 2019-02-08T19:09:55.689Z

## Reporter
- **Username**: karthik87mit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi,

Password change is not notified to the account owner if its made from the account settings. This is very crucial as once the account is compromised, the attacker can change the password without giving any clue to the victim.

Steps to reproduce the issue:

1. Sign in with a valid username and password to www.starbucks.com
2. Go to your settings and personal info.
3. click change your password
4. Change your password
5. Looks for notification in your email.
6. No emails are sent.

Can be reproducible with all valid accounts.

Password changed via the forgot password reset flows are notified while this notification is missing. 

Thanks,
Karthik

## Attachments
No attachments
