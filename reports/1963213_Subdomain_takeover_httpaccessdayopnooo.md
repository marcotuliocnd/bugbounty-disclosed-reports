# Subdomain takeover http://accessday.opn.ooo/

## Report Details
- **Report ID**: 1963213
- **URL**: https://hackerone.com/reports/1963213
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-27T08:51:52.874Z
- **Disclosed**: 2023-06-11T07:04:41.266Z

## Reporter
- **Username**: secsoya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
I found unused accessday.opn.ooo subdomain was delegated to wix.com and not claimed.

##Steps To Reproduce:
- Visit http://accessday.opn.ooo/
- This domain pointing towards to WIX cdn, anyone can claim this subdomain

##Similar report:
https://hackerone.com/reports/1256389
https://hackerone.com/reports/996956
https://hackerone.com/reports/1183296

## Impact

An attacker can claim this subdomain and abused for specific purposes

## Attachments
- Screenshot_2023-04-27_15_44_24.png
