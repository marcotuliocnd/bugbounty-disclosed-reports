# SSL expired subdomain leads to API swap with main and flagged cookies. Unable to log device ids and certain session tokens. 

## Report Details
- **Report ID**: 1024880
- **URL**: https://hackerone.com/reports/1024880
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-03T00:13:30.387Z
- **Disclosed**: 2020-12-03T22:48:42.920Z

## Reporter
- **Username**: babykeem
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
**SUMMARY**

- Replacing the login page of **launchpad.37signals.com** with subdomain **help-basecamphq.37signals.com** greats you to a login page in which is unsecure and with header (**sec-fetch-site: same-origin**) injected into your headers you can disable cookies such as .

**STEPS TO REPRODUCE** 

1. Visit *https://help-basecamphq.37signals.com/signin?login_hint* and continue to sign in while capturing the request

2. Compare to launchpad.37signals.com login...

**help-basecamphq.37signals.com SIGN-IN LOGS + RESPONSE**
 ```
Calling URL: https://help-basecamphq.37signals.com/session
Post Data: utf8=%E2%9C%93&authenticity_token=&product=bcx&account_id=2479412&username=VALIDCREDENTIALS&password=VALIDCREDENTIALS&commit=Log+in
Sent Headers:
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36
Content-Type: application/x-www-form-urlencoded
Sent Cookies:

Address: https://3.basecamp.com/4888641/
Response code: 200 (OK)
Received headers:
Server: openresty
Date: Mon, 02 Nov 2020 23:32:48 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Accept-CH: DPR,Width,Viewport-Width,Downlink,Save-Data
Public-Key-Pins-Report-Only: max-age=3600; includeSubdomains; pin-sha256="6X0iNAQtPIjXKEVcqZBwyMcRwq1yW60549axatu3oDE="; pin-sha256="Slt48iBVTjuRQJTjbzopminRrHSGtndY0/sj0lFf9Qk="; pin-sha256="LCa0a2j/xo/5m0U8HTBBNBNCLXBkg7+g+YpeiGJm564="; report-uri="https://zapier.com/hooks/catch/3b7uh7/"
X-Robots-Tag: none
ETag: W/"da919800df1367ee83ad09a4e8fe78c2"
Cache-Control: max-age=0, private, must-revalidate
X-Release: bc5cc4f1db8d95d854d5363d908bb0be30245a88
X-Ratelimit: {"name":"General","period":60,"limit":1000,"remaining":999,"until":"2020-11-02T23:33:00Z"}
X-Request-Id: a4e1be70-ecb8-4320-9fa5-08a2b4007558
X-Runtime: 0.696588
X-Request-Path: /4888641/
Strict-Transport-Security: max-age=15552000; includeSubDomains; preload
X-Queue-Time: 0.00046443939208984375
Timing-Allow-Origin: *
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 15634
Received cookies:
identity_id: BAhpBJz5SQE%3D--c110fcda2f9ee0d25cbb9ebea290070e022da703
session_token: 054bc465dea644def06f
device_id: BAhpA5Qtlg%3D%3D--e1a66b59f23ea1bccfd0e310927e0dc706d4dbce
_launchpad_session: 5P%2FfNTAmA5cclQ1dBfPhXtvXOpm%2BaxyiJLJ8VqLD95GHNA0jbTQdu9cGszq8mtCqhmdZg%2BUA03yzs6RSQ9dnDS5PfwtV1oEHHHfhtWvGUnc2oLVlKJ8dOK7s581jQ9LSOuYOCv4GvLaGGDGDDOlvrj%2FIppMx6I9k5gi6Ibhpib7DqRuktM83tuasg36MFmve55MY1dGccBMNDd6FqKNviEM9t8zthz6ow0H3K3%2Fovme591IU%2BQ%3D%3D--%2FUz7acgdurSFzVU4--AogFxSLfddRsqIaZzI5J6g%3D%3D
X-Release: bc5cc4f1db8d95d854d5363d908bb0be30245a88
_mkra_stck: db%3A1604359968.4249594
bc3_identity_id: BAhpBJz5SQE%3D--b6e61bb3f8a17a66d662d5b3e43bd70afaf466fa
bc3_session_verification_token: 054bc465dea644def06f
_bc3_session: 2w4ATDX9GM4pdfRmBxqvSTpR%2FoGr0h4u4zmMb8meRZGblBiAk4rdULGqlBMjKq8AJTXRqU50SqWbfPzGAKRDxhBLLqBZNs23JWUhGrGItTuSJG1WxLd3GcncYX0IinK4fz8VUEXcH6SsLxEv87n0lwjOc7TD5jZwsWDMY9ksYIkzKAwVseRZ7PLP3HYiuPW%2BtucDPZNR4KTauOJFoExRE2F9ZcbLQova0vQJYJiWBlSq2zEgwO16n0gDeb7lVzpoBkHGo8NjjJjnbFhQc1%2BvJIW843ExsAScMhBEhK8njOAGYqTHs65WFpYtWyzHHoegyU6JfDc%3D--8n%2FHProwiptDpUSX--Oz0NifYBBD0HPkKVs44RKQ%3D%3D
X-Request-Id: a4e1be70-ecb8-4320-9fa5-08a2b4007558
X-Runtime: 0.696588
```

