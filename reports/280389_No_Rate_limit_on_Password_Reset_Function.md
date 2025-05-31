# No Rate limit on Password Reset Function

## Report Details
- **Report ID**: 280389
- **URL**: https://hackerone.com/reports/280389
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-19T10:58:34.318Z
- **Disclosed**: 2017-12-12T15:15:38.464Z

## Reporter
- **Username**: akaash_pantherdefence
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Hello Infogram Security Team
***************************

###Description:-
I have identified that when resetting the password, the request has no rate limit which then can be used to brute force through one request. Which can be annoying to the infogram users.

###Steps to reproduce:-
* Request for password reset link.
* Catch the above request in burp suit send it to the repeater
* Now send continuous request to the server.

**NOTE:**  *Every time you will receive the same response which is {"status":"ok"}*

>HTTP/1.1 200 OK
Date: Thu, 19 Oct 2017 10:39:31 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 15
Connection: close
Server: nginx
X-DNS-Prefetch-Control: off
Strict-Transport-Security: max-age=10886400
X-Download-Options: noopen
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: no-referrer
X-Frame-Options: SAMEORIGIN
ETag: W/"f-VaSQ4oDUiZblZNAEkkN+sX+q3Sg"
X-Infogram-Server: b302

{"status":"ok"}

* I tried sending 25 request which was success. (It can be more..) 
{F230753}

###Solution:- 
You should limit the rate for password reset links to avoid such kind of issues.

*************************
Best Regards
*Akaash Sharma :)*

## Attachments
- poc.jpg
