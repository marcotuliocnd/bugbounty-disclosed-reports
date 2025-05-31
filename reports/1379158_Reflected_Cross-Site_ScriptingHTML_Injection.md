# Reflected Cross-Site Scripting/HTML Injection

## Report Details
- **Report ID**: 1379158
- **URL**: https://hackerone.com/reports/1379158
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-10-23T08:48:55.726Z
- **Disclosed**: 2021-12-17T16:54:03.525Z

## Reporter
- **Username**: jak0_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
The default ASP page at https://███/redirect/default.asp is vulnerable to reflected Cross-Site Scripting in the "url" parameter. To reproduce the issue just visit the following URL and an alert should pop up:
- https://██████████/redirect/?url=%3Cscript%3Ealert(document.domain)%3C/script%3E

It seems that the redirects subdomain is used to forward users to internal resources, so this vulnerability could be used to execute JavaScript in the context of an internal user and use the browser as a proxy or steal credentials for internal resources.

In a practical attack scenario, the XSS payload could change the location of the following VPN endpoints to a phishing site and capture VPN credentials:
- https://██████████
- https://██████
- https://███

## Impact

This vulnerability could be used practically in phishing attacks to proxy traffic through internal users' browsers and ultimately lead to internal credential leaks.

## Attachments
No attachments
