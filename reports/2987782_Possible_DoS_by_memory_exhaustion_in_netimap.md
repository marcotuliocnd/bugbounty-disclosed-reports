# Possible DoS by memory exhaustion in net/imap 

## Report Details
- **Report ID**: 2987782
- **URL**: https://hackerone.com/reports/2987782
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-02-11T08:22:26.514Z
- **Disclosed**: 2025-04-27T13:45:48.613Z

## Reporter
- **Username**: manun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Net::IMAP implements Internet Message Access Protocol (IMAP) client functionality in Ruby. Starting in version 0.3.2 and prior to versions 0.3.8, 0.4.19, and 0.5.6, there is a possibility for denial of service by memory exhaustion in `net-imap`'s response parser. At any time while the client is connected, a malicious server can send can send highly compressed `uid-set` data which is automatically read by the client's receiver thread. The response parser uses `Range#to_a` to convert the `uid-set` data into arrays of integers, with no limitation on the expanded size of the ranges. Versions 0.3.8, 0.4.19, 0.5.6, and higher fix this issue.

## Impact

This vulnerability causes Denial of Service by memory exhaustion for the projects using net-imap for connecting to an imap server.

## Attachments
No attachments
