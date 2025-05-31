# `stringstream` allocates uninitialized Buffers when number is passed in input stream on Node.js 4.x and below

## Report Details
- **Report ID**: 321670
- **URL**: https://hackerone.com/reports/321670
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-03T21:51:21.472Z
- **Disclosed**: 2018-05-11T14:54:16.685Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report n uninitialized Buffer allocation issue in `stringstream`.
It allows to extract sensitive data from uninitialized memory or to cause a DoS by passing in a large number, in setups where typed user input can be passed to the stream (e.g. from JSON), on Node.js 4.x and lower.

# Module

**module name:** `stringstream`
**version:** 0.0.5
**npm page:** `https://www.npmjs.com/package/stringstream`

## Module Description

> Decode streams into strings The Right Way(tm)

## Module Stats

740 368 downloads in the last day
4 606 368 downloads in the last week
19 182 466 downloads in the last month

# Vulnerability

## Vulnerability Description

See https://github.com/mhart/StringStream/blob/v0.0.5/stringstream.js#L32

The problem arises when a number is passed in the stream. That is unlikely to be attacker-controlled in real-world setups, but still possible. The API should not propagate the already-bad Buffer issue further.

On Node.js 4.x and below (4.x is still supported), this exposes uninitialized memory, which could contain sensitive data.

On Node.js 6.x and newer, this is type-checked on Node.js side and thows an error there.

## Steps To Reproduce:

```js
var stringstream = require('stringstream')
var stream = stringstream('hex', 'utf8')
stream.pipe(process.stdout)
stream.write(10000);
stream.end();
```

Run on Node.js 4.x (or lower). `hex`/`utf8` is irrelevant, the issue is reproducable with all encodings.

## Supporting Material/References:

- Arch Linux Current
- Node.js 4.8.7

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Sensitive uninitialized memory exposure
Denail of Service
This issue affects only setups using Node.js 4.x (still supported) or lower.

## Attachments
No attachments
