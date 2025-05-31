# XSS in https://www.coursera.org/courses/

## Report Details
- **Report ID**: 127163
- **URL**: https://hackerone.com/reports/127163
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-31T17:18:39.880Z
- **Disclosed**: 2016-09-14T08:44:08.874Z

## Reporter
- **Username**: secalert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coursera

## Vulnerability Information
DESCRIPTION
=================
It has been identified that the page located at https://www.coursera.org/courses/ is prone to cross-site scripting issues. Cross-site Scripting (XSS) refers to client-side code injection attack wherein an attacker can execute malicious scripts (also commonly referred to as a malicious payload) into a legitimate website or web application. 

IMPACT
=================
A XSS vulnerability arises when web applications take data from users and dynamically include it in web pages without first properly validating the data. XSS vulnerabilities allow an attacker to execute arbitrary commands and display arbitrary content in a victim user's browser. A successful XSS attack leads to an attacker controlling the victim’s browser or account on the vulnerable web application. 

TEST ENVIRONMENT
=================
1) Firefox 45.0 on Mac OS X 10.11.3

PROOF OF CONCEPT
=================
Please use the Mozilla Firefox Browser to verify the identified issue!

1) legit request: https://www.coursera.org/courses/?query=coursera

2) If you try to pass a xss payload to the "query" param as string it will be encoded correctly and is therefore not vulnerable - but if you now change the „query“ param to „query[]“ you will be able to inject html and javascript code.

2.1) proof of concept 1: https://www.coursera.org/courses/?query[]=secalert%22/%3E%3Cmarquee+onstart=alert(document.domain)%3E

2.2) Proof of Concept 2: https://www.coursera.org/courses/?query[]=secalert%22/%3E%3Cimg%20src=secalert%20onerror=confirm%28document.domain%29%3E

It will be rendered like this:
```html
<span data-reactid=".255dmgqjchs.1.1.1.2.1.0.0">You searched for <strong>secalert"/><marquee onstart=alert(document.domain)></strong>.</span>
```

SCREENSHOT
===========
Screenshots are attached.

REMEDIATION
============
1) All input should be neutralized before being reflected back to client (i.e. browser), not just parameters that the user is supposed to specify, but all data in the request, including hidden fields, cookies, headers, the URL itself, and  so forth.
2) Make use of entity encoding in the used context. See also: https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet

CREDITS
=======
David Vieira-Kurz aka @secalert (https://hackerone.com/secalert)


## Attachments
- coursera-xss-1.png
- coursera-xss-2.png
- coursera-xss-3.png
