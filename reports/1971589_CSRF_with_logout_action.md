# CSRF with logout action

## Report Details
- **Report ID**: 1971589
- **URL**: https://hackerone.com/reports/1971589
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2023-05-03T20:27:08.526Z
- **Disclosed**: 2023-06-16T07:59:20.707Z

## Reporter
- **Username**: mbi3s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi, I wanted let you know and saw that previously similar issue was fixed.
Repro steps: Go to https://weblate.org/pl/ and click top right icon for logging in (user-tab user-anonymous, https://weblate.org/saml2/login/?next=/pl/).
Log in using username and password (https://hosted.weblate.org/accounts/login/?next=/idp/login/process/). 
Logged in on site https://weblate.org/pl/ use link: https://weblate.org/logout/
See logged out.

The similar result with using external page with prepared CSRF payload like:
`<a href="https://weblate.org/logout/"> Click me to see bonus pack`
Here as logged in user use this link from external page, next go to tab where logged in and refresh the page - see logged out there too.

Best regards,

## Impact

Bad actor can affect the user's login status - logged out.

## Attachments
No attachments
