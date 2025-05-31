# Signup with any email and enable 2FA without verifying email

## Report Details
- **Report ID**: 699200
- **URL**: https://hackerone.com/reports/699200
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-21T09:55:35.329Z
- **Disclosed**: 2020-04-23T12:35:27.346Z

## Reporter
- **Username**: rioncool22
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
##Description :
When i signup, i can enable 2FA without verification my email.

##Attack Scenario : 
1. The Attacker signup with the victim email.
2. Go to `Two factor authetication` and enable 2FA

## Impact

when the victim want to register in this [site](https://dashboard.omise.co/),  they can't, because they email claims by attacker.
and if the victim reset the password to get back the email, he can, but he can't login because need 2FA code.

## Attachments
No attachments
