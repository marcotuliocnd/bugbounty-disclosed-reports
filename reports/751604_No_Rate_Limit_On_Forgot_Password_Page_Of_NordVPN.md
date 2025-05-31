# No Rate Limit On Forgot Password Page Of NordVPN

## Report Details
- **Report ID**: 751604
- **URL**: https://hackerone.com/reports/751604
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-04T20:44:30.396Z
- **Disclosed**: 2020-02-08T14:25:13.895Z

## Reporter
- **Username**: th3pr0xyb0y
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
## Introduction
A little bit about Rate Limit:
A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache.
In case a client made too many requests within a given timeframe, HTTP-Servers can respond with status code 429: Too Many Requests.
## Description:-
I have identified that when Forgetting Password for account , the request has no rate limit which then can be used to  loop  through one request. Which can be annoying to the root users sending mass password to one email.

## Steps To Reproduce The Issue
Step 1-Go To This Link https://ucp.nordvpn.com/lost-password
Enter Email  Click On Forget Password 
Step 2- Intercept This Request In Burp And Forward Till You Found Your Number In Request Like {"email":"your email here"}
-----------------------------------------------------------------------------------
POST /api/v1/users/password/remind HTTP/1.1
Host: ucp.nordvpn.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://ucp.nordvpn.com/lost-password
Content-Type: application/json
X-CSRF-TOKEN: bf5c83a8cc20614f5860b7d78db33defd0a7b771298df0a75697f1233887c533
Origin: https://ucp.nordvpn.com
Content-Length: 33
Connection: close
Cookie: __cfduid=d8a4abc6bf515ac9af9ed7f26ad7ce34d1575488422; PHPSESSID=fd0c1b36e54de850296372c91d6661f6; FirstSession=source%3D%28direct%29%26medium%3D%28none%29%26campaign%3Ddirect%26term%3D%26content%3D%26date%3D20191204; CurrentSession=source%3D%28direct%29%26medium%3D%28none%29%26campaign%3Ddirect%26term%3D%26content%3D%26date%3D20191204; _gcl_au=1.1.939613586.1575488429; fontsCssCache=true; _ga=GA1.2.1984155519.1575488431; _gid=GA1.2.1153866363.1575488431; _tq_id.TV-63728145-1.1291=fee56460f81b26c8.1575488432.0.1575491145..; ReturningSession=source%3D%28direct%29%26medium%3D%28none%29%26campaign%3Ddirect%26term%3D%26content%3D%26date%3D20191204; cf_clearance=4398f1d0e3c4c4ddbb9daa33c7f5345c8fb6d622-1575490166-0-150; locale=en; nord_countdown=1575525918702

{"email":"██████████"}
------------------------------------------------------------------------------------
Step 3- Now Send This Request To Intruder And Repeat It 100 Time By Fixing Any Arbitrary Payload Which Doesn't No Effect Request I Choose Accept-Language: en-US,en;q=0.$5$

Step 4 - See You Will Get 200 ok Status Code & 100 + Email In Your INBOX
See It Is Resulting In Mass Mailing Or Email Bombing To Your Users Which Is Bad For Business Impact

##Solution -
I Will Recommend You To Add A ReCaptcha & Sort Of Something Which Requires Manual Human Interaction To Proceed Like You Can Add Captcha Like 2+2=___ so that it cannot be brute forced and you also can have a limit at the backend for particular number upto 5 times a day user can request Forget Password Email or Link something like that will prevent you from someone exploiting this vulnerability

##POC- Find Video Attached Below

## Impact

If You Are Using Any Email Service Software API Or Some Tool Which Costs You For Your Email This Type Of Attack Can Result You In Financial Lose And It Can Also Slow Down Your Services It Can Take Bulk Of Storage In Sent Mail Although If Users Are Affected By This Vulnerability They Can Stop Using Your Services Which Can Lead To Business Risk

## Attachments
No attachments
