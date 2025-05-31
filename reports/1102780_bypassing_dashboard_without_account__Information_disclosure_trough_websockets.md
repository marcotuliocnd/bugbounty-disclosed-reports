# bypassing dashboard without account + Information disclosure trough websockets 

## Report Details
- **Report ID**: 1102780
- **URL**: https://hackerone.com/reports/1102780
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-13T15:55:38.406Z
- **Disclosed**: 2021-04-20T13:57:04.868Z

## Reporter
- **Username**: deb0con
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
**Sumarry :** 
I found a information disclosure for bypassing parameter url attacker can redirect to dashboard without login user/pass page
and websocket can be exposed in response/dashboard.

**URL Effected**
https://support.nextcloud.com/#password_reset

### Steps To Reproduce:
  * Opened directory at https://support.nextcloud.com/#password_reset
  * Forget-password  and repeat url to burp-suite
  * In directory added a parameter bypass is ``//%0d%0aSet-Cookie:%20crlf-injection=mickeybrew//``
  * and look a responsive , you can be redirect to dashboard panel without user/pass
  * Show the ``network-browser`` and you can found api directory and websocket
  * Directory websocket is https://support.nextcloud.com/api/v1/signshow
  * Opened it and **Boom** You can see Information disclosure through websocket

**Request**
```
GET #password_reset/%0d%0aSet-Cookie:%20crlf-injection=mickey HTTP/1.1
Host: support.nextcloud.com
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 91
```
 ### Screenshots POC
█████
██████
███████
███

## Impact

It may cause the attacker to log into the dashboard page without logging in via user/pass, and the attacker finds sensitive files on open fires.

## Attachments
No attachments
