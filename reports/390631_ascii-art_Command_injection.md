# [ascii-art] Command injection

## Report Details
- **Report ID**: 390631
- **URL**: https://hackerone.com/reports/390631
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-05T06:31:48.648Z
- **Disclosed**: 2018-09-08T08:36:27.752Z

## Reporter
- **Username**: pontus_johnson
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a command injection vulnerability in the **ascii-art npm** module.
It allows arbitrary shell command execution through a maliciously crafted command line argument.

# Module

**module name:** ascii-art
**version:** 1.4.3
**npm page:** `https://www.npmjs.com/package/ascii-art`

## Module Description

>Images, fonts, tables, ansi styles and compositing in Node.js & the browser. 100% JS.
>
>In the beginning there was colors.js but in the fine tradition of vendors calling out a problem they have the solution to, chalk was introduced. In that same vein, I offer ascii-art as an update, expansion and generalization of MooAsciiArt and at the same time it can replace your existing ansi colors library.
>
>It features support for Images, Styles, Tables and Figlet Fonts as well as handling multi-line joining automatically.

## Module Stats

56 downloads in the last day
217 downloads in the last week
1432 downloads in the last month

# Vulnerability

## Vulnerability Description

ascii-art does not sanitize the `target` command line argument, and subsequently passes it to `child_process.exec()`, thus allowing arbitrary shell command injection.

## Steps To Reproduce:

1. Install ascii-art: `sudo npm install -g ascii-art` (On a pristine Google Cloud instance, I also had to install pkg-config, libcairo2-dev, libjpeg-dev and libgif-dev, and then install ascii-art with unsafe-perm=true).
2. Run ascii-art with malicious argument: `ascii-art preview 'doom"; touch /tmp/malicious; echo "'`
3. Check that the injected command was executed: `ls /tmp/`

## Patch

Command execution happens [here](https://github.com/khrome/ascii-art/blob/9059daa5fcbf2c6a8813bbf072a1477d91e7b61d/bin/ascii-art#L210):

`exec('open "http://www.figlet.org/fontdb_example.cgi?font='+target.toLowerCase()+'.flf"')`

`exec` could be replaced by `execFile`, which would force developers to separate the command and its arguments.

## Supporting Material/References:

- Operating system: Debian GNU/Linux 9.5 (stretch)
- Node.js v8.11.3
- npm v5.6.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Arbitrary shell command execution.

## Attachments
No attachments
