# [public-api.wordpress.com] Stored XSS via Crafted Developer App Description

## Report Details
- **Report ID**: 293743
- **URL**: https://hackerone.com/reports/293743
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-29T15:38:11.655Z
- **Disclosed**: 2017-12-01T13:35:43.503Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hi,

An injection in the "App Description" field within the [WordPress Developers](https://developer.wordpress.com) platform can be used to store and reflect JavaScript in the `public-api.wordpress.com` context.

## Steps to reproduce

1) As the "adversary" user, please visit the WordPress.com [My Apps](https://developer.wordpress.com/apps/) page and select "Create New Application"

2) Populate the "Name" and "Website URL" fields with generic data, and set the Redirect URL to `https://google.com` for the purposes of this demonstration

3) Next, please copy the below proof of concept payload into the "Description" field, save your App, and take note of the client ID

4) Substitute the client ID into the following URL (which can be accessed by any user to reproduce this vulnerability)

```
https://public-api.wordpress.com/oauth2/authorize?client_id=YourID&redirect_uri=https://google.com&response_type=code&blog=
```

5) Finally, mouse over the `TESTLINK` text to execute the JavaScript payload.

### Proof of concept payload

```
'"><div id="test"><head><base href="javascript://"/></head><body><a href="/. /, /' onmouseover=confirm(document.domain); abc=abc">TESTLINK
```

### Supporting evidence

{F243076}

## Verified conditions

At the time of testing, I have successfully confirmed exploitability in the following environments:

* Chrome OS 63.0.3239.50 (Official Build) beta (64-bit)
* Firefox 55.0.3 stable (32-bit) on Ubuntu 16.04.3 LTS

Thanks,

Yasin

## Impact

An adversary can leverage this vulnerability in a crafted API authorisation request that, if issued by another WordPress.com user, will cause arbitrary JavaScript code to execute within the target's browser in the context of their WordPress session.

## Attachments
- WP_API_XSS.png
