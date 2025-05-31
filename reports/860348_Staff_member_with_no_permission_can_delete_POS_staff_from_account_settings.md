# Staff member with no permission can delete POS staff from account settings

## Report Details
- **Report ID**: 860348
- **URL**: https://hackerone.com/reports/860348
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-27T15:25:02.717Z
- **Disclosed**: 2020-09-14T19:56:50.204Z

## Reporter
- **Username**: kunal94
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Team

#Description
Shopify POS also has staff settings only for POS purposes where an admin can add POS Shopify staff along with fname,lname, email address, and generated pin.
Reference - https://help.shopify.com/en/manual/sell-in-person/pos-classic/setup/staff-settings
After creation, Shopify POS staff displays in /admin/settings/account, and Vulnerability arises when staff members with no permission can delete Shopify POS staff from account settings.

#Step To Reproduce

+ Go to the Shopify POS app from the admin session.
{F805568}

+ Currently, I've Shopify Plus Partner Sandbox/Monthly, so in a sandbox environment, staff POS staff settings are not enabled, however, we can modify response and enable the POS staff member feature on the sandbox environment to test.

+ Intercept Shopify POS app area from burp suite and notice the GRAPHQL response

**Request**

`POST /graphql-proxy/admin HTTP/1.1
Host: pos-channel.shopifycloud.com
`

`{"operationName":"Overview","variables":{},"query":"query Overview {\n  shop {\n    currencyCode\n    ianaTimezone\n    countryCode\n    features {\n      retailPackage\n      __typename\n    }\n    staffPermissionsBetaFlag: beta(name: \"pos_web_admin_staff_user_permissions\")\n    accountSetupQuestionsAnswers {\n      answer\n      handle\n      __typename\n    }\n    plan {\n      trial\n      __typename\n    }\n    accountOwner {\n      email\n      __typename\n    }\n    __typename\n  }\n  locations(first: 50) {\n    edges {\n      node {\n        name\n        id\n        addressVerified\n        hasActiveInventory\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  products(first: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
`

**Response**
```
{"data":{"shop":{"currencyCode":"INR","ianaTimezone":"America\/New_York","countryCode":"IN","features":{"retailPackage":true,"__typename":"ShopFeatures"},"staffPermissionsBetaFlag":false,"accountSetupQuestionsAnswers":[{"answer":"No locations yet","handle":"number_locations","__typename":"AccountSetupQuestionsAnswer"},{"answer":"1","handle":"offline_brick_and_mortar","__typename":"AccountSetupQuestionsAnswer"},{"answer":"1","handle":"offline_markets_fairs","__typename":"AccountSetupQuestionsAnswer"},{"answer":"1","handle":"offline_temp_shops","__typename":"AccountSetupQuestionsAnswer"}],"plan":{"trial":false,"__typename":"ShopPlan"},"accountOwner":{"email":"kunal94@wearehackerone.com","__typename":"StaffMember"},"__typename":"Shop"},"locations":{"edges":[{"node":{"name":"khudirampally, bagdogra","id":"gid:\/\/shopify\/Location\/35202859030","addressVerified":false,"hasActiveInventory":true,"__typename":"Location"},"__typename":"LocationEdge"},{"node":{"name":"test","id":"gid:\/\/shopify\/Location\/35202891798","addressVerified":true,"hasActiveInventory":true,"__typename":"Location"},"__typename":"LocationEdge"}],"__typename":"LocationConnection"},"products":{"edges":[{"node":{"id":"gid:\/\/shopify\/Product\/4351723438102","__typename":"Product"},"__typename":"ProductEdge"}],"__typename":"ProductConnection"}},"extensions":{"cost":{"requestedQueryCost":60,"actualQueryCost":12,"throttleStatus":{"maximumAvailable":600000.0,"currentlyAvailable":599988,"restoreRate":30000.0}}}}
```

+ In the response, we have `"staffPermissionsBetaFlag":false`, use Burp Match and Replace rule on response body and set the value from `"staffPermissionsBetaFlag":false` to `"staffPermissionsBetaFlag":true`.

{F805580}

+ Again refresh the page and we have access to Shopify POS Staff manage area.
{F805581}

+ Navigate to  "Manage POS staff" and add POS staff
{F805609}

+ Save it and when you go to `/admin/settings/account` and we can see Shopify POS staff down below:
{F805612}

+ Next, Logged in as staff member with no permission, and navigate to `/admin/settings/account`, down below staff member can also see POS staff account, open POS staff account area, and click on delete, and the account will be deleted successfully.

{F805625}

+ I have set the severity as low since I don't know about the level of POS staff's impact on the Shopify store.



Thanks
Kunal

## Impact

+ User with no permission at all can delete "Shopify POS staff" completely.

## Attachments
- Screenshot_2020-04-27_at_8.15.52_PM.png
- Screenshot_2020-04-27_at_8.26.53_PM.png
- Screenshot_2020-04-27_at_8.28.18_PM.png
- Screenshot_2020-04-27_at_8.37.47_PM.png
- Screenshot_2020-04-27_at_8.39.49_PM.png
- Screen_Recording_2020-04-27_at_8.45.32_PM.mov
