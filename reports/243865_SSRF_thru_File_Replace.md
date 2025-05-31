# SSRF thru File Replace

## Report Details
- **Report ID**: 243865
- **URL**: https://hackerone.com/reports/243865
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-27T23:09:52.847Z
- **Disclosed**: 2018-01-06T23:11:36.808Z

## Reporter
- **Username**: zuh4n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
Hello Team,

**_Version:_**
8.2.0

**_Details:_**
I have found a possibility of Server Side Request Forgery via file 'Replace' functionality. An attacker / malicious user is able to scan local network and able to enumerate open TCP ports. The root of cause of this vulnerability:
- you are allowing to use localhost IPs in order to take a file;
- different errors returning for success and fail requests, e.g. in case if TPC port is opened - server respond is following: `Unknown mime-type: text/html; charset=UTF-8` or `A valid response status line was not found in the provided string`. In case when port is closed: `Unable to connect to 127.0.0.1:1 . Error #0: stream_socket_client(): unable to connect to 127.0.0.1:1 (Connection refused)`

**_Steps to reproduce:_**
- Login at Dashboard by any user who is able (e.g. Admin group);
- Navigate to Files > File Manager page;
- Open Replace for any uploaded file > Add remote files;
- I used following endpoints:

_TCP Port 1 (closed)_
http://127.0.0.1:1
`Unable to connect to 127.0.0.1:1 . Error #0: stream_socket_client(): unable to connect to 127.0.0.1:1 (Connection refused)`

_TCP Port 80 (open)_
http://127.0.0.1:80
`Unknown mime-type: text/html; charset=UTF-8`

_TCP Port 3305 (closed)_
http://127.0.0.1:3305
`Unable to connect to 127.0.0.1:3305 . Error #0: stream_socket_client(): unable to connect to 127.0.0.1:3305 (Connection refused)`

_TCP Port 3306 (open)_
http://127.0.0.1:3306
`A valid response status line was not found in the provided string`


**_PoC:_**
{F198015}

**_Attack scenario:_**
This feature can be used to launch SSRF attack to map the internal network. For example, this feature can be used to identify the internal open ports

Let me know in case if you have any questions.

Thanks,
Stas


## Attachments
- concrete_ssrf.png
