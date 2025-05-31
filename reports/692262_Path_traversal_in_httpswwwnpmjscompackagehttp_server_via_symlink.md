# Path traversal in https://www.npmjs.com/package/http_server via symlink

## Report Details
- **Report ID**: 692262
- **URL**: https://hackerone.com/reports/692262
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-11T10:37:09.961Z
- **Disclosed**: 2019-12-04T19:56:48.103Z

## Reporter
- **Username**: vineetpandey
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path traversal in http_server
It allows an attacker to read arbitrary system files.

# Module

**module name:** http_server
**version:** 1.0.12
**npm page:** `https://www.npmjs.com/package/http_server`

## Module Description

> Copy description from npm page

## Module Stats

Weekly downloads: 35

# Vulnerability

## Vulnerability Description

With a symbolically linked file in the working directory, it is possible to read arbitrary files outside of the web root directory.

## Steps To Reproduce:

1. Install the http_server: npm install http_server -g

2. Create a symlink file within the directory
ln -s /etc/shadow test_shadow

3. Request the file within browser
http://localhost:8888/test_shadow

## Patch

Reject the symbolically linked path files.

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Kali Linux
- Node.js v12.8.0
- NPM v6.11.3
- Firefox 60.8.0esr

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

> Hunter's comments and funny memes goes here

## Impact

It allows attacker to read content of arbitrary file on remote server and could leverage attacks like remote code execution.

## Attachments
- 1.png
- 2.png
