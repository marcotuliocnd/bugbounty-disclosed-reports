# Misconfiguration: Missing Custom Error Page (CWE-12 & CWE-756)

## Report Details
- **Report ID**: 228873
- **URL**: https://hackerone.com/reports/228873
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-16T17:29:14.060Z
- **Disclosed**: 2017-05-16T19:09:58.965Z

## Reporter
- **Username**: wala3at
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Hi 
I found that custom errors for ```` http://portswigger.net ```` application framework `are not configured.,
so application vulnerable to CWE-756 & CWE-12
https://cwe.mitre.org/data/definitions/12.html
https://cwe.mitre.org/data/definitions/756.html
- Impact:

Default error pages gives detailed information about the error that occurred, and should not be used in production environments.

Attackers can leverage the additional information provided by a default error page to mount attacks targeted on the framework, database, or other resources used by the application.


- POC:

````   http://portswigger.net/%5c.../file  ````
{F185140}

thanks


## Attachments
- portswigger-misconfig-page.png
