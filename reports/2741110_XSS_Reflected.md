# XSS Reflected

## Report Details
- **Report ID**: 2741110
- **URL**: https://hackerone.com/reports/2741110
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-09-25T21:40:26.863Z
- **Disclosed**: 2024-12-18T19:41:19.603Z

## Reporter
- **Username**: k0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
### **Description**

Reflected Cross-Site Scripting (XSS) occurs when a web application accepts untrusted data in an HTTP request and includes that data in its immediate response without proper sanitization or validation. This vulnerability allows an attacker to inject malicious scripts into web pages viewed by other users. When victims click on a specially crafted link containing the attacker's payload, the server reflects the input back to the user's browser, executing the malicious script within the context of the victim’s session. This can lead to various attacks, such as cookie theft, session hijacking, or phishing.

### **References**

- [OWASP XSS (Cross Site Scripting)](https://owasp.org/www-community/attacks/xss/)
- [MDN Web Docs on XSS](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting)
- [CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')](https://cwe.mitre.org/data/definitions/79.html)

## Impact

If an attacker can control a script that is executed in the victim's browser, then they can typically fully compromise that user. Amongst other things, the attacker can:

- Perform any action within the application that the user can perform.
- View any information that the user is able to view.
- Modify any information that the user is able to modify.
- Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user.

There are various means by which an attacker might induce a victim user to make a request that they control, to deliver a reflected XSS attack. These include placing links on a website controlled by the attacker, or on another website that allows content to be generated, or by sending a link in an email, tweet or other message. The attack could be targeted directly against a known user, or could be an indiscriminate attack against any users of the application.

## System Host(s)
www.████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
This URL demonstrates a potential XSS (Cross-Site Scripting) attack by injecting hidden JavaScript code. Here’s how it works:

1. **Open the URL:** When the user navigates to the URL, the server processes the request with the embedded parameters.

```url
https://www.██████/tags/image/sizzle-reel?&view=K0X%22%20AutoFocus%20%2526%252362%20OnFocus%0c%3dprompt%601%60%20kaos%3d%22uwps2&sort=date
```

2. **Hidden code execution:** The URL contains special characters and encoded payloads (`%22`, `%2526`, `%252362`, `%60`, etc.) that are interpreted in different ways by the browser or the application.

███████

3. **XSS attack:** Specifically, the injected code (`AutoFocus`, `OnFocus`, `kaos="uwps2"`) attempts to execute when a particular event occurs. In this case, it could be something like a focus event (`OnFocus`). When a user interacts with an element on the page (for example, clicks a link or inputs data), the hidden code executes, potentially triggering the XSS payload.

████████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
