# Reflected XSS on delivery.glovoapp.com

## Report Details
- **Report ID**: 1264805
- **URL**: https://hackerone.com/reports/1264805
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-15T23:55:35.008Z
- **Disclosed**: 2021-08-18T07:02:21.112Z

## Reporter
- **Username**: celesian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glovo

## Vulnerability Information
## Summary:
Hi, there's a reflected XSS vulnerability present on the https://delivery.glovoapp.com/referrals/ endpoint.

## Steps To Reproduce:
Opening the following URL should trigger the prompt() window specified in the request parameters, indicating that arbitrary javascript can be injected into the page.
- https://delivery.glovoapp.com/referrals/?email=%22%3E%3CsCriPt%20class%3Ddalfox%3Eprompt%281%29%3C%2Fscript%3E&lang=rs

## Impact

An attacker can do several client-side attacks on Glovo customers.

## Attachments
No attachments
