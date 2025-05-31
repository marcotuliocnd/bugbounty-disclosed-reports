# xss on reset password page

## Report Details
- **Report ID**: 1763404
- **URL**: https://hackerone.com/reports/1763404
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-11-06T02:22:04.551Z
- **Disclosed**: 2023-01-06T18:49:04.315Z

## Reporter
- **Username**: 0x53_0x52_0x59
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
target:https://█████/Default.aspx?TabId=81&ctl=SendPassword&returnurl=%252fUOTSHelpDesk

When a user goes on the forget password page and enters a username it is reflected onto the page. An attacker could simply enter a username like <script>alert(1)</script> and it would execute an alert not to mention there is no csrf protection allowing a attacker to possibly chain csrf with this and cause alot of harm.


references:
https://owncloud.com/security-advisories/reflected-xss-in-login-page-forgot-password-functionallity/
https://hackerone.com/reports/125059

## Impact

an attacker could steal cookies from a user social engineer them or redirect them

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
go to https://████/Default.aspx?TabId=81&ctl=SendPassword&returnurl=%252fUOTSHelpDesk
enter a payload in username field

## Suggested Mitigation/Remediation Actions
put a character limit and sanitize user input



## Attachments
No attachments
