# [www.█████] Path-based reflected Cross Site Scripting

## Report Details
- **Report ID**: 1159371
- **URL**: https://hackerone.com/reports/1159371
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-09T18:10:16.554Z
- **Disclosed**: 2022-04-07T20:08:56.113Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
The `www.██████` endpoint is vulnerable to path-based reflected XSS which allows attackers to pass rogue JavaScript to unsuspecting users.

## Impact

This flaw allows attackers to pass rogue JavaScript to unsuspecting users. Since the user’s browser has no way to know the script should not be trusted, it will execute the script, which can then access any cookies, session tokens, or other sensitive information retained by the browser and used with your website. In fact, here is a list of 21 other things that hackers can do with an XSS flaw: https://s0md3v.github.io/21-things-xss/

## System Host(s)
www.██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit `https://www.█████████/███/"><script>alert(document.domain)</script>`

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
