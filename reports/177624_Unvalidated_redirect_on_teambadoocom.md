# Unvalidated redirect on team.badoo.com

## Report Details
- **Report ID**: 177624
- **URL**: https://hackerone.com/reports/177624
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-23T09:13:56.683Z
- **Disclosed**: 2016-12-03T12:22:31.916Z

## Reporter
- **Username**: tsug0d
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
#Domain affected: 
https://team.badoo.com/  (corp.badoo.com)

#PoC (Tested on Firefox): 
https://team.badoo.com/%0d%0adata:text/html;text,%3Csvg%2fonload%3Dprompt%281%29%3E
{F129735}

#Describe:
team.badoo.com may vulnerable to CRLF injection, when we inject %0d%0a into url, the Location header, entire content after %0d%0a and '/' will appear in Response header:
{F129733}

Since your server is configured pretty good that i can't do attack like HTTP response splitting or redirect to external url, i decided to test XSS on it.

Using Data URI scheme which is a uniform resource identifier (URI) scheme that provides a way to include data in-line in web pages as if they were external resources can bypass it and triggered XSS:
{F129734}


 







## Attachments
- crlf.png
- xss.png
- poc.png
