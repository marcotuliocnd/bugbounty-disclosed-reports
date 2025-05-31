# Password protection can be removed for newly created development store 

## Report Details
- **Report ID**: 965510
- **URL**: https://hackerone.com/reports/965510
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-08-24T00:36:27.340Z
- **Disclosed**: 2020-09-14T18:59:32.051Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Details
Per https://help.shopify.com/en/partners/dashboard/managing-stores/development-stores#the-development-store-password-page, it states that the password **can only be removed once the store has been transferred or switch to a paid plan**.

```
You can remove the password page only after you transfer the store to a merchant or switch the store to a paid plan.
```

However, it is still possible to remove the password by using the GraphQL **PreferencesSave** operation.

## Steps to reproduce
1. Create a development store using a partner account
2. From that shop admin, go to **Online Store > Preferences**
3. Make any change to the page and intercept the request
4. Update the `passwordProtection.enabled` property to `false`

The store is now paswordless.

## Demo
████

## Impact

Disable development store password

## Attachments
No attachments
