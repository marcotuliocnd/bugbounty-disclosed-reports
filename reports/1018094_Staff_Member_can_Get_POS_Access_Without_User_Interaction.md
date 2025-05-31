# Staff Member can Get POS Access Without User Interaction

## Report Details
- **Report ID**: 1018094
- **URL**: https://hackerone.com/reports/1018094
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-25T00:54:24.000Z
- **Disclosed**: 2020-11-19T22:08:27.893Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

I found that it is possible for a staff member to grant themselves POS access without user interaction from admin.

## Steps to reproduce
- Login as a staff member with `Manage Locations` permission only, in a shop that has POS channel up and running (Could be Lite)
- Make sure your staff member account didn't have POS enabled 
- Make this GraphQL call

```json
{"query":"mutation {retailUserDataUpdate(id:\"gid://shopify/StaffMember/63779504283\",retailUserData:{posAccess:true,pin:\"1423\"}){staffMember{name canAccessPrivateApps authenticationSettings{tfaEnabled}}userErrors{message}}}"}
```

Replace `63779504283` with your personal staff member id, you can find it in `https://your-store.myshopify.com/admin/settings/account/` and click your account name, then you staff member id is in the url.

- Now your staff member account has POS enabled, and pin is set.

## Impact

It will allow to a staff member to POS takeover without user interaction.

## Attachments
No attachments
