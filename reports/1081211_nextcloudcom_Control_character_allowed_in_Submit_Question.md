# [nextcloud.com] Control character allowed in Submit Question

## Report Details
- **Report ID**: 1081211
- **URL**: https://hackerone.com/reports/1081211
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-19T06:46:46.763Z
- **Disclosed**: 2021-01-20T12:08:47.129Z

## Reporter
- **Username**: lmhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
**Issue descriptions**
We found that the maximum length of the first and last name fields was not set to 32 characters at registration and to 1000 characters when using the profile update form. The attacker can use this method as a malware attack, the user will redirect to a website that contains malware or hijack.

**URL Effected**
https://nextcloud.com/contact/

### Steps To Reproduce:
  * Open directory url https://nextcloud.com/contact/
  * Repreat url to burp suite 
  * Chage a subject ``Organization-name`` your payloads.txt
  * "Subject Name" has been effected a Control character allowed vulnerable but you can use this for hijacking emails
  * Paste a victim emails to sent a malware attack
  * Sent request to victim emails, and boom this emails has been hijact.

**Proof On Concept**
```
POST /api/t/1/credit/share HTTP/1.1
Host: nextcloud.com
Connection: close
Upgrade-Insecure-Requests: 1

yourname=%24%21%25%24%5E%21%25%24%5E%25%21*%24%25%21*%5E%24%25*%26%21%25%24*%26%5E%21%26*%5E%24%26*%21%5E%26*%24%21%25%24%5E%21%25%24%5E%25%21*%24%25%21*%5E%24%25*%26%21&email=kittytrace%40wearehackerone.com&organization=Hello+your+account+has+been+hacked+please+visit+here+https%3A%2F%2Fevil.com%2F&role=Administrator&phone=Test&comments=TEST&gdprcheck=gdprchecked&captcha=10&checksum=a29a82e78e%3A478e965f1f8045a0beac0c1ba3424f10ca25f859543909747b89c33eec6df943
```
### Screenshots POC
F1163343
F1163344

## Impact

Attacker can sent a malware attack to victim email using a server notification emails this is can leads to Business Logic Errors
  * Email Hijacking
  * Control character allowed in username

## Attachments
- Screenshots.png
- ScreenshotsPOC.png
