# Http response is not ended although underlying socket is already destroyed

## Report Details
- **Report ID**: 676710
- **URL**: https://hackerone.com/reports/676710
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-08-19T16:11:10.534Z
- **Disclosed**: 2020-01-15T19:58:51.621Z

## Reporter
- **Username**: verdaster
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**
When node server receives http request and hooks to end, finish and error events are attached on response object to handle cases when response is closed/ended but underlying socket is abruptly terminated then none of those events is fired. This leads to state when response seems to be still alive, although it's internal state of connection is destroyed. So basically after socket is destroyed this event is not propagated to http response object.

**Description:**
This can lead to two states:

1) If response is handled locally it remains open and if used to eg. stream data from file it keeps file handle opened until server is stopped.

2) In case of request proxying another response stream remains open which can lead to DOS on target server where the request is proxyed to. In case of Apache httpd the server stops responding after certain number of such requests if no timeout is configured.

In both cases the system becomes unusable after certain time, based on incoming traffic and remains in this state until restarted.

## Steps To Reproduce:

  1. start node http server (server.js)
  2. connect with example client (client.js)
  3. http request will remain active although underlying socket is already destroyed until scheduled timeout kicks in and emits error which triggers attached error handler

## Impact:
Attack can possibly lead to open handles exhausting or in case of request proxying to eg. Apache httpd DOS attack.

## Supporting Material/References:

Below are details about platform tested and code to reproduce with proxy example in attachments. I have used stream's utility function pipeline to handle emitted events on streams.

Version: v12.8.1
Platform: 4.15.0-58-generic #54~16.04.1-Ubuntu x86_64 GNU/Linux
Subsystem: net/http

## Impact

DOS attack and resource exhausting.

## Attachments
- client.js
- server.js
