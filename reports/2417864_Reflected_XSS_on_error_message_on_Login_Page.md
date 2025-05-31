# Reflected XSS on error message on Login Page

## Report Details
- **Report ID**: 2417864
- **URL**: https://hackerone.com/reports/2417864
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-03-15T07:51:53.308Z
- **Disclosed**: 2024-05-03T18:06:08.817Z

## Reporter
- **Username**: kurogai
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Greetings!

I've found a reflected XSS on a login page on█████ . The vulnerable link is: `https://███████/users/login?error=<img src='x' onerror="alert(document.domain)">`

█████████

## Impact

An attacker can inject crafted javascript that can steal user cookies, impersionate, steal information, deface the website and redirect user to another domain

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Access `https://██████/users/login?error=<img src='x' onerror="alert(document.domain)">`

## Suggested Mitigation/Remediation Actions
Sanitize the output with htmlspecialchars();



## Attachments
No attachments
