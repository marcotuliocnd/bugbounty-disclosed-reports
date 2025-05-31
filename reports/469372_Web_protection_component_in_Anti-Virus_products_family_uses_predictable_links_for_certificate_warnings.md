# Web protection component in Anti-Virus products family uses predictable links for certificate warnings

## Report Details
- **Report ID**: 469372
- **URL**: https://hackerone.com/reports/469372
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-18T11:43:54.956Z
- **Disclosed**: 2019-11-25T11:58:25.041Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
**Summary**

Websites can predict links used in certificate warnings, Safe Money prompts, anti-phishing warnings and similar pages. This allows them to initiate actions without the user's knowledge.

**Description**

The links used to override certificate warnings have the following format: `https://<host>/?<link_id>_kis_cup_<GUID>_`. Here, `GUID` is identical for all certificate warnings and `link_id` is a value that is being counted up continuously. So if a website can get hold of one such link, it can predict what future links will look like. This allows triggering actions on behalf of the user, e.g. overriding the wrong certificate for another website. Similarly, websites can permanently disable Safe Money protection for a banking website, the prompt there uses the same link format and the same `link_id` counter. And while an anti-phishing warning is overridden with `http://touch.kaspersky.com/kis_cup_<GUID>_<link_id>` it's once again the same values, so triggering this action automatically is possible as well.

The easiest way for a website to get hold of a valid link appears to be downloading its own certificate warning. Since certificate warnings are first-party as far as the website is concerned, it has complete access to them. The server needs to serve a valid certificate first so that the website can load, then switch to an invalid certificate so that any request will result in a certificate warning page from Kaspersky. The website can then download this warning page and read out the links from it.

**Environment**

* Scope: Application
* Product name: Kaspersky Internet Security
* Product version: example: 19.0.0.1088
* OS name and version (incl SP): Windows 10.0.17134
* Attack type: Insecure Direct Object Reference
* Maximum user privileges needed to reproduce your issue: no privileges

**Steps to reproduce**

Multiple steps to reproduce here to demonstrate various attacks possible, all tested in Firefox 64. First overriding a certificate:

1. Edit the file %WINDIR%\sysnative\drivers\etc\hosts as administrator and add the following line: 93.184.216.34 www.google.com (that's the IP address of example.com to simulate a MitM attack).
2. Go to https://www.google.com/ in your browser - note how Kaspersky will display a certificate warning page.
3. Now download the attached `rebinding_server.py` and `certerror_override.html` to some directory on your computer and run `rebinding_server.py` (Python 3 required). This will run an HTTPS server on https://localhost:5000/, with an additional server on http://localhost:5001/ that will make the primary server alternate between the first (supposedly valid) and second (invalid) SSL certificate.
4. Open https://localhost:5000/certerror_override.html in your browser (override the certificate warning, real attackers would use a website with a valid certificate).
5. The page masquerades as a warning from Kaspersky about your network not being protected, which is probably true if the attackers managed MiTM www.google.com and show you this page. Click the "I understand the risks and wish to continue" link. 
6. An additional warning by Kaspersky opens saying: "You are about to go to an insecure web resource. Are you sure you want to continue?" That warning is in line with what you already saw, so you click "Continue."
7. You will be redirected to https://www.google.com/ - the MiTM attack succeeded. The page says "Not Found," the certificate warning is gone.

Now disabling Safe Money functionality:

1. Make sure that Safe Money functionality is enabled in Kaspersky settings and set to "Prompt for action" on first access (the default value).
2. Go to https://www.bankofamerica.com/ in your browser - note how Kaspersky will ask you whether you want to open this page in a safe browser.
3. Now download the attached `rebinding_server.py` and `disable_safemoney.html` to some directory on your computer and run `rebinding_server.py` (Python 3 required). This will run an HTTPS server on https://localhost:5000/, with an additional server on http://localhost:5001/ that will make the primary server alternate between the first (supposedly valid) and second (invalid) SSL certificate.
4. Open https://localhost:5000/disable_safemoney.html in your browser (override the certificate warning, real attackers would use a website with a valid certificate).
5. Note how you are being redirected to https://www.bankofamerica.com/ without any further warning, Safe Money functionality has been permanently disabled for this site. An actual attack might prefer to disable the functionality temporarily however, as this wouldn't leave any traces.

And overriding anti-phishing prompts:

1. Go to https://www.amtso.org/check-desktop-phishing-page/ in your browser - note how Kaspersky will prevent you from going there, indicating that it is a phishing page.
2. Now download the attached `rebinding_server.py` and `phishing_override.html` to some directory on your computer and run `rebinding_server.py` (Python 3 required). This will run an HTTPS server on https://localhost:5000/, with an additional server on http://localhost:5001/ that will make the primary server alternate between the first (supposedly valid) and second (invalid) SSL certificate.
3. Open https://localhost:5000/phishing_override.html in your browser (override the certificate warning, real attackers would use a website with a valid certificate).
4. Note how you are being redirected to https://www.amtso.org/check-desktop-phishing-page/ without any further confirmation, anti-phishing functionality will no longer warn stop you from going there until Kaspersky is restarted. There is a message being displayed saying "Threat of data loss" in the title and "Allowed link" in the message body, this is confusing and unlikely to make the user suspect anything.

**Recommendations**

Warning pages should not be first-party to the pages affected by them. Instead of directly serving HTML content within a 499 response, Kaspersky could produce a redirect to kis.v2.scr.kaspersky-labs.com here and produce the content under that location. This would prevent websites from accessing contents of such warning pages.

Even then, links triggering such important actions shouldn't be predictable. This is most easily achieved by using a real cryptographic signature such as HMAC-SHA256. A link like `http://touch.kaspersky.com/?id=<link_id>&host=<host>&signature=<HMAC-SHA256(secret, link_id || host)>` cannot be manipulated without knowing the user-specific secret which will hopefully never be exposed to the web.

## Impact

Attackers able to MiTM user's internet connection (e.g. on a public WiFi) will be able to trick the user into unwittingly confirming a certificate override for high profile websites such as Google, thus essentially disabling MiTM protection offered by SSL.

Also, arbitrary websites will be able to disable Safe Money or anti-phishing protection for any website without any user interaction. Other Kaspersky Internet Security functionality might be similarly affected.

## Attachments
No attachments
