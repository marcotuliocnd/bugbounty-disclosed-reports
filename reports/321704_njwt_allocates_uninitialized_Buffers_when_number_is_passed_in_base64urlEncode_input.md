# `njwt` allocates uninitialized Buffers when number is passed in base64urlEncode input

## Report Details
- **Report ID**: 321704
- **URL**: https://hackerone.com/reports/321704
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-03-04T01:20:27.353Z
- **Disclosed**: 2018-06-14T19:51:43.128Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report an uninitialized Buffer allocation issue in `njwt`.
It allows to extract sensitive data from uninitialized memory or to cause a DoS by passing in a large number, in setups where typed user input can be passed (e.g. from JSON).

# Module

**module name:** `njwt`
**version:** 0.4.0
**npm page:** `https://www.npmjs.com/package/njwt`

## Module Description

> nJwt is the cleanest JSON Web Token (JWT) library for Node.js developers. nJwt removes all the complexities around JWTs, and gives you a simple, intuitive API, that allows you to securely make and use JWTs in your applications without needing to read rfc7519.

## Module Stats

6 683 downloads in the last day
58 416 downloads in the last week
183 352 downloads in the last month

# Vulnerability

## Vulnerability Description

See https://github.com/jwtk/njwt/blob/0.4.0/index.js#L42-L48

The problem arises when a number is passed in, e.g. from user-submitted JSON-encoded data.
The API should not propagate the already-bad Buffer issue further.

On Node.js 6.x and below, this exposes uninitialized memory, which could contain sensitive data.

This can be also used to cause a DoS on any Node.js version by consuming the memory when large numbers are passed on input.

## Steps To Reproduce:

`console.log(require('njwt').base64urlEncode(200))` (Node.js 6.x and lower — note uninitialized memory in output)

`require('njwt').base64urlEncode(1e8)` (any Node.js verision — note memory usage and time)

## Supporting Material/References:

> OS: Arch Linux current
> Node.js 6.13.0
> Node.js 9.5.0

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

Sensitive uninitialized memory exposure on Node.js 6.x or lower
Denail of Service on any Node.js version

## Attachments
No attachments
