# Script Editor preview token still working with uninstalled application, even for unpublished script

## Report Details
- **Report ID**: 915940
- **URL**: https://hackerone.com/reports/915940
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-07-05T16:02:24.404Z
- **Disclosed**: 2020-08-25T21:34:33.512Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Within the Script Editor application, it is possible to preview a script on the storefront and proceed to purchase. Once the user click on the preview link, it opens `https://{shop}.myshopify.com/admin/scripts/preview?script_id={script_id}` which then generate a preview token to be used by the storefront. As an example, it redirects back the user to `https://{shop}.myshopify.com/cart?preview_script_id={preview_script_id}`. Per my testing, that token doesn't seem to be expiring and can still be used even if the Script Editor application has been uninstalled. 

Taking that into consideration, a malicious user could've created an unpublished script applying discounts to carts and if he has access, even uninstall the app. That could be done by a malicious hired Shopify Developer/Collaborator which had to do some work on a given store.

On the other hand, if a script has been applied to an order, a clickable `Script name was run on this order (Script Editor)` message is left on its **Timeline** so the admin can better understand why a discount has been applied. That said, it is possible to update a script name to an "empty" character resulting in the user not being able to deep-link from the order timeline to the Script Editor. By doing so, the user is also unable to edit the script as the application itself uses an hyperlink on the script name to open the edit page - meaning that the only way to edit the script would be to directly open the script editor page located at `https://script-editor.shopifycloud.com/scripts/{id}`.

## Steps to reproduce - Updating a script name to an empty character
1. Open the **Script Editor** application and create a new script 
1. By clicking **Save draft**, a request will be made to  `PATCH https://script-editor.shopifycloud.com/scripts/{id}`
1. Intercept the request and/or replay it by updating the `name` property to an empty character. A zero-widthspace character can be copied from https://qwerty.dev/whitespace/

**Order timeline - Hyperlink suppressed as script name is using empty character**
{F894857}

**Script Editor Application - Unable to edit the script**
{F894858}

## Impact

A malicious user which had access to the store admin at some point, could've created unpublished script to apply discounts to carts which become a bit invisible to the admin if the application is uninstalled and/or using empty character for the script name.

For example, someone selling its store in the marketplace could make use of this.

To mitigate the issue, introducing a time based  expiration of the `preview_script_id` might do it.

## Attachments
- Order_-_Timeline_no_hyperlink.png
- Script_Editor_App_-_No_hyperlink_to_edit.png
