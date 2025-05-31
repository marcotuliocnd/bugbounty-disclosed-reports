# XSS in GOCD Analytics Plugin

## Report Details
- **Report ID**: 2433634
- **URL**: https://hackerone.com/reports/2433634
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-03-25T18:10:29.474Z
- **Disclosed**: 2024-03-27T01:47:30.965Z

## Reporter
- **Username**: aviv_keller
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gocd

## Vulnerability Information
[gocd/gocd-analytics-plugin (info-message.js#L28)](https://github.com/gocd/gocd-analytics-plugin/blob/c9b5f776539b3eb68dc3177c87b99b40319f8b22/assets/js/pages/info-message.js#L28) is vulnerable to XSS via the `?msg=` parameter. 
By supplying an attack payload such as `?msg=%3Csvg%2Fonload%3Dalert%28%22XSS%22%29%20%3E`, `<svg/onload=alert("XSS") >` will be injected into the webpage.

```js
$(document).ready(function () {
  const msg = window.location.search.match(/[&?]msg=([^&]+)/);
  const msgText = msg ? decodeURIComponent(msg[1]) : "No data collected for this metric, cannot generate analytics.";

  $(document.body).html(Utils.infoMessage(msgText));
});
```
> `Utils.infoMessage` basically just wraps `msgText` in a `</p>`

## Impact

An attacker can run malicious code on servers running this plugin, comprising the integrity and confidentiality of such servers.

## Attachments
No attachments
