# Missing rate limiting on password reset functionality allows to send lot of emails

## Report Details
- **Report ID**: 1691195
- **URL**: https://hackerone.com/reports/1691195
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-09-05T03:01:23.392Z
- **Disclosed**: 2023-03-05T17:51:35.189Z

## Reporter
- **Username**: primebeast
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
On next cloud after signing up
You can reset your password here : https://support.nextcloud.com/#password_reset
The mail you will get will redirect you to a website named Wokli.
And there you can also reset password using : https://ppp.woelkli.com/login

Here you can bypass the rate limit using IP rotate extension of burp suite.

Steps to reproduce:
 1. Go to https://ppp.woelkli.com/login
2. Enter your mail and click on reset password and intercept the request. The request will be something like this 

POST /lostpassword/email HTTP/2
Host: ppp.woelkli.com
Cookie: __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; oc_sessionPassphrase=YbNqNZBiBLj69oHQyf2o9Kcd9jlMXTrBm1Wv0xyF7aY4VI6t%2FTizoufLy8m0lU%2BHZ%2F0mCRK%2FC6VSZYjmztLv%2FQfYbjZxKVA0GtwP2q80D744o7CztCkWEtjQpvBK7jtX; ock6rp1oyjad=44hbnjo8uc6jjih95vtvie80kc
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Requesttoken: elTOLCp7a4nWX2tjz/8iSI1fDGEd8Qfqi5GpX/RNPlM=:LX++HX0TDvGabxMXp4taJ9cUVSlvq2XTvaTlHrUOByk=
Content-Length: 30
Origin: https://ppp.woelkli.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"user":"yougovxxx@gmail.com"}

3. Now send the request to repeater and try to resend it . After 7 to 8 tries it will give a rate limit and a response code of 429.
4. To bypass it login to your IP rotate and send the above request to intruder and and turn ON IP rotate and set the intruder to null payloads.
5. You will get lots of emails of reset password.


Solution: 
I Will Recommend You To Add A ReCaptcha & Sort Of Something Which Requires Manual Human Interaction To Proceed Like You Can Add Captcha Like 2+2=___ so that it cannot be brute forced and you also can have a limit at the backend for particular number upto 5 times a day user can request Forget Password Email or Link something like that will prevent you from someone exploiting this vulnerability

## Impact

If You Are Using Any Email Service Software API Or Some Tool Which Costs You For Your Email This Type Of Attack Can Result You In Financial Lose And It Can Also Slow Down Your Services It Can Take Bulk Of Storage In Sent Mail Although If Users Are Affected By This Vulnerability They Can Stop Using Your Services Which Can Lead To Business Risk

## Attachments
No attachments
