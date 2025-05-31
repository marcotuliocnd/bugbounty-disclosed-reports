# Cross-site Scripting (XSS) - Reflected on http://h1b4e.n2.ips.mtn.co.ug:8080 via Nginx-module

## Report Details
- **Report ID**: 1159362
- **URL**: https://hackerone.com/reports/1159362
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-09T17:55:53.585Z
- **Disclosed**: 2024-08-24T11:23:09.445Z

## Reporter
- **Username**: renzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hello,
I found a Reflected Cross site Scripting (XSS) on  http://h1b4e.n2.ips.mtn.co.ug:8080 . With this security flaw is possible rewrite the content of page, executing JS codes...

## Steps To Reproduce:
How we can reproduce the issue:

  1. Go to http://h1b4e.n2.ips.mtn.co.ug:8080/status%3E%3Cscript%3Ealert(31337)%3C%2Fscript%3E
  2. We can see alert message 31337
  
{F1259889}

## Supporting Material/References:

* https://owasp.org/www-community/attacks/xss/

## Impact

* The attacker can execute JS code.
* Rewrite the content of Page

## Attachments
- imagem_2021-04-09_145402.png
