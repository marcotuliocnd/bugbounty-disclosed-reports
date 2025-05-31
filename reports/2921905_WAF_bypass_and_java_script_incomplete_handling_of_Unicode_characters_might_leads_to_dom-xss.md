# WAF bypass and java script incomplete handling of Unicode characters might leads to dom-xss

## Report Details
- **Report ID**: 2921905
- **URL**: https://hackerone.com/reports/2921905
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2025-01-04T08:40:27.135Z
- **Disclosed**: 2025-01-13T17:46:07.057Z

## Reporter
- **Username**: clubbable
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: doppler

## Vulnerability Information
hello,

WAF :
 doppler uses cloudfare firewall to prevent unwanted malicous injections 
"https://share.doppler.com/ext/jquery/dist/jquery.min.js?c=%22%3Cscript%3Ealert(%27XSS%27)%3C/script%3E%22" by accessing the endpoint you'll get to know that!

But I found that this code "">%0D%0A%0D%0A<x '="foo"><x foo='><img src=x onerror=javascript:alert(`cloudfrontbypass`)//'>" bypass the cloud fare !
"https://share.doppler.com/ext/jquery/dist/jquery.min.js?c=%22%3E%0D%0A%0D%0A%3Cx%20%27=%22foo%22%3E%3Cx%20foo=%27%3E%3Cimg%20src=x%20onerror=javascript:alert(`cloudfrontbypass`)//%27%3E"
 it doesn't initiate the xss but I can able to bypass the WAF bypass!

DOM-XSS:
implementation of ce.escapeSelector is indeed vulnerable to DOM-based XSS due to its incomplete handling of Unicode characters, specifically surrogate pairs.

Here's why:

Surrogate Pairs:
Unicode uses surrogate pairs to represent characters outside the Basic Multilingual Plane (BMP).
A surrogate pair consists of two 16-bit code units that together represent a single character.
Incomplete Escaping:
The charCodeAt function returns the code unit at a specific index.
When dealing with a surrogate pair, charCodeAt will only return the code unit of the first or second surrogate, not the combined character.
This leads to incorrect escaping, as the hexadecimal representation of a single surrogate does not accurately represent the intended character.
XSS Exploitation:
An attacker could craft a malicious selector that includes a surrogate pair within it.
The incomplete escaping would allow the surrogate pair to be interpreted as part of the selector in unexpected ways.
This could potentially:
Manipulate the target of the selector, selecting unintended elements.
Inject JavaScript code into the selector, leading to arbitrary code execution within the context of the web page.
```
'div[id="\\uD83D\\uDC4D;alert(1)//"]'
```

## Impact

attackers can inject malicious code that steals sensitive user information like login credentials, personal details, and financial data.

## Attachments
No attachments
