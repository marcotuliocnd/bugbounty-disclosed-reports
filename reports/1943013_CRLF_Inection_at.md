# CRLF Inection at `██████████`

## Report Details
- **Report ID**: 1943013
- **URL**: https://hackerone.com/reports/1943013
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-04-11T20:55:52.384Z
- **Disclosed**: 2023-06-23T14:58:24.201Z

## Reporter
- **Username**: mo3giza
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mars

## Vulnerability Information
## Summary:

A CRLF Injection attack occurs when a user manages to submit a CRLF into an application. This is most commonly done by modifying an HTTP parameter or URL.

## Steps To Reproduce:

Navigate to this URL
█████:
```
┌──(azab㉿kali)-[~]
└─$ curl -i ███████ 
HTTP/1.1 307 Temporary Redirect
Date: █████ █████████ GMT
Content-Type: text/html
Content-Length: 164
Connection: keep-alive
Server: nginx
Location: ████████
Set-Cookie: CRLF_Injection_By_ze2pac

<html>
<head><title>307 Temporary Redirect</title></head>
<body>
<center><h1>307 Temporary Redirect</h1></center>
<hr><center>nginx</center>
</body>
</html>
```

## Impact

XSS, Open Redirect, HTTP Response Splitting... etc.

## Attachments
No attachments
