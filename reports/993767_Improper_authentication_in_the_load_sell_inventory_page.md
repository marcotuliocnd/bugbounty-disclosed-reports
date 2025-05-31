# Improper authentication in the load sell inventory page

## Report Details
- **Report ID**: 993767
- **URL**: https://hackerone.com/reports/993767
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-09-29T04:32:08.983Z
- **Disclosed**: 2020-10-08T09:39:17.953Z

## Reporter
- **Username**: niggy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:

Hello team,

I found an endpoint response all data relate to sell mode inventory that doesn't have improper authentication in the link: 
https://cs.money/load_sell_mode_inventory

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Open directly the link:
https://cs.money/load_sell_mode_inventory
  2. Observe the result

## Supporting Material/References:


  * [attachment / reference]

## Impact

All most data in the site to view then user have to login the first. I think that you are missing authentication for these pages.

## Attachments
- load_sell_mode_inventory.PNG
