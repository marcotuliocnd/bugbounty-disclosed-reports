# No Rate Limiting on /reset-password-request/ endpoint

## Report Details
- **Report ID**: 1331268
- **URL**: https://hackerone.com/reports/1331268
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-06T14:10:25.848Z
- **Disclosed**: 2021-10-04T13:50:56.212Z

## Reporter
- **Username**: 1bdool492
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
## Summary:
Description
Hi there !
I noticed when we hit the /reset-password-request/ endpoint too many times via some proxy for e.g:- (Burp) there is no rate limit on that endpoint and you can spam the email with 100’s of requests and resend even more password reset emails to the users as there is no rate limiting on that.
I tried this on this /reset-password-request/ endpoint and like I said I was successful for sending ~10and was even able to send like 10+ request to the user for password reset requests
I have identified that when Forgetting Password for account , the request has no rate limit which then can be used to loop through one request. Which can be annoying to the root users sending mass password to one email.
## Steps To Reproduce:
Step 1-Go To This Link https://app.upchieve.org/resetpassword Enter Email Click On Forget Password
step 2- Intercept This Request In Burp And Forward Till You Found Your Number In Request Like {"user":{"email":"██████████"}}
```
POST /auth/reset/send HTTP/2
Host: app.upchieve.org
Cookie: _gcl_au=§1.1.1484875457.1629240358§; _ga=§GA1.2.1200070654.1629240360§; connect.sid=§s%3Azm4qR_w6G3xyFEBjquQQfWAhmDlfXBkO.LPSI5xUtE%2B%2FlZd65QiAzzYEgp2pW6TlVO%2F5UlvC1OBU§; _gid=§GA1.2.1429370326.1630958388§; _gat=§1§; ph_JRMZGA_RF-346IQfReUvbuoVD3Q94BM7Jij8Nk4dQbA_posthog=§%7B%22distinct_id%22%3A%2217b60522c0a339-0f288d6d60a8e08-31634645-100200-17b60522c0b74%22%2C%22%24device_id%22%3A%2217b564af5ff434-0cd1c655575f638-31634645-100200-17b564af60053%22%2C%22%24sesid%22%3A%5B1630958414668%2C%2217bbcb20111115-0336f90363f9f1-31634645-100200-17bbcb2011214b%22%5D%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22%24referrer%22%3A%22https%3A%2F%2Fupchieve.org%2F%22%2C%22%24referring_domain%22%3A%22upchieve.org%22%2C%22%24session_recording_enabled%22%3Atrue%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%7D%7D§; _gat_gtag_UA_133171872_1=§1§
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.$5$
Accept-Encoding: gzip, deflate
Newrelic: eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI2NzQ5NzQiLCJhcCI6IjQyOTE2NTEzMyIsImlkIjoiMjJhZDMxMDMwNTBkOGRhZSIsInRyIjoiNGEzMTljODFlMmQyN2Y1MzlkMGJhNTc2ZjY5Yjc2MjAiLCJ0aSI6MTYzMDk1ODQxNDY3Nn19
Traceparent: 00-4a319c81e2d27f539d0ba576f69b7620-22ad3103050d8dae-01
Tracestate: 2674974@nr=0-1-2674974-429165133-22ad3103050d8dae----1630958414676
Content-Type: application/json;charset=utf-8
X-Requested-With: XMLHttpRequest
Content-Length: 32
Te: trailers
Connection: close

{"email":"§████████§"}
```

Send it to the intruder and repeat it by 50 times
You will get 200 OK status
I already attached the PoC video too if you don't understand my explanation


{F1438577}

## Supporting Material/References:
https://hackerone.com/reports/751604
https://hackerone.com/reports/441161
https://hackerone.com/reports/280534
https://blog.pentesteracademy.com/api4-2019-weak-password-no-rate-limiting-7e37a144cf3c

## Impact

Impact If You Are Using Any Email Service Software API Or Some Tool Which Costs You For Your Email This Type Of Attack Can Result You In Financial Lose And It Can Also Slow Down Your Services It Can Take Bulk Of Storage In Sent Mail Although If Users Are Affected By This Vulnerability They Can Stop Using Your Services Which Can Lead To Business Risk

## Attachments
- upr.png
