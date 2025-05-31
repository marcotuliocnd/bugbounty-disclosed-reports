# Cross Domain leakage of sensitive information - Leading to Account Takeover at Instagram Brand

## Report Details
- **Report ID**: 209352
- **URL**: https://hackerone.com/reports/209352
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-27T16:10:19.736Z
- **Disclosed**: 2019-06-22T14:12:56.962Z

## Reporter
- **Username**: saurabhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
**Product / URL**

https://instagram-brand.com/register/reset/<the security token here>?email=<your email here>

**Description and Impact**
After a user clicks on the password reset link obtained in inbox, the page for password resetting functionality opens. If you monitor the HTTP Requests that are done while that page is loaded, you will come to know that the 'Password Leakage Link' is leaked to third party websites.

The owner of that website can perform a security compromise by grabbing those links.

**Q. How will can account takeover be done?**
Ans: The third party has the password reset link. So they will request it in the browser. In the link, the email is also there. So, they know the username and they will set a new password and now they can use this information to perform complete account takeover.

**Additional Information:**
The referrer header does not need a user interaction i.e. clicking the third party link. All the links are instantaneously transferred without any dependence on some other action.

**Solution:**
The solution is very very SIMPLE. Just include the following HTML code in the following in code between <head> tags of the html of the page: <meta name="referrer" content="never" /> 
This will not send referrer headers to third party websites.


**Reproduction Instructions / Proof of Concept**
1. Click on your password reset link.
2. Observe the GET Requests using a local proxy.

Request # 1:

`GET /<the parameters and values> HTTP/1.1
Host: www.google-analytics.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://en.instagram-brand.com/register/reset/<the security token here>?email=<the email address here>
Connection: keep-alive`


Request # 2:

`GET /<the parameters and values> HTTP/1.1
Host: pixel.wp.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://en.instagram-brand.com/register/reset/<the security token here>?email=<the email address here>
Connection: keep-alive`

`

## Attachments
No attachments
