# Open Redirect filter bypass through '\' character via URL parameter

## Report Details
- **Report ID**: 840736
- **URL**: https://hackerone.com/reports/840736
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-05T19:25:29.379Z
- **Disclosed**: 2020-04-06T15:39:02.330Z

## Reporter
- **Username**: droop3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: myndr

## Vulnerability Information
Hi, I hope I find you all safe and good regarding those hard times nowadays.

## Summary:
Found an Open Redirect vulnerability on http://meta.myndr.net by bypassing the trusted domain filter using a '\' character.

I was able to get the original redirection URL from the register button located at http://dashboard.myndr.net/auth/login

Original Redirection URL
```http://meta.myndr.net/latest/meta-data/filter-id/add?ref_url=http://dashboard.myndr.net/auth/register?id= ```

Malicious URL 
```http://meta.myndr.net/latest/meta-data/filter-id/add/?ref_url=http://phishing.com\dashboard.myndr.net/../../../ ```

The vulnerable URL parameter is ```ref_url```

The trusted domain (or string) is ```dashboard.myndr.net```

It can be bypassed only from its beginning!  (between ```http://``` and the string) and not after ```.net```

## Steps To Reproduce:
Navigate to : ```http://meta.myndr.net/latest/meta-data/filter-id/add/?ref_url=http://phishing.com\dashboard.myndr.net/../../../```

You will be redirected to ```phising.com``` domain

## PoC: attached to the report

## Impact

1. Phishing campaigns can be initiated using such a vulnerability
2. It is an efficient way to bypass monitoring and email filters within an organization (the organization can check the "trust" level of each domains that they receive emails from)

## Attachments
- Screencast_04-05-2020_03_17_46_PM.webm
