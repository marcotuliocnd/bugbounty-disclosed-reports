# Cookie HttpOnly Flag Not Set 

## Report Details
- **Report ID**: 190194
- **URL**: https://hackerone.com/reports/190194
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-10T20:36:00.681Z
- **Disclosed**: 2016-12-29T21:17:06.554Z

## Reporter
- **Username**: lulliii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello,
I detected that this cookie was set without the HttpOnly flag. When this flag is not present, it is possible to access the cookie via client-side script code. The HttpOnly flag is a security measure that can help mitigate the risk of cross-site scripting attacks that target session cookies of the victim. If the HttpOnly flag is set and the browser supports this feature, attacker-supplied script code will not be able to access the cookie. 

Response:
HTTP/1.1 200 OK
Connection: keep-alive
Server: gunicorn
Date: Sat, 10 Dec 2016 20:32:04 GMT
Transfer-Encoding: chunked
Set-Cookie: csrf_token=UFvQJjblqfHesnXpRwPXM2uIAC1B9hZ4; expires=Sat, 17 Dec 2016 20:32:04 GMT; Path=/; secure
X-Gratipay-Version: 2017
X-Frame-Options: SAMEORIGIN
Content-Type: text/html; charset=UTF-8
Cache-Control: no-cache
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
Via: 1.1 vegur


## Attachments
No attachments
