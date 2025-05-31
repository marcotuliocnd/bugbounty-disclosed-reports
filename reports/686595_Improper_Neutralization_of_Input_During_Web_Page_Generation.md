# Improper Neutralization of Input During Web Page Generation

## Report Details
- **Report ID**: 686595
- **URL**: https://hackerone.com/reports/686595
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-03T02:40:58.605Z
- **Disclosed**: 2020-05-14T17:37:03.035Z

## Reporter
- **Username**: null_rhythm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Cross-site scripting (XSS) vulnerabilities occur when:

    1. Untrusted data enters a web application, typically from a web request.
    2. The web application dynamically generates a web page that contains this untrusted data. 

**Description:**

## Impact
Once the malicious script is injected, the attacker can perform a variety of malicious activities. The attacker could transfer private information, such as cookies that may include session information, from the victim's machine to the attacker. The attacker could send malicious requests to a web site on behalf of the victim, which could be especially dangerous to the site if the victim has administrator privileges to manage that site.

## Step-by-step Reproduction Instructions

1. From the Search Center of █████████ for example  [https://www.███/Home/Search?searchDomain=flagship&tag=1%20mlg]
2. By Searching for "alert(String.fromCharCode(88,83,83))//--%0D%0A%3E%3C/SCRIPT%3E%22%3E%27%3E%3CSCRIPT%3Ealert(String.fromCharCode(88,83,83))%3C/SCRIPT%3E&redirect=%27%3Balert(String.fromCharCode(88,83,83))//%27%3Balert(String.fromCharCode(88,83,83))//%22%3B%0D%0Aalert(String.fromCharCode(88,83,83))//%22%3Balert(String.fromCharCode(88,83,83))//--%0D%0A%3E%3C/SCRIPT%3E%22%3E%27%3E%3CSCRIPT%3Ealert(String.fromCharCode(88,83,83))%3C/SCRIPT%3E&token=%27%3Balert(String.fromCharCode(88,83,83))//%27%3Balert(String.fromCharCode(88,83,83))//%22%3B%0D%0Aalert(String.fromCharCode(88,83,83))//%22;"
3. Cross-site scripting (XSS) vulnerabilities occurs

## Product, Version, and Configuration (If applicable)
Web Server
IIS
Operating System
Windows Server
JavaScript Libraries
jQuery3.2.1
jQuery Migrate3.0.0
jQuery UI1.12.1

## Suggested Mitigation/Remediation Actions
Strategy: Input Validation

Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a whitelist of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does.

## Impact

The server reads data directly from the HTTP request and reflects it back in the HTTP response. Reflected XSS exploits occur when an attacker causes a victim to supply dangerous content to a vulnerable web application, which is then reflected back to the victim and executed by the web browser.

## Attachments
No attachments
