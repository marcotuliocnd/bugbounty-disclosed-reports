# IDOR when moving contents at CrowdSignal

## Report Details
- **Report ID**: 915127
- **URL**: https://hackerone.com/reports/915127
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-04T03:26:20.493Z
- **Disclosed**: 2020-11-18T14:22:49.381Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
You can move your contents via `Move to` button at https://app.crowdsignal.com/dashboard
And when you click to `Move to > My Content` you will send a POST request to `/dashboard` like that :

{F893407}

`actionable[]` parameter's value is the content's ID. And if you change this ID to victim's content ID, you will see victim's content at `My Content` page. But you can't see responses or edit it. You can only change status etc if you have a free account.

So I found another way to takeover victim's content completely via team account.
In team accounts, you have another move option that named `Move to another user`. Basically, you can move your contents to users (in your team) .
And if you follow same steps again but with `Move to another user` option, you can see victim's content in your team user's account.

**Please note, content IDs are sequential, so attacker can takeover any content.**

## Steps To Reproduce:
- **With Free account (limited access to victim's content)**
  1. Go to https://app.crowdsignal.com/dashboard
  1. Click to checkbox on your any content and turn on Intercept at Burp Suite
  1. Click to `Move to > My Content`
  1. And change `actionable[]` parameter's value with victim's content ID.
  1. Go to `My Content`.
- **With Team account (full access to victim's content)**
  1. Add your second email on https://app.crowdsignal.com/users/list-users.php and confirm it
  2. Go to https://app.crowdsignal.com/dashboard
  3. Click to checkbox on your any content and turn on Intercept at Burp Suite
  4. Click to `Move to > Move to another user`
  5. Select your second account, click `Move`
  6. Change `actionable[]` parameter's value with victim's content ID.
  7. Go to your second account and check dashboard

## PoC video for full access to victim's content:
{F893412}

## Impact

IDOR leads to takeover victim's content

Thanks,
Bugra

## Attachments
- request.PNG
- CrowdSignal-IDOR.mp4
