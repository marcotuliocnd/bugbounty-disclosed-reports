# Path Traversal on Resolve-Path

## Report Details
- **Report ID**: 315760
- **URL**: https://hackerone.com/reports/315760
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-13T21:48:00.573Z
- **Disclosed**: 2018-02-22T21:20:52.170Z

## Reporter
- **Username**: orange
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
The author of `resolve-path` told me that I can submit this to here. The vulnerability already reported to the author and got a fixed!

## Module

**module name:** resolve-path
**version:** 1.3.3
**npm page:** `https://www.npmjs.com/package/resolve-path`

### Description

Resolve a relative path against a root path with validation.

This module would protect against commons attacks like GET /../file.js which reaches outside the root folder.

### Module Stats

Stats
[8264] downloads in the last day
[48226] downloads in the last week
[210556] downloads in the last month

~[2526672] estimated downloads per year

## Description

The library failed to process path like `C:../../` on Windows

## Steps To Reproduce:

```js
require('resolve-path')("C:/windows/temp/", "C:../../")
```

## Supporting Material/References:

- Windows 10
- Node v8.9.4
- NPM 5.6.0

## Wrap up

- [Y] I contacted the maintainer to let him know
- [N] I opened an issue in the related repository

## Impact

This is a high-dependency library, for example: [KoaJS](https://github.com/koajs/koa) is suffered from this vulnerability

[21086] downloads in the last day
[113573] downloads in the last week
[462543] downloads in the last month
~[5550516] estimated downloads per year

## Attachments
No attachments
