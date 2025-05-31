# environment variable leakage in error reporting

## Report Details
- **Report ID**: 526258
- **URL**: https://hackerone.com/reports/526258
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-04-04T08:41:17.109Z
- **Disclosed**: 2019-09-03T08:54:52.755Z

## Reporter
- **Username**: mcollina
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

I would like to report the leak of environment variables in https://github.com/senecajs/seneca
It make a user indavertely leak private credentials (such as AWS keys) to public spaces.

# Module

**module name:** [MODULE NAME]
**version:** [MODULE VERSION]
**npm page:** `https://www.npmjs.com/package/[MODULE NAME]`

## Module Description

A Node.js toolkit for Microservice architectures

## Module Stats

> Replace stats below with numbers from npm’s module page:

1711 downloads in the last day
7199 downloads in the last week
29241 downloads in the last month

# Vulnerability

## Vulnerability Description

> Description about how the vulnerability was found and how it can be exploited, how it harms package users (data modification/lost, system access, other.

When a process using Seneca crashes, it prints out all of its environment variables. These are typically picked up by log monitoring system, and they might end up in less secured placed. As a result, it can end up in public bug reports, such as
https://github.com/senecajs/seneca-transport/issues/88. 

## Steps To Reproduce:

```
var seneca = require('seneca')()
seneca.die()
```

## Patch

```
diff --git a/lib/common.js b/lib/common.js
index ef3e398..e992cd6 100644
--- a/lib/common.js
+++ b/lib/common.js
@@ -339,10 +339,7 @@ exports.makedie = function(instance, ctxt) {
         process.arch +
         ', platform=' +
         process.platform +
-        (!full ? '' : ', path=' + process.execPath) +
-        ', argv=' +
-        Util.inspect(process.argv).replace(/\n/g, '') +
-        (!full ? '' : ', env=' + Util.inspect(process.env).replace(/\n/g, ''))
+        (!full ? '' : ', path=' + process.execPath)

       var when = new Date()
```

## Supporting Material/References:

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: N

> Hunter's comments and funny memes goes here

## Impact

Access to cloud accounts. I got a 55$ bill out of this.

## Attachments
No attachments
