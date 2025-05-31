# JumpCloud API Key leaked via Open Github Repository.

## Report Details
- **Report ID**: 716292
- **URL**: https://hackerone.com/reports/716292
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-10-17T11:14:33.624Z
- **Disclosed**: 2019-12-30T15:40:29.038Z

## Reporter
- **Username**: vinothkumar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Summary:** Open Github Repo Leaking Starbucks JumbCloud API Key

**Description:** 
Team,

While going through Github search I discovered a public repository which contains Jumbcloud API Key of Starbucks. 

Repo:  [https://github.com/██████████/Project](https://github.com/██████████/Project).
File: [https://github.com/████/Project/blob/0d56bb910923da2fbee95971778923f734a25f68/getSystemUsers.go](https://github.com/████/Project/blob/0d56bb910923da2fbee95971778923f734a25f68/getSystemUsers.go)

```
req.Header.Add("x-api-key", "████████")
```

**POC**
* List systems ```
curl -H "x-api-key: ████████" "https://console.jumpcloud.com/api/systems"
``` There are multiple AWS instances present

* ```
curl -H "x-api-key: █████" "https://console.jumpcloud.com/api/systemusers"
```
* SSO Applications ```curl -H "x-api-key: ██████" "https://console.jumpcloud.com/api/applications"
``` AWS login SAM config is presents. This would leads to AWS account takeover

## Impact

This issue impact is critical as through this API anyone could 
* Execute commands on systems [https://docs.jumpcloud.com/1.0/commands/create-a-command](https://docs.jumpcloud.com/1.0/commands/create-a-command)
* Add/Remove users which has access to internal systems
* AWS Account Takeover

## Attachments
No attachments
