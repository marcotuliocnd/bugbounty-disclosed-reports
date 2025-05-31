# Stored Self XSS on https://app.crowdsignal.com (in Photo Insert App) + Stored XSS on https://*your-subdomain*.survey.fm

## Report Details
- **Report ID**: 667188
- **URL**: https://hackerone.com/reports/667188
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-04T17:49:50.225Z
- **Disclosed**: 2019-10-21T14:58:34.284Z

## Reporter
- **Username**: ali
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Steps:
1. Go to https://app.crowdsignal.com/dashboard and click Create a New > Quiz
2. Add Multiple Choice to your page and click image button, upload a photo and click upload.
3. Start the burp suite and click Save button. Look at the request (poc1.png) and you will see media_code= parameter. It will be your photo's id and change it as payload and forward the request. Payload: "><svg/onload=alert(document.domain)> 
4. Now you will see xss (poc2.png). Copy the quiz link and open it the new tab. You will see second xss (poc3.png). And this one is stored xss.

## Impact

XSS

## Attachments
- poc1.png
- poc2.png
- poc3.png
