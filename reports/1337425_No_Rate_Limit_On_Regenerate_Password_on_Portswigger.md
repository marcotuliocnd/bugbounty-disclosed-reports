# No Rate Limit On Regenerate Password on Portswigger

## Report Details
- **Report ID**: 1337425
- **URL**: https://hackerone.com/reports/1337425
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-09-12T10:49:43.724Z
- **Disclosed**: 2021-09-13T13:03:20.201Z

## Reporter
- **Username**: thespiritman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
##Introduction

A little bit about Rate Limit:
A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache.
In case a client made too many requests within a given timeframe, HTTP-Servers can respond with status code 429: Too Many Requests.


##Description

Tested on FireFox
Domain:  https://portswigger.net/

Steps To Reproduce:
1: First Log In into your Portswigger Account
2: GoTo On Your Account Setting
3: Click On `Change Password` Button
4: Then it will take you to the given URL: https://portswigger.net/users/regeneratepassword
5: Click on `Generate New Password` Button
6: Intercept the request in your Burp Suite.The request like following  will be generated:


	POST /users/regeneratepassword HTTP/2
	Host: portswigger.net
	Cookie: ███ __███ __█████████
	User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
	Accept: */*
	Accept-Language: en-US,en;q=0.5
	Accept-Encoding: gzip, deflate
	X-Requested-With: XMLHttpRequest
	Content-Type: multipart/form-data; boundary=---------------------------416617285834040720984250847584
	Content-Length: 579
	Origin: https://portswigger.net
	Referer: https://portswigger.net/users/regeneratepassword
	Te: trailers

	-----------------------------416617285834040720984250847584
	Content-Disposition: form-data; name="RequestVerificationToken"

	█████████
	-----------------------------416617285834040720984250847584
	Content-Disposition: form-data; name="actionType"

	Generate new password
	-----------------------------416617285834040720984250847584
	Content-Disposition: form-data; name="ajaxRequest"

	true
	-----------------------------416617285834040720984250847584--




7: Send the request to the Burp Intruder and drop the request and Turn Off the Intercept in Burp Suite.
8: Goto the Intruder.In Positions Tab, click on `Clear`.
9: In request, goto the `Accept-Language: en-US,en;q=0.5`.
	And add position:
					Accept-Language: en-US,en;q=0.§5§

10: Goto the Payloads Tab,select `Numbers` in Payload Type.				
11: Input Range from 1 to 100 in Number Range of Payloads Option. And input step 1.
12: Then Start Attack.
13: Check the response of the request then you will be able to see the `200 Ok` which means the request have been succcessfully executed.
13: Wait Some moment so that all the request executed successfully.Then lots of mail from Portswigger to regenerate 	 your password should pop up. Soon your mail box will fill up by Portswigger mail.

## Impact

If you are using any Email Service Software API Or some tool which costs you for your Email.Then this type of Attack can result you in Financial Lose and it can also slow down your services.It can take bulk of storage in sent mail.And this can lead to Business Risk.

## Attachments
No attachments
