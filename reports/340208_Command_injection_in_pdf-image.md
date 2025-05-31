# Command injection in 'pdf-image'

## Report Details
- **Report ID**: 340208
- **URL**: https://hackerone.com/reports/340208
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-18T18:24:40.746Z
- **Disclosed**: 2018-05-29T20:43:43.830Z

## Reporter
- **Username**: defmax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report command injection in pdf-image
It allows executing commands on the server 

# Module

**module name:** pdf-image
**version:** 1.0.5
**npm page:** `https://www.npmjs.com/package/pdf-image`

## Module Description

> Provides an interface to convert PDF's pages to png files in Node.js by using ImageMagick.


## Module Stats

[2013] downloads in the last week

# Vulnerability

## Vulnerability Description

> Description about how the vulnerability was found and how it can be exploited, how it harms package users (data modification/lost, system access, other.

## Steps To Reproduce:

> The constructGetInfoCommand would be initializing the command that is to the passed to 'exec' of getInfo(). The user input is not getting validated in #L26 of constructGetInfoCommand and it leads to command injection in #L43.

https://github.com/mooz/node-pdf-image/blob/master/index.js#L26
https://github.com/mooz/node-pdf-image/blob/master/index.js#L43## Patch

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Kali linux 
- Nodejs v8.10.0
- Npm v5.8.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An attacker could execute arbitrary shell commands

## Attachments
No attachments
