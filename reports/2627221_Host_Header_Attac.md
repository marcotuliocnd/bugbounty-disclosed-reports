# Host Header Attac

## Report Details
- **Report ID**: 2627221
- **URL**: https://hackerone.com/reports/2627221
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-27T09:00:23.478Z
- **Disclosed**: 2025-02-08T19:47:29.344Z

## Reporter
- **Username**: n_ob_o_dy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
The application is vulnerable to Host Header Injection. An attacker can manipulate the Host header to redirect users to arbitrary domains or potentially poison web caches.
Steps to reproduce:
-------------------
1. Navigate to https://rubygems.org/ and intercept the request.
1. Add header ==Forwarded: host=evil.com== and forward the request.
1. Notice you will be redirect to attacker's malicious website.

## Impact

Successful exploitation can lead to user redirection to malicious sites, phishing attacks, and potential data loss. The overall impact of a Host Header attack can be significant, leading to financial loss, reputational damage, and legal consequences. It's crucial to address this vulnerability promptly to protect users and systems.

## Attachments
- Recording__1.mp4
