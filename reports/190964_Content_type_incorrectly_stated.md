# Content type incorrectly stated

## Report Details
- **Report ID**: 190964
- **URL**: https://hackerone.com/reports/190964
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-12-13T23:08:13.319Z
- **Disclosed**: 2016-12-27T13:41:07.695Z

## Reporter
- **Username**: lulliii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello,
Issue detail:
The response contains the following Content-type statement:
Content-Type: image/jpeg
The response states that it contains a JPEG image. However, it actually appears to contain unrecognized content.  
Issue background:
If a web response specifies an incorrect content type, then browsers may process the response in unexpected ways. If the specified content type is a renderable text-based format, then the browser will usually attempt to parse and render the response in that format. If the specified type is an image format, then the browser will usually detect the anomaly and will analyze the actual content and attempt to determine its MIME type. Either case can lead to unexpected results, and if the content contains any user-controllable data may lead to cross-site scripting or other client-side vulnerabilities.  In most cases, the presence of an incorrect content type statement does not constitute a security flaw, particularly if the response contains static content. You should review the contents of the response and the context in which it appears to determine whether any vulnerability exists.  
Issue remediation:
For every response containing a message body, the application should include a single Content-type header which correctly and unambiguously states the MIME type of the content in the response body.  

Response:
HTTP/1.1 200 OK
Connection: keep-alive
Server: gunicorn
Date: Tue, 13 Dec 2016 22:58:22 GMT
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-Gratipay-Version: 2020
Set-Cookie: csrf_token=gasIdvRVcAs5Fp26DVBn8BJPK7zY1S9r; expires=Tue, 20 Dec 2016 22:58:22 GMT; Path=/; secure
X-Xss-Protection: 1; mode=block
Content-Type: image/jpeg
Cache-Control: no-cache
Via: 1.1 vegur
Content-Length: 8571

## Attachments
No attachments
