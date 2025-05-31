# Web protection component in Anti-Virus products family ignores HSTS security policy

## Report Details
- **Report ID**: 461780
- **URL**: https://hackerone.com/reports/461780
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-13T11:10:31.336Z
- **Disclosed**: 2019-09-05T07:30:47.781Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
**Summary**
Kaspersky Internet Security seems to ignore the Strict-Transport-Security HTTP header. This allows Man-in-the-Middle attacks on websites that would normally be immune to them. The only requirement is the user confirming the certificate override, something that can be achieved by social engineering.

**Description**
When a browser encounters an SSL certificate error, it will usually allow users to override it and continue to the site. This is meant mostly for intranet devices that use self-signed SSL certificates. However, for websites using Strict-Transport-Security HTTP header there is no such override possibility - these websites declared that they will always have a valid certificate, so a certificate error is a certain sign of a Man-in-the-Middle attack. It is known that users will often disregard warnings (see <https://adrifelt.github.io/sslinterstitial-chi.pdf> for example), so the decision isn't left to the user here. Browsers (at least Chrome 71 and Firefox 63) just don't give users a choice, proceeding to the site isn't possible.

Kaspersky Internet Security breaks up HTTPS connections in order to scan them. This means in particular that it takes over certificate validation and overrides. There seems to be no special handling of websites on Google's HSTS preload list (<https://hstspreload.org/>) or websites sending Strict-Transport-Security HTTP header. Overriding a certificate error is always possible with merely two clicks. This puts users at risk in case of Man-in-the-Middle attacks.

**Environment**
- Scope: Application
- Product name: Kaspersky Internet Security
- Product version: 19.0.0.1088
- OS name and version (incl SP): Windows 10.0.17134
- Attack type: MitM
- Maximum user privileges needed to reproduce your issue: no privileges

**Steps to reproduce**
1. Open your browser (I tested in Firefox 63) and go to https://www.google.com/. The regular Google Search page appears.
2. Edit the file %WINDIR%\sysnative\drivers\etc\hosts as administrator and add the following line: `93.184.216.34 www.google.com` (that's the IP address of example.com to simulate a MitM attack).
3. Reload www.google.com in the browser.

While Kaspersky Internet Security will warn you about a wrong SSL certificate, users can still click "I understand the risks" to ignore the error. That's despite www.google.com being on the HSTS preload list and despite Kaspersky Internet Security seeing it send Strict-Transport-Security HTTP header before. The MitM protection is considerably weakened compared to the security level provided by the browsers.

Note that the presence of Kaspersky Internet Security is easy to detect, so attackers might decide to execute this attack only if it is present.

## Impact

Attackers on public WiFi networks might redirect SSL-encrypted traffic of Kaspersky users to their server in a bet that users will override the certificate warning - which they often will. State-level attackers could do the same when targeting dissidents. They will even be able to attack high-profile websites such as Google which are normally immune to MitM due to their use of HSTS.

## Attachments
No attachments
