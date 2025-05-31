# Reflected XSS of media.indrive.com

## Report Details
- **Report ID**: 2503113
- **URL**: https://hackerone.com/reports/2503113
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-05-13T12:34:58.195Z
- **Disclosed**: 2024-07-02T13:18:01.647Z

## Reporter
- **Username**: zxwo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
hi,
I find a rxss of media.indrive.com
just view:
```
https://media.indrive.com/login/response/██████
```
will execute javascript.
████

## Impact

1.Stealing user accounts: Malicious users can use XSS code to obtain various user accounts, including email accounts, social media accounts, etc. Stealing user cookie information: XSS attacks can steal the cookie information stored by the user in the browser, thereby posing as the user identity to enter the website.
2.Hijacking the user session: Attackers can use XSS code to hijack the user's browser session and perform arbitrary operations, such as making illegal transfers, forced publishing logs, sending emails, etc. Spreading worms and viruses: XSS attacks can inject malicious code to make the user's browser perform malicious operations, and even spread worms and viruses.
3.Forced pop-up advertising pages: Malicious users can use XSS code to forcefully pop up advertising pages, thereby gaining traffic or performing other malicious operations.
4.Altering page information: XSS attacks can arbitrarily alter page information, including deleting articles. Obtaining client information: XSS attacks can obtain client information, such as the user's browsing history, real IP, open ports, etc. Controlling the victim's machine to attack other websites: Malicious users can use XSS code to control the victim's machine and then launch attacks on other websites. Elevating user permissions: XSS attacks can use other vulnerabilities to expand attacks and even elevate user permissions, including further penetrating the website.

## Attachments
No attachments
