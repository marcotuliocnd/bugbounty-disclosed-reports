# HTML injection in email content during registration via FirstName/LastName parameter

## Report Details
- **Report ID**: 1256496
- **URL**: https://hackerone.com/reports/1256496
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-09T22:41:59.868Z
- **Disclosed**: 2021-12-18T09:42:30.575Z

## Reporter
- **Username**: ibrahimatix0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hi,
I just found an issue when register account in https://mtnmobad.mtnbusiness.com.ng/#/auth/registerUser
It allows an attacker to inject malicious text include html code in email content.

## Steps To Reproduce:


  1. Go to https://uat.id.manulife.ca/mortgagecreditor/register?ui_locales=en-CA.
  1. Use the following payload as your First Name:
  1. Put the following code as first name:
```
<h1>Ibrahim</h1>
```
  1. Fill other forms and submit


  {F1371367}

## Impact

html code injection

## Attachments
- Capture.PNG
