# Denial of Service: nghttp2 use of uninitialized pointer

## Report Details
- **Report ID**: 335608
- **URL**: https://hackerone.com/reports/335608
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-04-10T18:46:30.736Z
- **Disclosed**: 2020-02-13T23:47:23.557Z

## Reporter
- **Username**: jasnell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
While investigating https://hackerone.com/reports/335533 and while following the same reproduction steps, I uncovered a bug in nghttp2 that causes use of an uninitialized pointer for an altsvc frameresulting in crash. The error can be easily triggered by a remote attacker by sending malformed ALTSVC and GOAWAY frames to the server, or by a malicious server sending same to the client. For Node.js, the result is a crashed process. The report has been submitted to the nghttp2 author who is working on a fix and is working on a fixed release.

## Impact

Crashing the Node.js process causing a Denial of Service

## Attachments
No attachments
