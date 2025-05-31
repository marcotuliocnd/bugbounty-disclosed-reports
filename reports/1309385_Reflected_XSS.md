# Reflected XSS [██████]

## Report Details
- **Report ID**: 1309385
- **URL**: https://hackerone.com/reports/1309385
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-18T04:05:42.426Z
- **Disclosed**: 2022-04-29T14:06:38.791Z

## Reporter
- **Username**: fdeleite
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Reflected cross-site scripting (XSS) arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way. An attacker can execute JavaScript arbitrary code on the victim's session.
Steps To Reproduce

 Go to this URL:
https://█████/7/0/33/1d/www.citysearch.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.domain)%3E

## Impact

- Perform any action within the application that the user can perform.
- View any information that the user is able to view.
- Modify any information that the user is able to modify.
- Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user.
- Steal user's cookie.

## Attachments
No attachments
