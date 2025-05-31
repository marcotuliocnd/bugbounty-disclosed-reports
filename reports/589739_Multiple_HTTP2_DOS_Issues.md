# Multiple HTTP/2 DOS Issues

## Report Details
- **Report ID**: 589739
- **URL**: https://hackerone.com/reports/589739
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-05-24T20:53:30.231Z
- **Disclosed**: 2019-08-16T23:40:09.482Z

## Reporter
- **Username**: jasnell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
A security researcher has conducted a broad survey of HTTP/2 implementations to investigate common Denial of Service attack vectors. The Node.js implementation has been found to be subject to a number of these issues. (On the plus side, we're not the only ones! ;-) ...)

This work is still under embargo and has not yet been disclosed. 

Specifically:

* Data Dribble Attack: "This program will request 1MB of data from a specified resource. It will request this same resource over 100 streams (so, 100MB total). It manipulates window sizes and stream priority to force the server to queue the data in 1-byte chunks."

* Ping Flood (nginx variant):  "Nginx and libnghttp2 (used by Apache, Tomcat, node.js, and others) has a 10K-message limit on the number of control messages it will queue. Sending a controlled number of messages may enable an attacker to force the server to hold 10K messages in memory..."

* Resource Loop: "(actually, it should be called “Priority Shuffling”): This program continually shuffles the priority of streams in a way which causes substantial churn to the priority tree. Node.js [is] particularly impacted."

* Reset Flood: "This opens a number of streams and sends an invalid request over each stream. In some servers, this solicits a string of stream RSTs. In [Node.js] the servers may queue the RSTs internally until they run out of memory."

* O-Length Headers Leak: "This sends a stream of headers with a 0-length header name and 0-length header value. [Node.js] allocates memory for these headers and keeps the allocation alive until the session dies. Because the names and values are 0 bytes long, the cumulative length never exceeds the header size limit."

* Internal Data Buffering: "This opens the HTTP/2 window so the server can send without constraint; however, it leaves the TCP window closed so the server cannot actually write (many of) the bytes on the wire. Then, the client sends a stream of requests for a large response object which the target queues internally. This appears to work to create a long-ish standing queue in node.js"

Each is a distinct issue that will need to be looked at individually. I've edited the descriptions to remove references to vulnerabilities in other HTTP/2 implementations that have not yet been disclosed.

---

Additional details from the report:

```
“Data Dribble” on node.js: node.js seems to queue the data internally. For a 1MB output file
requested 100 times in parallel fast enough that node.js is constantly processing input,
node.js’s RSS rises by 808MB and then falls by 120MB (for an aggregate rise of 688MB).
(Actually, it looks like the numbers vary a bit across tests, but I think the end result is “a lot”.)
However, node.js does not have the excess CPU utilization which Nginx exhibits. If you
instead delay the sends considerably so that node.js has time to try to send in the meantime, it
looks like node.js will kill off the session before the input queue grows more than a few
hundred MB.

“Internal Data Buffering” on node.js: For a 1MB output file requested 100 times in parallel
(but sent with 24 requests per SSL frame), node.js behaves in an interesting way. It appears to
buffer some, but not all, data internally. It seems to continue reading (and processing requests
and queueing data to satisfy those requests) for as many streams as it can until it can’t read
any more. Once it can’t read anymore, it appears to try to write and realize the writing is
blocked. At that point, it seems to switch to reading frames from the wire and queuing the
requests internally (without processing them). (All of this is conjecture and is based on what
I’ve observed rather than a detailed analysis of the code.) So, if you pack the 100 requests
into a single SSL frame, node.js’s RSS increases by approximately 246MB. Or, if you send
585 requests in a single SSL frame, node.js’s RSS increases by approximately 1,296MB. For
reasons that are not entirely clear to me, if you send 100K requests each on three different
connections (approximately 2.8MB of request data per connection, node.js will run out of
memory and crash. The other interesting thing that happens is on the session ending. When
the session ends, it looks like node.js temporarily starts reading everything which is left in the
input queue, tries to process the requests, and store the request output in memory. So,
sending 100,000 requests (approximately 2.8MB of request data) and then closing the
connection can make node.js temporarily use 12GB of RSS.

Resource Loop on node.js: Over the loopback interface, node.js can handle roughly ~10 Mb/s
before the assigned thread uses 100% of its CPU core (on an m5.24xlarge). RSS rose from
50MB at the start of the test to 236MB by the end of test (~3 minutes). RSS rose another
156MB when a second stream was added. With two streams, serving of content to another
(non-attacking) connection was severely impacted.

Zero-length Headers on node.js: With truly 0-length headers (i.e. the payload is 0 bytes), the
server will accept and process an unlimited number; however, they don’t seem to create a
standing queue on the server side. The processing overhead is much lighter than the
“Resource Loop” test. (Roughly 25 Mb/s only produces a 75% CPU load on the server.) With
0-length headers which are Huffman encoded into 1-byte or greater headers, the server input
for that socket (and only that socket) seems to get blocked for ~ 2 minutes, until the
connection is killed off. It appears that the server will hold the connection open even if the
client goes away. That behavior allows a different kind of DoS attack (exhaust server file
descriptors or kernel receive buffers).

Reset Flood on node.js: The server queue grows without an obvious bound until the
connection dies or the server runs out of memory and dies. After the connection ends, the
server is unresponsive while GC runs
```

## Impact

Multiple denial of service vectors.

## Attachments
No attachments
