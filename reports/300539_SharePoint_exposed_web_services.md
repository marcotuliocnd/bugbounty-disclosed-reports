# SharePoint exposed web services

## Report Details
- **Report ID**: 300539
- **URL**: https://hackerone.com/reports/300539
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-26T04:48:57.261Z
- **Disclosed**: 2019-12-02T19:03:05.540Z

## Reporter
- **Username**: linkks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Microsoft SharePoint is a web application platform developed by Microsoft. Because of improper configuration an anonymous user has access to the SharePoint Web Services.

The impact of this vulnerability

The SharePoint Web Services can disclose sensitive information. This information can be used to launch further attacks.

How to fix this vulnerability

Restrict access to this page.

## Impact

GET /_vti_bin/lists.asmx?WSDL HTTP/1.1
Cookie: slbPersist=942183690.0.0000; WSS_FullScreenMode=false
Host: ███
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

## Attachments
No attachments
