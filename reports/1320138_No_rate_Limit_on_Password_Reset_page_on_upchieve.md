# No rate Limit on Password Reset page on upchieve

## Report Details
- **Report ID**: 1320138
- **URL**: https://hackerone.com/reports/1320138
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-26T12:01:41.545Z
- **Disclosed**: 2022-03-26T17:58:45.164Z

## Reporter
- **Username**: rupachandransangothi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
## Summary:
Introduction
A little bit about Rate Limit:
A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache.
In case a client made too many requests within a given timeframe, HTTP-Servers can respond with status code 429: Too Many Requests.
## Description:-
I have identified that when Forgetting Password for account , the request has no rate limit which then can be used to loop through one request. Which can be annoying to the root users sending mass password to one email.

## Steps To Reproduce:

Step 1 - Go To This Link  https://app.upchieve.org/resetpassword
Enter Email Click On  Password reset
Step 2- Intercept This Request In Burp And Forward Till You Found Your Number In Request Like {"email":"your email here"}
POST /auth/reset/send HTTP/1.1
Host: app.upchieve.org
Connection: close
Content-Length: 33
sec-ch-ua: ";Not A Brand";v="99", "Chromium";v="88"
tracestate: 2674974@nr=0-1-2674974-429165133-b9956c2e6b3639e7----1629976379525
traceparent: 00-e7350f9e341fa39e254aa02c0f122da0-b9956c2e6b3639e7-01
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
newrelic: eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI2NzQ5NzQiLCJhcCI6IjQyOTE2NTEzMyIsImlkIjoiYjk5NTZjMmU2YjM2MzllNyIsInRyIjoiZTczNTBmOWUzNDFmYTM5ZTI1NGFhMDJjMGYxMjJkYTAiLCJ0aSI6MTYyOTk3NjM3OTUyNX19
Content-Type: application/json;charset=UTF-8
Accept: application/json, text/plain, /
X-Requested-With: XMLHttpRequest
Origin: https://app.upchieve.org
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: connect.sid=s%3AkYhTVAV6Oj2QjvpjuTv3wJ1zKt5ufbMJ.uk31xcaQ3wYhGhW5ENHODg%2BPAi%2F%2BXR8DRmrBGOtAAv0; _gcl_au=1.1.1255782218.1629976051; __cf_bm=b5af105528eef748000d008d193bda0737ac24eb-1629975748-1800-AcBqcZPRoF1OJRXniCl5v9UBOoadddugz8c4P3RSHhLOz92UsACn7wdtKq3E0xUEGHhdTt6W8MlhhmtWaHQtIM+EBAomTYnbZ9ZxfnFt+BpeqOfbbOQYmCGhspVzU4fAzCaC1Bun8/SDKAkqHRkD/Dw=; _ga=GA1.2.238689867.1629976053; _gid=GA1.2.344859836.1629976053; _gat_gtag_UA_133171872_1=1; ph_JRMZGA_RF-346IQfReUvbuoVD3Q94BM7Jij8Nk4dQbA_posthog=%7B%22distinct_id%22%3A%226125176260945b0022963f91%22%2C%22%24device_id%22%3A%2217b8224bdc1b90-0dfb1b4a415c87-53e3566-1fa400-17b8224bdc2dd5%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22%24referrer%22%3A%22%24direct%22%2C%22%24referring_domain%22%3A%22%24direct%22%2C%22%24session_recording_enabled%22%3Atrue%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24sesid%22%3A%5B1629976379518%2C%2217b8224c6b14ef-0de7d34a9af7ee-53e3566-1fa400-17b8224c6b2ea5%22%5D%2C%22%24user_id%22%3A%226125176260945b0022963f91%22%7D

{"email":"testgokulab@gmail.com"}
Step 3- Now Send This Request To Intruder And Repeat It 100 Time By Fixing 150 Null payloads.

Step 4 - See You Will Get 200 ok Status Code & many Email In Your INBOX
See It Is Resulting In Mass Mailing Or Email Bombing To Your Users Which Is Bad For Business Impact.


## Recommendations for Fixing/Mitigation

I Will Recommend You To Add A ReCaptcha & Sort Of Something Which Requires Manual Human Interaction To Proceed Like You Can Add Captcha Like 2+2=_ so that it cannot be brute forced and you also can have a limit at the backend for particular number upto 5 times a day user can request Forget Password Email or Link something like that will prevent you from someone exploiting this vulnerability

## Impact

Impact
If You Are Using Any Email Service Software API Or Some Tool Which Costs You For Your Email This Type Of Attack Can Result You In Financial Lose And It Can Also Slow Down Your Services It Can Take Bulk Of Storage In Sent Mail Although If Users Are Affected By This Vulnerability They Can Stop Using Your Services Which Can Lead To Business Risk

## Attachments
- POC_1.png
- POC2.png
- POC_3.png
- POC_4.jpeg
