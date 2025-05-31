# Limited Privilege User Can Create Unauthorized Referrals on partners.shopify.com

## Report Details
- **Report ID**: 1457471
- **URL**: https://hackerone.com/reports/1457471
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-21T15:09:56.143Z
- **Disclosed**: 2025-03-20T20:23:47.059Z

## Reporter
- **Username**: samux
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
###Summary

I have been working on the partner web portal and have noticed the referrals feature contains an issue where a user with limited privileges can create referrals in an unauthorized manner.

###Steps to Reproduce

First you must authenticate with an administrator user and then invite another with limited privileges

{F1587397}

You may notice that the invited user does not have any privileges on the referral functionality.

When you authenticate with the user with limited privileges and then go to the referral functionality

`https://partners.shopify.com/partner_id/referrals/`

███████

You may notice that the user does not have the appropriate privileges to access this functionality.

Now, when the administrator accesses this same functionality.

███

It can be seen that the administrator can do several things, including `Submit a POS Lead`. Entering this url generates the following endpoint:


`https://partners.shopify.com/partner_id/partner_leads/pos`

In this way if the user with limited privileges accesses this URL.

█████

Instead of getting an error, the user can create a new POS Lead within the referrals. By completing the information.


████


It is observed that he was able to complete it with success.

Thanks.

## Impact

Through this vulnerability, an attacker can bypass the implemented restriction in order to perform an action without authorization.

## Attachments
- limited_user.png
