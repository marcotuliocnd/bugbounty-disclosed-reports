# Apache HTTP Server: mod_proxy_ajp: Possible request smuggling

## Report Details
- **Report ID**: 1594627
- **URL**: https://hackerone.com/reports/1594627
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-08T10:29:46.620Z
- **Disclosed**: 2022-07-09T19:25:47.839Z

## Reporter
- **Username**: ricterz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Inconsistent Interpretation of HTTP Requests ('HTTP Request Smuggling') vulnerability in mod_proxy_ajp of Apache HTTP Server allows an attacker to smuggle requests to the AJP server it forwards requests to.  This issue affects Apache HTTP Server Apache HTTP Server 2.4 version 2.4.53 and prior versions.

## Impact

Information disclosure, RCE

## Attachments
No attachments
