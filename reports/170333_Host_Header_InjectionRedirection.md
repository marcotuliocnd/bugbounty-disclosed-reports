# Host Header Injection/Redirection

## Report Details
- **Report ID**: 170333
- **URL**: https://hackerone.com/reports/170333
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-09-19T06:45:55.200Z
- **Disclosed**: 2018-02-08T23:15:27.189Z

## Reporter
- **Username**: rootnp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
rubygems.org is vulnerable to host header injection because the host header can be changed to something outside the target domain.

Attack vectors are somewhat limited but depends on how the host header is used by the back-end application code. If code references the hostname used in the URL such as password reset pages, an attacker could spoof the host header of the request in order to trick the application to forwarding the password reset email to the attackers domain instead, etc. Other attack vectors may also be possible through manipulation of hyperlinks or other misc. code that relies on the host/domain of the request.

nc rubygems.org 80
GET / HTTP/1.1
Host: google.com

HTTP/1.1 301 Moved Permanently
Server: nginx
Date: Mon, 19 Sep 2016 06:44:25 GMT
Content-Type: text/html
Transfer-Encoding: chunked
Connection: keep-alive
Location: https://google.com/
X-UA-Compatible: IE=Edge,chrome=1


## Attachments
No attachments
