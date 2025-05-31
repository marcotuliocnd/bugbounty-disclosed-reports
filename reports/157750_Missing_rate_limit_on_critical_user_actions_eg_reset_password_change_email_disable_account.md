# Missing rate limit on critical user actions e.g. reset password, change email, disable account.

## Report Details
- **Report ID**: 157750
- **URL**: https://hackerone.com/reports/157750
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-09T03:33:15.107Z
- **Disclosed**: 2019-04-11T18:20:39.979Z

## Reporter
- **Username**: rohitdua
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi

I found that there are no rate limitations present on actions that require a password inside the account settings.
Actions:
[Paypal email change](https://hackerone.com/settings/bounties)
[Account email change](https://hackerone.com/settings/email/edit)
[Password Change](https://hackerone.com/settings/pass/edit)
[Disable Account](https://hackerone.com/settings/disable) *(this will not be useful to attacker)*

These sensitive actions require additional verification of password so as to protect the user even if the account is left open and is accessed by an attacker.
The attacker can try the dictionary attack *(or infinite wild guessing)*  with multiple threads on password on any of these actions without getting rate limited or locked out.

## Attachments
No attachments
