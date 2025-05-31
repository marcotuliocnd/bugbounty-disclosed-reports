# Cross site scripting 

## Report Details
- **Report ID**: 1250199
- **URL**: https://hackerone.com/reports/1250199
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-02T19:25:13.683Z
- **Disclosed**: 2021-07-29T19:35:36.604Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Cross-site Scripting (XSS) refers to client-side code injection attack wherein an attacker can execute malicious scripts into a legitimate website or web application. XSS occurs when a web application makes use of unvalidated or unencoded user input within the output it generates.

## Impact

Malicious JavaScript has access to all the same objects as the rest of the web page, including access to cookies and local storage, which are often used to store session tokens. If an attacker can obtain a user's session cookie, they can then impersonate that user.

Furthermore, JavaScript can read and make arbitrary modifications to the contents of a page being displayed to a user. Therefore, XSS in conjunction with some clever social engineering opens up a lot of possibilities for an attacker.

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
url: poc
https://www.███████/███████url=https://www.███████/%22%3Cscript%3Ealert(String.fromCharCode(88,%20115,%20115,%2032,%2066,%20121,%2032,%2079,%20108,%20100,%2077,%20111,%20104,%2097,%20109,%20109))%3C/script%3E
█████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
