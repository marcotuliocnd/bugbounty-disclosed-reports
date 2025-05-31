# Denial of Service by memory exhaustion in net/imap

## Report Details
- **Report ID**: 3108869
- **URL**: https://hackerone.com/reports/3108869
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-04-26T16:00:42.715Z
- **Disclosed**: 2025-04-27T15:10:47.800Z

## Reporter
- **Username**: masamune_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Summary

There is a possibility for denial of service by memory exhaustion when net-imap reads server responses. At any time while the client is connected, a malicious server can send can send a "literal" byte count, which is automatically read by the client's receiver thread. The response reader immediately allocates memory for the number of bytes indicated by the server response.

This should not be an issue when securely connecting to trusted IMAP servers that are well-behaved. It can affect insecure connections and buggy, untrusted, or compromised servers (for example, connecting to a user supplied hostname).

## Details
The IMAP protocol allows "literal" strings to be sent in responses, prefixed with their size in curly braces (e.g. {1234567890}\r\n). When Net::IMAP receives a response containing a literal string, it calls IO#read with that size. When called with a size, IO#read immediately allocates memory to buffer the entire string before processing continues. The server does not need to send any more data. There is no limit on the size of literals that will be accepted.

## Impact

Memory exhaustion leading to program crash or system instability

## Attachments
No attachments
