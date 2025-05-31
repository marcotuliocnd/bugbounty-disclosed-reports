# HttpOnly Flag not set 

## Report Details
- **Report ID**: 224006
- **URL**: https://hackerone.com/reports/224006
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-04-26T09:57:53.495Z
- **Disclosed**: 2017-05-18T04:18:33.479Z

## Reporter
- **Username**: secachhunew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by
JavaScript. If a malicious script can be run on this application then the cookie will be accessible and can
be transmitted to another site.

HTTP/1.1 200 OK
Server: nginx
Date: Wed, 26 Apr 2017 08:27:17 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Vary: Accept-Encoding
Vary: Accept-Encoding
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' stats.cihar.com; script-src 'self' 'unsafe-inline' cdnjs.cloudflare.com stats.cihar.com; connect-src 'self' api.rollbar.com; object-src 'none'; child-src 'none'; frame-ancestors 'none';
Content-Language: en
Vary: Cookie, Accept-Language
ETag: W/"ff14ef4db73c24a6ed8819291ad57358"
X-Frame-Options: SAMEORIGIN
Set-Cookie: csrftoken=6Z5qdWjjwMwKO8RDp687iboelfA31rlu37AeDGGn6zQX2FmjEaBdV6Uae3PzrTYR; expires=Wed, 25-Apr-2018 08:27:17 GMT; Max-Age=31449600; Path=/; secure
Set-Cookie: django_language=en; Path=/
Strict-Transport-Security: max-age=31536000; includeSubdomains;
X-Content-Type-Options: nosniff
Content-Length: 30247

## Attachments
No attachments
