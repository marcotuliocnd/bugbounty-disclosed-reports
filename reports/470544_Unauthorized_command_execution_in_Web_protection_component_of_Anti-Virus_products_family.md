# Unauthorized command execution in Web protection component of Anti-Virus products family

## Report Details
- **Report ID**: 470544
- **URL**: https://hackerone.com/reports/470544
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-21T10:06:03.890Z
- **Disclosed**: 2019-11-24T08:58:48.414Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
**Summary**
When no browser extension is installed, arbitrary webpages can take control of the Kaspersky command interface and disable parts of the functionality for example.

**Description**
Without a browser extension (e.g. because extension installation not confirmed by user, unsupported like in MS Edge or uninstalled via https://hackerone.com/reports/470519), Kaspersky fall back to injecting its script directly into the webpage. There are provisions to prevent the webpage from discovering the address of these script, which are trivially circumvented by the webpage downloading itself. There are also provisions to inject the script before any webpage scripts can run, so that unmanipulated references to various JavaScript objects can be stored. These provisions can also be circumvented by manipulating the objects and rerunning Kaspersky's script then. As a result, webpages can get full access to Kaspersky's command interface which allows disabling Anti-Banner and Private Browsing functionality for example (either completely or on specific sites), adding URLs to the blocklist and much more. Worse yet: by exposing Kaspersky's internal processing to the web, bugs in this processing code will turn into Remote Code Execution vulnerabilities allowing websites to execute code with the privileges of the SYSTEM user (I haven't explored this possibility further).

**Environment**
- Scope: Application
- Product name: Kaspersky Internet Security
- Product version: 19.0.0.1088
- OS name and version (incl SP): Windows 10.0.17134
- Attack type: Command Injection
- Maximum user privileges needed to reproduce your issue: no privileges

**Steps to reproduce**
I tested this with Chrome 71, it should work with any other browser as well however.

1. Go to Kaspersky settings and make sure that Anti-Banner and Private Browsing features are turned on.
2. Download attached `server.py` and `disable_features1.html` to some directory on your computer and run `server.py` (Python 3 required). This is a very rudimentary HTTP server running on http://localhost:5000/, you could use some other web server as well.
3. Edit the file %WINDIR%\sysnative\drivers\etc\hosts as administrator and add the following line: `127.0.0.1 www.google.example.com`. Normally, you would just use a subdomain of a domain you own - the host name has to start with "www.google." for Kaspersky's script to be injected there.
4. Make sure that no Kaspersky browser extension is installed in your browser. If it is, disable the extension and restart the browser.
5. Go to http://www.google.example.com:5000/disable_features1.html with your browser.
6. Check Kaspersky settings and note that Anti-Banner and Private Browsing features are now disabled.

## Impact

Websites gain full control of Kaspersky's command interface and can disable or manipulate its functionality. They can also attack potential vulnerabilities of the avp.exe process running with elevated privileges.

## Attachments
No attachments
