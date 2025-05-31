# Reflected XSS In https://███████

## Report Details
- **Report ID**: 1094276
- **URL**: https://hackerone.com/reports/1094276
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-03T21:06:35.128Z
- **Disclosed**: 2021-02-10T21:01:14.144Z

## Reporter
- **Username**: sleepnotf0und
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi security team,
According to my report #1092618, The VDP team agreed that ***████*** and it's subdomains is in the scope of the DoD program
So I continue testing that domain

##Vulnerable Website URL:
https://███████████████%3CSvg%20OnLoad=alert(1)%3E

##Description of Security Issue:
Reflected XSS in path parameter (URI)

## Impact

Executing Javascript on behalf of the victim

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1 - Visit https://███
2 - Visit the error page /customerror
3 - Add the URI payload <Svg%20OnLoad=alert(1)>
4 - Final link https://██████████████████%3CSvg%20OnLoad=alert(1)%3E

## Suggested Mitigation/Remediation Actions
Sanitize the URI Path parameter



## Attachments
No attachments
