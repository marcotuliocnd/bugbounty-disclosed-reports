# IDOR to view User Order Information

## Report Details
- **Report ID**: 287789
- **URL**: https://hackerone.com/reports/287789
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-11-06T17:42:59.907Z
- **Disclosed**: 2018-09-17T15:33:04.833Z

## Reporter
- **Username**: meals
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bohemia

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!


**Description:** There is an idor to view other user's order information and determine their IP addresses and other order infromation

## Application & Version:

https://store.bistudio.com/order/1003793?confirmed=true

## Steps To Reproduce:
1. Login to your account
2. Visit the above endpoint
3. You can iterate through the order ID to view other users details.

## Supporting Material/References:

{F237085}
{F237086}

## Attachments
- Screen_Shot_2017-11-06_at_12.42.03_PM.png
- Screen_Shot_2017-11-06_at_12.40.46_PM.png
