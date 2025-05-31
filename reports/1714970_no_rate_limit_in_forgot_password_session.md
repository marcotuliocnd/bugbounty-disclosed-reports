# no rate limit in forgot password session

## Report Details
- **Report ID**: 1714970
- **URL**: https://hackerone.com/reports/1714970
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-28T08:19:38.847Z
- **Disclosed**: 2022-09-29T18:17:25.871Z

## Reporter
- **Username**: irfadps
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
A little bit about Rate Limit:
A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache.
In case a client made too many requests within a given timeframe, HTTP-Servers can respond with status code 429: Too Many Requests.
## Description:-
I have identified that when Forgetting Password for account , the request has no rate limit which then can be used to loop through one request. Which can be annoying to the root users sending mass password to one email

Steps To Reproduce The Issue

setp1 - clik this link  =    https://www.yelp.com/login?return_url=https://www.yelp.com/seeyousoon?fsid=iY6PnT2UYrAnv0ASZEs3oQ

Step 2- Intercept This Request In Burp And Forward Till You Found Your Number In Request Like

POST /j/collect?v=1&_v=j97&aip=1&a=1720823427&t=event&ni=1&_s=9&dl=https%3A%2F%2Fwww.yelp.com%2Flogin%3Freturn_url%3Dhttps%3A%2F%2Fwww.yelp.com%2Fseeyousoon%3Ffsid%3DiY6PnT2UYrAnv0ASZEs3oQ&ul=en-us&de=UTF-8&dt=Log%20In%20-%20Yelp&sd=24-bit&sr=1920x940&vp=1910x753&je=0&ec=New%20Signup&ea=signup%20click&el=submit%20forgot%20password&_u=SICAAAABAAAAAC~&jid=215130607&gjid=774412709&cid=AF761EB18AB1E206&tid=UA-30501-24&_gid=232424112.1664351398&_r=1&z=1311429197 HTTP/2
Host: www.google-analytics.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: text/plain
Content-Length: 0
Origin: https://www.yelp.com
Referer: https://www.yelp.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Te: trailers
Connection: close

Step 3- Now Send This Request To Intruder And Repeat It 100 Time By Fixing Any Arbitrary Payload Which Doesn't No Effect Request I Choose Accept-Language: en-US,en;q=0.$5$

Step 4 - See You Will Get 200 ok Status Code & 100 + Email In Your INBOX
See It Is Resulting In Mass Mailing Or Email Bombing To Your Users Which Is Bad For Business Impact


I Will Recommend You To Add A ReCaptcha & Sort Of Something Which Requires Manual Human Interaction To Proceed Like You Can Add Captcha Like 2+2=_ so that it cannot be brute forced and you also can have a limit at the backend for particular number upto 5 times a day user can request Forget Password Email or Link something like that will prevent you from someone exploiting this vulnerability

## Impact

If You Are Using Any Email Service Software API Or Some Tool Which Costs You For Your Email This Type Of Attack Can Result You In Financial Lose And It Can Also Slow Down Your Services It Can Take Bulk Of Storage In Sent Mail Although If Users Are Affected By This Vulnerability They Can Stop Using Your Services Which Can Lead To Business Risk

## Attachments
No attachments
