# Ability to link a Google account to another staff account/store owner that isn't linked yet

## Report Details
- **Report ID**: 892904
- **URL**: https://hackerone.com/reports/892904
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-06-06T20:38:03.221Z
- **Disclosed**: 2020-07-14T23:15:11.980Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
The https://pos-channel.shopifycloud.com/graphql-proxy/admin endpoint allows us to update a staff email address that is having a Shopify ID.

Taking that into consideration, if a store is setup to use **Google Apps** as login service and if a staff/store owner hasn't yet linked his account to a Google one (meaning he never logged in using Google), it is possible to update their email to our own Google email address resulting in us being able to log into their account. By doing so, our Google account ends up linked to the staff member/store owner. 

## Steps to reproduce 
1. As a staff member with **Point Of Sale** access, open up **Point of Sale** > **Staff** page and select the staff you want to link your Google account with.
2. Open up your browser network inspection tab and save its profile. Copy the CURL request that is being made to https://pos-channel.shopifycloud.com/graphql-proxy/admin **StaffMemberUpdate** operation.
3. From the copied CURL request, update the `email` field from the payload to your own email of the configured Google Apps domain.
4. Logout from the store and log back in using the `Google Apps` email you just set.

## Demo
{F857469}

## Impact

Recently, maybe when you guys fixed [872380](https://hackerone.com/reports/872380),  [867513](https://hackerone.com/reports/867513) or some other reports, you also fixed updating the email address of a store owner using the **StaffMemberUpdate** operation of https://pos-channel.shopifycloud.com/graphql-proxy/admin endpoint. However, the shop owner himself is still able to update his email address using that endpoint. Thus, by leveraging a XSS targeting the shop owner, we would technically be able to link it to our Google account, giving us access to shop owner features as described on https://help.shopify.com/en/manual/your-account
{F857468}

Besides that, without any XSS, that can exploited to link our Google account to any other staff account that isn't yet linked.

## Attachments
- Shop_owner_features.png
