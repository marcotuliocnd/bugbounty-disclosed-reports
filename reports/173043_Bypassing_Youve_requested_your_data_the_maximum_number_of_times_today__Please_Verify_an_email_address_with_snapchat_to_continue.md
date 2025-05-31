# Bypassing "You've requested your data the maximum number of times today." + "Please Verify an email address with snapchat to continue" 

## Report Details
- **Report ID**: 173043
- **URL**: https://hackerone.com/reports/173043
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-30T00:38:35.237Z
- **Disclosed**: 2016-11-25T21:44:21.329Z

## Reporter
- **Username**: marwan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Hello Again , I found an 2 issues in `accounts.snapchat.com/accounts/downloadmydata` 
- The first one : Bypassing The maximum number of Data Requests per day and download the Account Data any time the Attacker wants.
- The Second : Download The Account Data without any Email verification.

____

Requirements : 
====================
- Snapchat Account.
- Software to intercept the request.

____

Summary: [First_Issue]
====================
According to This note in `Download My Data` Page 
`Note: There is a limit to the number of times per day you can download your data. ` and when the user do more than 2 requests Per day another massage appear saying `" You've requested your data the maximum number of times today. Please try again tomorrow.`  . By Using this Infected POST Method `POST /accounts/downloadmydata HTTP/1.1`  the Attacker can Make Unlimited Data requests Per day at any time he want without any restriction and every time he do it the site creates new download link + send a massage to his email, He even Can run intruder Attack Without any TIMEOUT.

____

Steps To Produce[First_Issue][Text_vresion]
====================
// Note : The first three steps If the Attacker Doesn't Have the Request Yet. //
1- Login to Activated Account throw https://accounts.snapchat.com/accounts/login
2- Browse to https://accounts.snapchat.com/accounts/downloadmydata
3- Trun on Intercept and click on `Submit Request` Button now send the request to The Repeater, and Go back to the page and click the button again to reach the maximum times per day.
4- Now when you refresh the page a massage appears saying `"You've requested your data the maximum number of times today."`
5- Now go back to the repeater and repeat the request and every time the attacker repeat it a new download link generates  + an email sent to his email.

{F124019}

____

Summary: [Second_Issue]
====================
According to [This Support page ](https://support.snapchat.com/en-US/article/download-my-data) 
`"We take the security of your data very seriously, so you [must] have a verified email address to download your data."` , Well Using The Same POST Method The Attacker can replace The Cookie and the xsrf_token too his own then repeat the request and the download link will pop-up after refreshing the page., Even when the page have a massage says "Please Verify an email address with snapchat to continue".


____

Steps To Produce[Second_Issue][Text_vresion]
====================
1- The Attacker will use the same POST Method that already saved in the repeater / Used in Issue one /
```
POST /accounts/unlock HTTP/1.1
Host: accounts.snapchat.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://accounts.snapchat.com/
Cookie: xsrf_token=qGtjuAOo2-wbMhSh5pSleQ; sc-a-session=MDAxOjAwMTrcu9aIg5J6CABp9Jgq2spVOpj0cpFQFvfTGYYk8x1lEB6EK9Ii4_-ThiXAIwaPuGx0zNKyVJNVWpF5lV7ouGvH; sc-cookies-popup-dismissed=true; sc-a-nonce=a0979ef3-d7e0-4f53-8514-cc7984ebb8fa
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 38

xsrf_token=AoaRT596SUeoTsWqXjzNPQvsZko
```
2- The Attacker will change The ` xsrf_token=kB5hC3JiO-au9yaO83iOTMqCvM4` & `cookie` But How he will get the New xsrf_token of the session ? Simply By logging in to his account then Browse to https://accounts.snapchat.com/accounts/unlock and turn on intercept then click The "Unblock" Button. Now the New cookie and the xsrf_token Will show up in the request Like This :

```
POST /accounts/unlock HTTP/1.1
Host: accounts.snapchat.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://accounts.snapchat.com/
Cookie: xsrf_token=9a8P2IH9ehlGqcMEoMdYhQ; sc-a-session=MDAxOjAwMTrSJkcOKBemtdP07Rus9rErOnjN2IzGZfERcnmbHdGfXAMoxOocWkm0VbnVJ-FopWhFYdiLF__mnp1BBrE; _ga=GA1.2.1347861360.1475026774; sc-cookies-popup-dismissed=true; sc-language=en-US; sc-a-nonce=d15d9f88-6fd0-4aeb-9ebe-d878f7eea3e0
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 38

xsrf_token=YdA7InrMTUVKsPDtuNtUB1HZHdI <======= 
```


3- Now The will Attacker go Back to the First request and replace the xsrf_token and the cookie of the session with the right one.

4- Now Repeat The Request and refresh `Download My Data` Page you will see The `Zip` file link at the top Section / "Your Data is Ready " / and in the bottom you will see This Massage "Please Verify an email address with snapchat to continue".

{F124016}

____

POC Shows The two Issues With Full_Steps [Video]:
====================
https://youtu.be/fzHxL8QZ9AE

____

Other stuff|:
====================
So what if the Attacker Logout After Doing issue one , When he login again in a different day and use the same method the server will response with  302 Found , To fix this he will use the same Trick that he used in issue 2, By browsing to `accounts/unlock` etc etc." and do unlimited requests again.

____
Thank you for your patience
Best regards,
@Marwan




## Attachments
- Not_verified_POC.png
- Unlimited_Requests_Per_Day_POC.png
