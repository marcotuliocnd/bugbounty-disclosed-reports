# Unauthorized command execution in Web protection component of Anti-Virus products family [FF, Chrome]

## Report Details
- **Report ID**: 470553
- **URL**: https://hackerone.com/reports/470553
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-21T11:05:56.521Z
- **Disclosed**: 2019-11-24T08:58:50.265Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
**Summary**
When Kaspersky Protect browser extension is installed in Firefox or Chrome, arbitrary webpages can take control of the Kaspersky command interface and disable parts of the functionality for example.

**Description**
Unlike with https://hackerone.com/reports/470544 or https://hackerone.com/reports/470547, with the Kaspersky Protect browser extension in Chrome and Firefox the extension functionality is properly isolated from the website. However, when the URL Advisor frame is being displayed, data is being sent to it via a regular `window.postMessage()` call without restricting the message recipient to specific origins. So a webpage can replace the frame's contents by some of its own and intercept this message. A particular piece of data contained in the message is the location of Kasperky's command interface. As a result, webpages can get full access to Kaspersky's command interface which allows disabling Anti-Banner and Private Browsing functionality for example (either completely or on specific sites), adding URLs to the blocklist and much more. Worse yet: by exposing Kaspersky's internal processing to the web, bugs in this processing code will turn into Remote Code Execution vulnerabilities allowing websites to execute code with the privileges of the SYSTEM user (I haven't explored this possibility further).

**Environment**
- Scope: Application
- Product name: Kaspersky Internet Security
- Product version: 19.0.0.1088
- OS name and version (incl SP): Windows 10.0.17134
- Attack type: Command Injection
- Maximum user privileges needed to reproduce your issue: no privileges

**Steps to reproduce**
I tested this with Firefox 64 and Chrome 71.

1. Go to Kaspersky settings and make sure that Anti-Banner and Private Browsing features are turned on.
2. Download the attached `ssl_server.py` and `disable_features3.html` to some directory on your computer and run `ssl_server.py` (Python 3 required). This is a very rudimentary HTTPS server running on https://localhost:5000/ with an invalid certificate, you could use some other web server as well.
3. Edit the file %WINDIR%\sysnative\drivers\etc\hosts as administrator and add the following line: `127.0.0.1 www.google.example.com`. Normally, you would just use a subdomain of a domain you own and a valid certificate - the host name has to start with "www.google." for URL Advisor to apply to the site.
4. Make sure that Kaspersky Protect browser extension is enabled in your browser.
5. Go to https://www.google.example.com:5000/disable_features3.html with your browser (override warning about invalid certificate).
6. Check Kaspersky settings and note that Anti-Banner and Private Browsing features are now disabled.

## Impact

Websites gain full control of Kaspersky's command interface and can disable or manipulate its functionality. They can also attack potential vulnerabilities of the avp.exe process running with elevated privileges.

## Attachments
No attachments
