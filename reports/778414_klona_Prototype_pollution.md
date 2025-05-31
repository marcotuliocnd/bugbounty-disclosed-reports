# [klona] Prototype pollution

## Report Details
- **Report ID**: 778414
- **URL**: https://hackerone.com/reports/778414
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-01-20T17:03:43.298Z
- **Disclosed**: 2020-01-23T11:17:26.602Z

## Reporter
- **Username**: skyn3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Prototype pollution in klona
It allows adding arbitrary property to Prototype while deep cloning an object

# Module

**module name:** klona
**version:** <1.1.1
**npm page:** `https://www.npmjs.com/package/klona`

## Module Description

A tiny (366B) and fast utility to "deep clone" Objects, Arrays, Dates, RegExps, and more!

## Module Stats

356 weekly downloads

# Vulnerability

## Vulnerability Description

See: https://snyk.io/vuln/SNYK-JS-LODASH-450202

## Steps To Reproduce:

Described here: https://github.com/lukeed/klona/pull/11/files

Note:
This vulnerability was reported directly to owner here https://github.com/lukeed/klona/pull/11 on 10/01/2020.
Fix published in v1.1.1 on 15/01/2020

# Wrap up

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: Y

> Hunter's comments and funny memes goes here

{F690469}

## Impact

Denial of Service and possible Remote code execution by overriding object's property methods like `toString`

## Attachments
- ZomboMeme_18012020195556.jpg
