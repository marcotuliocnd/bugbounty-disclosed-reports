# Cross-site Scripting (XSS) - Reflected on http://callertunez.mtn.com.gh/wap/noauth/sharedetail.ftl via `callback` parameter 

## Report Details
- **Report ID**: 1147176
- **URL**: https://hackerone.com/reports/1147176
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-03T04:27:39.467Z
- **Disclosed**: 2024-08-24T11:25:07.800Z

## Reporter
- **Username**: renzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hello,
I found a Reflected Cross site Scripting (XSS) on http://callertunez.mtn.com.gh/wap/noauth/sharedetail.ftl via `callback` parameter . With this security flaw is possible rewrite the content of page, executing JS codes...

## Steps To Reproduce:
How we can reproduce the issue:

  1. Go to http://callertunez.mtn.com.gh/wap/noauth/sharedetail.ftl?callback=">><img%20src=x%20onerror=confirm("Renzi")>&type=
  2. And we can see alert with Renzi message...

{F1252321}


## Supporting Material/References:
* https://owasp.org/www-community/attacks/xss/

## Impact

* The attacker can execute JS code.
* Rewrite the content of Page

## Attachments
- imagem_2021-04-03_012543.png
