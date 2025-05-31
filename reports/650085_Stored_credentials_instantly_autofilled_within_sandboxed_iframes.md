# Stored credentials instantly autofilled within sandboxed iframes

## Report Details
- **Report ID**: 650085
- **URL**: https://hackerone.com/reports/650085
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-18T21:31:18.836Z
- **Disclosed**: 2019-09-10T17:42:33.416Z

## Reporter
- **Username**: alesandroortiz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
# Summary
Stored credentials are instantly autofilled within sandboxed iframes, disregarding effective origin of sandboxed iframes and the expected cross-origin restrictions

# Description
Kaspersky is expected to obey cross-origin restrictions which apply to sandboxed iframes. However, the Kaspersky Chrome extension will automatically fill-in stored credentials for the iframe's URL-based origin, even though the sandboxed iframe has an effective origin of `null`. This behavior appears to disregard the effective origin of sandboxed iframes and the expected cross-origin restrictions that would apply because of the effective origin.

For attacks, no user interaction is required (drive-by). The user only needs to load a page, and Kaspersky will immediately autofill stored credentials on page load. No prior interaction with the sandboxed iframe is required.

# Environment
- Scope: Application
- Product name: Kaspersky Password Manager (Chrome extension)
- Product version: 4.1.15
- OS name and version (incl SP): Windows 10 OS Version 1809 (Build 17763.557)
- Chrome version: 75.0.3770.100 (Official Build) (64-bit) (cohort: Stable)
- Attack type: Sensitive user data disclosure
- Maximum user privileges needed to reproduce your issue: no local privileges needed, remote

# Steps to reproduce
Demo login form (set up): https://alesandroortiz.com/~aor/security/creds-tests/test-form.html
Page containing iframe (vuln demo): https://alesandroortiz.com/~aor/security/creds-tests/test-case-sandbox.html
Page in iframe (attacker page): https://alesandroortiz.com/~aor/security/creds-tests/test-ucc-iframe.html

## Set up (to store credentials in site-controlled origin):
1. Navigate to https://alesandroortiz.com/~aor/security/creds-tests/test-form.html
2. Enter any values into the email and password input fields, then submit form. (Simulates a login on a site-controlled form.)
3. On the next page, click "Save" when Kaspersky prompts to save credentials for the origin.

## Steps to reproduce:
1. Navigate to https://alesandroortiz.com/~aor/security/creds-tests/test-case-sandbox.html

### Expected behavior:
Kaspersky does not immediately autofill credentials in the sandboxed iframe because there are no credentials stored for the unique origin (`null`). The effective origin is `null`.

### Observed behavior:
Kaspersky immediately autofills credentials in the fully sandboxed iframe, which is on its own unique origin (`null`), because there are stored credentials for the URL-based origin (`https://alesandroortiz.com`).

# Other info

The important sandbox attribute value relevant to this report is `allow-same-origin`. If this value is NOT set, the iframe will be in its own unique origin (`null`), meaning it should be untrusted. If the value is set, the iframe will be in its normal origin (based on iframe URL's origin), meaning it can interact normally with its own origin.

Sandbox bypass works on both same origin (e.g. `https://example.com`) and different origin within same domain (e.g. `https://subdomain.example.com`), even though sandbox attribute without `allow-same-origin` value by spec should be treated as a completely unique origin (e.g. `null`). Correctly following spec, Chrome sets window.origin to `null` for fully sandboxed iframes. Same-origin policy goes both ways: When a particular resource (e.g. iframe) is restricted by policy from interacting with other resources (e.g. parent window), those other resources (e.g. parent window) are also restricted from interacting with the restricted resource (e.g. iframe).

See HTML spec: https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-sandbox

> The sandbox attribute, when specified, enables a set of extra restrictions on any content hosted by the iframe. [...] When the attribute is set, the content is treated as being from a unique origin, forms, scripts, and various potentially annoying APIs are disabled, links are prevented from targeting other browsing contexts, and plugins are secured. The `allow-same-origin` keyword causes the content to be treated as being from its real origin instead of forcing it into a unique origin;

For different phrasing, also see https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#Attributes under the sandbox attribute's possible values:

> allow-same-origin: If this token is not used, the resource is treated as being from a special origin that always fails the same-origin policy.

# Demo source 

Attached HTML files are source of hosted files. To demo on your own site, change the URLs in all files to reference your demo site. Screen recording demonstrating reproduction method is also attached.

## Impact

A sandboxed iframe loaded on target site can exfiltrate credentials with no user interaction (drive-by). Sites do not expect sandboxed iframes to be able to obtain user credentials used on their site, due to expected cross-origin restrictions.

Some sites with user-controlled content use sandboxed iframes loaded from their own domain or subdomain to render user-controlled content. The vulnerability allows an attacker to exfiltrate stored credentials in when a user visits the page on the target site containing the specially crafted user-controlled content.

## Attachments
No attachments
