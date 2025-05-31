# IDOR  [mtnmobad.mtnbusiness.com.ng]

## Report Details
- **Report ID**: 1698006
- **URL**: https://hackerone.com/reports/1698006
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-09-12T13:25:43.161Z
- **Disclosed**: 2022-10-13T07:18:08.412Z

## Reporter
- **Username**: insomnia_hax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Steps To Reproduce:

  1.  Go to https://mtnmobad.mtnbusiness.com.ng/#/dashboard/home with burp proxy
  1. Intercept a POST request to /app/dashboardData and review its response you will see emails and ids 
  1. Go to https://mtnmobad.mtnbusiness.com.ng/#/userProfile
  1. change name, mobile, address etc. and intercept with burp proxy
  1. change the id and the email with victim's and forward the request
  1. The changes will be saved in the victim's account


# Note:

If you already know account's email and id you can skip step 1 and 2

## Supporting Material/References:

  {F1922714}

## Impact

An attacker can change every user's account information

## Attachments
- recording-1662989071964.webm
