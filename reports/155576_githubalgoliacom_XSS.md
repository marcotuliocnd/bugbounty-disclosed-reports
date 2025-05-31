# [github.algolia.com] XSS

## Report Details
- **Report ID**: 155576
- **URL**: https://hackerone.com/reports/155576
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-31T10:30:18.884Z
- **Disclosed**: 2016-09-01T11:32:23.008Z

## Reporter
- **Username**: bogdantcaciuc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
Hello , i found a Cross-Site-Scripting in your github subdomain.
All you have to do is to search in this input ( i attached input.PNG )

Search about ,,document domain'' 
Alert was executed , because you don't sanitize the query which comes from github 

Search about ,,svg onload'' -> github.algolia.com


Thanks.

## Attachments
- input.PNG
- xss.PNG
