# [now.informatica.com] Reflective XSS

## Report Details
- **Report ID**: 106678
- **URL**: https://hackerone.com/reports/106678
- **State**: Closed
- **Severity**: high
- **Submitted**: 2015-12-23T21:36:50.432Z
- **Disclosed**: 2016-12-09T10:10:18.321Z

## Reporter
- **Username**: robd4k
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
XSS vulnerability lies on `http://now.informatica.com/launch-next-bigdata-registration-inxpo.html?Source=homepage`

#POC

* Sign up for big data management Virtual launch event

* on parameter `company_name`  inject `'"><img src=x onerror=alert(1)>`

## Attachments
- Screenshot_2015-12-24-05-33-19.png
