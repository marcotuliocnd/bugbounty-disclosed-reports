# Possible CSRF during external programs

## Report Details
- **Report ID**: 174470
- **URL**: https://hackerone.com/reports/174470
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-07T09:25:30.895Z
- **Disclosed**: 2016-10-18T20:00:13.703Z

## Reporter
- **Username**: malcolmx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello,

at first i want to say that my report is the same of this report #148517 i see you accept it
as a valid one so i reported this

HackerOne allow users to Made  external programs pages for programs 
the request i test will be (The original Request )

```
POST /external_programs HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-CSRF-Token: QPxj69iMMHCtU+KrbEgKN4V2FvpgMfLSNdxMqAHlGiYc67nzsqEof33U+7Ot4b0tlyER++xPuvlP8SsyzvHg8Q==
X-Requested-With: XMLHttpRequest
Referer: https://hackerone.com/directory/new
Content-Length: 2201
Content-Type: multipart/form-data; boundary=---------------------------69012895419981
Cookie: __cfduid=d392bc78bdc47358777e96f553ba0dfd81465710456; _ga=GA1.2.113987850.1465710458; __Host-remember_me_token=BAhbCFsGaQK6q0kiGWozc3lrNWdYM3NlUjljcDlrVXI4BjoGRVRJIhcxNDc1NjY3NDg0LjA1MDMwMzIGOwBG--86fb937b8501cdfb5d966d667170cd46bc807d06; __Host-session=YXZIM09kM09tQnZJK0QyNnh6N0IxeWYwcTdOcXRtN2FjcHZwMmtHOHhWbmN5djlEUGNQdCtIWDQvRmQ3OEd2Skx2NU5oYkxxVFE3VlhzTG9nUG5xbzJQMnI1OEZyRUtpV2l4ZExxVkc3WXVWUHF5ZWhwbndld0J5T2RVQ3VIdVpEL3JSaWtEd3d1S3VMMGNKZzdib1VMT3FqbHJTOGtwYXArOHZlOHYvODBZeVpWa3doSHRMRUF5RHBYejNkUnFWcFp3TU8yaTJ1ZDZpc0RvSUtKY0tKb1VUSmpmMkRpT09oQjRBeHZXdElGNlFJZ2YwY293eTV2L3FvMnJTK3oxQXoyVzV5WGtlRUlzcEt0MzYwMnZ5QTBoaVIvWlRPS2JVYW1pTFp1RCttS0E2d3gyOTkwT3MyZktGYjgxenhEdVpob0drZVNCWkI3STJ1dDhMUzZXYVFzZUtCeXRMVUZWdXVnWmg1THMzZ1phV3l3NDhtcEtSZ2VuL2Y3MHJ1SzJBam5wVUpMVnJwbzdLUkRoWmFwbnRkZ3VHYXFyNkJBNSsxaUUxZytDUy9vRVgrby9LRUw1R01URFQzSnJIK2hmei0tY2RUVnNpcGFWK2lTTjZqTUt4S2xaQT09--3077fffe1af7167a430e145b831f251b987d701e
Connection: keep-alive

-----------------------------69012895419981
Content-Disposition: form-data; name="authenticity_token"

QPxj69iMMHCtU+KrbEgKN4V2FvpgMfLSNdxMqAHlGiYc67nzsqEof33U+7Ot4b0tlyER++xPuvlP8SsyzvHg8Q==
-----------------------------69012895419981
Content-Disposition: form-data; name="name"

test
-----------------------------69012895419981
Content-Disposition: form-data; name="handle"

edmodotest
-----------------------------69012895419981
Content-Disposition: form-data; name="about"


-----------------------------69012895419981
Content-Disposition: form-data; name="website"

edmodo.com
-----------------------------69012895419981
Content-Disposition: form-data; name="twitter_handle"


-----------------------------69012895419981
Content-Disposition: form-data; name="policy"

Exclusions

While researching, we'd like to ask you to refrain from:

    Denial of service
    Spamming
    Social engineering (including phishing) of edmodo staff or contractors
    Any physical attempts against edmodo property or data centers

-----------------------------69012895419981
Content-Disposition: form-data; name="policy_url"


-----------------------------69012895419981
Content-Disposition: form-data; name="scopes[]"


-----------------------------69012895419981
Content-Disposition: form-data; name="scopes[]"


-----------------------------69012895419981
Content-Disposition: form-data; name="offers_rewards"

true
-----------------------------69012895419981
Content-Disposition: form-data; name="thanks_url"


-----------------------------69012895419981
Content-Disposition: form-data; name="disclosure_url"


-----------------------------69012895419981
Content-Disposition: form-data; name="disclosure_method"

email
-----------------------------69012895419981
Content-Disposition: form-data; name="disclosure_email"

policy@edmodo.com
-----------------------------69012895419981
Content-Disposition: form-data; name="profile_picture"; filename=""
Content-Type: application/octet-stream


-----------------------------69012895419981
Content-Disposition: form-data; name="_ignore"


-----------------------------69012895419981--

```

