# Stored Xss On "https://www.question.com/"

## Report Details
- **Report ID**: 1901706
- **URL**: https://hackerone.com/reports/1901706
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-03-12T00:36:18.041Z
- **Disclosed**: 2024-09-20T18:00:59.744Z

## Reporter
- **Username**: mathara
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drugs_com

## Vulnerability Information
Hi Team I'm Find the Stored Xss On your Site

Stored XSS, also known as persistent XSS, is the more damaging than non-persistent XSS. It occurs when a malicious script is injected directly into a vulnerable web application.

Steps To Reproduce:

1.  Go To Your Site https://www.question.com/
2. Nave https://www.question.com/ask/
5. Ask a Question Enter the Payload ```<iframe onload=alert(document.domail)>```
3.  Click to Sumit Question & Redirect to https://www.question.com/iframe-onload-alert-9-1631390.html
4. XSS was Tigred you See the Popup

POC

████

Tested on Firefox and chrome.

## Impact

The attacker can steal data from whoever checks the report.

## Attachments
No attachments
