# Content spoofing in lookup.nextcloud.com

## Report Details
- **Report ID**: 171497
- **URL**: https://hackerone.com/reports/171497
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-09-23T16:56:06.861Z
- **Disclosed**: 2016-10-10T14:56:44.467Z

## Reporter
- **Username**: csanuragjain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
**Scenerio**
An attacker can include any arbitrary text using specially crafted nextcloud url.
This is done using character /%0d%0a.

**Steps**
1) Attacker distributed the below url by means of spamming or through his website
https://lookup.nextcloud.com/%0d%0ahas%20moved%20to%20www.evil.com.Please%20visit%20evil.com%20Present%20resource
2) Victim see below text 
The requested URL / has moved to www.evil.com.Please visit evil.com Present resource was not found on this server.
3) Since the text came from official site so user believes and gets into attacker trap

**Resolution**
Crafted text should not be responded back in the response HTML

## Attachments
- lookup.PNG
