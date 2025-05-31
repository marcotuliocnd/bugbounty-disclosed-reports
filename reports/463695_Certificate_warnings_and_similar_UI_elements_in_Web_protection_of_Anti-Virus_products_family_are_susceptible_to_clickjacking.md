# Certificate warnings and similar UI elements in Web protection of Anti-Virus products family are susceptible to clickjacking

## Report Details
- **Report ID**: 463695
- **URL**: https://hackerone.com/reports/463695
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-17T10:02:35.319Z
- **Disclosed**: 2019-08-28T17:54:56.804Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
**Summary**
Clickjacking can be used to trick users into overriding certificate warnings, disabling Safe Money functionality or phishing alerts.

**Description**
On certificate warning pages, a single click is sufficient to trigger overriding a wrong certificate. While an additional warning is displayed outside of the browser, the message is very generic and won't really tell users what they are agreeing to. This allows attackers who can MiTM user's connections (e.g. on a public WiFi) to attack SSL-protected connections. The issue reported under https://hackerone.com/reports/461780 makes matters worse here because certificates can be overridden even for high-profile websites like Google.

**Environment**
- Scope: Application
- Product name: Kaspersky Internet Security
- Product version: example: 19.0.0.1088
- OS name and version (incl SP): Windows 10.0.17134, tested browsers are Firefox 64, Internet Explorer 11, Microsoft Edge
- Attack type: Clickjacking
- Maximum user privileges needed to reproduce your issue: no privileges

**Steps to reproduce**
1. Edit the file %WINDIR%\sysnative\drivers\etc\hosts as administrator and add the following line: `93.184.216.34 www.google.com` (that's the IP address of example.com to simulate a MitM attack).
2. Go to https://www.google.com/ in your browser - note how Kaspersky will display a certificate error page.
3. Now download the attached certerror_clickjacking.html and open it in your browser (can be opened directly from the file system).
4. The page masquerades as a warning from Kaspersky about your network not being protected, which is probably true if the attackers managed to show you this page. Click the "I understand the risks and wish to continue" link. Note: this has been tested with the English version of Kaspersky, there is a slight chance that this link won't be positioned correctly with other languages.
5. An additional warning by Kaspersky opens saying: "You are about to go to an insecure web resource. Are you sure you want to continue?" That warning is in line with what you already saw, so you click "Continue."
6. Now go to https://www.google.com/ again. Note how the site loads now (shows "Not Found"), the certificate error is gone.

The link you clicked on in step 4 didn't belong to the certerror_clickjacking.html page but rather to the certificate error page for www.google.com. So when you clicked it you actually confirmed to override the wrong certificate of www.google.com.

Other warning pages displayed by Kaspersky are similarly affected by clickjacking. So the attackers could trick you into clicking the link which disables Safe Money protection for your bank for example. Or the link that permanently overrides the phishing warning for almost-my-bank.com. Both these actions would have worked without an additional confirmation, so no social engineering required - the user merely needs to click somewhere on the attacker's page.

**Recommendations**
Browsers' certificate error pages are resilient to clickjacking. Both Firefox and Chrome will require **two** clicks on **different** parts of the page to override a certificate: first "Advanced" button, then the actual override. This approach is also advisable for other reasons: technical details only confuse the general population, the important information being that they should leave the page which is not secure. Only people who are technical enough to look at the advanced section should see the override possibility.

Also, the additional confirmation message displayed by Kaspersky should be made less generic. At the very least, it should mention the website that the user is overriding the certificate for.

Finally, there is no valid reason for the Safe Money prompt to appear within a frame, so this could be prevented using X-Frame-Options HTTP header.

## Impact

On a public network, attackers might redirect user's unencrypted (plain HTTP) traffic to their server and display a message to them that they would plausibly want to override. If the user clicks the override link then, they will have unwittingly overridden the wrong certificate warning for some SSL-protected website and will have given attackers the possibility to hijack this connection.

## Attachments
No attachments
