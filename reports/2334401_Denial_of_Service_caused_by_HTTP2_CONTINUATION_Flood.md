# Denial of Service caused by HTTP/2 CONTINUATION Flood

## Report Details
- **Report ID**: 2334401
- **URL**: https://hackerone.com/reports/2334401
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-01-25T12:51:51.084Z
- **Disclosed**: 2024-04-22T19:52:39.534Z

## Reporter
- **Username**: bart
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I sent the following report to Apache Tomcat Security Team. They confirmed the report and assigned CVE-2024-24549. I'd like to ask if this is eligible for a bounty.

I'd like to report a DoS vulnerability in Tomcat. I tested 10.1.18 and 11.0 (tomcat:latest and tomcat:11.0 docker images respectively) and it seems that both are vulnerable.

An attacker can send headers using HTTP/2 CONTINUATION frames up to the limit of header bytes, header size and connection overhead so that connection is not dropped by a server (GOAWAY/ENHANCE_YOUR_CALM). Once frames are sent a connection is left intact and a new connection starts. After a few connections like these the server crashes with (java.lang.OutOfMemoryError: Java heap space) in the code connected to HPackHuffman decoding.

The lack of experience with Java does not allow me to debug this properly to give you a definitive answer what is causing the problem however here is my best guess:
* When sending HEADERS + N * CONTINUATION frames are sent the actual headers are stored in memory.
* When TCP connection is idle (and possibly when connection is dropped) the headers stay in memory.
* Because of this even a small number of connections are able to occupy hundreds of MB of server memory.

I'm attaching an exploit (in Golang) with reproduction steps:
* Start tomcat docker container (-m 800m limits memory to 800MB just to prove the point faster):
    `docker run -m 800m -d -p 7777:8080 --name tomcat tomcat:latest`
* SSH into a container to enable HTTP/2 (https://tomcat.apache.org/tomcat-8.5-doc/config/http.html#HTTP/2_Support).
* Stop and start container to pick up new config:
    `docker stop tomcat`
    `docker start tomcat`
* Run exploit:
    `go run exploit.go -address "[ip]:7777" -connections 50`

To test it I started a remote EC2 server. After a few seconds after the exploit starts the server becomes unresponsive, CPU goes to 100% and memory usage fills quickly (observe with docker stats). After a few seconds you'll see OOM errors in catalina log (see attachment). While the CPU will drop to 0% soon, no new connections will be processed by the server even when the exploit is not running anymore.

Here's how exploit.go works:
* It pregenerates 100 headers, each 10 chars long.
* It starts connections (-connections flag means how many active connections can be running at a time). Each connection:
    * Sends HEADERS frame.
    * Sends 8 CONTINUATION frames, each consists of 100 random headers (10 chars name and 10 chars value). These params are almost reaching the header size limits but not exceeding them so connection is not dropped.
    * Once headers are sent, connection is left intact and new connection starts.

It seems that finding a reason why the server is crashing can be challenging for the server admin because even a single full HTTP request is not made (note that the last CONTINUATION frame doesn't have END_HEADERS flag) so they won't see HTTP requests in the logs. I'm not aware of any configuration params that can prevent this attack. Thus, it seems the only mitigation is turning off HTTP/2 support (or code fix).

## Impact

It causes a server crash so complete availability loss.

## Attachments
No attachments
