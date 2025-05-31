# H1514 Removed Staff members who had "Apps" permission can still modify flow app connections

## Report Details
- **Report ID**: 416983
- **URL**: https://hackerone.com/reports/416983
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-10-01T17:57:50.647Z
- **Disclosed**: 2019-06-14T18:05:30.030Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
**Summary:** 
It's been found that removed staff members who had "Apps" permission can still modify flow app connection settings due to improper authorization.

**Description:**
Flow app (https://apps.shopify.com/flow) allows users to connect their Google Sheets, Trello and Asana accounts to their flow accounts to be used later in workflows (e.g storing new customer information to google spreadsheet).

It's been found that when a user tries to connect his google account, he is redirected to `https://flow-connectors.shopifycloud.com/gsheet/connect?shop_domain=[shop].myshopify.com&shop_id=[shop-id]&path_hmac=[path_hmac]`, the parameter `path_hmac` is the only way the application determines whether the user can modify the connection settings for that shop or not and it's the same for all staff members and doesn't depend on any session as it's hmac of the path `/gsheet/connect?shop_domain=[shop].myshopify.com&shop_id=[shop-id]`  

With that said, it's possible for a staff member who had "Apps" permission then was removed to modify the connection settings for Google SpreadSheets, Trello and Asana by just saving the `path_hmac`.

## Steps To Reproduce:

1. Login to your shop as the shop owner and add a staff member with only "Apps" permission.
2. Install flow app: https://apps.shopify.com/flow
3. Login with the new user you added and navigate to `https://[Your-Shop].myshopify.com/admin/apps/flow/connectors`
4. Click All **Settings** links next to Google Sheets, Trello and Asana and save them
5. Login with the shop owner and remove the user you added
6. You can now use the links you saved to modify connectors settings.

**Live PoC:**
You can modify my shop's google spread sheet connection by navigating to `https://flow-connectors.shopifycloud.com/gsheet/connect?shop_id=24615823&path_hmac=%2BPnVhhFIC49KrHZGqwC08LoSMSkieG7UHWgtnriV2vQ%3D`

## Impact

Through this vulnerability a removed staff member will be able to modify google spread sheet, trello and asana connections to connect his own accounts so that workflow actions regarding the connections go to his accounts and therefore he can still access the shop data.

## Attachments
No attachments
