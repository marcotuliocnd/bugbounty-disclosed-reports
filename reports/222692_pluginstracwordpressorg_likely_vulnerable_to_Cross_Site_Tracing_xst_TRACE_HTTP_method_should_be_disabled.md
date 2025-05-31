# plugins.trac.wordpress.org likely vulnerable to Cross Site Tracing (xst), TRACE HTTP method should be disabled

## Report Details
- **Report ID**: 222692
- **URL**: https://hackerone.com/reports/222692
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-21T07:17:35.489Z
- **Disclosed**: 2019-11-03T16:17:13.138Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Background ##
A Cross-Site Tracing (XST) attack involves the use of Cross-site Scripting (XSS) and the TRACE HTTP method. According to RFC 2616, "TRACE allows the client to see what is being received at the other end of the request chain and use that data for testing or diagnostic information." XST could be used as a method to steal user's cookies via Cross-site Scripting (XSS) even if the cookie has the "HttpOnly" flag set and/or exposes the user's Authorization header.

The TRACE method, while apparently harmless, can be successfully leveraged in some scenarios to steal legitimate users' credentials. This attack technique was discovered by Jeremiah Grossman in 2003, in an attempt to bypass the HttpOnly tag that Microsoft introduced in Internet Explorer 6 sp1 to protect cookies from being accessed by JavaScript. As a matter of fact, one of the most recurring attack patterns in Cross Site Scripting is to access the document.cookie object and send it to a web server controlled by the attacker so that he/she can hijack the victim's session. Tagging a cookie as HttpOnly forbids JavaScript to access it, protecting it from being sent to a third party. However, **the TRACE method can be used to bypass this protection and access the cookie even in this scenario.**

Modern browsers now prevent TRACE requests being made via JavaScript, however, **other ways of sending TRACE requests with browsers have been discovered, such as using Java and Flash.**

## PoC ##
`curl -X TRACE -H "X-Header: geeknik/pentest" https://plugins.trac.wordpress.org`
```
TRACE / HTTP/1.1
User-Agent: curl/7.26.0
Host: plugins.trac.wordpress.org
Accept: */*
X-Header: geeknik/pentest
```
Since the server responds to this request, including echoing back my fake header, it is likely vulnerable to XST attacks and the step outlined in the mitigation section should be taken as soon as possible.

## Secondary PoC ##
Depending on how the server logs are collected and read, it may be possible to trigger XSS flaws in secondary applications using this method:
`curl -X TRACE -H "Via: <svg/onload=alert('XSS')>" https://plugins.trac.wordpress.org`
```
TRACE / HTTP/1.1
User-Agent: curl/7.26.0
Host: plugins.trac.wordpress.org
Accept: */*
Via: <svg/onload=alert('XSS')>
```

## Mitigation ##
In Apache versions 1.3.34, 2.0.55 and later, set the `TraceEnable` directive to `off` in the main configuration file and then restart Apache.

## Attachments
No attachments
