# Apache HTTP Server: HTTP/2 DoS by memory exhaustion on endless continuation frames

## Report Details
- **Report ID**: 2453322
- **URL**: https://hackerone.com/reports/2453322
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-04-08T20:33:40.580Z
- **Disclosed**: 2024-04-24T18:29:50.989Z

## Reporter
- **Username**: bart
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I'd like to report Apache httpd vulnerability (CVE-2024-27316) that was recently fixed.
* Advisory: https://httpd.apache.org/security/vulnerabilities_24.html

## Impact

HTTP/2 incoming headers exceeding the limit are temporarily buffered in nghttp2 in order to generate an informative HTTP 413 response. If a client does not stop sending headers, this leads to memory exhaustion.

## Attachments
No attachments
