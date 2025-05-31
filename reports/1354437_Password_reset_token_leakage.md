# Password reset token leakage

## Report Details
- **Report ID**: 1354437
- **URL**: https://hackerone.com/reports/1354437
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-09-29T10:25:04.176Z
- **Disclosed**: 2022-03-26T17:59:52.390Z

## Reporter
- **Username**: shiv_shakti
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
Reset Password link : http://hackers.upchieve.org/setpassword?token=a3c448b1eb9b982f93ec39a7181ec1a2

1.Open Password reset page from email.
2.Intercept the request(I have used burp suite)
3.You can see the link for reset password in below requests

POST /j/collect?v=1&_v=j93&a=1038273919&t=pageview&_s=1&dl=https%3A%2F%2Fhackers.upchieve.org%2Fsetpassword%3Ftoken%3Da3c448b1eb9b982f93ec39a7181ec1a2&dp=%2Fsetpassword&ul=en-us&de=UTF-8&dt=UPchieve&sd=24-bit&sr=1366x768&vp=1366x657&je=0&_u=wCCAAUABAAAAAC~&jid=185704536&gjid=1537782490&cid=83313712.1632910097&tid=UA-133171872-1&_gid=1095396647.1632910097&_r=1&gtm=2ou9r0&z=1390812166 HTTP/2
Host: www.google-analytics.com
Content-Length: 0
Sec-Ch-Ua: "Chromium";v="93", " Not;A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Content-Type: text/plain
Accept: */*
Origin: https://hackers.upchieve.org
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

POC video : recording-1632911031270.webm

@thug645

## Impact

Misconfiguration

## Attachments
- recording-1632911031270.webm
