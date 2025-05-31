# Able to upload backgrounds before entering 2FA

## Report Details
- **Report ID**: 1080839
- **URL**: https://hackerone.com/reports/1080839
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-18T14:02:39.350Z
- **Disclosed**: 2021-02-03T14:37:30.631Z

## Reporter
- **Username**: mr_vrush
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
Hi Team, 
I am able to see and use uploaded backgrounds and able to upload new ones without proper authentication of 2FA. I hope you remember this report #993786.

## Steps To Reproduce:

  1. Login with a steam account and enable 2FA.
  1. Now logout your account. Clear all the cookies.
  1. Now again login into your account now don't enter the 2FA code.
  1. Go to the 3d.cs.money
  1. If you are a Prime subscriber you are able to upload the custom backgrounds by pressing the "ctrl+v" combination. If you have already uploaded some backgrounds you are able to see those too.

## Supporting Material/References:
Please check the attachment F1162263.

## Impact

Able to access subdomain without proper authentication.
It should be accessible after the proper authentication.
Thanks

## Attachments
- recording-1610978030099.webm
