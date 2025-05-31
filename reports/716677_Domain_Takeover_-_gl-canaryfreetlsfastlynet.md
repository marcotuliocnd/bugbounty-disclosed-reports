# Domain Takeover - gl-canary.freetls.fastly.net

## Report Details
- **Report ID**: 716677
- **URL**: https://hackerone.com/reports/716677
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-10-17T19:13:16.156Z
- **Disclosed**: 2023-05-30T06:50:33.091Z

## Reporter
- **Username**: mike12
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hello Gitlab!

The domain `gl-canary.freetls.fastly.net` is whitelisted in gitlab.com Content Security Policy. See `Content-Security-Policy` HTTP header from gitlab.com:

```
Content-Security-Policy: connect-src 'self' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net wss://gitlab.com https://sentry.gitlab.net https://customers.gitlab.com https://snowplow.trx.gitlab.net; frame-ancestors 'self'; frame-src 'self' https://www.google.com/recaptcha/ https://www.recaptcha.net/ https://content.googleapis.com https://content-compute.googleapis.com https://content-cloudbilling.googleapis.com https://content-cloudresourcemanager.googleapis.com https://*.codesandbox.io; img-src * data: blob:; object-src 'none'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net https://www.google.com/recaptcha/ https://www.recaptcha.net/ https://www.gstatic.com/recaptcha/ https://apis.google.com 'nonce-bjSllX/7AnVrXL1QQxsb+w=='; style-src 'self' 'unsafe-inline' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net; worker-src https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net https://gitlab.com blob:
```

This domain can be controlled from any fastly.com account:
1. Register at https://www.fastly.com/signup
2. Go to https://manage.fastly.com/services/all
3. Create a new service 
4. Use `gl-canary.global.ssl.fastly.net` as domain. (Fastly automatically creates <name>.freetls.fastly.net. See https://docs.fastly.com/en/guides/setting-up-free-tls#support-for-http2-ipv6-and-tls-12)
5. Configure hosts

## Impact

An attacker can use the domain to bypass the CSP and execute malicious client-side code (for example, the client application may have an XSS vulnerability).
The domain could potentially be used elsewhere in Gitlab application (CDN, for example).

## Attachments
No attachments
