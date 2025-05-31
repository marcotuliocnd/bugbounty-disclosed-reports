# HTTP multi-header compression denial of service

## Report Details
- **Report ID**: 1886139
- **URL**: https://hackerone.com/reports/1886139
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-24T15:02:31.204Z
- **Disclosed**: 2023-02-24T23:04:06.173Z

## Reporter
- **Username**: monnerat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
A server can send an HTTP response with many occurrences of Transfer-Encoding and/or Content-Encoding headers. Each listed encoding allocates a buffer. The number of encodings listed within each header is already limited but the number of headers is not, allowing an HTTP response to consume all available memory.

## Impact

Consumes all available memory, resulting in a DoS.

## Attachments
No attachments
