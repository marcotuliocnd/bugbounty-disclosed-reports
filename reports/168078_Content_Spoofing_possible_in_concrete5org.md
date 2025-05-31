# Content Spoofing possible in concrete5.org

## Report Details
- **Report ID**: 168078
- **URL**: https://hackerone.com/reports/168078
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-13T17:30:28.851Z
- **Disclosed**: 2017-07-23T10:30:48.396Z

## Reporter
- **Username**: csanuragjain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
An attacker can include any arbitrary text using specially crafted concrete5 url.
This is done using character /%0d%0a.
**Input**
https://www.concrete5.org/%0d%0ahas%20moved%20to%20www.evil.com.Please%20visit%20evil.com%20Present%20resource

**Output**
The requested URL / has moved to www.evil.com.Please visit evil.com Present resource was not found on this server.

This attacks are difficult to perform but they may spoof the user in downloading malwares since user believes the text to be coming from yelp site.

## Attachments
No attachments
