# XSS in IE11 on portswigger.net via Flash

## Report Details
- **Report ID**: 182160
- **URL**: https://hackerone.com/reports/182160
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-11-14T21:07:33.860Z
- **Disclosed**: 2016-11-30T16:32:07.216Z

## Reporter
- **Username**: opnsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Hello Portswigger Security Team,

There is a reflective XSS vulnerability in portswigger.net. The flash file `https://portswigger.net/burp/tutorials/video-js/video-js.swf` is from an old video.js library (version 3.2.0) which is vulnerable to XSS.
This XSS will be blocked by CSP instruction `object-src https://portswigger.net/knowledgebase/papers/;` but it will execute on browsers that don't enforce this CSP like Internet Explorer 11.

POC link : https://portswigger.net/burp/tutorials/video-js/video-js.swf?readyFunction=alert%28document.domain%2b'%20XSSed!'%29

POC instructions :
- Open the POC link in Internet Explorer 11 with flash active
- The javascript payload executes in `https://portswigger.net`
(Tested on Windows 10)

Mitigation :
To solve this issue, replace the old `https://portswigger.net/burp/tutorials/video-js` library with the updated video.js library from http://videojs.com/. It is also better to host any swf file on a sandbox subdomain.

Regards,

Enguerran @opnsec

## Attachments
- Portswigger_XSS.png
