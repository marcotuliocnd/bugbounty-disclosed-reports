# JSBeautifier BApp: Race condition leads to memory disclosure

## Report Details
- **Report ID**: 187134
- **URL**: https://hackerone.com/reports/187134
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-01T00:10:48.976Z
- **Disclosed**: 2016-12-07T10:25:57.869Z

## Reporter
- **Username**: jelmer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Description
====================
If an attacker builds up multiple connections which will be released at the same time having a response Content-Length of 0, leaving out the response Content-Length header or having a higher Content-Length than the actual response while insinuating starting a doc-type then the stacked up connections will interfere with each other and, besides other weird behavior, will scramble the response buffers through each other.

The following behaviors have been observed.
 - Burp strips the content completely and comes back with only the headers
 - Buffers between the requests get scrambled up leading to content leaking between them
 - The original byte sequence in the buffer gets scrambled
 - Characters will get replaced with new characters

Reproduction
====================
In order to find this vulnerability I wrote a proof of concept HTTP server. This server will listen on 127.0.0.1:8000 and when opening http://127.0.0.1:8000/memspy the browser will build up open requests to the server which it will not release until a defined amount of requests are met. Then when the satisfied amount of open connections have been built up the server it will release them simultaneously.

The response the server will reply with to all these connections looks as follows:

```
HTTP/1.1 200 OK
Content-Length: -12000
Meta:%s:%d
Content-Type: text/html

<![a-z0-9]{1024}>
```

With [a-z0-9]{1024} I mean it will repeat 1 of the characters in the set a-z, 0-9, 1024 times. This character will be randomized between requests to easily distinguish between different responses. The Meta header will contain the character which was chosen in this randomization process and the batchId. A batch just means a set of requests being released at the same time.

The file spy.html will perform the requests and display the result on the screen so the result can be analyzed from the browser. Besides that there is a kill-switch for the threads. If you put 'killall=true' in the JavaScript console it will stop creating new new threads which can be useful.
The variable threads in the JavaScript must always correspond the connLimit int in Go. This regulates how many threads there should be opened. The vulnerability can be successfully triggered with as little as 4 threads and 16 characters per thread. Lower limits have not been tested.

Impact
====================
With further improvement an attacker can reliably eavesdrop on a victims browsing data if the attacker is able to lure the victim to it's server so the required connections can be established.
The response data being manipulated is also a concerning thing to note. An attacker can deliberately hold up a bunch of requests and trigger this behavior which will scramble the response and with it valuable client-side protection will be weakened.
I was unable to verify the possibility of recovering the internal memory layout remotely which could assist in circumventing ASLR but I imagine this is not too weird to consider as a possibility considering the nature of this vuln.

Discovery
====================
I was testing out the Collaborator server and due to a lack of input points I started doing random stuff. That's when I suddenly noticed that when you put the intruder on 100 threads the response would slightly differentiate every so many requests. Quite puzzled as to how this could happen I tracked down the syscalls emitted by the Burp Collaborator server which didn't reveal any anomalies.

From there I verified that it wasn't in the server so I figured it must have been something within the client processing behavior. The Collaborator server did not make use of Gzip compression or something somewhat logical which may have caused this behavior so I figured it must be a memory leak or something in the way multiple incoming requests are being handled.

From there I built a HTTP server with the capability to hold and release multiple requests but it didn't work until I copy/pased the original response from the Collaborator server as response in my server. From there it was quite clear the Content-Length was wrongly specified and there was a need for the response to start with "<!" in order to trigger it.

So, the final conclusion is, when multiple threads are being processed and the content-length has to be guessed and there is some form of doctype specification present, burp will manipulate something internally which should not be touched by multiple threads at the same time. I don't have the source but that is my best guess to look for this vulnerability.

I added some screenshots
1. Shows how the responses from the Collaborator server differentiated
2. Shows how the syscall emitted by the Collaborator server was correct but incorrectly interpreted by Burp
3. Shows the first successes with the HTTP server when it was able to hold and burst requests
4. First passive eavesdropping on memory
5. Substantial amounts of internal memory leaking
6. The final PoC server in action. Every column should be presented as the character preceding it enclosed by "<!" and ">". Burp mixes the buffers around. The other 2 digits are the batchId and pckt length
7. The PoC executing not through burp to illustrate what the server is actually sending

Some recommendations while using the server:
You may have to try a couple of times before it works properly. It is important to first start the server and after that open http://127.0.0.1:8000/memspy with the browser. The server waits specifically for 20 open connections right now and then beams them out simultaneously. If the browser naively sent a request for favicon.ico or something there will be a request too many.
spy.html must be in the same folder as 

When the server is running and you have connected with the memspy endpoint it will look something like this:
```
[system@localhost pocs]$ go run burp-pckt-burst-memspy.go 
0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.^Csignal: interrupt
```
0.1.2.3, etc represent the request number in hexadecimal.
X means the wanted amount of open connections have been achieved and the responses are being flushed


## Attachments
- 1-primal-weirdness.png
- 2-syscall.png
- 3-first-success.png
- 4-first-win.png
- 5-bigleak.png
- 6-win.png
- 7-wo-burp.png
- burp-pckt-burst-memspy.go
- spy.html
