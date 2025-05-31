# Vulnerable javascript dependency at Main domain

## Report Details
- **Report ID**: 1188643
- **URL**: https://hackerone.com/reports/1188643
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-07T20:48:11.682Z
- **Disclosed**: 2021-08-02T00:03:15.984Z

## Reporter
- **Username**: dantt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hello, 

Issue detail,

Burp observed 1 outdated JavaScript libraries with 4 known vulnerabilities.
Burp detected bootstrap version 4.0.0, which has the following vulnerabilities:

CVE-2019-8331: XSS in data-template, data-content and data-title properties of tooltip/popover 
CVE-2018-14041: XSS in data-target property of scrollspy 
CVE-2018-14040: XSS in collapse data-parent attribute 
CVE-2018-14042: XSS in data-container property of tooltip

Host:  https://sifchain.finance
Path:  /wp-content/themes/icos/assets/js/vendor/bootstrap.min.js

{F1293110}

## Impact

Potential XSS

## Attachments
- sifchain2.png
