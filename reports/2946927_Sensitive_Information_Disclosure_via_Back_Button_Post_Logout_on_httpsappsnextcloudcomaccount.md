# Sensitive Information Disclosure via Back Button Post Logout on https://apps.nextcloud.com/account/

## Report Details
- **Report ID**: 2946927
- **URL**: https://hackerone.com/reports/2946927
- **State**: Closed
- **Severity**: low
- **Submitted**: 2025-01-18T04:10:38.553Z
- **Disclosed**: 2025-03-16T14:50:41.954Z

## Reporter
- **Username**: vulnerability_is_here
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
A cache control vulnerability was identified on the https://apps.nextcloud.com/account/ page. After logging out, sensitive information such as the user's first name, last name, and email address remains accessible by using the browser's back button. This occurs due to improper caching of authenticated pages, allowing unauthorized access to sensitive user information.


## Steps To Reproduce:
1. Navigate to https://apps.nextcloud.com/account/ and log in using valid credentials.

2. Observe that the account dashboard displays sensitive information such as your name, email, and other details.

3. Click on the Logout button.

4. Press the Back button on the browser.

5. Observe that the previous page containing sensitive information is still accessible without re-authentication.

## Supporting Material/References:
* OWASP Secure Headers Project: https://owasp.org/www-project-secure-headers/

* MDN Web Docs - Cache-Control Header: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control

## Impact

- Privacy Violation: Sensitive information is exposed to unauthorized access.

- Regulatory Non-Compliance: Fails to comply with GDPR or similar data protection regulations.

- Security Risk: In shared computer scenarios, another user could retrieve the cached content.

## Attachments
No attachments
