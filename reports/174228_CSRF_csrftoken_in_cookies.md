# CSRF csrftoken in cookies

## Report Details
- **Report ID**: 174228
- **URL**: https://hackerone.com/reports/174228
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-10-05T23:21:18.358Z
- **Disclosed**: 2016-12-07T21:18:09.022Z

## Reporter
- **Username**: promx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hi,

Your web application generates CSRF token values inside cookies
which is not a best practice for web applications as revelation of cookies can reveal CSRF Tokens as well.
Authenticity tokens should be kept separate from cookies and should be isolated to change operations in the account only.

More description:
This report tells that the CSRF tokens are present inside of the cookies value which is not a best practice and if the cookie is intercepted and compromised than the CSRF token will also be vulnerable.

This is the Captured request of edit Statement HTTP ,In this request you can see CSRF token is generating in cookies named as csrftoken

HTTP/1.1 200 OK
Connection: close
Server: gunicorn
Date: Wed, 05 Oct 2016 23:09:42 GMT
Cache-Control: no-cache
X-Gratipay-Version: 1986
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Content-Type: text/html; charset=UTF-8
Set-Cookie: csrf_token=zxRkWnGq3I5bMcXDRUWuWWXjxdsO1JtZ; expires=Wed, 12 Oct 2016 23:09:42 GMT; Path=/; secure
X-Xss-Protection: 1; mode=block
Via: 1.1 vegur
Content-Length: 400168

Regards,
Promx

## Attachments
- gratipay.png
