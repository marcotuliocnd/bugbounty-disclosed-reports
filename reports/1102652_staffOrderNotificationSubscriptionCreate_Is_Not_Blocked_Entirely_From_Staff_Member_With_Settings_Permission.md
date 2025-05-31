# staffOrderNotificationSubscriptionCreate Is Not Blocked Entirely From Staff Member With Settings Permission

## Report Details
- **Report ID**: 1102652
- **URL**: https://hackerone.com/reports/1102652
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-02-13T10:11:14.066Z
- **Disclosed**: 2022-02-09T20:58:34.749Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

I found that the GraphQL call `staffOrderNotificationSubscriptionCreate` is not blocked from the staff member with Settings permission

## Steps to reproduce
- Login as a staff member with `Settings` permission
- Make this GraphQL call to `https://yoursubdomain.myshopify.com/admin/internal/web/graphql/core?operation=SwitcherNoStores`

```
{"query": "mutation{staffOrderNotificationSubscriptionCreate(notificationRecipientIdentifier:\"testingforshopify@ngailong.com\",notificationRecipientType:EMAIL){staffOrderNotificationSubscription{id}}} "}
```

- The response you see should be `Access denied for staffOrderNotificationSubscription field. Required access: `read_notification_settings` access scope. Also: User must have access to orders.`, and you would think this means a dead end, but reality is you have already added the order notification to the settings
- Visit `/admin/settings/notifications` as an admin, you should notice the email `testingforshopify@ngailong.com` is added to the order notification already

## Screenshot video
{F1194404}

## Impact

I found that the GraphQL call `staffOrderNotificationSubscriptionCreate` is not blocked from the staff member with Settings permission

## Attachments
- poc_settings_email.mov
