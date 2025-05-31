# Clickjacking on cas.acronis.com login page

## Report Details
- **Report ID**: 971234
- **URL**: https://hackerone.com/reports/971234
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-31T13:45:40.667Z
- **Disclosed**: 2020-11-03T09:10:26.593Z

## Reporter
- **Username**: dgirlwhohacks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Steps To Reproduce:

    Create a new HTML file
Source code:
<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I Frame</title>
</head>
<body>
<h2>Clickjacking Vulnerability</h2>
<iframe src="https://cas.acronis.com/" frameborder="0" height="700px" width="850px"></iframe>
</body>
</html>
 
    Save the file as whatever.html
    Open document in browser 

Reference: https://hackerone.com/reports/591432

FIX-
The vulnerability can be fixed by adding "frame-ancestors 'self';" to the CSP (Content-Security-Policy) header.
NOTE

Best Regards,
Dgirl

## Impact

Attacker may tricked user, sending them malicious link then user open it clicked some image and their account unconsciously has been deactivated

## Attachments
- UiRedressing.png
