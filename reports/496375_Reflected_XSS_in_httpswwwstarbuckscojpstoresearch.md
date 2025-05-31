# Reflected XSS in https://www.starbucks.co.jp/store/search/

## Report Details
- **Report ID**: 496375
- **URL**: https://hackerone.com/reports/496375
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-15T07:09:59.135Z
- **Disclosed**: 2019-05-22T16:54:28.693Z

## Reporter
- **Username**: wa1m3im
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Please indicate NA, if not applicable. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** 
I found a Refrect XSS in store locator pages.


**Description:**
This vulnerability would allow a user to insert javascript payloads which can be reflected in a browser.

## Steps To Reproduce:

1. Go to https://www.starbucks.co.jp/store/search/?free_word=%22%3E%3Cscript%3Ealert()%3C/script%3E%3E



## Reproduction environment
Firefox 65.0

## Impact

It is possible to run arbitrary javascript.


Thank you.

## Attachments
- alert.png