{F126498}

- i removed one token from the request and the (Edited Request was)

```
POST /external_programs HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-CSRF-Token: QPxj69iMMHCtU+KrbEgKN4V2FvpgMfLSNdxMqAHlGiYc67nzsqEof33U+7Ot4b0tlyER++xPuvlP8SsyzvHg8Q==
X-Requested-With: XMLHttpRequest
Referer: https://hackerone.com/directory/new
Content-Length: 2007
Content-Type: multipart/form-data; boundary=---------------------------69012895419981
Cookie: __cfduid=d392bc78bdc47358777e96f553ba0dfd81465710456; _ga=GA1.2.113987850.1465710458; __Host-remember_me_token=BAhbCFsGaQK6q0kiGWozc3lrNWdYM3NlUjljcDlrVXI4BjoGRVRJIhcxNDc1NjY3NDg0LjA1MDMwMzIGOwBG--86fb937b8501cdfb5d966d667170cd46bc807d06; __Host-session=YXZIM09kM09tQnZJK0QyNnh6N0IxeWYwcTdOcXRtN2FjcHZwMmtHOHhWbmN5djlEUGNQdCtIWDQvRmQ3OEd2Skx2NU5oYkxxVFE3VlhzTG9nUG5xbzJQMnI1OEZyRUtpV2l4ZExxVkc3WXVWUHF5ZWhwbndld0J5T2RVQ3VIdVpEL3JSaWtEd3d1S3VMMGNKZzdib1VMT3FqbHJTOGtwYXArOHZlOHYvODBZeVpWa3doSHRMRUF5RHBYejNkUnFWcFp3TU8yaTJ1ZDZpc0RvSUtKY0tKb1VUSmpmMkRpT09oQjRBeHZXdElGNlFJZ2YwY293eTV2L3FvMnJTK3oxQXoyVzV5WGtlRUlzcEt0MzYwMnZ5QTBoaVIvWlRPS2JVYW1pTFp1RCttS0E2d3gyOTkwT3MyZktGYjgxenhEdVpob0drZVNCWkI3STJ1dDhMUzZXYVFzZUtCeXRMVUZWdXVnWmg1THMzZ1phV3l3NDhtcEtSZ2VuL2Y3MHJ1SzJBam5wVUpMVnJwbzdLUkRoWmFwbnRkZ3VHYXFyNkJBNSsxaUUxZytDUy9vRVgrby9LRUw1R01URFQzSnJIK2hmei0tY2RUVnNpcGFWK2lTTjZqTUt4S2xaQT09--3077fffe1af7167a430e145b831f251b987d701e
Connection: keep-alive


-----------------------------69012895419981
Content-Disposition: form-data; name="name"

test
-----------------------------69012895419981
Content-Disposition: form-data; name="handle"

edmodotest
-----------------------------69012895419981
Content-Disposition: form-data; name="about"


-----------------------------69012895419981
Content-Disposition: form-data; name="website"

edmodo.com
-----------------------------69012895419981
Content-Disposition: form-data; name="twitter_handle"


-----------------------------69012895419981
Content-Disposition: form-data; name="policy"

Exclusions

While researching, we'd like to ask you to refrain from:

    Denial of service
    Spamming
    Social engineering (including phishing) of edmodo staff or contractors
    Any physical attempts against edmodo property or data centers

-----------------------------69012895419981
Content-Disposition: form-data; name="policy_url"


-----------------------------69012895419981
Content-Disposition: form-data; name="scopes[]"


-----------------------------69012895419981
Content-Disposition: form-data; name="scopes[]"


-----------------------------69012895419981
Content-Disposition: form-data; name="offers_rewards"

true
-----------------------------69012895419981
Content-Disposition: form-data; name="thanks_url"


-----------------------------69012895419981
Content-Disposition: form-data; name="disclosure_url"


-----------------------------69012895419981
Content-Disposition: form-data; name="disclosure_method"

email
-----------------------------69012895419981
Content-Disposition: form-data; name="disclosure_email"

policy@edmodo.com
-----------------------------69012895419981
Content-Disposition: form-data; name="profile_picture"; filename=""
Content-Type: application/octet-stream


-----------------------------69012895419981
Content-Disposition: form-data; name="_ignore"


-----------------------------69012895419981--

```

