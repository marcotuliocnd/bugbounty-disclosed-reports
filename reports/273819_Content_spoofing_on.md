# Content spoofing on

## Report Details
- **Report ID**: 273819
- **URL**: https://hackerone.com/reports/273819
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-02T17:26:27.869Z
- **Disclosed**: 2023-11-28T08:59:16.877Z

## Reporter
- **Username**: nonamehiiden
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Scenerio
An attacker can include any arbitrary text using specially crafted tor project url.
Reporting this but not sure if this is in scope (text injection not marked in exclusion list)
Kindly mark it as informative in case if it is out of scope.

Steps
1) Attacker distributed the below url by means of spamming or through his website
Go To-
https://www.torproject.org/index%20not%20found%20at%20this%20server!%20Server%20is%20currently%20on%20maintanance.%20______________________________________________________________________________________________________________________________________________________________________________________________________________%20______________________________________________________________________________________________________________________________________________________________________________________________________________%20Please%20visit%20at.HTTP:/EVIL.ATTACKER.COM%20for%20latest%20updates.%20______________________________________________________________________________________________________________________________________________________________________________________________________________%20______________________________________________________________________________________________________________________________________________________________________________________________________________%20Changes%20are%20in%20progress
2) Since the text came from official site so user believes and gets into attacker trap.

Best Regards
Aryan.

## Attachments
No attachments
