# [h1-2102] shopApps query from the graphql at /users/api returns all existing created apps, including private ones

## Report Details
- **Report ID**: 1085332
- **URL**: https://hackerone.com/reports/1085332
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-23T14:10:23.056Z
- **Disclosed**: 2022-07-15T08:23:26.500Z

## Reporter
- **Username**: inhibitor181
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
I have seen that there is query called shopApps executable on the `/[ID]/users/api` graphql that returns a huge amount of apps (it timeouts with a limiting). In the response I have noticed the returned apps also include the private apps, so I do not think that this is intented like this. Using this method, one can grab all the apps, including private ones from shopify.

## Steps To Reproduce:
1. Login to shopify.plus as the admin
2. Go to users, monitor the request and send the POST made to `/[ID]/users/api` to repeater
3. Change the body with this one :

```
{"query":"query xxx { shopApps(first:10000) { edges { node { id isPrivate handle name title shopifyApiClientId } } } }"}
```

In the response, if you search for `"isPrivate":true` you will see also private apps.

## Supporting Material/References:
Screenshots attached

## Impact

One can grab all the shopify apps, including the private ones that I assume are not meant to be accessible.

## Attachments
- Screenshot_from_2021-01-23_15-03-07.png
- Screenshot_from_2021-01-23_15-02-39.png
- Screenshot_from_2021-01-23_15-02-25.png
