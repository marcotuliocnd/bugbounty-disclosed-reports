# Reflected XSS due to vulnerable version of sockjs

## Report Details
- **Report ID**: 1100326
- **URL**: https://hackerone.com/reports/1100326
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-10T19:29:54.986Z
- **Disclosed**: 2022-04-29T17:38:24.702Z

## Reporter
- **Username**: chip_sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
There is reflected XSS on *.simperium.com. The bug exists due to a vulnerable version of sockjs library.

## Platform(s) Affected:
simperium.com
js.simperium.com

## Steps To Reproduce:
  1. Visit https://simperium.com/sock/1/0/0/0/htmlfile?c=alert('XSS')//
  2. You will see an alert message because of executed JS

## Impact

XSS may be used by an attacker to perform a lot of things, for example, to steal user session

## Attachments
- XSS.PNG
