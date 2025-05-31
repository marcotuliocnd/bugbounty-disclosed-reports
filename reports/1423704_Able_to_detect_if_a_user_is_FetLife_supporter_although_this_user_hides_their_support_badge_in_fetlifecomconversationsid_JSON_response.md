# Able to detect if a user is FetLife supporter although this user hides their support badge in fetlife.com/conversations/{id} JSON response

## Report Details
- **Report ID**: 1423704
- **URL**: https://hackerone.com/reports/1423704
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-12-11T09:27:19.067Z
- **Disclosed**: 2022-02-11T11:43:06.806Z

## Reporter
- **Username**: trieulieuf9
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fetlife

## Vulnerability Information
UserA is a FetLife supporter, he also hides his support badge in his account privacy setting so that people don't know he is a supporter. However, UserB can start a conversation with userA, and by looking at `is_supporter` field in JSON response of their conversation . UserB knows that UserA is a FetLife supporter.

UserB get the following information of userA by requesting `fetlife.com/conversations/{userA-userB-conversation-id}`
```
"with_users":
[
    {
        "id": {id},
        "nickname": "userA",
        "is_supporter": true,
        "show_badge": false,
        "identity": "30F Switch",
        "url": "/users/{id}",
        "avatar_url": "{avatar_url}",
        "role": "member",
        "starts_at": 0,
        "location": "Antarctica"
    }
]
```

Full request and response: F1541333

## Attack condition
For this attack to succeed, attacker needs to start a conversation with victim regardless of victim accepting conversation request or not. Therefore, this attack works with users who set their Inbox privacy settings to `Open`, `Kinky`,`Hardcore`

## Step to Reproduce
1. Prepare 2 accounts, userA and userB. UserA is a FetLife supporter.
2. UserB goes to userA profile and start a conversation with userA from there
3. UserB goes to `https://fetlife.com/inbox`
4. UserB open browser Developer tool and open conversation he just started.
5. UserB looks at Network tab and find the request `fetlife.com/conversations/{userA-userB-conversation-id}` with JSON response
6. UserB sees `is_supporter` field to check if userA is a supporter or not.

## Impact

Attacker can detect if a user is a FetLife supporter or not. This attack works on all users, except user with `strict` inbox privacy settings.

## Attachments
- conversations_request_response.txt
