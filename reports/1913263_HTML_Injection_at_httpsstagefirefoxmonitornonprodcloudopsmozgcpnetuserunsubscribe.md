# HTML Injection at https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/unsubscribe

## Report Details
- **Report ID**: 1913263
- **URL**: https://hackerone.com/reports/1913263
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-03-20T17:50:34.952Z
- **Disclosed**: 2023-10-20T09:32:12.474Z

## Reporter
- **Username**: avram
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
Hello, 

The "Unsubscribe" page seems to be affected by Cross-Site Scripting (XSS) .Unfortunately my IP was blocked and I couldn't go ahead with the test to find a real proof of concept. So I'll just stick to this

POC:

https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/unsubscribe?%27%22%3E%3C/title%3E%3Cscript%3Ealert(xss)%3C/script%3E%3E%3Cmarquee%3E%3Ch1%3EXSS%3C/h1%3E%3C/marquee%3E 

Cheers

## Impact

An attacker could use this to inject malicious client side code, such as JavaScript, and execute it within the context of another user. This could possibly lead to user account compromises, user’s being socially engineered and many more attacks against the application’s users.

## Attachments
- Screenshot_2023-03-20_at_17.42.34.png
- Screenshot_2023-03-20_at_17.46.22.png
