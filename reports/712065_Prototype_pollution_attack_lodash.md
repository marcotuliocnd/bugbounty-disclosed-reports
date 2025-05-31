# Prototype pollution attack (lodash)

## Report Details
- **Report ID**: 712065
- **URL**: https://hackerone.com/reports/712065
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-10-11T12:06:20.745Z
- **Disclosed**: 2020-04-27T22:14:18.244Z

## Reporter
- **Username**: posix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a prototype pollution vulnerability in lodash.
It allows an attacker to inject properties on Object.prototype

Module
module name: lodash
version: 4.17.15
npm page: https://www.npmjs.com/package/lodash

Module Description
The Lodash library exported as Node.js modules.

Module Stats
25,228,177 downloads in the last week

Vulnerability
Vulnerability Description
This is a similar with this vulnerability: https://hackerone.com/reports/380873

The functions merge, mergeWith, and defaultsDeep can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

Steps To Reproduce:
Craft an object by "zipObjectDeep" function of lodash

const _ = require('lodash');
_.zipObjectDeep(['__proto__.z'],[123])
console.log(z) // 123

## Impact

Variable. Server crash or the server becoming unable to respond to all request is garanteed, but more significant impact like remote code execution can be achieved in some cases.

## Attachments
No attachments
