# Stored XSS in assets.txmblr.com

## Report Details
- **Report ID**: 870703
- **URL**: https://hackerone.com/reports/870703
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-11T11:15:09.682Z
- **Disclosed**: 2020-05-11T17:39:23.673Z

## Reporter
- **Username**: keer0k
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
# Description

Hi, i would like to report a issue that i think is legitimate. to get this XSS we need to create a Post in the attacker account with a payload, after this, it's necessary that a victim reblog this post and so, enter in the edit mode of their own blog, after this the victim will see a button with "CLICK ME" value, so, when the victim click in "CLICK ME" the XSS will be triggerd.

PoC payload:
```
<form>
<input type=submit formaction=javascript:alert(document.domain)>
</form>
```

# Steps to reproduce
1. go to your account
2. create a post with the payload mentioned before
3. victim reblog the post
4. victim enter in the edit mode of their own blog
5. victim click in "CLICK ME" button
6. XSS will be triggerd

## Impact

it is possible to perform malicious actions on the victim's account

## Attachments
No attachments
