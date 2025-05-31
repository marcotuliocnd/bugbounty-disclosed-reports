# No Rate Limit On forgot Password Leading To Massive Email Flooding

## Report Details
- **Report ID**: 794395
- **URL**: https://hackerone.com/reports/794395
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-12T10:51:28.854Z
- **Disclosed**: 2020-02-25T09:58:48.316Z

## Reporter
- **Username**: el_chapo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: companyhub

## Vulnerability Information
## Summary:

No rate limit check on forgot password which can lead to mass mailing and spamming of users and possible employees
A little bit about Rate Limit:
A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache.
In case a client made too many requests within a given timeframe, HTTP-Servers can respond with status code 429: Too Many Requests or you can include a captcha to limit request.

## Browsers Verified In:
firefox (Linux system)

## Steps To Reproduce:
1.Go to https://accounts.companyhub.com/auth/credentials/forgotpassword

intercept the request with burpsuite



POST /a/forgot-password HTTP/1.1
Host: accounts.companyhub.com
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: */*
Accept-Language: en-US,en;q=0.§5§
Accept-Encoding: gzip, deflate
Referer: https://accounts.companyhub.com/auth/credentials/forgotpassword
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 30
Connection: close
Cookie: __cfduid=df9a10acb0ed6c3beb1b456f31191d0381581499643; _ga=GA1.2.1112499432.1581499640; _gid=GA1.2.2026149887.1581499640; _fbp=fb.1.1581499643165.621914857; _fs=2989895d-637f-4b63-bc3b-b3b5ceb33acf; _vwo_uuid_v2=D5757B6FC071256FD467820472A6D965A|f925869832a8407414983209a1daab5c; _hjid=bda621b0-e531-45fb-993f-9ac81e3a7ae8; intercom-id-twdxtxyf=abf22278-1e30-4465-bd01-12a10502a7c1; intercom-session-twdxtxyf=cnNEd3Q0eDVDdTZmc28wVzF4ZUhweWdUWlc5MlFNZnJZcW9hb1lVUUxDTEF6cTgvdThLT2pzQ2lOcmlXNVJ3YS0tOXhOWnF0aGFDUFc4OFVubUkvUFBEUT09--5b7b04d1c0de01fa7e67a15878dd03e06fa495c7; ch_terms_accepted=true; CompanySize=3; .ch_lang=en; _vis_opt_s=1%7C; utm_source=app.companyhub.com; utm_content=%2F; __resolution=1280%7C772; __remember_me=true; _gali=txtEmail; _gat=1

Email=apugodspower%40gmail.com

#Now you Send This Request To Intruder And Repeat It 100+ Times By Fixing Any Arbitrary Payload Which Does No Effect On Request So I Choose Accept-Language: en-US,en;q=0.$5$

4.Now You Will Get 200 ok Status Code & 100+(Depending on how many u wish to send) Email In Your INBOX
See It Is Resulting In Mass Mailing Or Email Bombing To Your Users Which Is Bad For Business Impact


## Supporting Material/References:
Screenshots POC is applied below

#below is poc i got 71 mail which can bring huge business impact on customers

## Impact

If You Are Using Any Email Service Software API Or Some Tool Which Charges You For Email sent This Type Of Attack Can Result You In Financial Lose And It Can Also Slow Down Your Services, It Can cause huge mails In Sent Mail Of Users, Affected By This Vulnerability They Can Stop Applying for a career in your company

## Attachments
- HUB_POC.png
- POCHUB.png
