# Reflected-XSS on https://www.topcoder.com/tc via pt parameter

## Report Details
- **Report ID**: 789652
- **URL**: https://hackerone.com/reports/789652
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-05T23:29:12.057Z
- **Disclosed**: 2020-09-04T19:53:55.302Z

## Reporter
- **Username**: laz0rde
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
##Summary:
I Found an XSS(Reflected) at the URL mentioned 
and the injected parameter is: pt
Steps To Reproduce:
1-go to this URL [https://www.topcoder.com/tc?module=ReviewBoard&pt=1]
$$you will recognize that is parameter (pt) is reflecting its value into the page
2- try injecting this parameter with HTML tags or XSS payloads 
the payloads I used 
1-for HTML Injection = <a+href="https://bing.com">LINK</a>
2-for XSS = <script>confirm(1)</script>

## Impact

XSS can be used for :
1- Cookie stealing 
2- Pishing attacks
3- URL redirection 
etc....

## Attachments
- XSS2222.mp4
