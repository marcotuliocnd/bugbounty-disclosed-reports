# [Gnip Blogs] Reflected XSS via "plupload.flash.swf" component vulnerable to SOME 

## Report Details
- **Report ID**: 218451
- **URL**: https://hackerone.com/reports/218451
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-04T05:39:38.957Z
- **Disclosed**: 2017-05-08T17:58:56.487Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,

The following endpoints are exposed to reflected cross-site scripting by way of a vulnerable "**plupload.flash.swf**" component on WordPress.

A comprehensive explanation of this vulnerability can be found on resolved report #134738:

> WordPress is vulnerable against a Same-Origin Method Execution (SOME) vulnerability that stems from an insecure URL sanitization problem performed in the file plupload.flash.swf. The code in the file attempts to remove flashVars [...] but fails to do so, enabling XSS via ExternalInterface.

## Proof of Concept

To reproduce this vulnerability, please access the below Proof of Concept link in the latest version of Firefox with **Adobe Flash enabled**. I have confirmed exploitability on Windows 7 x64.

```
https://blog-origin.gnip.com//wp-includes/js/plupload/plupload.flash.swf?%#target%g=alert&uid%g=XSS&

https://blog.gnip.com//wp-includes/js/plupload/plupload.flash.swf?%#target%g=alert&uid%g=XSS&

https://engineering.gnip.com//wp-includes/js/plupload/plupload.flash.swf?%#target%g=alert&uid%g=XSS&

https://engineering-origin.gnip.com//wp-includes/js/plupload/plupload.flash.swf?%#target%g=alert&uid%g=XSS&
```

Please let me know if you require any additional information regarding this vulnerability.

Thanks!

## Attachments
No attachments
