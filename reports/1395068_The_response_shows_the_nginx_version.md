# The response shows the nginx version

## Report Details
- **Report ID**: 1395068
- **URL**: https://hackerone.com/reports/1395068
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-11-09T04:35:40.678Z
- **Disclosed**: 2021-11-11T08:05:00.552Z

## Reporter
- **Username**: cametome006
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
## Summary:
On visiting the https://cache.judge.me/ .It show the nginx version 

## Steps To Reproduce:

==send :==
```
GET / HTTP/1.1
Host: cache.judge.me
Cookie: _ga=GA1.2.907415772.1636450777; _gid=GA1.2.1767694824.1636450777; _fbp=fb.1.1636450778172.127612364; _hjid=00598a42-40f4-48cb-84ec-20b9bd4273cd; _hjFirstSeen=1; _fw_crm_v=525f94b4-2c39-4a15-fdd9-de190f62db0e; _hjAbsoluteSessionInProgress=0
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Te: trailers
Connection: close
Content-Length: 0
```

==And the response shows the nginx version==

```HTTP/2 200 OK
Date: Tue, 09 Nov 2021 04:22:44 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 21
Server: nginx/1.20.0
Vary: origin
Access-Control-Allow-Credentials: true
Access-Control-Expose-Headers: WWW-Authenticate,Server-Authorization
Cache-Control: no-cache
Accept-Ranges: bytes

{"message":"Welcome"}```
 
If you want more information comment below

## Impact

An attacker can use this information for further attacks

## Attachments
No attachments
