# Bruteforce password recovery code

## Report Details
- **Report ID**: 743545
- **URL**: https://hackerone.com/reports/743545
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-11-21T17:54:12.936Z
- **Disclosed**: 2020-01-18T17:45:58.360Z

## Reporter
- **Username**: 0x3c3e
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
## Summary
It's possible to bruteforce recovery code from SMS as iOS application doesn't have limits for incorrect inputs. I have tried 50+ different combinations until I reached code from SMS.

## Steps To Reproduce
1. Click "Use another option" on application startup view
1. Enter your phone number
1. Click "Forgotten number"
1. Click "OK" on pop-up window
1. Bruteforce 4 digits code 

## PoC video
https://youtu.be/QV80pD0wZsE

## Mitigation
1. Limit quantity of attempts to enter recovery code
1. Don't store recovery code on target device to compare it with user's input

## Details
Devices: Iphone SE (13.2), Iphone 6s (12.4)
App: Bumble (5.140.0)

## Impact

Account takeover.

## Attachments
No attachments
