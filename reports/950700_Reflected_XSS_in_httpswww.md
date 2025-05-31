# Reflected XSS in https://www.█████/

## Report Details
- **Report ID**: 950700
- **URL**: https://hackerone.com/reports/950700
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-04T07:51:25.522Z
- **Disclosed**: 2020-09-29T20:33:43.160Z

## Reporter
- **Username**: nirajgautamit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello Security Team,
I would like to report the XSS vulnerability on your system.
Steps To Reproduce:
Visit the following POC link and move your mouse allover index page: 
https://www.████/(Z(%22onmouseover=alert%60%60%20%22))/████████/█████.aspx

1. Tested on firefox browser:

███████
2.Tested on google chrome browser:

█████████

## Impact

An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim, or for phishing attacks.

## Attachments
No attachments
