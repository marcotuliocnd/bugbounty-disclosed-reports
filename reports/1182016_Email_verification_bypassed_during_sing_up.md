# Email verification bypassed during sing up (████████)

## Report Details
- **Report ID**: 1182016
- **URL**: https://hackerone.com/reports/1182016
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-01T16:00:31.007Z
- **Disclosed**: 2021-08-19T15:50:43.553Z

## Reporter
- **Username**: ibrahimatix0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Normally ███ ask users to verify their email during registration but i found a way to bypass this so than an attacker can create accounts with emails that are not his own abusing the intigrity of MTN.
## Steps To Reproduce:

  1. Create an account with you owned email, verify it.
  1. Go ████ and change your email to the desired email you will not be asked to verify the ownership, in this case I changed mine to ```███████```.
  1. Email verification bypassed successfully.

## Supporting Material/References:

## Impact

This issue can be used to bypass email verification on signup. Attackers can create account on behalf on any person without having access to the email account.

## Attachments
No attachments
