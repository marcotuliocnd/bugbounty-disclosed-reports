# Out of order TLS handshake / application data messages lead to segmentation fault

## Report Details
- **Report ID**: 335495
- **URL**: https://hackerone.com/reports/335495
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-04-10T15:22:13.135Z
- **Disclosed**: 2020-02-13T23:47:34.586Z

## Reporter
- **Username**: jzebor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** 
IMPORTANT NOTE: I have already been working with the NodeJS core security team on this issue and have provided core files, POC and many other pieces of information. I was told by James Snell to report via Hackerone to make it official however all the relevant details on this issue have already been provided to NodeJS team. This report will be minimal since all details are already with the team which needs them.

**Description:** Sending interleaved handshake messages in the TLS handshake OR sending TLS handshake messages AFTER the handshake has completed (after finished msg) causes a segmentation fault of the NodeJS process. This is present in v9 and v10, using TLS module. The issue can be exposed with servers which use TLS in normal "server authentication" mode AND servers which require mutual authentication (client certificates).


## Steps To Reproduce:

  1. Setup TLS server with node. 
  2. Perform a normal handshake but insert a Client Key Exchange message AFTER the TLS handshake finished message.
  3. Observe segmentation fault of node process.

Stacktrace, core file and reproduction script(s) have all been provided to Anna Henningsen on the NodeJS core team.

## Impact: Denial of service, seg fault leads to the node instance inability to service additional clients.

## Supporting Material/References: All of this has already been provided to Core NodeJS security team.

  * List any additional material (e.g. screenshots, logs, references, commits, code examples, etc.).

## Impact

Segmentation fault of the process leads to denial of service.

## Attachments
No attachments
