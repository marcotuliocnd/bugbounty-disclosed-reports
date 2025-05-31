# Remote code execution on Basecamp.com

## Report Details
- **Report ID**: 365271
- **URL**: https://hackerone.com/reports/365271
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-06-13T07:27:51.328Z
- **Disclosed**: 2020-11-26T18:22:15.199Z

## Reporter
- **Username**: gammarex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
A critical flaw in Basecamp's profile image upload function leads to remote command execution. Images are converted on the server side, but not only image files but also PostScript/EPS files are accepted (if renamed to .gif). This is probably due to ImageMagick / GraphicsMagick being used for image conversion, which calls a PostScript interpreter (Ghostscript) if the input file starts with '%!'. The used Ghostscript version however has a security bug (CVE-2017-8291) leading to remote command execution.

/Proof of concept/: Upload the attached rce.gif file as profile image (change the `ping -c1 attacker.com' to some other shell command).

/Mitigation/: Upgrade Ghostscript; also, before processing uploaded images make sure they are real image files (e.g. based on magic header)

## Impact

Gain a remote shell; from here start exploitation/privilege escalation

## Attachments
- rce.gif
