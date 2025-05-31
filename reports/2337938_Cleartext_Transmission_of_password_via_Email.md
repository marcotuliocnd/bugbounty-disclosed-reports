# Cleartext Transmission of password via Email

## Report Details
- **Report ID**: 2337938
- **URL**: https://hackerone.com/reports/2337938
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-01-28T14:57:16.628Z
- **Disclosed**: 2024-04-22T04:21:38.560Z

## Reporter
- **Username**: tuannq_gg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sheer_bbp

## Vulnerability Information
## Summary:
After successfully signup as a fan, the password was then sent to email by cleartext

## Steps To Reproduce:
1. After successfully signup as a fan, check the email and see that the password was sent in cleartext, it does not appear in the UI, just F12 and you can see the user password
{F3012123}

## Impact

If the mail channel was sniffed, the attacker can compromise user accounts easily

## Attachments
- image.png
