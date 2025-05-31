# HTTP Request Smuggling due to CR-to-Hyphen conversion

## Report Details
- **Report ID**: 922597
- **URL**: https://hackerone.com/reports/922597
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-13T14:57:33.146Z
- **Disclosed**: 2020-10-17T19:15:29.014Z

## Reporter
- **Username**: amitklein
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** [add summary of the vulnerability]
Apparently, node.js converts CR in HTTP request headers to hyphen before parsing. This can lead to HTTP Request Smuggling as it is a non-standard interpretation of the header.

**Description:** [add more details about this vulnerability]
Consider an HTTP request with Content[CR]Length header . Suppose a proxy in front of node.js ignores the Content[CR]Length header (and therefore assumes a 0-length body). node, on the other hand, converts the CR to a hyphen and uses the value of the (newly formed...) Content-Length header. HTTP Request Smuggling ensues.

## Steps To Reproduce:
This is the HTTP stream that demonstrates the vulnerability:
GET / HTTP/1.1
Host: www.example.com
Content[CR]Length: 42
Connection: Keep-Alive

GET /proxy_sees_this HTTP/1.1
Something: GET /node_sees_this HTTP/1.1
Host: www.example.com

A proxy server that ignores the invalid Content[CR]Length header will assume that the body length is 0 (since there's no body length indication), and will thus transmit the stream up to (but not including) the GET /proxy_sees_this. It will wait for node to respond (which interestingly does happen, even though node.js does expect the body - perhaps on GET requests, the URL is invoked regardless of the body?), then the proxy forwards the second request (from its perspective) - the GET /proxy_sees_this. Node then silently discards the expected 42 bytes of the body of the first request, and thus starts parsing the 2nd request from GET /node_sees_this.
HTTP Request Smuggling ensues.

[Also, if you were able to find the piece of code responsible for this issue, please add a link to it in the source repository.]

## Impact: [add why this issue matters]
HTTP Request Smuggling can lead to web cache poisoning, session hijacking, cross site scripting, etc.

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, references, commits, code examples, etc.).

## Impact

HTTP Request Smuggling can lead to web cache poisoning, session hijacking, cross site scripting, etc.

## Attachments
No attachments
