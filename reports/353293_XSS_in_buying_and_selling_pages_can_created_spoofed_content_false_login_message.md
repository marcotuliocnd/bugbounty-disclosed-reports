# XSS in buying and selling pages, can created spoofed content (false login message)

## Report Details
- **Report ID**: 353293
- **URL**: https://hackerone.com/reports/353293
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-17T03:28:43.462Z
- **Disclosed**: 2018-09-08T06:12:19.084Z

## Reporter
- **Username**: kiyell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reverb

## Vulnerability Information
Previously this issue was resolved at another location in report #351376
After spending more time searching the website, I found additional areas where this problem persists:

https://sandbox.reverb.com/my/buying/orders?query=
https://sandbox.reverb.com/my/selling/listings?query=
https://sandbox.reverb.com/my/selling/orders?query=

These queries render several html tags along with the class attribute. This allows a user to spoof content and make it appear to come from Reverb.com. 

In this PoC I use several tags along with the class attribute to prompt a user to click an outside link. The message uses Reverb.com CSS branding and appears authentic.

PoC: https://sandbox.reverb.com/my/buying/orders?query=%3Cspan%20class%3D%22bottom-alert%20%20videos-header%22%3E%3Cstrong%3ELog%20In%20to%20Reverb%3C%2Fstrong%3E%3Cbr%3E%3Ccode%3EDue%20to%20multiple%20unsuccessful%20attempts%20to%20login%20to%20your%20account.%20Your%20account%20has%20been%20locked%20for%20your%20protection.%20Please%20click%20below%20to%20unlock%20it%3C%2Fcode%3E%20%3Cbr%3E%3Cbr%3E%3Ca%20href%3D%22http%3A%2F%2Fbadwebsite.com%22%3E%3Cspan%20class%3D%22btn%20button%20button--orange%20button--wide%22%3EUnlock%3C%2Fspan%3E%3C%2Fspan%3E%3C%2Fa%3E

## Impact

An attacker can create a link on behalf of Reverb.com to persuade a logged in user to take a number of different actions like visiting a malicious website to steal account information.

## Attachments
- Reverb_XSS_additional_vectors.JPG
