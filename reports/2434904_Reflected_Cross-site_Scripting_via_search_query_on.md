# Reflected Cross-site Scripting via search query on ██████

## Report Details
- **Report ID**: 2434904
- **URL**: https://hackerone.com/reports/2434904
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-03-26T16:32:57.151Z
- **Disclosed**: 2024-05-03T18:06:55.779Z

## Reporter
- **Username**: neg0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi team

I found a reflected xss via search query on ████████ that allows an attacker to execute Javascript code into victim's browser.

## PoC

1- Doing subdomain enumeration of ██████████, i found the following one: ████████
2- On the search query i saw that is injecting inside an h6 html tag:

██████████

3- So to html escape, i used the following payload to trigger the XSS: `</h6><image/src/onerror=alert(document.cookie)>`

████

## Impact

An incorrect sanitization of search query parameter allows an attacker to execute JS code into victim's browser.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Proof-of-concept above on the description.

## Suggested Mitigation/Remediation Actions
Sanitize input data from the user to avoid html/XSS injections.



## Attachments
No attachments
