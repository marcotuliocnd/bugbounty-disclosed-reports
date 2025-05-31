# reflected xss in https://wordpress.com/start/account/user

## Report Details
- **Report ID**: 2055132
- **URL**: https://hackerone.com/reports/2055132
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-07T15:28:52.463Z
- **Disclosed**: 2023-11-15T11:22:58.648Z

## Reporter
- **Username**: secureighty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
xss after login at https://wordpress.com/start/account/user?variationName=free&redirect_to=javascript:alert(document.domain)

## Platform(s) Affected:
web

## Steps To Reproduce:

  1. auth normally
  1. go to https://wordpress.com/start/account/user?variationName=free&redirect_to=javascript:alert(document.domain) **while already authenticated** and click continue
  1. xss procs

## Supporting Material/References:

█████

## Impact

XSS can be used to steal cookies, modify html content, and much more

## Attachments
No attachments