**launchpad.37signals.com SIGN-IN LOGS + RESPONSE**
```
Calling URL: https://launchpad.37signals.com/session
Post Data: utf8=%E2%9C%93&authenticity_token=&product=bcx&account_id=2479412&username=VALIDCREDENTIALS&password=VALIDCREDENTIALS&commit=Log+in
Sent Headers:
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36
Content-Type: application/x-www-form-urlencoded
Sent Cookies:

Address: https://launchpad.37signals.com/basecamp/2479412/signin
Response code: 200 (OK)
Received headers:
Server: openresty
Date: Tue, 03 Nov 2020 00:04:38 GMT
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Status: 200 OK
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
X-Robots-Tag: noindex
ETag: W/"dc3b5ec708ae44cc631cdf4e5bcd6d07"
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 8b45d3f2-5977-4d3c-b016-202865d4e134
X-Runtime: 0.007610
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Timing-Allow-Origin: *
Received cookies:
_launchpad_session: Upml5Bl1Hh0jrE7qcFRh5OMw22YOsNQp4p0BOLKEOlI5YgGcHC0po4BpNCGnNK8GRISr3Omfn3hvkoFx9U3%2B1TRcz27e%2FZHLANAyMaqvIKUKXYKdDRvpUjAqiRvbe8RYbZuuNe9YbdRfngx4ABu6FNnQS%2BcsvWhdEqtPDWXPK0ZEuUmIO3d03bU2dtz9t1XqRGzhgwDF8tALeqUd5MzWNe5uY2u9zuCMFs9zBh5OTGISLNJV9JcvIlN2NIAKfb6eSII8g0XK1LM%2FeSx47S7dYFEU9XlSo7HkrbocB%2BSWfDbqauZRWh6%2FwIHHv%2FiuCxgHoNjuWgWj9E9vLTkAS22bExBinfLfvqHssvEeJqNoCwCi--qm6qML%2BXUGcwR4kD--rT7LCfzseLJcC72KjPIYbw%3D%3D
Response Source:
<!DOCTYPE html>
<html lang="en" class="full_height" >
<head>
  <meta name="robots" content="noarchive" />
  <meta name="viewport" content="width=100%, initial-scale=1.0, maximum-scale=1.0">
  <meta name="referrer" content="origin-when-cross-origin">
```

**OVERVIEW**
- Both logins were made with no past connections or requests. You can see that help-basecamp went through with the login and launchpad.37signals.com did not and classified my request as a robot. Not only this but help-basecamp also does not record or properly distribute cookies (identity_id, devide_id, session_token, and _launchpad_session were **ALL** flagged during the login). No other requests were trailed with this subdomain but I will be further investigating with this if consented. 

**CONCLUSION**
- *https://help-basecamphq.37signals.com/* is a vulnerable and expired subdomain in which shares all attributes with launchpad.37signals.com except it fails to flag important cookies and fails to flag robotic requests and stop credential stuffing.

**PS**: as you can also see I was able to exempt the authenticity_token from both logins with the request still going through.

## Impact

Attackers can bypass SSL verification and important cookies to access an unauthorized login page.

## Attachments
No attachments
