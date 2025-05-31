# XSS found on Snapchat website

## Report Details
- **Report ID**: 125849
- **URL**: https://hackerone.com/reports/125849
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-25T03:11:04.743Z
- **Disclosed**: 2018-05-26T10:10:01.808Z

## Reporter
- **Username**: esnard
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Hi Snapchat Team,

I've found a reflected XSS vulnerability on this page:
https://www.snapchat.com/add/snapchat

Example:
https://www.snapchat.com/add/%22%3E%3Ch1%3EXSS%3C%2Fh1%3E

Note: you should visit the page with a mobile user-agent since the server displays different information based on the User-Agent HTTP header sent by the browser.

There are 6 places where the username isn't protected against XSS attacks:
- 4 `meta` tags: twitter:title, twitter:image, og:title, og:image
- 1 `object` tag: snapcode
- 1 `h2` tag: username

This could lead to JavaScript execution, UI redressing or open redirects.

## Attachments
No attachments
