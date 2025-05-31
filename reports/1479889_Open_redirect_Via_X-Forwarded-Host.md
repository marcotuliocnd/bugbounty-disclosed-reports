# Open redirect Via X-Forwarded-Host

## Report Details
- **Report ID**: 1479889
- **URL**: https://hackerone.com/reports/1479889
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-02-13T07:20:16.330Z
- **Disclosed**: 2024-11-17T10:08:25.555Z

## Reporter
- **Username**: ndizon_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
## Summary:
I have found this bug since feb. 8,2022, when my open redirect in https://dashboard.omise.co got duplicated
here where I first bug report my bug( https://hackerone.com/reports/1470535 ) since nobody response that's why I made new report for it.

## Steps To Reproduce:
[add details for how we can reproduce the 
  1. Open https://link.omise.co
  2. Capture the request of the site
  3.  Add this `X-Forwarded-Host: example.com` below Host
  4. Now you will get redirected in the site

## Supporting Material/References:


  * [attachment / reference]

## Impact

An attacker can use this to make the user go to malicious website.

## Attachments
No attachments
