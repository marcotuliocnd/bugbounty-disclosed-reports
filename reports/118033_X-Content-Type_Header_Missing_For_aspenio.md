# X-Content-Type Header Missing For aspen.io

## Report Details
- **Report ID**: 118033
- **URL**: https://hackerone.com/reports/118033
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-22T20:23:53.051Z
- **Disclosed**: 2017-06-15T16:42:18.413Z

## Reporter
- **Username**: bugdiscloseguys
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.

Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.
If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform.
http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
https://www.owasp.org/index.php/List_of_useful_HTTP_headers.
Thanks


## Attachments
No attachments
