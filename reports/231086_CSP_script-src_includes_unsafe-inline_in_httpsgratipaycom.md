# CSP "script-src" includes "unsafe-inline" in https://gratipay.com

## Report Details
- **Report ID**: 231086
- **URL**: https://hackerone.com/reports/231086
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-23T12:57:07.282Z
- **Disclosed**: 2017-07-10T09:59:44.036Z

## Reporter
- **Username**: d4rk_g1rl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
#SUMMARY:

Related Report: #225833

Gratipay is using unsafe-inline in script-src csp headers which allows the use of inline resources, such as inline <script> elements, javascript: URLs, inline event handlers, and inline <style> elements.
Proof Of Concept

#By Using cURL:

      curl -I https://gratipay.com


The results See my attached photo.

Above CSP headers containing "script-src: header which have "unsafe-src" attribute in it.

This does not result in an immediate threat, but should be excluded, if possible, as a best practice. For further information, see
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src

Regards,


## Attachments
- grati.png
