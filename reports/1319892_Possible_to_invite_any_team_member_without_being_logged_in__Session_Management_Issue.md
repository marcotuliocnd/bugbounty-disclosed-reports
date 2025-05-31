# Possible to invite any team member without being logged in. [ Session Management Issue ]

## Report Details
- **Report ID**: 1319892
- **URL**: https://hackerone.com/reports/1319892
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-26T06:30:52.137Z
- **Disclosed**: 2021-09-03T19:28:46.902Z

## Reporter
- **Username**: basant0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trycourier

## Vulnerability Information
Hi,
I would like to report session management issue to you, while testing i found that we can easily invite or we can easily perform invite related action, even we logged out from the the account. This mean the session are not properly managed. I didn't checked the other functionality under session management but this can prove the session won't expired after the account admin logout from his account. 

{F1425667}


#STEP TO REPRODUCE:
1. Login to your account
2. Go to the invite and intercept the invite request from the burp suite

```javascript
POST /studio/invitations?_ga=1033804257.1629921862&tenantId=583b9369-f31c-4355-bcc4-785aad9cf78f HTTP/2
Host: api.courier.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json; charset=UTF-8
Content-Length: 57
Origin: https://www.trycourier.app
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Authorization: eyJraWQiOiJPRTlwVkdlQUtCVTNxMnFlTnFPWXB6YVpobm9FK1NnaUYwdGhtMkFaSU1nPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiN2UzNzI2Ny0zOWQwLTQwNzUtOTVlMS01NTIyYzNhOWRiM2YiLCJhdWQiOiI1ZjRmbWVjMnFudXNjcDg5cWJ0OG5zdWZ0aiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJldmVudF9pZCI6IjQwYmU4Y2UzLTkxZDAtNGU0Yi1hOWE1LTBmZmVkOWUxMjAzYiIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjI5OTIzOTU3LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9wdGJSenFpTHciLCJjb2duaXRvOnVzZXJuYW1lIjoiYjdlMzcyNjctMzlkMC00MDc1LTk1ZTEtNTUyMmMzYTlkYjNmIiwiZXhwIjoxNjI5OTYwMTkzLCJpYXQiOjE2Mjk5NTY1OTMsImVtYWlsIjoiaWxvdmVidWdib3VudHlAZ21haWwuY29tIn0.gbqkE49TaxOgYwCnSkAUeausim-Phn-D1lWu_ZEuwFRGP1lBpzzNnlA3-AOCfPDjjAcueeHZJtWyMYBuDTKzFE5ZONOwo1LOyDS8TU--Ud_NAw1NO52HmeQZHGGstk4mkYd7ceAco1YpakRjaJ3SsSZlafOIk6jw6y82_ylodr1_F8iNY5--mqW5D_ioKSgcjQGpNj_ytNIQdCPsowz-LWOoNaEtwT4MjydYB1SJ1HtLNKyVatfdEWAS3FDsBaR2nOBG_Yp7hoC4leuiYTtSkPR0PlEJBqBlbRR8FJHF4-Ksa7x3D-3tQvLHq62HyVMH25QHuyQYvKbyLEFKEEr8HQ
Referer: https://www.trycourier.app/
Te: trailers

{"email":"trycourier@yopmail.com","role":"ADMINISTRATOR"}
```

3. Now logout from your account and try to send the request again. The expectation is "Session Expired or Login to perform the action". but the request executing successfully without being logged in to account. 

```javascript
HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 135
Date: Thu, 26 Aug 2021 06:13:32 GMT
X-Amzn-Requestid: 4785534c-81b7-454e-b89e-ffee8fc9014f
Access-Control-Allow-Origin: https://www.trycourier.app
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Amzn-Remapped-Content-Length: 135
X-Ratelimit-Remaining: 34
X-Amz-Apigw-Id: EqSZ4EhOIAMFdHw=
Vary: Origin
X-Ratelimit-Limit: 50
X-Content-Type-Options: nosniff
X-Amzn-Trace-Id: Root=1-6127310b-7cd190a16e3ea71251218f51
X-Cache: Miss from cloudfront
Via: 1.1 239ab88732bfa02ab05c2b2116638aeb.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: TPE51-C1
X-Amz-Cf-Id: b4UjaeoBTQuIFaG-eI-Fvyv44U_i8HIVnX_DaBlHqS7VQDjF0kOzNA==

{"code":"eyJlbmNyeXB0ZWREYXRhIjoiMWFjYjRlNzU4MjNmNDhlZWJlNTJjZWEwMTE5ZGIxOTkiLCJpdiI6IjQ3ZWQyZmNmZGVhM2E4OTYyM2VkYTE1Y2U0OTFkMzE2In0="}
```

SOLUTION:
1. Instantly expire the session once the account admin logouts from his account. 

#Please let me know if you need any extra information

## Impact

Once the session is hijacked, attacker can easily perform the request even the account admin revoke his session.

## Attachments
- Screenshot_from_2021-08-26_12-05-45.png
