# `whereis` concatenates unsanitized input into exec() command

## Report Details
- **Report ID**: 319476
- **URL**: https://hackerone.com/reports/319476
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-02-25T06:53:14.046Z
- **Disclosed**: 2018-03-28T06:17:58.607Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report command injection in `whereis`
It allows to inject arbitrary shell commands by trying to locate crafted filenames.

# Module

**module name:** whereis
**version:** 0.4.0
**npm page:** `https://www.npmjs.com/package/whereis`

## Module Description

> Simply get the first path to a bin on any system.

## Module Stats

Stats
101 downloads in the last day
5 403 downloads in the last week
18 945 downloads in the last month

~227 340 estimated downloads per year [JUST FOR REFERENCE,  ~DOWNLOADS PER MONTH*12]

# Vulnerability

## Vulnerability Description

File name argument is not properly escaped before being concatenated into the command that is passed to `exec()`.

See lines https://github.com/vvo/node-whereis/blob/master/index.js#L4-L12

## Steps To Reproduce:

```js
var whereis = require('whereis');
var filename = 'wget; touch /tmp/tada';
whereis(filename, function(err, path) {
  console.log(path);
});
```

Observe file `/tmp/tada` created.

## Supporting Material/References:

- Arch Linux Current
- Node.js 9.5.0
- npm 5.6.0
- bash 4.4.012

# Wrap up

- I contacted the maintainer to let him know: N
- I opened an issue in the related repository: N

## Impact

For setups where unsanitized user input could end up in `whereis` argument, users would be able to execute arbitrary shell commands.

## Attachments
No attachments
