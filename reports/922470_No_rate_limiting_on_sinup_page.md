# No rate limiting on sinup page

## Report Details
- **Report ID**: 922470
- **URL**: https://hackerone.com/reports/922470
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-07-13T11:14:56.115Z
- **Disclosed**: 2020-09-28T10:18:05.018Z

## Reporter
- **Username**: faeeq24
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Team,

Summary:
As a best practice a login page should have a rate limiting.
Below is the captured request of respective login page of nextcloud.com
--------------------------------------------------------------------------------------------------------------------
POST /index.php/apps/preferred_providers/password/submit/D4oCzV7LrgyTtULRXsOp2 HTTP/1.1
Host: efss.qloud.my
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 65
Origin: null
Connection: close
Cookie: ocn6e46ay0uf=g5gaufmdvaa2ab480rl3m3e2fp; oc_sessionPassphrase=rXsGoXrFnFNmXjG7wqHo25XUJ75w4gCINgeLpQ6nUy8GJQel2%2F14gFzIIhagLg7o8uuIcNuNiWKdhzxUtdyDoPaPPsqsSqHk6xbJYMK1U0DuVvM%2BJ%2Bz8rB6%2B9j25LcYT; __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0

ocsapirequest=&email=<targer username>&password=<target password>
---------------------------------------------------------------------------------------------------------------------
Steps to reproduce :
1. Tamper login page and send the request to Burp Intruder.
2. Configure the payloads
3. Start the Burp Intruder

POC: 
in the attached image.


As you can see i have sent more than 85 requests ,
Therefore all the requests are being exexuted with response code 200

## Impact

Impact:
An attacker can freely bruteforce any username and can takeover any account.

## Attachments
- nextcloud1.png
