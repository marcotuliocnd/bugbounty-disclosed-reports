# Assertion failed in node::http2::Http2Session::~Http2Session() leads to HTTP/2 server crash

## Report Details
- **Report ID**: 2453328
- **URL**: https://hackerone.com/reports/2453328
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-04-08T20:41:07.954Z
- **Disclosed**: 2024-04-29T21:01:40.904Z

## Reporter
- **Username**: bart
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
An attacker can make the Node.js HTTP/2 server completely unavailable by sending a small amount of HTTP/2 frames packets with a few HTTP/2 frames inside. It is possible to leave some data in nghttp2 memory after reset when headers with HTTP/2 CONTINUATION frame are sent to the server and then a TCP connection is abruptly closed by the client triggering the Http2Session destructor while header frames are still being processed (and stored in memory) causing a race condition.

* Advisory: https://nodejs.org/en/blog/vulnerability/april-2024-security-releases
* HackerOne report: 2319584

## Impact

Server crashes instantly after sending a few HTTP/2 frames.

## Attachments
No attachments
