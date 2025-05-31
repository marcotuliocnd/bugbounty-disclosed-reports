# HackerOne Staging uses Production data for testing

## Report Details
- **Report ID**: 1392511
- **URL**: https://hackerone.com/reports/1392511
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-11-05T17:15:10.769Z
- **Disclosed**: 2021-11-05T20:52:15.780Z

## Reporter
- **Username**: tk0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Today I received an email related to smart rewards from HackerOne. This included staging environment details, such as:

```
sender: no-reply+staging@hackerone.com
Privacy / Terms links pointing to domain: https://www.enorekcah.com/...
``` 

This basically tells us that HackerOne is using hacker data (real users) in their lower environment (STAGING). Usually this should be avoided and production data should not be copied into lower environments -> using live data for testing.

See attachment which holds a copy of received email: ████

## Impact

Privacy issues related to customer/hacker data in HackerOne.

Cheers!
@tk0

## Attachments
No attachments
