# Unauthenticated access to webmail at maildev.happytools.dev leading to compromised wordpress site api.happytools.dev [RCE]

## Report Details
- **Report ID**: 1067547
- **URL**: https://hackerone.com/reports/1067547
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-28T17:39:22.701Z
- **Disclosed**: 2021-02-01T15:37:32.327Z

## Reporter
- **Username**: superman85
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Dear Team,

Today when I trying to find bugs on happy tools I have found 2 domains below for staging environment
- https://maildev.happytools.dev
- https:// api.happytools.dev

Two websites above ssl certificate was expired. But you can adjust your date-time to 02/02/2020 or before that time to access those sites normally

## Platform(s) Affected:
https:// api.happytools.dev

## Steps To Reproduce:

  1. https://api.happytools.dev/wp-login.php?action=lostpassword and forgot password for user `api`
  1. Go to https://maildev.happytools.dev to get reset password link and set new password for user `api` (I did not try to do that)
  1. After changing password for user `api`, we can control wordpress cms and may upload plugins/themes contain backdoor or harmful scripts to this server

## Supporting Material/References:
Some screen shots PoC

{F1132811}

{F1132810}

████████

## Impact

Takeover wordpress site api.happytools.dev

## Attachments
- forgot_pass_2.png
- forgot_pass_1.png
