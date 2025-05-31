# Permanent DoS with one click.

## Report Details
- **Report ID**: 975827
- **URL**: https://hackerone.com/reports/975827
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-06T19:07:58.328Z
- **Disclosed**: 2020-11-19T07:45:47.650Z

## Reporter
- **Username**: asdasdasdasdasda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hello Team, messages of a user who deletes their account leave DoS effects on another user.


## Platform(s) Affected:
[website/mobile app/service]

## Steps To Reproduce & PoC:
Before you start testing, create two accounts.
cyanpiny+attacker@gmail.com
cyanpiny+victim@gmail.com
Confirm e-mails to send messages.

  1. Log into the attacker's account.
  2. Message the victim from the attacker's account.
  3. Delete the attacker's account.
  4. Log into the victim's account.
  5. Check the victim's message box.
  6. The victim cannot use the account again.

Video:
{F978195}

## Impact

The victim cannot use the account again.

## Attachments
- Tumblr-DoS.mp4
