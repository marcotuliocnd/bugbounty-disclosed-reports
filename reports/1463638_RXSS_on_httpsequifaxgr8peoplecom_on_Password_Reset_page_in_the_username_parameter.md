# RXSS on https://equifax.gr8people.com on Password Reset page in the username parameter

## Report Details
- **Report ID**: 1463638
- **URL**: https://hackerone.com/reports/1463638
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-28T23:48:12.778Z
- **Disclosed**: 2022-03-09T17:15:26.045Z

## Reporter
- **Username**: miguel_santareno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: equifax

## Vulnerability Information
Hello,

While testing your program i came across a website that is owned by informatica and is vulnerable to RXSS on Password Reset page in the username parameter

POC:
https://equifax.gr8people.com/index.gp?method=cappportal.showPortalValidateChangePasswordCode&username=%27%22%3E%3Cimg%20src=x%20onerror=alert(1)%3E

Payload:'"><img src=x onerror=alert(1)>

works both on firefox and chrome.

firefox.png and chrome.png

Note that we can observe that the domain belongs to informatica by the footer of the page "© 2019 Equifax, Inc. All rights reserved."

regards
miguel santareno

## Impact

Attackers can execute scripts in a victim’s browser to hijack user sessions, deface web sites, insert hostile content, redirect users, hijack the user’s browser using malware, etc.

## Attachments
- firefox.png
- google.png
