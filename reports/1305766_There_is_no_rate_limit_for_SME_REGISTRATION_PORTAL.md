# There is no rate limit for SME REGISTRATION PORTAL

## Report Details
- **Report ID**: 1305766
- **URL**: https://hackerone.com/reports/1305766
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-08-15T08:24:59.496Z
- **Disclosed**: 2022-09-19T05:41:27.495Z

## Reporter
- **Username**: sachinrajput
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
The speed limit for the https://mtngbissau.com/registo/ endpoint has not been implemented.
## Steps To Reproduce:
1. Go to the https://mtngbissau.com/registo/
2.  fill out the Registration form
3. Send request to Intruder.
4. Set your payloads and start attack.
5. There is no rate-limit.

## Impact

Attacker can register false n-number of request which lead to DDos attack.

## Attachments
- Screenshot_(410).png
