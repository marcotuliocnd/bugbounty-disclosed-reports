# Kaspersky Password Manager is vulnerable to HTML injection in the browser action pop-up via user name

## Report Details
- **Report ID**: 435618
- **URL**: https://hackerone.com/reports/435618
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-07T11:33:36.938Z
- **Disclosed**: 2018-12-24T05:31:48.182Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
*Note*: According to https://www.securityweek.com/kaspersky-adds-password-manager-bug-bounty-program and some other sources, Kaspersky Password Manager is in scope for this program. The program description doesn't reflect this however.

**Summary**
There is a stored XSS vulnerability in popover.html (the page being displayed as browser action pop-up in the Kaspersky Password Manager browser extension) via user names. While exploitation is complicated due to Content Security Policy, this isn't harmless either.

**Description**
popover.html fails to escape user names, so this is a proper stored XSS vulnerability. However, Content Security Policy prevents arbitrary script execution here. What can still be done is injecting HTML code. For my proof of concept I chose to inject an external stylesheet and an iframe tag. The result is a perfectly spoofed master password prompt, for the user this is impossible to distinguish from the real thing.

**Environment**
- Scope: Application
- Product name: Kaspersky Password Manager
- Product version: 9.0.1.447
- OS name and version (incl SP): Windows 10 Version 1803
- Attack type: XSS
- Maximum user privileges needed to reproduce your issue: no privileges

**Steps to reproduce**
1. Download the attached tricky_login.html, x.html, x.css files into a directory and make them available via any web server (localhost will do).
2. Make sure Kaspersky Password Manager is installed in your browser and unlocked.
3. Go to http://.../tricky_login.html with your browser (I tried this with Firefox 62 and Chrome 70).
4. Enter any credentials into the login form and click "Log in."
5. Allow Kaspersky Password Manager to save these credentials. Note that the dialog shows exactly the user name you entered - while the webpage manipulated it to add HTML code at the end, the HTML code follows after a number of spaces so that it is cut off in the display here.
6. Now the page claims that something went wrong and asks you to try again. At the same time, KPM icons on the input fields also claim an issue and ask you to use the toolbar button - these icons have been manipulated by the website. Do as you are told and click the toolbar button.
7. Note how the toolbar button displays a proper master password prompt to you. In Firefox you will see a warning but only if the web server isn't using HTTPS. Enter something into the master password field and click "Unlock."

You will see an alert message saying: "Gotcha! Your password is: ..." The page you entered your password on didn't belong to Kaspersky Password Manager, it was rather x.html from this proof of concept.

## Impact

As long as CSP is enabled, the impact is limited. However, as this proof of concept illustrates, this still allows websites to spoof trusted KPM user interface and trick users into entering their passwords. At the very least, websites could inject tracking images to monitor KPM usage.

## Attachments
No attachments
