# [domokeeper] Unintended Require

## Report Details
- **Report ID**: 538938
- **URL**: https://hackerone.com/reports/538938
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-16T01:03:04.098Z
- **Disclosed**: 2019-07-04T09:37:27.121Z

## Reporter
- **Username**: ermilov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Unintended Require vulnerability in `domokeeper`
It allows reading arbitary json files and load non-production code.

# Module

**module name:** domokeeper
**version:** 0.2.0
**npm page:** `https://www.npmjs.com/package/domokeeper`

## Module Description

domokeeper server: a pluggable domotic control server for Raspberry Pi 2/3

## Module Stats

[24] downloads in the last day
[45] downloads in the last week
[72] downloads in the last month

# Vulnerability

## Vulnerability Description

`domokeeper` is an express server which dynamically loads (with help of `require()`) some parts of the code. As long as the path to required module is passed in a HTTP request without any sanitization, anybody can cause code to load that was not intended to run on the server.

source code example:

index.js
line 83
```
app.get('/plugins/:id', function (req, res) {
  var plugin = require(req.params.id);
  res.json(plugin);
})
```

In addition, the fact that output of the module is passed to server response directly (in the example above) leads to an information leakage. For example it is possible to read `package.json` file or any other json file.

Detailed description of this bug can be found here: https://nodesecroadmap.fyi/chapter-1/threat-UIR.html

## Steps To Reproduce:

* install `domokeeper`

```
npm i domokeeper
```

* run it

```
node node_modules/domokeeper/bin.js
```

* by default it starts at `localhost:43569`, so by navigating to `http://localhost:43569/plugins/.%2Fpackage.json` in the browser you are able to read the output of `package.json` file

## Patch

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- OS: Linux Mint current
- Node.js: 8.15.0
- NPM:6.4.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An attacker is able to control the x in require(x) and cause code to load that was not intended to run on the server or read json files.

## Attachments
No attachments
