# OTP reflecting in response sensitive data exposure leads to account take over

## Report Details
- **Report ID**: 1318087
- **URL**: https://hackerone.com/reports/1318087
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-08-24T17:10:12.801Z
- **Disclosed**: 2022-03-26T18:00:23.038Z

## Reporter
- **Username**: rupachandransangothi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
## Summary:
Sensitive data that is otp is reflecting in the response of phone number otp verification in https://app.upchieve.org 

## Steps To Reproduce:


  1. Signin with a account
  2.After signin it will ask for phone number for otp verification.
3.Capture the request using burpsuite and see the response 
4.Now otp is exposing in the response.
5.Account take over is happening.

## Impact

Any attacker can login into user account with his/her otp verification which is a high impact of this website.sensitive data is exposing here

## Attachments
- POC_sensitivedataexposure.png
