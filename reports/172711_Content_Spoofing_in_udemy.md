# Content Spoofing in udemy

## Report Details
- **Report ID**: 172711
- **URL**: https://hackerone.com/reports/172711
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-09-28T18:34:26.531Z
- **Disclosed**: 2017-07-23T10:29:19.948Z

## Reporter
- **Username**: csanuragjain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: udemy

## Vulnerability Information
**Scenerio**
An attacker can include any arbitrary text using specially crafted udemy url.
Reporting this but not sure if this is in scope (text injection not marked in exclusion list)
Kindly mark it as informative in case if it is out of scope

Issue seems to be because of source_page=clp param. If this is removed text injection wont work. Also it seems error handling is not proper in case of source_object_id param since this vulnerability occur when you insert a string inside source_object_id param.

**Steps**
1) Attacker distributed the below url by means of spamming or through his website
https://www.udemy.com/api-2.0/recommended-courses/?source_action=view&source_object=course&source_object_id=},{Kindly%20move%20to%20our%20new%20beta%20website%20evil.com&source_page=clp
2) Victim see below text 
{"detail": "Invalid source object id: },{Kindly move to our new beta website evil.com"}
3) Since the text came from official site so user believes and gets into attacker trap

**Resolution**
Crafted text should not be responded back in the response HTML

## Attachments
- ContentSpoofing.PNG
