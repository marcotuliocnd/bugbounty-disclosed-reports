# SOAP WSDL Parser SQL Code Execution

## Report Details
- **Report ID**: 390359
- **URL**: https://hackerone.com/reports/390359
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-08-03T22:44:59.457Z
- **Disclosed**: 2019-01-16T19:16:49.737Z

## Reporter
- **Username**: websecnl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
SOAP WSDL Parser SQL Code Execution

**Description:**
It was possible to parse WSDL resources and read all functions from the SOAP Admin Panel, therefor i was able to repeat the sql query with a tampered request with my own custom SQL command.
i was able to extract all the database names for PoC, there is no doubt in my mind that i could login to the admin panel and compromise the entire DoD Information System.

## Impact
Remote Code Execution

## Step-by-step Reproduction Instructions

1. Visit:███ and go to the staff links 'CIMScan'
Image: █████/34570b2eaa899ae001e1bc666be3546a.png
2. ████/c400bc1369bddeca580646b14c38a562.png
3. ████/32e085f593bfbf8599359d968cf52dc0.png

## Product, Version, and Configuration (If applicable)
Web Application

## Suggested Mitigation/Remediation Actions
I will report it to CIMScan since i am not sure if this affect's your code, it might very well be the code of CIMScan which in that case you will need to remove it from your website to prevent employees from being compromised.

## Impact

Remote Code Execution

## Attachments
No attachments
