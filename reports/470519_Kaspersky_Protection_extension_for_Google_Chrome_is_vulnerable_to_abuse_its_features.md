# Kaspersky Protection extension for Google Chrome is vulnerable to abuse its features

## Report Details
- **Report ID**: 470519
- **URL**: https://hackerone.com/reports/470519
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-21T08:50:01.669Z
- **Disclosed**: 2019-11-25T12:45:30.788Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
**Summary**
The Google Chrome extension "Kaspersky Protection" (installed automatically by Kaspersky Internet Security) can be tricked by arbitrary websites into uninstalling browser extensions.

**Description**
Kaspersky Protection for Google Chrome has some functionality to uninstall malicious browser extensions. The uninstallation is triggered by the warning page. Since that page is marked as web accessible, any website can load this frame. Also, the page receives its data (including the extension to be uninstalled) via a regular `postMessage()` call and doesn't check message origin - any website can send this.

This issue is somewhat alleviated by the fact that recent Chrome versions will no longer allow extension-triggered uninstalls without an additional user confirmation. So the browser will display an additional prompt. Uninstalling the Kaspersky Protection extension itself doesn't produce such a prompt however.

**Environment**
- Scope: Application
- Product name: Kaspersky Internet Security
- Product version: 19.0.0.1088
- OS name and version (incl SP): Windows 10.0.17134
- Attack type: Command injection
- Maximum user privileges needed to reproduce your issue: no privileges

**Steps to reproduce**
First uninstalling Adblock Plus extension:

1. Make sure that Kaspersky Protect extension is enabled in Chrome.
2. Make sure to install Adblock Plus in Chrome from https://chrome.google.com/webstore/detail/adblock-plus/cfhdojbkjhnklbpkdaibdccddilifddb.
3. Download the attached `remove_extension.html` file and open it in Chrome (opening from local filesystem will work).
4. Move your mouse and click somewhere on the page.

Note how the browser displays a prompt to remove Adblock Plus, noting that the removal was requested by Kaspersky Protect. Despite the prompt being very clear, there is potential for social engineering here, e.g. if the page claims that Kaspersky detected a malicious extension.

Now uninstalling Kaspersky Protect extension itself:

1. Make sure that Kaspersky Protect extension is enabled in Chrome.
2. Download the attached `remove_self.html` file and open it in Chrome (opening from local filesystem will work).
3. Move your mouse and click somewhere on the page.

Note how Kaspersky Protect extension is completely gone, and with it any protection it provided. For non-technical users, there is no way to recover: Chrome will no longer offer you to install the extension unless you create a new browser profile. And while the extension is in Chrome Web Store, it is unlisted and cannot be found through search.

## Impact

Arbitrary websites can make Kaspersky Protect extension uninstall itself. They can also trigger uninstallation of other browser extensions but have to rely on social engineering for the user to confirm the uninstall prompt.

## Attachments
No attachments
