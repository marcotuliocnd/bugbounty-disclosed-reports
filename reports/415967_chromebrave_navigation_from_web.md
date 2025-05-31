# chrome://brave navigation from web

## Report Details
- **Report ID**: 415967
- **URL**: https://hackerone.com/reports/415967
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-09-28T22:10:33.055Z
- **Disclosed**: 2018-10-23T19:13:25.251Z

## Reporter
- **Username**: qab
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

It's possible to navigate to the infamous 'chrome://brave' (and all other) privileged page from web, requiring only a single click. This is possible by opening popups with the 'noopener' attribute.

## Products affected: 

 
Brave: 0.24.0 
V8: 6.9.427.23 
rev: f657f15bf7e0e0c50a2b854c6b05edb59bfc556c 
Muon: 8.1.6 
OS Release: 10.0.17134 
Update Channel: Release 
OS Architecture: x64 
OS Platform: Microsoft Windows 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 69.0.3497.100

## Steps To Reproduce:

1. Host attached PoC from web
2. Click button

## Impact

This is a direct violation of SOP, we can open any URL of which chrome://brave is the worst as it could lead to RCE.

## Attachments
- anchor.html
