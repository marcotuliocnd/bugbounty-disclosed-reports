# [www.coursera.org] Leaking password reset link on referrer header

## Report Details
- **Report ID**: 303322
- **URL**: https://hackerone.com/reports/303322
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-01-08T18:49:48.170Z
- **Disclosed**: 2018-02-14T18:17:12.566Z

## Reporter
- **Username**: flex0geek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coursera

## Vulnerability Information
Hi team,
the user gets the email with a password reset link when opening it you will be redirected to password reset page when clicking on external links within the reset password page leaked password reset token in the referer header.

## steps:
1. open lost password page
2. enter your email and click reset password
3. open the password reset link
4. before opening the link open Burp Suite and capture the requests and you will see the request like that:

## Request:
```
GET /action/0?ti=4076177&Ver=2&mid=9b0beb68-99de-9e8e-24c4-2a60a29e1fae&evt=pageLoad&sid=bdbfb02f-0&lt=21519&pi=0&lg=en-US&sw=1920&sh=1080&sc=24&tl=Coursera%20|%20Online%20Courses%20From%20Top%20Universities.%20Join%20for%20Free%20|%20Coursera&p=https%3A%2F%2Fwww.coursera.org%2Freset%2Fconfirm%2FfhkMvqlYr4bpqkJHwn34iItOBcqCrO93MgB_pFphDhJNFKS-xq7sONu7vU7-KO5beOIM6kQqpW5RObgx6oUdKg.BTnS_SxKArWEXhC1TaVSUw.6I-Dxu6IbrszddoG8hvvSFyLmnIB4Tvxih9uGEwxYMuXRnJb7ihNbij1W_VKYMI591ic7DYedPHLUFeTaP39b2Z_bD2Je3NNuCLrASHsRxbpYKbxlle8FA_DK_b6Co4m%3Futm_medium%3Demail%26utm_source%3Dother%26utm_campaign%3Dnotifications.auto.Ztk28_SiEee7Ygp2ZjNHOA%23%2F%3F_k%3Dlz8f7f&r=&msclkid=N&rn=721572 HTTP/1.1
Host: bat.bing.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: https://www.coursera.org/reset/confirm/fhkMvqlYr4bpqkJHwn34iItOBcqCrO93MgB_pFphDhJNFKS-xq7sONu7vU7-KO5beOIM6kQqpW5RObgx6oUdKg.BTnS_SxKArWEXhC1TaVSUw.6I-Dxu6IbrszddoG8hvvSFyLmnIB4Tvxih9uGEwxYMuXRnJb7ihNbij1W_VKYMI591ic7DYedPHLUFeTaP39b2Z_bD2Je3NNuCLrASHsRxbpYKbxlle8FA_DK_b6Co4m?utm_medium=email&utm_source=other&utm_campaign=notifications.auto.Ztk28_SiEee7Ygp2ZjNHOA
Cookie: MUID=156E6B1CB499683B2539603BB0996B81; MUIDB=156E6B1CB499683B2539603BB0996B81
Connection: close
```
the password link and token confirm leaked on external host, can you see this reports #6884, #738.

## Impact

It allows the person who has control of `bat.bing.com` to change the user's password (CSRF attack), because this person knows reset password token of the user, uses a new user's password of his choice and authenticity_token is not needed to make it happen,

Thanks.

## Attachments
No attachments
