# Reflected XSS on mtnhottseat.mtn.com.gh

## Report Details
- **Report ID**: 1069527
- **URL**: https://hackerone.com/reports/1069527
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-01T03:55:44.244Z
- **Disclosed**: 2021-05-24T07:38:00.883Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
hello dear

I have found Reflected XSS on mtnhottseat.mtn.com.gh
parameters injectable /api/v2/subscribe/;

my payload "><img src=x onerror=alert(document.domain)>

URL: https://mtnhottseat.mtn.com.gh/api/v2/subscribe/;%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E

{F1140524}

## Impact

Malicious JavaScript has access to all the same objects as the rest of the web page, including access to cookies and local storage, which are often used to store session tokens. If an attacker can obtain a user's session cookie, they can then impersonate that user.

Furthermore, JavaScript can read and make arbitrary modifications to the contents of a page being displayed to a user. Therefore, XSS in conjunction with some clever social engineering opens up a lot of possibilities for an attacker.

## Attachments
- Capture.PNG
