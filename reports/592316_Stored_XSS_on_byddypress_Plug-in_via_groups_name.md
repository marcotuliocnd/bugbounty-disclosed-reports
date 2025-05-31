# Stored XSS on byddypress Plug-in via groups name

## Report Details
- **Report ID**: 592316
- **URL**: https://hackerone.com/reports/592316
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-29T13:45:33.100Z
- **Disclosed**: 2019-07-27T00:35:51.929Z

## Reporter
- **Username**: yxw21
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hi, I found that there is a storage xss in another output group name, but this xss needs to press the key combination to trigger. Just create or modify the group information, set the group name to the following payload, 
```
<a href="accesskey=x onclick=alert(document .domain)//"></a>
```
and then access Group page, 
if you are macos need to press, 
shift+control+option+x,
if you are windows, 
you need to press shift+alt+x, 
then it will trigger xss
{F498582}

Don't forget to enable the group feature

## Impact

Rce via xss

## Attachments
- 1.png
