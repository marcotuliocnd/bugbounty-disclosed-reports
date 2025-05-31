# Subdomain takeover in GitLab Pages [george.ratelimited.me]

## Report Details
- **Report ID**: 2523677
- **URL**: https://hackerone.com/reports/2523677
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-05-28T21:30:00.118Z
- **Disclosed**: 2024-08-11T18:04:13.985Z

## Reporter
- **Username**: fdeleite
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
It's possible to take over subdomains that point to GitLab Pages. While adding a subdomain no verification of domain ownership is required.

## POC Steps 

1. Go to http://george.ratelimited.me/ (tested in Firefox)


{F3307364}

## Impact

Attackers could perform several attacks like:

  -  Cookie Stealing
  - Phishing campaigns.
  -  Bypass Content-Security Policies and CORS.

## Attachments
- image.png
