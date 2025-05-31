# [admin.c2fo.com] Open Redirect

## Report Details
- **Report ID**: 39198
- **URL**: https://hackerone.com/reports/39198
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2014-12-12T20:54:33.762Z
- **Disclosed**: 2016-10-29T16:08:53.614Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: c2fo

## Vulnerability Information
PoC (FireFox):
https://admin.c2fo.com///www.google.com/%2e%2e

HTTP Request:
GET ///www.google.com/%2e%2e HTTP/1.1
Host: admin.c2fo.com

HTTP Response:
Location: //www.google.com/%2e%2e/


## Attachments
No attachments
