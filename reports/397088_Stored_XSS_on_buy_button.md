# Stored XSS on buy button

## Report Details
- **Report ID**: 397088
- **URL**: https://hackerone.com/reports/397088
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-08-19T18:20:45.555Z
- **Disclosed**: 2018-09-29T17:31:26.349Z

## Reporter
- **Username**: tony_tsep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I found an XSS vulnerability on buy button.
**Steps to reproduce**
Go to Settings > General > Store currency > Change formatting and add on "HTML with currency" the payload `€{{amount}} "><img src=x onerror=prompt(document.domain)>`
After that go to buy button and you will see that the payload triggers there.

## Impact

A staff member can takeover another account.

## Attachments
- xss.png
