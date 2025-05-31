# Header Injection In app.legalrobot.com

## Report Details
- **Report ID**: 264405
- **URL**: https://hackerone.com/reports/264405
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-29T18:33:01.777Z
- **Disclosed**: 2018-02-01T14:42:39.282Z

## Reporter
- **Username**: cuso4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
As per policy header injection are low priority bug but i recently discovered that when attacker change host to a special domain then victim will be redirect there....

My Request :

GET /sign-in HTTP/1.1
Host: app.legalrobot.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: __cfduid=d89f1b742903f9fedf12446b6bf8c8af51503233541; _ga=GA1.2.77695220.1503233606; ajs_user_id=%22jB5saN68Z69Dd64Rp%22; ajs_group_id=null; ajs_anonymous_id=%2271e53feb-3f14-49bc-acf8-25c0b9255d72%22; intercom-id-nmyyq5i5=ec9d124c-3c23-4608-9a39-f903db254744; _gat=1
Connection: close
Upgrade-Insecure-Requests: 1



200 RESPONSE 

CHANGED HOST TO XNXX.COM  ..SO REQUEST :

GET /sign-in HTTP/1.1
Host: xnxx.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: __cfduid=d89f1b742903f9fedf12446b6bf8c8af51503233541; _ga=GA1.2.77695220.1503233606; ajs_user_id=%22jB5saN68Z69Dd64Rp%22; ajs_group_id=null; ajs_anonymous_id=%2271e53feb-3f14-49bc-acf8-25c0b9255d72%22; intercom-id-nmyyq5i5=ec9d124c-3c23-4608-9a39-f903db254744; _gat=1
Connection: close
Upgrade-Insecure-Requests: 1



RESPONSE :


HTTP/1.1 301 Moved Permanently
Date: Tue, 29 Aug 2017 18:29:20 GMT
Content-Type: text/html; charset=iso-8859-1
Connection: close
Location: http://www.xnxx.com/sign-in
Vary: Accept-Encoding
Server: cloudflare-nginx
CF-RAY: 3961933e8d168860-BOM
Content-Length: 235

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="http://www.xnxx.com/sign-in">here</a>.</p>
</body></html>



It's 301 so it should not allow to moved permenanlty to a different domain this may lead to some serious attacking senario...

as fix we can block xnxx and other impactfull host 


ps: please use xnxx.com only ( as a purpose use facebook.com and others domain also but there os no redirect )  we can find many  domain as xnxx.com so there must be a strict waf ..



## Attachments
No attachments
