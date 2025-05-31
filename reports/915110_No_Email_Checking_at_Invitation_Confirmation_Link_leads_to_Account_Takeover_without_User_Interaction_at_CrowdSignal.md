# No Email Checking at Invitation Confirmation Link leads to Account Takeover without User Interaction at CrowdSignal

## Report Details
- **Report ID**: 915110
- **URL**: https://hackerone.com/reports/915110
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-07-04T01:36:04.584Z
- **Disclosed**: 2020-11-18T14:23:12.728Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
When you have a team account, you can invite users to your team from https://app.crowdsignal.com/users/list-users.php
If you invite a user, you will see this :
{F893386}
As you can see, there is confirmation link and we can see it from our dashboard.
And if you invite existing email in website, you can see the confirmation link again. And in this link, there is no e-mail check, when you click to confirmation link, you will log-in to victim's account without any error, credentials.

## Steps To Reproduce:

  1. Go to https://app.crowdsignal.com/users/list-users.php with your team account
  1. Invite an existing email (write victim's email)
  1. And click to confirmation link with your account
  1. You will log-in to victim's account directly

## PoC video :
{F893388}

## Impact

Account Takeover without user interaction

Thanks,
Bugra

## Attachments
- 1.PNG
- CrowdSignalATO.mp4
