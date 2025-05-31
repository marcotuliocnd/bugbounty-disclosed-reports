# Stored XSS on app.crowdsignal.com  your-subdomain.crowdsignal.net via Thank You Header

## Report Details
- **Report ID**: 1842822
- **URL**: https://hackerone.com/reports/1842822
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-22T00:03:41.265Z
- **Disclosed**: 2023-02-24T10:33:03.068Z

## Reporter
- **Username**: 0xwega74
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi, I hope you're having a good day.

I found an Stored XSS at app.crowdsignal.net.

## Platform(s) Affected:
app.crowdsignal.net

## Steps To Reproduce:

  1. Go to https://app.crowdsignal.com/dashboard and create a project
  1. Add any thing to the project and publish the project and intercept the request while publishing.
  1. Edit the Thank You Header with this payload `<a href='javascript:alert(document.domain);'>Click Me</a>`
  1. Open the Project you published and fill the form and click submit you will be redirected to thank you page click at the button and the XSS will fired.

## Supporting Material/References:

████████

## Impact

Stored XSS

## Attachments
No attachments
