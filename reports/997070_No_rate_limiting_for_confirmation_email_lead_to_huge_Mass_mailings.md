# No rate limiting for confirmation email lead to huge Mass mailings

## Report Details
- **Report ID**: 997070
- **URL**: https://hackerone.com/reports/997070
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-03T12:05:01.128Z
- **Disclosed**: 2020-11-04T10:45:00.563Z

## Reporter
- **Username**: lmhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
**Issue Description**
No rate limit means their is no mechanism to protect against the requests you made in a short frame of time. If the repetition doesn't give any error after 50, 100, 1000 repetitions then their will be no rate limit set. vulnerable has registred in [#297359](https://hackerone.com/reports/297359) [#774050](https://hackerone.com/reports/774050) [#922470](https://hackerone.com/reports/922470)

**URL Effected**
https://efss.qloud.my/index.php/apps/registration/

###Step-by-step Reproduction Instructions
  * Go to url https://efss.qloud.my/index.php/apps/registration/
  * Add the victim emails, and repreat to burp-suite
  * Sent request to burp-intruder, and clear all payloads ``§``
  * In the payloads set a ``null-payloads`` and run intruder
  * **Boom** 1Million request sent to victim-email

**Request**
```
POST /index.php/apps/registration/ HTTP/1.1
Host: efss.qloud.my
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 142
Origin: null
Connection: close
Upgrade-Insecure-Requests: 1

email=victimattack%40gmail.com&requesttoken=Cdt30n8l%2FBhsd0fTp4wDDyvOvA26umsBZgymNLTrJWI%3D%3AZL8W4SURzVcIIAm06cNxOlm5jUrP1QloEW3RWO2SQQA%3D
```
**Responsive Vulnerability**
```
HTTP/1.1 200 OK
Date: Sat, 03 Oct 2020 11:58:21 GMT
Server: Apache/2.4.29 (Ubuntu)
Strict-Transport-Security: max-age=15552000; includeSubDomains; preload
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: SAMEORIGIN
X-Permitted-Cross-Domain-Policies: none
X-Robots-Tag: none
X-XSS-Protection: 1; mode=block
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 13400
Connection: close
Content-Type: text/html; charset=UTF-8
```
**Proof On Concept**
F1012847
F1012846

## Impact

the attacker can send a request to the victim's email using a cloud server

## Attachments
No attachments
