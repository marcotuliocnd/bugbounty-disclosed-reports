# Missing X-Frame-Options header

## Report Details
- **Report ID**: 49888
- **URL**: https://hackerone.com/reports/49888
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-03-03T11:06:04.726Z
- **Disclosed**: 2017-11-09T20:28:08.895Z

## Reporter
- **Username**: abdul_r3hman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
URL https://staging.seatme.us/

Vulnerability:
The server didn't return an X-Frame-Options header which means that this website could be at 
risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate 
whether or not a browser should be allowed to render a page in a <frame> or <iframe>. 
Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded 
into other sites.

Impact:
The impact depends on the affected web application.

Remedy:
Configure your web server to include an X-Frame-Options header.

Reference:
https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options

## Attachments
No attachments
