# Non-store owners can transfer Shopify-managed domain to another domain provider

## Report Details
- **Report ID**: 1820953
- **URL**: https://hackerone.com/reports/1820953
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-03T12:12:32.654Z
- **Disclosed**: 2024-01-17T22:23:43.698Z

## Reporter
- **Username**: boy_child_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
According to docs [here](https://help.shopify.com/en/manual/domains/managing-domain-ownership/transferring-shopify-domains#transfer-your-shopify-managed-domain-to-another-domain-provider), only store owners can transfer domains to another domain provider.
{F2100708}

This is not enforced as users/staff members without the `Transfer domain to another Shopify store` permission can perform this action as well as staff members that aren't a store owner in themselves.

## Shops Used to Test:
███

## Steps To Reproduce:
1. Login as a staff member with these permissions only:
{F2100711}

2. From your Shopify admin, go to `Settings > Domains`.
3. In the Shopify-managed domains section, click the name of the domain that you want to transfer.
4. Click `Transfer domain > Transfer to another provider`.
5. Review the information, and then click `Confirm`. The domain authorization code is displayed on your domain's information page.
6. Give the domain authorization code to your new domain provider to verify the transfer.
7. Done.

## Supporting Material:
███████

## Impact

Shopify-managed domains can be transferred to another domain provider by a staff member without `Transfer domain to another Shopify store` permission and a non-store owner.

## Attachments
- Screenshot_from_2023-01-03_15-02-32.png
- Screenshot_from_2023-01-03_15-03-05.png
