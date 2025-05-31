# Reflected XSS in www.dota2.com

## Report Details
- **Report ID**: 292457
- **URL**: https://hackerone.com/reports/292457
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-22T20:40:21.090Z
- **Disclosed**: 2018-05-09T17:39:38.711Z

## Reporter
- **Username**: jr0ch17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
Hi guys,

##Description
I found another XSS in www.dota2.com. This time it is located in **http://www.dota2.com/international/live/5/5/1**. However it seems that when you can change the /5/5 folders to any other number (to confirm) and it still worked. I tested this on http://www.dota2.com/international/live/1/1/1 and with other random digits.

##Steps to reproduce
1. Using any browser (except IE), go to
`www.dota2.com/international/live/5/5/1})}});alert(document.cookie);(test=>{{({<!--`
2. You'll see an alert box with your cookie.

I was able to confirm the XSS works in Firefox, Chrome and Opera so the payload successfully bypasses the Chrome XSS filter since the reflection point is directly in a javascript.

{F241581}

## Impact

As you know, with a reflected XSS, a malicious user could trick a user into browsing to a URL which would trigger the XSS and steal the user's cookie, capture keyboard strokes, etc and eventually take over a user's account. 

Thanks,

JR0ch17

## Attachments
- Dota2_XSS.png
