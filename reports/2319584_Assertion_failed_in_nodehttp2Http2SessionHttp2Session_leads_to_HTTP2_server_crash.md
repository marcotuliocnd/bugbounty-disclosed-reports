# "Assertion failed" in node::http2::Http2Session::~Http2Session() leads to HTTP/2 server crash

## Report Details
- **Report ID**: 2319584
- **URL**: https://hackerone.com/reports/2319584
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-01-15T14:48:55.123Z
- **Disclosed**: 2024-04-08T22:25:42.342Z

## Reporter
- **Username**: bart
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**

I discovered a vulnerability in Node.js HTTP/2 stack (`http2`) package. An attacker can send a very small amount of TCP packets with a few HTTP/2 frames inside. After a few seconds a Node.js (latest: 21.5.0 and latest LTS: v20.11.0) server crash with the following stack:
```
  #  node[3253]: virtual node::http2::Http2Session::~Http2Session() at ../src/node_http2.cc:534
  #  Assertion failed: (current_nghttp2_memory_) == (0)

----- Native stack trace -----

 1: 0xca5430 node::Abort() [node]
 2: 0xca54b0 node::errors::SetPrepareStackTraceCallback(v8::FunctionCallbackInfo<v8::Value> const&) [node]
 3: 0xce7156 node::http2::Http2Session::~Http2Session() [node]
 4: 0xce7192 node::http2::Http2Session::~Http2Session() [node]
 5: 0x106f01d v8::internal::GlobalHandles::InvokeFirstPassWeakCallbacks() [node]
 6: 0x10f3215 v8::internal::Heap::PerformGarbageCollection(v8::internal::GarbageCollector, v8::internal::GarbageCollectionReason, char const*) [node]
 7: 0x10f3d7c v8::internal::Heap::CollectGarbage(v8::internal::AllocationSpace, v8::internal::GarbageCollectionReason, v8::GCCallbackFlags) [node]
 8: 0x10ca081 v8::internal::HeapAllocator::AllocateRawWithLightRetrySlowPath(int, v8::internal::AllocationType, v8::internal::AllocationOrigin, v8::internal::AllocationAlignment) [node]
 9: 0x10cb215 v8::internal::HeapAllocator::AllocateRawWithRetryOrFailSlowPath(int, v8::internal::AllocationType, v8::internal::AllocationOrigin, v8::internal::AllocationAlignment) [node]
10: 0x10a8866 v8::internal::Factory::NewFillerObject(int, v8::internal::AllocationAlignment, v8::internal::AllocationType, v8::internal::AllocationOrigin) [node]
11: 0x15035f6 v8::internal::Runtime_AllocateInYoungGeneration(int, unsigned long*, v8::internal::Isolate*) [node]
12: 0x7f41df699ef6 
Aborted (core dumped)
```
The attack is easy to perform so a permanent Denial of Service is possible. It is also hard to debug from server admins (check Impact section).

**Description:**

The `http2` package has an  assertion in the `Http2Session` destructor which check if current memory usage of nghttp2 library (`current_nghttp2_memory_`) has been reset to 0.
```c++
Http2Session::~Http2Session() {
  CHECK(!is_in_scope());
  Debug(this, "freeing nghttp2 session");
  // Explicitly reset session_ so the subsequent
  // current_nghttp2_memory_ check passes.
  session_.reset();
  CHECK_EQ(current_nghttp2_memory_, 0);
}
```
However it is possible to leave some data in nghttp2 memory (or counter is improperly implemented) after reset when headers with HTTP/2 [`CONTINUATION` frame](https://datatracker.ietf.org/doc/html/rfc9113#name-continuation) are sent to the server and then a TCP connection is abruptly closed by the client triggering the `Http2Session` destructor while header frames are still being processed (and stored in memory).

## Steps To Reproduce:

  1. Start a `http2` server.
  2. Send a HTTP/2 request:
     * Send necessary init frames.
     * Send `HEADERS` frame for a simple `GET /` request (with no `END_HEADERS` flag).
     * Send `CONTINUATION` frame with a single header (also with no `END_HEADERS` flag).
  3. Disconnect TCP connection.

I'm attaching an exploit in Golang that demonstrates the issue. It starts a loop and in each iteration it opens a TCP connection to the server. It sends necessary headers and then just leaves the connection open. After 10 seconds, another go routine simply exists the application which kills all opened TCP connections which triggers the bug. To run it simply run: `go run ./exploit2.go -address [server]`. For simplicity it works only for `h2c` (HTTP/2 without TLS) server but with extra code it should work against any Node.js server (with TLS).

I was testing it against the simple Node.js server:
```nodejs
const http2 = require('http2');
const fs = require('fs');

const server = http2.createServer();

server.on('error', (err) => console.error(err));

server.on('stream', (stream, headers) => {
    // Respond to the request with a simple hello world message
    stream.respond({
        'content-type': 'text/plain; charset=utf-8',
        ':status': 200
    });
    stream.end('Hello World with HTTP/2!');
    console.log("Request handled")
});

server.listen(7777, () => {
    console.log('Server is running on http://localhost:7777');
});
```

## Impact

An attacker can make the Node.js HTTP/2 server completely unavailable. Because of the fact that send HTTP/2 frames never establish a full HTTP request, the server admins may have problems with debugging the issue or rate-limiting the attacker (requests not visible in the logs). The payload sent to exploit the issue is also very small.

Additionally, an attack can cause some problems with data integrity because `GOAWAY` frames will not be sent but they contain (often important): `Last-Stream-ID` parameter, from specification:
> The last stream identifier in the GOAWAY frame contains the highest-numbered stream identifier for which the sender of the GOAWAY frame might have taken some action on or might yet take action on. All streams up to and including the identified stream might have been processed in some way.

This means that clients may submit duplicate request for request that have been already processed by a server.

## Attachments
- Screen_Recording_2024-01-15_at_15.40.42.mov
- exploit2.go
