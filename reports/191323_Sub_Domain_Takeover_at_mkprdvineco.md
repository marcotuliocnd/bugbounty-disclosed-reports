# Sub Domain Takeover at mk.prd.vine.co

## Report Details
- **Report ID**: 191323
- **URL**: https://hackerone.com/reports/191323
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-15T07:09:31.204Z
- **Disclosed**: 2017-02-13T22:04:02.039Z

## Reporter
- **Username**: punkrock
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hey

It looks like the EC2 Instance at `mk.prd.vine.co` has been stopped and now it has been assigned to someone else

#### Proof of Concept

1. `http://mk.prd.vine.co/` few days back didn't have port 443 open but now it does have an open port 443

Response 
```
< HTTP/1.1 426 Upgrade Required
< Date: Thu, 15 Dec 2016 07:06:34 GMT
< Content-Type: text/plain
< Content-Length: 16
< Connection: keep-alive
```

Also `http://mk.prd.vine.co/%00` pops an error

```
< HTTP/1.1 400 Bad Request
* Server awselb/2.0 is not blacklisted
< Server: awselb/2.0
< Date: Thu, 15 Dec 2016 07:06:58 GMT
< Content-Type: text/html
< Content-Length: 171
< Connection: close

<html>
<head><title>400 Bad Request</title></head>
<body bgcolor="white">
<center><h1>400 Bad Request</h1></center>
<hr><center>awselb/2.0</center>
</body>
</html>
```

So it looks like now someone's load balancer is pointing to `mk.prd.vine.co`

## Attachments
No attachments
