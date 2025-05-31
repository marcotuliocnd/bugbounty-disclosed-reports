# Cross Site Scripting (XSS) – Reflected

## Report Details
- **Report ID**: 409230
- **URL**: https://hackerone.com/reports/409230
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-12T21:51:03.753Z
- **Disclosed**: 2020-09-29T20:32:34.264Z

## Reporter
- **Username**: jayhanspara
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Reflected Cross-site Scripting (XSS) occur when an attacker injects browser executable code within a single HTTP response.When a web application is vulnerable to this type of attack, it will pass unvalidated input sent through requests back to the client.**

**The value of request parameter is copied into the value of an HTML tag attribute which is encapsulated in double quotation marks.The input was echoed unmodified in the application's response.  This  proof-of-concept attack demonstrates that it is possible to inject arbitrary JavaScript into the application's response.  **

**Vulnerable Link  : https://www.███/**

**In the attachment you can find the request, response and the screenshot of  vulnerability.**
## Step-by-step Reproduction Instructions

1. copy the request of Vulnerable URL and send it to the repeater tab in burp suite .
2.  Hit on the go button of the repeater's sub tab and will find the response. 
3. Right click with in the response tab and click on show response on browser and click on the copy button 
4. Paste  the copied URL in the web browser you will find the popup which display the domain of the website.

## Suggested Mitigation/Remediation Actions
Input should be validated as strictly as possible on arrival, given the kind of content that it is expected to contain. For example, personal names should consist of alphabetical and a small range of typographical characters, and be relatively short; a year of birth should consist of exactly four numerals; email addresses should match a well-defined regular expression. Input which fails the validation should be rejected, not sanitized.
User input should be HTML-encoded at any point where it is copied into application responses. All HTML metacharacters, including < > " ' and =, should be replaced with the corresponding HTML entities (&lt; &gt; etc).

## Impact

## Impact
    Cookie Stealing - A malicious user can steal cookies and use them to gain access to the application.
    Arbitrary requests - An attacker can use XSS to send requests that appear to be from the victim to the web server.
    Malware download - XSS can prompt the user to download malware. Since the prompt looks like a legitimate request from the
     site, the user may be more likely to trust the request and actually install the malware.
    Defacement - attacker can deface the website usig javascript code.

## Attachments
No attachments
