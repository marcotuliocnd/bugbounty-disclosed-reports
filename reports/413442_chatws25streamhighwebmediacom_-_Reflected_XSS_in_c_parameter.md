# [chatws25.stream.highwebmedia.com] - Reflected XSS in c parameter

## Report Details
- **Report ID**: 413442
- **URL**: https://hackerone.com/reports/413442
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-24T16:31:10.710Z
- **Disclosed**: 2018-09-26T12:15:35.623Z

## Reporter
- **Username**: kazan71p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Hi Team,

Found that `chatws25.stream.highwebmedia.com` is vulnerable to reflected XSS in `c` parameter, we can verify it with following URL, it is also a Cloudflare filter bypass:

https://chatws25.stream.highwebmedia.com/ws/007/tgpraolp/htmlfile?c=███

```
https://chatws25.stream.highwebmedia.com/ws/007/tgpraolp/htmlfile?c=███████
```

{F350412}

## Impact

One of the most common XSS attack vectors is to hijack legitimate user accounts by stealing their session cookies.

## Attachments
- Screenshot_at_Sep_25_01-29-41.png
