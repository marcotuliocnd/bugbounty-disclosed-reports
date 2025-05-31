# Pause-based desync in Apache HTTPD

## Report Details
- **Report ID**: 1667974
- **URL**: https://hackerone.com/reports/1667974
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-08-12T17:34:36.518Z
- **Disclosed**: 2022-08-25T07:02:46.335Z

## Reporter
- **Username**: albinowax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Apache was vulnerable to a pause-based desync. This vulnerability is described in detail in my whitepaper here: https://portswigger.net/research/browser-powered-desync-attacks#pause

## Impact

This enables server-side HTTP Request Smuggling when Apache is deployed as a back-end server, and it also enables MITM attackers to inject arbitrary JavaScript in spite of TLS.

## Attachments
No attachments
