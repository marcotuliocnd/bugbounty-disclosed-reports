# Denial of Service by resource exhaustion CWE-400 due to unfinished HTTP/1.1 requests

## Report Details
- **Report ID**: 868834
- **URL**: https://hackerone.com/reports/868834
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-08T07:45:07.938Z
- **Disclosed**: 2020-10-17T19:24:45.481Z

## Reporter
- **Username**: shogunpanda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** Node.js is vulnerable to HTTP denial of service (DOS) attacks based on delayed requests submission which can make the server unable to accept new connections.

**Description:**

An attacker can open an arbitrary number of HTTP connections and keep the server busy by never completing the request phase.

Node.js only has two requests timeouts:

1. [server.timeout](https://nodejs.org/docs/latest-v12.x/api/http.html#http_server_timeout) that controls the maximum number of milliseconds the socket can be idle. This also includes the server processing time. 
2. [server.headersTimeout](https://nodejs.org/docs/latest-v13.x/api/http.html#http_server_headerstimeout) (Added in Node 11.3.0), that controls the maximum number of milliseconds allowed to receive the full request headers before timing out.

Handling of request bodies is specific to the application code and core Node.js never consumes or parses the request bodies. 

Currently, the body parsing and handling is performed by the following modules:
* [fastify](https://www.fastify.io/)
* [restify](https://restify.com/)
* [busboy](https://github.com/mscdex/busboy), used by [fastify-multpart](https://github.com/fastify/fastify-multipart/) and [multer](https://github.com/expressjs/multer)
* [raw-body](https://github.com/stream-utils/raw-body), used by [body-parser](https://github.com/expressjs/body-parser)

All of the modules above are vulnerable to the attack.

If part of the body is already sent, the body parsing modules above can be patched to impose a request body sending timeout and therefore mitigate the attack.

The application unfortunately can not completely handle this attack. If the attacker never starts sending the body after completing the submission of the headers, the application code is never invoked. 

Prior to Node.js 13.0.0, the default timeout for a request was 2 minutes, which is a countermeasure against this attack.
Starting with Node.js 13.0.0 instead, the default timeout has been changed to be 0 (which means no timeout) in order to address serverless deployments where long running requests are needed. Since the socket is never considered idle, the application is completely vulnerable to the attack.

While `server.headersTimeout` is able to detect a slow request, it is only effective if the delay happens during the headers phase (like in Slowloris attacks). If the attacker delays the start of the headers, the start of body sending or sends the body very slow without resulting in an idle socket, the attack is not detected.

In the long run an unprotected server will have a lot of pending requests to handle. At some point it will reach the open connections limit and therefore will not be able to serve additional requests, resulting in a Denial of Service.

## Steps To Reproduce:

1. From one or more attacking sources, open one or more HTTP connections to the target server
2. For each of the connection in step 1
     2.1. (Optional) Wait a certain amount of time before sending the first request header.
     2.2 Send all request headers with regular pausing.
     2.3 (Optional) Wait a certain amount of time before sending the body data.
     2.4. Send the request body with regular pausing.

All the substeps must be performed by sending periodically the smallest amount of data with the highest delay such that the server does not detect an idle socket. For Node 13.0.0 and above there is no idle timeout by default, so the attacker can wait an arbitrary time. For Node.js prior to 13.0.0, at least one byte each 2 minutes must be sent.

We have tested the following test cases:

1. **Connection established, none or partial headers sent then sending is paused:** If `server.timeout` is not 0, then idle detection is triggered and closes the connection with no response. With the default timeout of 0 in Node.js 13.0.0 and above, the server is completely vulnerable to the attack.
2. **Connection established, headers sent with long delays:** `server.headersTimeout` is triggered and closes the connection with no response. 
3. **Connection established, headers sent and sending is paused before starting the body:** If `server.timeout` is not 0, then idle detection is triggered and closes the connection with no response. With the default timeout of 0 in Node.js 13.0.0 and above, the server is completely vulnerable to the attack.
4. **Connection established, headers sent, body sent with long delays:** `server.timeout` is not able to detect the attack and the server is completely vulnerable to the attack.

What follows is a sample code which reproduces the problem. 

```javascript
const { createConnection } = require('net')

let start
let response = ''
let body = ''.padEnd(4096, '123')

const client = createConnection({ port: parseInt(process.argv[2], 10) }, () => {
  start = process.hrtime.bigint()

  // Send all the headers quickly so that server.headersTimeout is not triggered
  client.write('POST / HTTP/1.1\r\n')
  client.write('Content-Type: text/plain\r\n')
  client.write(`Content-Length: ${Buffer.byteLength(body)}\r\n`)
  client.write(`\r\n`)

  // Send the body very slower but in away that the server.timeout is not triggered
  let i = 0
  let interval = setInterval(() => {
    client.write(body[i])
    i++

    // Done sending, end the request
    if (i === body.length) {
      clearInterval(interval)
      client.write(`\r\n\r\n`)
    }
  }, 60000)
})

client.on('data', data => {
  response += data
  client.end()
})

client.on('close', () => {
  const duration = Number(process.hrtime.bigint() - start) / 1e9

  console.log(`Receive the following response (${response.length} bytes) in ${duration.toFixed(3)} s:\n\n`)
  console.log(response)
})
```

Once executed, the client will not receive a response before 4096 minutes. If multiple parallel execution of the code above targets the same server, it will result in service denial. 

## Impact

This attack has very low complexity and can easily trigger a DDOS on an unprotected server.

## Supporting Material/References:

We have written a patch for Node.js ([PR 33304](https://github.com/nodejs/node/pull/33304)) which introduces a new `http.Server` option called `requestTimeout` with a default value in milliseconds of `120000` (2 minutes).

When `requestTimeout` is a positive value, the server will start a new timer set to expire in `requestTimeout` milliseconds when a new connection is established. The timer is also set again if new requests after the first are received on the socket (this handles pipelining and keep-alive cases).
The timer is cancelled in the following case:

1. When the request body is completely received by the server.
2. When the response is completed. This handles the case where the application responds to the client without consuming the request body.
3. When the connection is upgraded, like in the WebSocket case.

If the timer expires, then the server responds with status code 408 and closes the connection. This prevents the DOS attack.

## Acknowledgement

This research was conducted and co-authored by me and [Matteo Collina](matteo.collina@nearform.com) and has been sponsored by [NearForm](https://nearform.com)

## Impact

If an attacker execute a significative amount of requests on a target server without completing any, the server at some point will reach the allowed number of open connections and will not be able to serve any further request, resulting in a Denial of Service.

## Attachments
No attachments
