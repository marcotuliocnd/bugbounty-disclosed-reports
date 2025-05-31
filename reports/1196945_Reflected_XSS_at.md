# Reflected XSS at [████████]

## Report Details
- **Report ID**: 1196945
- **URL**: https://hackerone.com/reports/1196945
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-14T03:04:47.781Z
- **Disclosed**: 2021-06-30T20:45:54.165Z

## Reporter
- **Username**: rook1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Reflected XSS was found on the URL which can be used to steal cookies or perform any action on the behalf of the user.

## Impact

Cookie stealing, browser hijacking or any action can be performed on the behalf of the victim user

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to `https://███████%22%20onclick=%22/%3E%22%3Cimg%20src=x%20onerror=alert(1);%3E&pt=PT-15951-Pv0qVVSOyrbtIuulh8prGw8eNt4-██████████`
2. It will execute the XSS payload in the `███=` parameter in the URL.

## Suggested Mitigation/Remediation Actions
Sanitize the `███=` URL parameter properly.



## Attachments
No attachments
