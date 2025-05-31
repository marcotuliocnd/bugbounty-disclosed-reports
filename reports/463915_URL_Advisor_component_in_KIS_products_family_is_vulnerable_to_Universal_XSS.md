# URL Advisor component in KIS products family is vulnerable to Universal XSS

## Report Details
- **Report ID**: 463915
- **URL**: https://hackerone.com/reports/463915
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-12-17T14:00:58.680Z
- **Disclosed**: 2019-08-28T17:54:25.462Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
**Summary**
In Microsoft Edge, URL Advisor UI is served as first-party content on every domain. So the XSS vulnerability I found in this UI automatically applies to all websites, it allows running code in the context of *any* domain.

**Description**
URL Advisor frame is located under https://www.google.com/<INJECT_ID>/ua/url_advisor_balloon.html and https://www.yahoocom/<INJECT_ID>/ua/url_advisor_balloon.html in Microsoft Edge (always the same INJECT_ID value). It gets its content from a message sent via `window.postMessage()` without validating message origin. Under some circumstances it will assign that data as link target, so a malicious website can make that link point to a javascript: URL. Clickjacking then allows making the user click that link - while sites like google.com use X-Frame-Options header to disallow framing, no such restrictions are in place for the url_advisor_balloon.html frame.

**Environment**
- Scope: Application
- Product name: Kaspersky Internet Security
- Product version: 19.0.0.1088
- OS name and version (incl SP): Windows 10.0.17134
- Attack type: Universal XSS
- Maximum user privileges needed to reproduce your issue: no privileges

**Steps to reproduce**
1. Download attached `server.py` and `universal_xss.html` to some directory on your computer and run `server.py` (Python 3 required). This is a very rudimentary HTTP server running on http://localhost:5000/, you could use some other web server as well.
2. Edit the file %WINDIR%\sysnative\drivers\etc\hosts as administrator and add the following line: `127.0.0.1 www.google.example.com`. Normally, you would just use a subdomain of a domain you own - the host name has to start with "www.google." for URL Advisor to apply to it.
3. Open Microsoft Edge and go to http://www.google.example.com:5000/universal_xss.html
4. As advised by the page, move your mouse and click somewhere on the page.

You will see an alert message saying: "Hi, this is JavaScript code running on www.google.com." That's the result of the code `alert('Hi, this JavaScript code is running on ' + document.domain)` executing in the context of the Google website. Injecting code into any other domain would have been easily possible as well.

**Recommendation**
This user interface should never be served as first-party, even once the vulnerability here is fixed. Any XSS vulnerability in Kaspersky code automatically elevates to Universal XSS otherwise, this is too dangerous. Frankly, I don't see why it is done in this way with Microsoft Edge - in Firefox and Internet Explorer the same UI is always served via kis.v2.scr.kaspersky-labs.com, so vulnerabilities here don't affect other websites.

## Impact

A malicious website can easily make users click by pretending to be a game. And while the user clicks, they will be allowing the attackers to inject code into various internet domains and exfiltrating data in the background.

## Attachments
No attachments
