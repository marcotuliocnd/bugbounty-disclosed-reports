# Reflected XSS - gratipay.com

## Report Details
- **Report ID**: 262852
- **URL**: https://hackerone.com/reports/262852
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-24T06:46:14.853Z
- **Disclosed**: 2017-08-24T23:01:51.105Z

## Reporter
- **Username**: tungpun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
# Summary

I would like to report a Reflected XSS on gratipay.com.

# Browsers Verified In

  * Firefox 55.0.2 (up to date)

# Steps To Reproduce

  Goto this URL:
`https://gratipay.com/on/npm/cx%00A<svg onload=alert(1)>`

{F215426}

## Attachments
- Screen_Shot_2017-08-24_at_2.44.20_PM.png
