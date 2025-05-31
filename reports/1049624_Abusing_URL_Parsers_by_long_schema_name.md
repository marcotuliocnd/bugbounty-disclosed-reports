# Abusing URL Parsers by long schema name

## Report Details
- **Report ID**: 1049624
- **URL**: https://hackerone.com/reports/1049624
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-12-03T11:02:57.081Z
- **Disclosed**: 2021-01-08T08:28:15.494Z

## Reporter
- **Username**: d4d
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
There is known technique to exploit inconsistency of URL parser and URL requester logic to perform Server Side Request Forgery attack. Firstly it was presented by Orange Tsai at [A New Era Of SSRF Exploiting URL Parser](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf). Firstly I found the familiar issue at old versions of curl, but exploit did not seems works at latest releases. But now I'm ready to share new exploit of issue.

## Steps To Reproduce:
Schema parser logic of curl library is vulnerable to "Abusing URL Parsers". Malicious user can use this weakness to bypass whitelist protection and perform Server Side Request Forgery against targets, that use vulnerable version of library.

  1. curl "ssrf3.twowaysyncapp.tk://google.com"  Protocol "ssrf3.twowaysyncapp.tk" not supported or disabled in libcurl
  1. curl "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.twowaysyncapp.tk://google.com" Host aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.twowaysyncapp.tk requested

## Supporting Material/References:
Details about attack presented at https://btlfry.gitlab.io/owasp/#/21 The main difference at new version of library subdomain name should be much longer.

  * F1102530

## Impact

Incorrect schema parser logic will allow malicious user to bypass protection mechanism and get access to the internal infrastructure of affected web servers.

## Attachments
- curl.png
