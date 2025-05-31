# Rate-limit protection get executed in the last stage of the registration process, allowing enumeration of existing account.

## Report Details
- **Report ID**: 262830
- **URL**: https://hackerone.com/reports/262830
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-24T03:32:33.601Z
- **Disclosed**: 2018-05-03T04:47:17.572Z

## Reporter
- **Username**: tolo7010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
Summary:
======
This may be low risk impact but I need to suggest on improvement on your existing rate-limit protection on the registration page, It is an easy workaround and make the current protection more secure.

Description:
========
Unikrn increases the registration security by requiring user to enter a secured password and providing a rate limit on registration, after several attempt the server denies over-registration by returning "Suspicious Activity - Multiple Accounts Detected. Please contact support at support@unikrn.com with further questions". However the rate limit get executed in the last stage of the registration process, still allows the attacker to enumerate account on this page. 

Steps To Reproduce:
==============
1. Go to https://unikrn.com/ and click "Sign up"
2. Fill in the registration form
3. Upon submitting the form, use proxy (burp) to intercept the connection and send to repeater

After the research - except the normal successfully registration, we can categorize the server responses into 3 cases (in the following log from burp repeater):

Request/Response Case 1 - Existing email with secured password, the server returns message "Email address already registered":

[REQUEST]:
POST /apiv1/register HTTP/1.1
Host: unikrn.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Referer: https://unikrn.com/
Content-Type: application/json
Application-Version: v3.8.5-28-g570b4be
Content-Length: 161
Cookie: [Long Cookie CUT]
Connection: close

{"email_address":"hackerone1@gmail.com","day":"1","month":"1","year":"1999","state":null,"password":"a12345678","password_confirm":"a12345678","session_id":null}

[RESPONSE]:
HTTP/1.1 200 OK
Date: Thu, 24 Aug 2017 02:38:22 GMT
Content-Type: application/json
Connection: close
Access-Control-Max-Age: 86400
Cache-Control: no-store, no-cache, must-revalidate
CI: M-production C-1 V-1.2.0
Content-Security-Policy: default-src 'none'; frame-ancestors 'none'
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Set-Cookie: CW=ghocb7rti601hf8k9valkk6r0mq2fua2; expires=Sun, 03-Sep-2017 02:38:22 GMT; Max-Age=864000; path=/; domain=.unikrn.com; secure; HttpOnly
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Vary: Accept-Encoding
Vary: Origin
X-XSS-Protection: 1; mode=block
Server: cloudflare-nginx
CF-RAY: 3932ef5ab9ab3198-SIN
Content-Length: 174

{"error":true,"success":false,"msg":"Email address already registered.","msg_trans":"Email address already registered.","data":null,"code":124,"flds":null,"flds_errors":null}

Request/Response Case 2 - Non-Existence email with secured password - after several attempts the server block the registration by sending the message "Suspicious Activity - Multiple Accounts Detected. Please contact support at support@unikrn.com with further questions".

[REQUEST - header omitted]:

{"email_address":"hackerone9@gmail.com","day":"1","month":"1","year":"1999","state":null,"password":"a12345678","password_confirm":"a12345678","session_id":null}

[RESPONSE - header omitted]:

{"success": false, "error": true, "msg": "Suspicious Activity - Multiple Accounts Detected. Please contact support at support@unikrn.com with further questions.", "msg_trans": "Suspicious Activity - Multiple Accounts Detected. Please contact support at support@unikrn.com with further questions.", "code": 0, "flds": null, "data": null}

Request/Response Case 3 - Non Existence with unsecured password - the server returns a message "Password must be at least 8 characters long and contain one capital letter and one number".

[REQUEST - header omitted]

{"email_address":"hackerone9@gmail.com","day":"1","month":"1","year":"1999","state":null,"password":"12345678","password_confirm":"12345678","session_id":null}

[RESPONSE - header omitted]:

{"error":true,"success":false,"msg":"password_invalid","msg_trans":"Password must be at least 8 characters long and contain one capital letter and one number.","data":null,"code":0,"flds":null,"flds_errors":null}

Analyze the registration process:
=====================
As we can see from the server response, if we provide existing email the server responses "Case 1", if we provide non-existence email the server responses "Case 2" and "Case 3" just by the secured password condition: if we enter secured password Case 2 will be returned, else returns Case 3. From this we can analyze the registration process as:
1. The user fill in the form and send data to the server
2. The server receives request from the client and do the following task in order:
- Check if email provided already in the database, if true -> return Case 1 and end the process. (Impact: user enumeration)
- Check if password provided are secured (one char+numbers = 8 chars min), if false -> return Case 3 and end the process. (Impact: user enumeration)
- [Rate-limit protection] Check if the attempt count reach limit, if true -> return Case 2 and end the process. (Impact: user enumeration)
- If the above test pass, register the new user and return successful page.

Recommendation:
============
the rate-limit protection must be place on the first stage of processing, this is to disable user enumeration attack:
1. The user fill in the form and send data to the server
2. The server receives request from the client and do the following task in order:
- [Rate-limit protection] Check if the attempt count reach limit, if true -> return Case 2 and end the process. (No user enumeration impact: not knowing whether the email are existing or not)
- Check if email provided already in the database, if true -> return Case 1 and end the process. 
- Check if password provided are secured (one char+numbers = 8 chars min), if false -> return Case 3 and end the process. (Impact: user enumeration)
- If the above test pass, register the new user and return successful page.

Optional improvement:
===============
- There is no CSRF token / Captcha in the registration page, this make the enumeration process even easier.

As I say this may be low risk, but the fix is easy and increase more security on the existing protection scheme.

Regards,
Tolo

## Attachments
No attachments
