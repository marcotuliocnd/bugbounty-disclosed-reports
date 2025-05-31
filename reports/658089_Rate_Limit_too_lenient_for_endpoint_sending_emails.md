# Rate Limit too lenient for endpoint sending emails

## Report Details
- **Report ID**: 658089
- **URL**: https://hackerone.com/reports/658089
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-07-24T13:40:32.847Z
- **Disclosed**: 2020-08-19T15:11:55.662Z

## Reporter
- **Username**: harshita174
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Rate-limiting is a process that is used to define the rate at which consumers can access APIs. Also, it determines the speed at which a consumer can access APIs. Rate limit is calculated in real time.

How to reproduce?

1. Sign-up for the account for WakaTime.  Domain - www.wakatime.com
2. After signing up login to the caviar account with login credentials
3. Then,press forgot password and enter your email or temporary email address i.e https://temp-mail.org 4. Open burpsuite and intercept the request from browser ,if you get the intercepted request.
5. Send the intercepted request to the intruder, In target section check the Host and Port section . In Positions section, clear all $signs and add $ sign to the anyone parameter In Payload section, add payload type to Numbers and set Numbers range.
6. After all settings done press start attack, and the attack started till it reaches the Number range that we will set in the Payload sections.
8. And you will get the mail regarding to the  password reset links to your mail box.

HTTP Request-

POST /api/v1/users/reset_password HTTP/1.1
Host: wakatime.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://wakatime.com/
Content-Type: application/json
X-CSRFToken: ad5d275dc3197936cc18040ae1882e89b04b6cf5b6d891d0dc337b38792f61b4
X-Requested-With: XMLHttpRequest
Content-Length: 34
Connection: close

## Impact

The user will get continuous email ragarding to password reset links till the attack stop.

## Attachments
- Screenshot_(173).png
