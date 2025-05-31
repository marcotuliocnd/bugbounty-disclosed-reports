# IDOR when editing users leads to Account Takeover without User Interaction at CrowdSignal

## Report Details
- **Report ID**: 915114
- **URL**: https://hackerone.com/reports/915114
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-07-04T01:52:20.526Z
- **Disclosed**: 2020-11-18T14:23:32.970Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
If you click `Edit` button on any user of your team at https://app.crowdsignal.com/users/list-users.php, you will send a GET request to `https://app.crowdsignal.com/users/invite-user.php?id=(userid)&popup=1`
In this endpoint, `id` parameter is vulnerable for IDOR. When you change the user ID, you will see victim's email in response like that :
{F893392}
And if you click `Update Permissions` button, you will log-in to victim's account directly.
Also, user IDs are sequential. And they have a simple range with `00010006` to `19920500+`

## Steps To Reproduce:

  1. Log-in to your team account at CrowdSignal
  1. Go to https://app.crowdsignal.com/users/invite-user.php?id=19920465&popup=1
  1. You will see my email, and if you click `Update Permissions`, you will takeover my account.
  1. You can change the user ID to random number with `00010006` - `19920500` range.

## Impact

IDOR leads to account takeover without user interaction

Thanks,
Bugra

## Attachments
- idor.PNG
