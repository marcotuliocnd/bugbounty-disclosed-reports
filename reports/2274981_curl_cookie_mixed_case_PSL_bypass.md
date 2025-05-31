# curl cookie mixed case PSL bypass

## Report Details
- **Report ID**: 2274981
- **URL**: https://hackerone.com/reports/2274981
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-12-06T12:00:29.999Z
- **Disclosed**: 2023-12-22T04:11:01.031Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
A vulnerability in curl allows a malicious HTTP server to set "super cookies" in curl that are then passed back to more origins than what is otherwise allowed or possible. This allows a site to set cookies that then would get sent to different and unrelated sites and domains.

It could do this by exploiting a mixed case flaw in curl's function that verifies a given cookie domain against the Public Suffix List (PSL). For example a cookie could be set with domain=co.UK when the URL used a lowercase hostname curl.co.uk, even though co.uk is listed as a PSL domain.

## Impact

Issue supercookies bypassing the Public Suffix List check.

## Attachments
No attachments
