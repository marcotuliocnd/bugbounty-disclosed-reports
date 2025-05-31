# Leaking password reset token via referrer from external Twitter share button

## Report Details
- **Report ID**: 244434
- **URL**: https://hackerone.com/reports/244434
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-29T16:21:51.505Z
- **Disclosed**: 2017-07-03T18:08:10.650Z

## Reporter
- **Username**: prateek_0490
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi Team,

#Description

It has been identified that the application is leaking referrer token to third party sites. In this case it was found that the pasword reset token is being leaked to third party sites which is a issue knowing the fact that it can allow any malicious users to use the token and reset the passwords of the victim.

Plus this issue becomes a bit more critical because I notice we can use the reset password tokens more then once which is another issue.

#Proof of concept

1) Request a password reset link for a valid account
2) Click on the reset link 
3) before resetting the password click on the social media links like twitter available in footer section
4) you wold notice the below request

```
GET /WakaTime HTTP/1.1
Host: twitter.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://wakatime.com/reset_password/4b4e9757-b66e-44e1-9b2e-898386cefe27/2017-06-29T16%3A41%3A37Z/eb4f3b8186b8385c71d6c9f715073177e2928c6c
Accept-Language: en-US,en;q=0.8
Cookie: guest_id=v1%3A149433114446813234; privacy_2017=1; ads_prefs="HBERAAA="; kdt=siie8hORVuREtE5Z1i9Q4JG0CPtpkDz8NoF3SWGw; remember_checked_on=1; 
```

As you can see in the referrer the reset token is getting leaked to third party sites. So, the person who has the complete control over that particular third party site can compromise the user accounts easily.

Best Regards,
Prateek Tiwari


## Attachments
No attachments
