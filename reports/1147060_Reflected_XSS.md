# Reflected XSS

## Report Details
- **Report ID**: 1147060
- **URL**: https://hackerone.com/reports/1147060
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-03T03:07:32.172Z
- **Disclosed**: 2021-06-03T16:31:58.282Z

## Reporter
- **Username**: fdeleite
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary
Reflected cross-site scripting (XSS) arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way. An attacker can execute JavaScript arbitrary code on the victim's session.

## Impact

-  Perform any action within the application that the user can perform.
-   View any information that the user is able to view.
-   Modify any information that the user is able to modify.
-   Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user..
- Steal user's cookie. 

 ### Supporting Material/References:

https://hackerone.com/reports/438240
https://portswigger.net/web-security/cross-site-scripting/reflected

## System Host(s)
www.██████.mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Go to:

 - https://www.█████████.mil/██████████=%27%3Balert(%27XSS!%27)%2F%2F

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
