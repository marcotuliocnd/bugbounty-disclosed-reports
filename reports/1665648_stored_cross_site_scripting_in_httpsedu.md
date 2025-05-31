# stored cross site scripting in https://████████.edu

## Report Details
- **Report ID**: 1665648
- **URL**: https://hackerone.com/reports/1665648
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-10T15:39:26.424Z
- **Disclosed**: 2023-09-08T17:20:25.876Z

## Reporter
- **Username**: maskedpersian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
It was observed that the application is vulnerable to cross-site scripting (XSS). XSS is a type of attack that involves running a malicious scripts on a victim’s browser.
poc attached
another parameter at #1636345
q_23463
payload: %22%27%3e%3csvg%2fonload%3dconfirm(666)%3e

## Impact

Cookie Stealing - A malicious user can steal cookies and use them to gain access to the application.
Arbitrary requests - An attacker can use XSS to send requests that appear to be from the victim to the web server.
Malware download - XSS can prompt the user to download malware. Since the prompt looks like a legitimate request from the
site, the user may be more likely to trust the request and actually install the malware.
Defacement - attacker can deface the website usig javascript code.

## System Host(s)
████.edu

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
video attached

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
