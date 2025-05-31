# XSS On meta tags in profile page

## Report Details
- **Report ID**: 159984
- **URL**: https://hackerone.com/reports/159984
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-17T08:37:30.104Z
- **Disclosed**: 2016-08-21T18:39:30.071Z

## Reporter
- **Username**: plazmaz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
The profile page (https://gitlab.com/u/<user>) does not properly sanitize quotation marks, allowing for injection of attributes into the meta tags. This allows for redirection to phishing sites and other various nefarious things. I've managed to get my [profile page](https://gitlab.com/u/Plazmaz) to redirect to Bing by setting my bio to 
`0;url=http://www.bing.com" http-equiv="refresh`

## Attachments
No attachments
