# Registration captcha bypass

## Report Details
- **Report ID**: 223324
- **URL**: https://hackerone.com/reports/223324
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-24T08:57:55.072Z
- **Disclosed**: 2017-05-17T14:14:53.006Z

## Reporter
- **Username**: blacky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hello,
I've found that it is possible to bypass captcha during registration. Attacker can automatize registration process and create multiple accounts.
Here are steps to reproduce:
1. Go to registration page. Type information and catch request in proxy.
2. Get correct answer for captcha and captcha ID. Here is mine:

```
POST /accounts/register/ HTTP/1.1
Host: demo.weblate.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: https://demo.weblate.org/
Cookie: csrftoken=m4egNuG72ZPay6HeEqmftrXti70UfoG2AIlbxXrKv6sW1yrSeFp2AcLucZxM1lfh; sessionid=1yefwddt15j1a1weo6dsk0znqrywvkbu; translate-tab=#suggestions
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 238

csrfmiddlewaretoken=efTfFdHlGlDFdHOuDFKRsLyINeABdaN0sT0apGsY9sgrG9y8dUNEzwmJH67tZ7mf&email=[erased]&content=&username=[erased]&first_name=test&captcha=16&captcha_id=c5c64ac6daee6cf44dce40660879085db4f352e90058fdbb0bOCAqIDI%3D
```

.3. Now attacker can use captcha answer and captcha ID to correctly register multiple times.

I tried to register once more using this captcha answer and captcha ID and it worked.

## Attachments
No attachments
