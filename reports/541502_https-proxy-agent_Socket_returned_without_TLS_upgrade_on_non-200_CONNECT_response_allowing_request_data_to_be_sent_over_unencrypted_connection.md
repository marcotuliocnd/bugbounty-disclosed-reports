# [https-proxy-agent] Socket returned without TLS upgrade on non-200 CONNECT response, allowing request data to be sent over unencrypted connection

## Report Details
- **Report ID**: 541502
- **URL**: https://hackerone.com/reports/541502
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-17T19:20:28.876Z
- **Disclosed**: 2019-09-25T08:21:57.569Z

## Reporter
- **Username**: kadler15
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a man-in-the-middle vulnerability in `https-proxy-agent`.
It allows an attacker with access to the network firewall or targeted proxy server to obtain secrets (e.g. a HTTP basic auth header) from the client trying to send HTTPS traffic via HTTP proxy.

# Module

**module name:** `https-proxy-agent`
**version:** 2.2.1
**npm page:** `https://www.npmjs.com/package/https-proxy-agent`

## Module Description

> This module provides an http.Agent implementation that connects to a specified HTTP or HTTPS proxy server, and can be used with the built-in https module.

## Module Stats

4314908 downloads in the last week

# Vulnerability

## Vulnerability Description

When targeting a HTTP proxy, `https-proxy-agent` [opens a socket](https://github.com/TooTallNate/node-https-proxy-agent/blob/2.2.1/index.js#L77) to the proxy, and sends the proxy server a [CONNECT request](https://github.com/TooTallNate/node-https-proxy-agent/blob/2.2.1/index.js#L203). E.g.:

```
CONNECT www.google.com:443 HTTP/1.1
Host: www.google.com
Connection: close
```

If the proxy server responds with 200 and the client is targeting a secure endpoint, `https-proxy-agent` [TLS-upgrades](https://github.com/TooTallNate/node-https-proxy-agent/blob/2.2.1/index.js#L154) the socket before returning it for use. This is normal and expected.

However, if the proxy server (or firewall blocking the request) responds with something other than a 200, `https-proxy-agent` incorrectly [returns the socket](https://github.com/TooTallNate/node-https-proxy-agent/blob/2.2.1/index.js#L170) without any TLS upgrade. Companion library `agent-base` [passes the socket off](https://github.com/TooTallNate/node-agent-base/blob/4.2.1/index.js#L141) to Node HTTP internals, which will write the pending request data to the socket. E.g.:

```
GET / HTTP/1.1
Host: www.google.com
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
Connection: close
```

The request data, which may contain basic auth credentials or other secrets, is sent over an unencrypted connection. An attacker with access to tcpdump contents at the firewall or proxy server can steal these secrets and impersonate the client.

## Steps To Reproduce:

Run a simple web server on port 80 that returns 403 in response to any request:
```bash
#!/bin/bash
while true; do
  echo -e "HTTP/1.1 403 FORBIDDEN\r\n$(date)\r\n\r\n<h1>hello world from $(hostname) on $(date)</h1>" |  nc -vl 80;
done
```

Send a a request to a remote server using the simple web server as a proxy:
```javascript
var url = require('url');
var https = require('https');
var HttpsProxyAgent = require('https-proxy-agent');

var proxyOpts = url.parse('http://127.0.0.1:80');
var opts = url.parse('https://www.google.com');
var agent = new HttpsProxyAgent(proxyOpts);
opts.agent = agent;
opts.auth = 'username:password';
https.get(opts);
```

Logs observed on the simple web server:
```
CONNECT www.google.com:443 HTTP/1.1
Host: www.google.com
Connection: close

GET / HTTP/1.1
Host: www.google.com
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
Connection: close
```

## Patch

Changes in a [commit from 2013](https://github.com/TooTallNate/node-https-proxy-agent/commit/ae03c687bd5667e4088f13bd1eda6228cb10f62d) to buffer and replay incoming proxy data in case of error should be reconsidered. Maybe the replaying can still be done when targeting an insecure endpoint, but it seems unsafe to return the socket without TLS upgrade in the secure endpoint case. It would be better to do something like:

```javascript
if (200 == statusCode) {
  // Happy path
} else if (secureEndpoint) {
  cleanup();
  socket.destroy();
  fn(new Error(`Could not establish TLS connection. Status code: ${statusCode}`));
} else {
  // Replay on insecure endpoint
}
```

There may also be a way for the agent to replay the incoming proxy data on and then destroy the socket before returning it.

## Supporting Material/References:

- Ubuntu 16.04 / Linux 4.15.0-43
- Node 10.15.3
- npm 6.4.1
- gnu-netcat 0.7.1

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

The vulnerability allows a determined attacker with access to the network firewall or targeted proxy server to see plaintext request data, which could expose auth credentials or other secrets.

## Attachments
No attachments
