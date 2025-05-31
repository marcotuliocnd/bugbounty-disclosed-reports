# [samsung-remote] Command injection

## Report Details
- **Report ID**: 394294
- **URL**: https://hackerone.com/reports/394294
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-08-13T17:51:39.108Z
- **Disclosed**: 2018-09-02T15:41:04.574Z

## Reporter
- **Username**: pontus_johnson
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a command injection vulnerability in the **samsung-remote** npm module.
It allows arbitrary shell command execution through a maliciously crafted argument.

# Module

**module name:** samsung-remote
**version:** 1.2.5
**npm page:** `https://www.npmjs.com/package/samsung-remote`

## Module Description

>Module for integration of Samsung SmartTV with your NodeJS application. Tested with Samsung D6000 TV.
>Inspired by this topic http://forum.samygo.tv/viewtopic.php?f=12&t=1792

## Module Stats

24 downloads in the last day
217 downloads in the last week
1024 downloads in the last month

# Vulnerability

## Vulnerability Description

samsung-remote does not sanitize the IP address argument, and subsequently passes it to child_process.exec(), thus allowing arbitrary shell command injection. It is not unlikely that some systems using this package will pass a user-controlled IP address to the function, thus inadvertently allowing arbitrary code execution by the user.

## Steps To Reproduce:

1. Install samsung-remote: `npm install samsung-remote --save`.
2. Create the following `index.js`file:

```
var remote = new SamsungRemote({
    ip: '127.0.0.1; touch /tmp/malicious;' 
});

remote.isAlive(function(err) {});
```
3. Execute `node index.js`
4. Check that the injected command was executed: `ls /tmp/`

## Patch

Command execution happens [here](https://github.com/natalan/samsung-remote/blob/bf7e68d78dddfb534d7ef6c501d0af5e4d32e788/lib/samsung-remote.js#L103):

`return exec("ping -c 1 " + config.ip, function (error, stdout, stderr) {`

`exec` could be replaced by `execFile`, which would force developers to separate the command and its arguments.

## Supporting Material/References:

- Operating system: Debian GNU/Linux 9.5 (stretch)
- Node.js v8.11.3
- npm v5.6.0

# Wrap up


- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Arbitrary shell command execution.

## Attachments
No attachments
