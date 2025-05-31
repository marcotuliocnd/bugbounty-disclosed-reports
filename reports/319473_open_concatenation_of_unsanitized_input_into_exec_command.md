# [open] concatenation of unsanitized input into exec() command

## Report Details
- **Report ID**: 319473
- **URL**: https://hackerone.com/reports/319473
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-25T06:14:22.741Z
- **Disclosed**: 2019-12-13T17:06:57.027Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report command injection in `open`.
It allows to inject arbitrary shell commands by specifing crafted urls.

# Module

**module name:** open
**version:** 0.0.5
**npm page:** `https://www.npmjs.com/package/open`

## Module Description

> Open a file or url in the user's preferred application.

## Module Stats

31 293 downloads in the last day
473 107 downloads in the last week
1 968 932 downloads in the last month

~23 627 184 estimated downloads per year

# Vulnerability

## Vulnerability Description

Urls are not properly escaped before concatenating them into the command that is opened using `exec()`.

## Steps To Reproduce:

```js
require("open")("http://example.com/`touch /tmp/tada`");
```

Observe `/tmp/tada/` file created.

Supporting Material/References:

- Arch Linux Current
- Node.js 9.5.0
- npm 5.6.0
- bash 4.4.012

# Wrap up

- I contacted the maintainer to let him know: N 
- I opened an issue in the related repository: N

## Impact

User A who can pass urls for them being `open`-ed on machine B can execute arbitrary shell commands on machine B.

## Attachments
No attachments
