# Malformed HTTP/2 SETTINGS frame leads to reachable assert

## Report Details
- **Report ID**: 800140
- **URL**: https://hackerone.com/reports/800140
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-02-20T00:15:45.906Z
- **Disclosed**: 2020-07-03T14:43:57.323Z

## Reporter
- **Username**: jzebor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
I do not expect any form of cash bounty for this issue. If we have discovered a unique vulnerability I only ask that Jordan Zebor and Adam Cabrey of F5 Networks be crediting with finding the issue.

**Summary:** A reachable assert in the NodeJS HTTP/2 implementation can result in a denial of service. 

**Description:** Attackers can send a series of malformed HTTP/2 SETTINGS frames to reach an assertion in code, causing the node process to exit with SIGABRT. This has been observed in v13.8.0 and v14.0.0-nightly20200213e23b12e130.

## Steps To Reproduce:
1) Create an example HTTP/2 server. I used the example code from here https://nodejs.org/api/http2.html#http2_http2_createsecureserver_options_onrequesthandler

2) Create an example client to send the attached cases in a loop. In this case, I used an internal fuzz testing tool that I unfortunately cannot share but I can attach the test cases which I sent. We discovered that by sending a malformed SETTINGS frame over and over (roughly 25 in a row) the node process will SIGABRT. 

3) Observe node process crash after series of requests are sent. I can consistently trigger this issue in 13.8.0 and 14.0.0. I will provide a stack trace, stack trace when run under valgrind, and the test case I used to reproduce the issue. If the core file is needed I can provide that as well.

I believe this is where the assertion is triggered.
https://github.com/nodejs/node/blob/f3682102dca1d24959e93de918fbb583f19ee688/src/node_http2.cc#L1521

## Impact: A reachable assert which leads to SIGBART of the entire node process. It's a denial of service issue.

## Supporting Material/References:
Notice with the attached examples are prefixed with the order in which they were sent. If you already know how to do all the connection preface setup then simply send the settings anomaly frame on a new connection over and over again. A visual representation of the settings frame which causes the issue can be seen in "SETTINGS_FRAME_DETAILS.png".

## Impact

A reachable assert which leads to SIGBART of the entire node process. It's a denial of service issue that an unauthenticated attacker can easily achieve. The CVSS calculator on this portal seems to be classifying the issue as "Critical", which I don't agree with. I believe this to be a "High" severity issue with this CVSS score - https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H

## Attachments
- 1_connection_preface_frame
- 2_headers_frame
- 3_server_settings_ack_frame
- 4_settings_anomaly
- SETTINGS_FRAME_DETAILS.png
