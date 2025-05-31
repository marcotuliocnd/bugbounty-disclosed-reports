# OS username disclosure

## Report Details
- **Report ID**: 258585
- **URL**: https://hackerone.com/reports/258585
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-10T10:20:40.567Z
- **Disclosed**: 2017-11-07T22:18:54.760Z

## Reporter
- **Username**: qab
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information

## Summary:

Using the webkitdirectory alongside minor user interaction, we are able to grab OS username of a victim.
This is because the webkitdirectory object is not properly sanitized after a folder has been picked. In my case, the downloads folder was the default folder to select and so I ended up with 'Abdulrahman/Downloads'

## Products affected: 

 
Brave: 0.18.14 
rev: ad92d029e184c4cff01b2e9f4916725ba675e3c8 
Muon: 4.3.6 
libchromiumcontent: 60.0.3112.78 
V8: 6.0.286.44 
Node.js: 7.9.0 
Update Channel: dev 
OS Platform: Microsoft Windows 
OS Release: 10.0.14393 
OS Architecture: x64

## Steps To Reproduce:

Open attached PoC and hold 'enter' for a bit.




## Attachments
- trap.html
