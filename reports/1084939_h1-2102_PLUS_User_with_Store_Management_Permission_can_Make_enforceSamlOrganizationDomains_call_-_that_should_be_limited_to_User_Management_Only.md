# [h1-2102] [PLUS] User with Store Management Permission can Make enforceSamlOrganizationDomains call - that should be limited to User Management Only

## Report Details
- **Report ID**: 1084939
- **URL**: https://hackerone.com/reports/1084939
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-23T01:09:35.059Z
- **Disclosed**: 2022-04-21T22:05:00.716Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
[PLUS] User with Store Management Permission can Make enforceSamlOrganizationDomains call - that should be limited to User Management Only

## Description: 
User with Store management permission as shown in below screenshot
{F1168574}

Should not have the ability to enforce SAML organization domains, because this should be limited to user with `User Management` permission only.

## Steps To Reproduce:
- As an org plus admin, visit https://shopify.plus/:org_plus_id/users/invite and invite an user to have store management permission - (The purpose is to enable the low-privileged user to have access to https://shopify.plus/:plus_org_id/stores/api
- As an org plus admin, create a Org domain, by visiting `https://shopify.plus/:id/users/security` and `Add Domain`
- Now login as the low-privileged user we created in the first step
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

- Click around until you see the call to `POST https://shopify.plus/34946971/stores/api`, send that to repeater and make the GraphQL call below
- Make this GraphQL call to enforce SAML integration with that domain, with `REPLACE_ME` replaced by the user id you got from above steps

```
POST https://shopify.plus/34946971/stores/api
...
...

{"query":"mutation  {\n  enforceSamlOrganizationDomains(domainIds:[\"REPLACE_ME\"]) {\n   userErrors{message} }}\n"}
```

## Impact

This action should not be carried out by users with `Store management` permission, although the impact is limited, this should still be restricted.

## Attachments
- Screen_Shot_2021-01-22_at_11.15.03_PM.png
