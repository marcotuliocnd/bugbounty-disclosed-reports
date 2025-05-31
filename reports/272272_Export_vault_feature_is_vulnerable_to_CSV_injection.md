# Export vault feature is vulnerable to CSV injection

## Report Details
- **Report ID**: 272272
- **URL**: https://hackerone.com/reports/272272
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-09-27T03:28:10.139Z
- **Disclosed**: 2017-09-28T07:58:09.848Z

## Reporter
- **Username**: kenziy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bitwarden

## Vulnerability Information
Hello guys

I don't know if you care about this issue but it seems that the export feature in your https://vault.bitwarden.com/#/tools is vulnerable to CSV injection. If a CSV contains a malicious command it may have big impact

Even though there is a popup notification for users before opening the CSV but due to it is coming from bitwarden site. User might trust the CSV.

I provide a video demo to show how the issue was found
https://www.youtube.com/watch?v=Y8zmUZu9z4c

Attack
-------
If the data inside the CSV if from other users then this might be a big impact. attackers will insert malicious command.

Im using this excel command
@SUM(1+1)*cmd|' /C calc'!A0

Fix
---
Prefix =, +, - and @ symbols with a ' in issues when exporting them to a .csv file might do the tricks.


Referrence
------------
https://hackerone.com/reports/111192
https://hackerone.com/reports/216243

Cheers
Kenziy

## Attachments
No attachments
