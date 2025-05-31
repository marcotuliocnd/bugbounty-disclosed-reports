# Store Admin Page Accessible Without Authentication at http://www.grouplogic.com/ADMIN/store/index.cfm

## Report Details
- **Report ID**: 1164854
- **URL**: https://hackerone.com/reports/1164854
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-14T12:46:44.460Z
- **Disclosed**: 2022-06-07T10:20:01.693Z

## Reporter
- **Username**: ub3rsick
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
The store admin page is accessible without authentication at below URL:
```
http://www.grouplogic.com/ADMIN/store/index.cfm
```

The store admin page provides functionalities such as the following:
- Add Edit Items
- Search Products
- Search Results
- Search Orders
- Orders Search Results
- Add New Promo Code
- Promo Code
- Add New How Hear
- How Hear

## Steps To Reproduce
Navigate to below URL from a browser to access the store admin page.

```
http://www.grouplogic.com/ADMIN/store/index.cfm
```

## Recommendations
It is highly recommended to implement proper access controls on administrator functionalities. Only authenticated admin users are to be allowed to access admin pages.

## Impact

Access to admin functionalities without authentication.

## Attachments
No attachments
