#  Bypass Email verification for monitoring at `monitor.mozilla.org`

## Report Details
- **Report ID**: 2712583
- **URL**: https://hackerone.com/reports/2712583
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-09-11T19:34:42.543Z
- **Disclosed**: 2025-01-22T10:03:43.603Z

## Reporter
- **Username**: 0d_amrr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:

I've found that I can Bypass Email verification from the leaked verfication token at `/api/v1/user/breaches` At `monitor.mozilla.org`

## Steps To Reproduce:

  1. Add email address for monitoring 
  1.  it needs Email verification from the email owner
  1. Go to `/api/v1/user/breaches` , you'll find the whole data for the verified emails and also the unverified emails with the leaked of its verification token
██████
  1. Go to the verification endpoint `/api/v1/user/verify-email?token=<verification token>&utm_campaign=verified-subscribers&utm_content=account-verification-email&utm_source=fx-monitor&utm_medium=email` and add the verification token in `token` parameter
  1. BOOM, you can now monitoring that email without any permissions from the owner of that email

## POC:

████

## Impact

## Summary:
The attacker can monitor all the email of his vectims without permissions from the owner of that email to verify that

## Attachments
No attachments
