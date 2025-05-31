# Sidekiq dashboard exposed at notary.shopifycloud.com

## Report Details
- **Report ID**: 1405673
- **URL**: https://hackerone.com/reports/1405673
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-19T15:20:43.669Z
- **Disclosed**: 2021-11-25T19:28:29.518Z

## Reporter
- **Username**: youstin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
Hi,

I found that the host https://notary.shopifycloud.com/ is exposing a sidekiq dashboard to the internet, for any unauthenticated user to use. I am not very familliar with Sidekiq, but from what I can tell its used for ruby background proccessing. 

I am fairly certain this dashboard is used to manage shopify instances, since browsing to `https://notary.shopifycloud.com/sidekiq/scheduled` reveals a list of jobs which domains as arguments. I checked a few of the domains and they all seem to be shopify hosts.

I have not tried stopping any of the proccesses in order to not cause any downtime or issues to shopify hosts.

██████████

## Impact

Stop workers & background processes for shopify hosts.

## Attachments
No attachments
