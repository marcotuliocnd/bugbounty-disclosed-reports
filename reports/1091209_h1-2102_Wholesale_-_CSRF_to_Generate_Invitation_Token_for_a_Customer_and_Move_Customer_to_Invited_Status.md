# [h1-2102] Wholesale - CSRF to Generate Invitation Token for a Customer and Move Customer to Invited Status

## Report Details
- **Report ID**: 1091209
- **URL**: https://hackerone.com/reports/1091209
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-31T13:14:18.876Z
- **Disclosed**: 2021-12-06T01:26:09.626Z

## Reporter
- **Username**: rhynorater
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
There is a CSRF vulnerability in the Wholesale application to generate an invitation token for a user and move that user to `invited` status.

## Steps To Reproduce:
1. Log in to Shopify and configure Wholesale
2. Add a price list
3. Add a customer with the tag `wholesale`
4. Adjust the pricelist to include the user with the `wholesale` tag
5. At this point you should see the user in the customer section (see figure 1)
6. Now, navigate to `https://poc.rhynorater.com/wholesaleShopify/CSRF.html`
7. Wait 30 seconds (for good measure)
8. Refresh the customer page and note that the user is in the status of `invited`

Figure 1
{F1178635}

## Supporting Material/References:

## Impact

Move customer to `invited` status and generated invite link.

## Attachments
- Screenshot_from_2021-01-31_22-06-15.png
