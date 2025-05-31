# CSP : Inline scripts can be inserted

## Report Details
- **Report ID**: 513105
- **URL**: https://hackerone.com/reports/513105
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-21T11:00:24.913Z
- **Disclosed**: 2019-03-21T17:39:43.596Z

## Reporter
- **Username**: darkdude
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semmle

## Vulnerability Information
Vulnerable URL:- https://lgtm-com.pentesting.semmle.net/

#Summery
Content Security Policy (CSP) is a client-side security model which allows developers to specify where different types of resources should be loaded, executed and embedded from. With CSP you can instruct the browser only to load javascript resources from a specific domain as well as block inline javascript running on the website. This is very helpful against XSS since most attacks requires inline javascript.

#Issue detail
The configuration removes the XSS sandboxing feature of Content Security Policy.
The 'unsafe-inline' directive allows scripts to be inserted inline in the HTML page. An attacker will be able to use script html tag (<script>...</script>) or event handlers (onload, onerror, ...) to load malicious scripts.

#Weak configuration 
script-src: 'unsafe-inline'

#Brup Responce
HTTP/1.1 200 OK
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block; report=https://lgtm-com.pentesting.semmle.net/browser_report/
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://www.gravatar.com https://img.shields.io; object-src 'none'; connect-src 'self' https://storage.googleapis.com; font-src 'self'; media-src 'self'; manifest-src 'self'; frame-src https://www.youtube.com; report-uri https://lgtm-com.pentesting.semmle.net/browser_report/; report-to https://lgtm-com.pentesting.semmle.net/browser_report/
Referrer-Policy: same-origin
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Deploy-Time: 1553109264000
Content-Type: text/html;charset=utf-8
X-UA-Compatible: IE=edge
X-Cloud-Trace-Context: b1a4900e9ad24c8d5eca45b4c3acc726;o=1
Vary: Accept-Encoding
Date: Thu, 21 Mar 2019 07:06:31 GMT
Server: Google Frontend
Cache-Control: private
Connection: close
Content-Length: 11525

#Refrences
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src
http://www.html5rocks.com/en/tutorials/security/content-security-policy/
https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage
https://speakerdeck.com/mikispag/making-csp-great-again-michele-spagnuolo-and-lukas-weichselbaum
https://dubell.io/exploiting-weak-content-security-policy-csp-rules-for-fun-and-profit/
https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/content-security-policy-csp-not-implemented/
https://www.netsparker.com/blog/web-security/content-security-policy/

## Impact

There is no direct impact of not implementing CSP on your website. However, if your website is vulnerable to a Cross-site Scripting attack CSP can prevent successful exploitation of that vulnerability. By not implementing CSP you’ll be missing out this extra layer of security.

## Attachments
- Capture1.PNG
- Capture.PNG
- Capture2.PNG
