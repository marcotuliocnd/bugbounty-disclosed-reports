# Prototype pollution in multipart parsing

## Report Details
- **Report ID**: 804772
- **URL**: https://hackerone.com/reports/804772
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-02-25T17:51:30.156Z
- **Disclosed**: 2020-02-28T10:55:15.010Z

## Reporter
- **Username**: mcollina
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a prototype pollution attack in fastify-multipart it allows to crash a remote server parsing multipart requests by sending a specially crafted request.

# Module

**module name:** fastify-multipart
**version:** all versions before < v1.0.5. v1.0.5 contains the fix. 
**npm page:** `https://www.npmjs.com/package/fastify-multipart`

## Module Description

[Fastify](https://www.fastify.io) plugin to parse the multipart content-type.

Under the hood it uses [busboy](http://npm.im/busboy).

## Module Stats

weekly downloads: 4900

# Vulnerability

## Vulnerability Description

Eran Hammer found this vulnerability for Hapi, he tested Fastify as well and found it vulnerable.
Here is the Hapi vulnerability report: https://www.npmjs.com/advisories/1479. 

## Steps To Reproduce:

> Detailed steps to reproduce with all required references/steps/commands. If there is any exploit code or reference to the package source code this is the place where it should be put.

## Patch

This was already released in https://github.com/fastify/fastify-multipart/pull/116 and version 1.0.5 issued.

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: N

I just need a CVE issued.

## Impact

It's a Denial of Service attack

## Attachments
No attachments
