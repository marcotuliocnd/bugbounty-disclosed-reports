# Reflected XSS in scores.ubnt.com

## Report Details
- **Report ID**: 130889
- **URL**: https://hackerone.com/reports/130889
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-14T19:43:14.557Z
- **Disclosed**: 2016-08-11T12:41:57.736Z

## Reporter
- **Username**: enmach
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Parameter p in https://scores.ubnt.com/form.html?uid=1&p=airFiber is vulnerable to XSS. If a user logs in at https://account.ubnt.com/login and visits https://scores.ubnt.com/form.html?uid=1&p=airFiber"><script>alert(document.cookie);</script>, a message box will be presented with his cookie. Attached is a POC (xss-scores-chrome.png). 

Vulnerable code of https://scores.ubnt.com/form.html is also attached (xss-vuln-code.png), where it is visible that product  (parameter p) is included without proper input validation. 

This vulnerability can be used to steal cookies (session data) from authenticated users  as also for phishing attacks. It can be exploited by  sending a malicious link to users or posting this link to a forum. 

As UBNT implements SSO, this can be very dangerous. 

To mitigate this vulnerability, consider the following:

*output encoding of all special characters
*input validation of data suplied from users

## Attachments
- xss-scores-chrome.png
- xss-vuln-code.png
