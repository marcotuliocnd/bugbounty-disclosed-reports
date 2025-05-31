# XSS in steam react chat client

## Report Details
- **Report ID**: 409850
- **URL**: https://hackerone.com/reports/409850
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-09-14T17:20:41.901Z
- **Disclosed**: 2019-01-07T20:00:19.267Z

## Reporter
- **Username**: zemnmez
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
The Steam chat client both sends and receives bbcode format chat messages. These map to HTML elements, and notably the [url] bbcode tag is supported for arbitrary URLs. React has strong XSS mitigations but does not mitigate `javascript:` URI based XSS.

This is rather difficult to exploit as the client transmits sanitised messages and receives over a binary WebSocket. I've attached a video of executing this XSS, which is persistent.

## Impact

I strongly believe an attacker could get remote code execution in Steam via this method. The Steam chat client uses the same codebase as the steam web chat client, and, I imagine does so using electron or some other webview system. These systems all expose functions which allow arbitrary calls to system to allow them to be competitive with e.g. windows forms.

## Attachments
- steam-xss-1-render.mp4
