# Reflected XSS on the data.gov (WAF bypass+ Chrome XSS Auditor bypass+ works in all browsers)

## Report Details
- **Report ID**: 265528
- **URL**: https://hackerone.com/reports/265528
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-02T18:21:43.165Z
- **Disclosed**: 2017-09-15T13:39:04.674Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
##Description
Hello. I discovered Cross-Site scripting issue on the https://www.data.gov/local/ endpoint.
The issue can be site-wide, and exploitable in any place, where pagination exist.

##The Impact and Severity
I assigned the High severity, because unlike the last #263226 report (that XSS was exploitable in the Firefox only), this XSS works in all browsers (Chrome/IE/Firefox).
But, considering that this case requires user interaction (hovering the mouse to the Page 2), the severity can be lowered to the Medium, if you consider so.

##POC (Reflected XSS)
Use this link in the Mozilla Firefox, Chrome or IE
https://www.data.gov/local/?&q&zzz%27onmou%3Cseover=1&ale%3Crt(%27xsp%27%3C)%3C;1;%20//

and hover the mouse to the page 2.
{F217930}

##Suggested fix
Sanitize the URLs in the `<div class="pagination">` block. 


## Attachments
- zxv.PNG
- zxc.PNG
