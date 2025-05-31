# Unauthorized command execution in Web protection component of Anti-Virus products family [IE]

## Report Details
- **Report ID**: 470547
- **URL**: https://hackerone.com/reports/470547
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-21T10:28:22.840Z
- **Disclosed**: 2019-11-24T08:58:24.472Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
**Summary**
When Kaspersky add-on is installed in Internet Explorer, arbitrary webpages can take control of the Kaspersky command interface and disable parts of the functionality for example.

**Description**
Unlike with https://hackerone.com/reports/470544, when the Kaspersky add-on is installed in Internet Explorer, Kaspersky doesn't inject its script directly into the webpage, so the webpage cannot re-execute it. However, this script is still running in the same context as the webpage. While provisions have been made to prevent manipulation of some JavaScript objects such as WebSocket, other objects have not received the same treatment. In particular, a website can intercept `String.indexOf()` calls made by Kaspersky's script and gain access to its namespace this way. As a result, webpages can get full access to Kaspersky's command interface which allows disabling Anti-Banner and Private Browsing functionality for example (either completely or on specific sites), adding URLs to the blocklist and much more. Worse yet: by exposing Kaspersky's internal processing to the web, bugs in this processing code will turn into Remote Code Execution vulnerabilities allowing websites to execute code with the privileges of the SYSTEM user (I haven't explored this possibility further).

**Environment**
- Scope: Application
- Product name: Kaspersky Internet Security
- Product version: 19.0.0.1088
- OS name and version (incl SP): Windows 10.0.17134
- Attack type: Command Injection
- Maximum user privileges needed to reproduce your issue: no privileges

**Steps to reproduce**
1. Go to Kaspersky settings and make sure that Anti-Banner and Private Browsing features are turned on.
2. Download the attached `server.py` and `disable_features2.html` to some directory on your computer and run server.py (Python 3 required). This is a very rudimentary HTTPS server running on https://localhost:5000/ with an invalid certificate, you could use some other web server as well.
3. Edit the file %WINDIR%\sysnative\drivers\etc\hosts as administrator and add the following line: `127.0.0.1 www.google.example.com`. Normally, you would just use a subdomain of a domain you own and a valid certificate - the host name has to start with "www.google." for Kaspersky's script to be injected there.
4. Go to https://www.google.example.com:5000/disable_features2.html with Internet Explorer (override warning about invalid certificate).
5. Check Kaspersky settings and note that Anti-Banner and Private Browsing features are now disabled.

## Impact

Websites gain full control of Kaspersky's command interface and can disable or manipulate its functionality. They can also attack potential vulnerabilities of the avp.exe process running with elevated privileges.

## Attachments
No attachments
