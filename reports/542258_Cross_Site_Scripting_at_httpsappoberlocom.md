# Cross Site Scripting at https://app.oberlo.com/

## Report Details
- **Report ID**: 542258
- **URL**: https://hackerone.com/reports/542258
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-18T21:25:51.107Z
- **Disclosed**: 2019-05-26T22:25:25.725Z

## Reporter
- **Username**: masterhackor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
1- create an account from **https://app.oberlo.com/**

2- path to https://app.oberlo.com/settings/account/profile

3- inject javascript code or xss payload at **Name** form

4- it will be printed at page and executed

payload that i used it **"><img src=x onerror=alert(document.domain)>**

## Impact

This vulnerability can be used by attacker to serve malicious JavaScript against any user.

## Attachments
- xss-poc.jpg
