# Takeover an account that doesn't have a Shopify ID and more

## Report Details
- **Report ID**: 867513
- **URL**: https://hackerone.com/reports/867513
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-07T00:51:25.479Z
- **Disclosed**: 2020-09-02T14:47:24.963Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Details
The https://pos-channel.shopifycloud.com/graphql-proxy/admin can be exploited to update a staff member email without any email confirmation. 

Using the partner dashboard, we've the ability to create a store that doesn't have a Shopify ID account on https://accounts.shopify.com. By using these two together, all we have to do is create an arbitrary store to an email that we own and confirm it with received email, then use the the POS Staff endpoint to update our email without having to validate it.

You'll then be prompted to create a Shopify ID for your stores (the new created one alongs with the victim stores) and you won't need to validate that you own the email since it is already verified.

## Steps to reproduce
1. Have a victim with a shop that doesn't have a Shopify ID
1. Open https://parners.shopify.com and create a development store
1. Within the store creation form, you'll need to update your shop email to one that doesn't exist within Shopify and that you own (so it can be validated). As the field is read-only, that can either be done by intercepting the request with an application like Burp or do the above **within your browser console** to update the form object.
```
window.RailsData.current_organization.business_email = "nonexistingemail@shopify.com";
window.RailsData.user.email = "nonexistingemail@shopify.com";
```
1.. Validate that you own the email address (Link sent to your email)
1. Add the **POS** to your shop **Sales Channels**
1. Open up the **POS > Staff**
1. Save your own staff page and copy the CURL request by using browser inspection
1. Replace the CURL payload email field with the victim email and send the request
1. Refresh your profile page in your Shop, you'll then be prompt to combine your account and note that you're not asked to validated the new email (victim's one).
1. Proceed with the Shopify ID creation
1. You now own the Shopify ID, you can just change its email to yours as the victim could still be recovering them by doing a forget password.

## Impact

That vulnerability has multiple impacts so I wasn't sure if I should've been creating multiple reports
1. Ability to take-over some account
{F818496}

1. Ability to create a verified Shopify ID with non-verified email (See the verified: **francisbeaudoin@hackerone.com**)
{F818494}

1. Ability to update Staff informations even when linked to a Shopify ID

For the later one, let's say you have a Shop with two staff members: A and B (the attacker). Staff B is aware that the Shop owner is about to transfer the Shop to Staff A. By exploiting the POS access endpoint, staff B would be able to move **first name, last name and email** between Staff A <--> Staff B so that once the shop owner would be selecting the right Staff within the UI, we would be sending it to the wrong person.

## Attachments
- Screen_Shot_2020-05-06_at_7.19.49_PM.png
- Takeover.mp4
