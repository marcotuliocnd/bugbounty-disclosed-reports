# xss on demo.nextcloud.com due to outdated version

## Report Details
- **Report ID**: 177713
- **URL**: https://hackerone.com/reports/177713
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-10-23T23:03:06.861Z
- **Disclosed**: 2016-11-26T14:05:06.899Z

## Reporter
- **Username**: bm666
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello. I found the possibility of introducing "html-tag" and of xss attack in the form of adding comments. Details video.
Payload: </textarea><img src=x onmouseover=alert(document.domain)>
Browser: Firefox 49.0
OS: Ubuntu 16.04

## Attachments
No attachments
