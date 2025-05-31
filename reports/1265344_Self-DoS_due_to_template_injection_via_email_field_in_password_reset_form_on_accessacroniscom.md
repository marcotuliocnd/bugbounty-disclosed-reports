# Self-DoS due to template injection via email field in password reset form on access.acronis.com

## Report Details
- **Report ID**: 1265344
- **URL**: https://hackerone.com/reports/1265344
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-07-16T12:29:55.664Z
- **Disclosed**: 2022-05-03T06:41:50.169Z

## Reporter
- **Username**: sudo_bash
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
HI acronis security team , how are you
I hope everyone is OK in the other side of the screen .
I found Template Injection in [https://access.acronis.com/reset_password/new] via the mail input .

## Steps To Reproduce:

 1. Open [https://access.acronis.com/reset_password/new] and Enter the mail Payload : sudo_bash{{8*8}}@wearehackerone.com
 2. After submite the mail , The resulte will Reflect in the page with the mail adress .

## Impact

- AngularJs CCTI may lead to xss .

## Attachments
- Template-Injection.png
- The_Injection_Result.png
- Template_Injection_Poc.mp4
