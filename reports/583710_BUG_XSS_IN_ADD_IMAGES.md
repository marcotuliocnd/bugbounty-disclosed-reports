# BUG XSS IN "ADD IMAGES"

## Report Details
- **Report ID**: 583710
- **URL**: https://hackerone.com/reports/583710
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-17T17:53:33.282Z
- **Disclosed**: 2019-07-18T16:44:48.075Z

## Reporter
- **Username**: rioncool22
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
I want to report bug XSS in "ADD IMAGES" 

How To Produce it : 
1. Login to your Account
2. Then Add Images With XSS Payload In filename (example : "><img src=x onerror=prompt(document.domain)>.png)
3. Click on Image that you upload
4. in the name of picture XSS will fired

## Impact

https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)

## Attachments
- Screencast_05-17-2019_01_52_09_PM.webm