{F126497}
- The Response was

```
HTTP/1.1 200 OK
Date: Fri, 07 Oct 2016 09:11:25 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 23
Connection: keep-alive
Cache-Control: private, no-cache, no-store, must-revalidate
Cf-Railgun: direct (waiting for pending WAN connection)
Content-Disposition: inline; filename="response."
Content-Security-Policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src www.youtube-nocookie.com a4l.hackerone-ext-content.com a5s.hackerone-ext-content.com b5s.hackerone-ext-content.com; connect-src 'self'; font-src 'self'; form-action 'self'; frame-ancestors 'none'; frame-src www.youtube-nocookie.com a4l.hackerone-ext-content.com a5s.hackerone-ext-content.com b5s.hackerone-ext-content.com; img-src 'self' data: www.google-analytics.com article-photos.hackerone-user-content.com cover-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-attachments.s3.amazonaws.com; media-src 'self'; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline';
Public-Key-Pins-Report-Only: pin-sha256="WoiWRyIOVNa9ihaBciRSC7XHjliYS9VwUGOIud4PB18="; pin-sha256="r/mIkG3eEpVdm+u/ko/cwxzOMo1bk4TyHIlByibiA5E="; pin-sha256="K87oWBWM9UZfyddvDfoxL+8lpNyoUB2ptGtn0fv6G2Q="; pin-sha256="iie1VXtL7HzAMF+/PVPR9xzT80kQxdZeJ+zduCB3uj0="; pin-sha256="cGuxAXyFXFkWm61cF4HPWX8S0srS9j0aSqN0k4AP+4A="; pin-sha256="bIlWcjiKq1mftH/xd7Hw1JO77Cr+Gv+XYcGUQWwO+A4="; pin-sha256="tXD+dGAP8rGY4PW1be90cOYEwg7pZ4G+yPZmIZWPTSg="; max-age=600; includeSubDomains;
Set-Cookie: __Host-session=MmExUGVZZm1hTURFUVdPcUZjZ1RJSzZTOHdIbUFBRTA5YmJ5RzkxbllFN0E0MGpibW0rK2lQM1phZDJ5MTJ2Z0wyVG1sbkswRk5VbGhJZFBEeU1kd2VrZTVzdktTWFhxdlZoZkVaKzVvenlOdUNMaFZ4NWVydlZaWFE2bDhZMHRwdEtKNmVxdGl6S2tKakZSUGRnSzh3UkZabGhkN3NFeXZJUlBzNXFCRkt3aGlWa255TURLeEZRczV2RXVSRllia3RWTWxqMW5Md0dsa3dBbGtheUlkODM1WlRXaWQ0bDZIMTVRSHNOcENXQWtxU3NjUkNnN2lYLzNHNVU1c3pKREx1YUE1STNmak95aVNXakdNMVgzSUt5UTRSeDdIZkNVa0NDcmpTYjhCQ2VmdFQwQjNkcjNYeW1LU1B4MXpGYXRlVGFWRElpZUVnTEpVSFF3Z2R6ZHV2WmxUNTcxMEhHMWs0Q0NQdHNkUS8zdzhJRXU1dGpYY3RUdm1ZRmdaOXB6NlNzSnd2aTZaMGg0MGNtaFRJL1dCcFhGK1JUY2JCdGpySEdwWGgwbmtRdU5KOG1VNkQ1NlcrSGJkTVBBYnloci0tclF5SGlwTDYvOTNCNC9mdDc1VGdnQT09--a5e9820750599900c23710fe48cb9e3b8f01df16; path=/; secure; HttpOnly
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-Request-Id: 143ffc42-845e-4f42-b02e-0217203976e6
X-Xss-Protection: 1; mode=block
Server: cloudflare-nginx
CF-RAY: 2ee03996db0e4149-CAI

{"handle":"edmodotest"}
```

{F126496}

Thanks

## Attachments
- Response.png
- Edited_request.png
- original_Request.png
