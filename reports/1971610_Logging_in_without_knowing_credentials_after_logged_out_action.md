# Logging in without knowing credentials after logged out action

## Report Details
- **Report ID**: 1971610
- **URL**: https://hackerone.com/reports/1971610
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2023-05-03T20:40:15.213Z
- **Disclosed**: 2023-06-16T07:59:38.002Z

## Reporter
- **Username**: mbi3s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi, I noticed weird behavior about logging in when preparing last report for you.
Repro steps: Log in using incognito/private mode on https://weblate.org/pl/ - click top right https://hosted.weblate.org/accounts/login/?next=/idp/login/process/ and use password-username.
As logged in on https://weblate.org/pl/ now log out - click top right icon (Logging out). Now logged out on https://weblate.org/pl/
But now, click again icon <a href="/saml2/login/?next=/pl/" class="user-tab user-anonymous"></a>
See logged in without interaction - like type password/credentials.

Additional information:
Checked with different browsers like Firefox and Chromium based.
You can many times logging out and just clicking icon (steps above) - be logged in.

Best regards,

## Impact

Scenario: user logging out so thinks is properly logged out, next person just clicks mentioned icon and is logged in as previous user without knowing credentials.
Possible sensitive data exposure / ATO.

## Attachments
No attachments
