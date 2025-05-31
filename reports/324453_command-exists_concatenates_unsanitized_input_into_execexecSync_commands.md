# `command-exists` concatenates unsanitized input into exec()/execSync() commands

## Report Details
- **Report ID**: 324453
- **URL**: https://hackerone.com/reports/324453
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-03-11T17:01:51.059Z
- **Disclosed**: 2018-05-11T20:06:37.907Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report command injection in `command-exists`.
It allows to inject and execute arbitrary shell commands while trying to determine if a crafted command exists.

# Module

**module name:** `command-exists`
**version:** 1.2.2
**npm page:** `https://www.npmjs.com/package/command-exists`

## Module Description

> node module to check if a command-line command exists

## Module Stats

5 480 downloads in the last day
74 405 downloads in the last week
294 869 downloads in the last month

# Vulnerability

## Vulnerability Description

`commandName` argument is not properly escaped before being concatenated into the command that is passed to `exec()`/`execSync()`.

See https://github.com/mathisonian/command-exists/blob/v1.2.2/lib/command-exists.js#L49-L94

## Steps To Reproduce:

```js
const commandExists = require('command-exists');
commandExists.sync('ls; touch /tmp/foo0');
commandExists('ls; touch /tmp/foo1');
```

Observe `/tmp/foo0` and `/tmp/foo1` being created.

## Supporting Material/References:

- Arch Linux current
- Node.js 9.7.1
- npm 5.7.1

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

For setups where unsanitized user input could end up in `command-exists` argument, users would be able to execute arbitrary shell commands.

## Attachments
No attachments
