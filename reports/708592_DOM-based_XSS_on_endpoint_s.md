# [█████] — DOM-based XSS on endpoint `/?s=`

## Report Details
- **Report ID**: 708592
- **URL**: https://hackerone.com/reports/708592
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-06T16:14:32.973Z
- **Disclosed**: 2019-12-02T20:02:45.805Z

## Reporter
- **Username**: usamasood
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Description

GET parameter `s` is vulnerable to DOM-based XSS on endpoint `/?s=`. XSS affects all users and no authentication or login is required.

## Proof of Concept

Visit the following URL for PoC:

https://██████/?s=%27%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

█████████

## Explanation

This DOM-based XSS vulnerability is due to lack of sanitization on the input fetched via search input field. 

Responsible JS file for this issue is:
`https://██████/wp-content/themes/iase/js/search.js`

On line 12, `var $search = ...` is getting input from the Search field but there is no sanitization for single quote which leads to this XSS vulnerability when it is appended.

█████

## Impact

An attacker can take over an account of an authenticated user by stealing any anti-CSRF tokens and using that token to takeover an account.

## Attachments
No attachments
