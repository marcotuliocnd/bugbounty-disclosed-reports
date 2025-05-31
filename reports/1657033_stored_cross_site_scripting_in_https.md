# stored cross site scripting in https://███

## Report Details
- **Report ID**: 1657033
- **URL**: https://hackerone.com/reports/1657033
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-02T12:00:48.554Z
- **Disclosed**: 2023-01-06T19:14:01.542Z

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
q_21655

## Impact

Cookie Stealing - A malicious user can steal cookies and use them to gain access to the application.
Arbitrary requests - An attacker can use XSS to send requests that appear to be from the victim to the web server.
Malware download - XSS can prompt the user to download malware. Since the prompt looks like a legitimate request from the
site, the user may be more likely to trust the request and actually install the malware.
Defacement - attacker can deface the website usig javascript code.

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
video attached

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
