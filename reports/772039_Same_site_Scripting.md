# Same site Scripting 

## Report Details
- **Report ID**: 772039
- **URL**: https://hackerone.com/reports/772039
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-01-11T03:52:50.245Z
- **Disclosed**: 2020-01-13T12:56:22.183Z

## Reporter
- **Username**: dre4dpir4terob3rts
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drive_net_inc

## Vulnerability Information
Same site scripting 
I have found an error of some misconfigured DNS in a subdomain of yours which causes same site scripting.

PoC
1 Open a terminal and type ping localhost.drive2.ru
You would see that it resolves back to 127.0.0.1
A screenshot has been attached

## Impact

This may cause security issues in multiple user systems. An attack procedure can be found here : https://seclists.org/bugtraq/2008/Jan/270

## Attachments
- test.png
