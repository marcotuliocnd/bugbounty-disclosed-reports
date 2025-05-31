# Stored XSS via ' profile ' at ███

## Report Details
- **Report ID**: 1921606
- **URL**: https://hackerone.com/reports/1921606
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-03-28T15:45:33.929Z
- **Disclosed**: 2023-06-23T14:59:03.530Z

## Reporter
- **Username**: 0xs4m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mars

## Vulnerability Information
hi team 
i found stored xss on profile 

1. Go to registration page  (██████)
2. Verified your account.
3. Go to login page and login your account.

For the fastly test, use this credentials to login (my test account)

█████████ For Attacker 

email: █████████
pass: Password
████ For Victime

email: █████████
pass: password

After login i change animal name to payload xss .. i open victime account and i put attacker profile url so i succeeded.

██████████

## Impact

Stored Cross Site Scripting which attacker can execute malicious javascript payload.

## Attachments
No attachments
