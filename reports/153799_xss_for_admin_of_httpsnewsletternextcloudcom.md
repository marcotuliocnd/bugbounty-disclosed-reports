# xss for admin of https://newsletter.nextcloud.com

## Report Details
- **Report ID**: 153799
- **URL**: https://hackerone.com/reports/153799
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-25T20:50:10.156Z
- **Disclosed**: 2017-02-17T11:03:59.020Z

## Reporter
- **Username**: sergeym
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
a site https://newsletter.nextcloud.com to have phplist 3.2.5

steps to reproduce:

1. to use firefox browser, latest version
2. go to  https://newsletter.nextcloud.com/admin/?page=viewtemplate&id=123%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

3. log in as admin
4. alert box with name of domain

please, look at my poc video in attachment (has been installed phplist 3.2.5 on the localhost)



## Attachments
- 1.avi
