# XSS on $shop$.myshopify.com/admin/ and partners.shopify.com via whitelist bypass in SVG icon for sales channel applications

## Report Details
- **Report ID**: 232174
- **URL**: https://hackerone.com/reports/232174
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-05-26T09:12:00.386Z
- **Disclosed**: 2017-06-27T23:49:28.072Z

## Reporter
- **Username**: bored-engineer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Description
Shopify allows developers to create a special type of application called a "[Sales Channel](https://help.shopify.com/api/sdks/sales-channel-sdk)". Developers are allowed to upload a 16x16 SVG "Navigation Icon" for their app provided the SVG follows the [design guidelines](https://help.shopify.com/api/sdks/sales-channel-sdk/design-guidelines/checklist#navigation-icon) which limits the allowed elements and attributes. For some reason when the SVG contains an XML entity this whitelist is no longer enforced allowing the developer to include malicious attributes such as `onload`. By uploading a malicious SVG a developer can obtain XSS on both partners.shopify.com, as well as any the admin panel of any shop which has authorized the sales channel. 

# Proof of Concept
This is relatively easy to reproduce, first create a new application within the [Partners dashboard](https://partners.shopify.com) then navigate to "Extensions" -> "Sales channel" to convert the application. After saving those changes a new field within the "App info" section titled "Navigation icon". Upload the following SVG:
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE svg [
    <!ENTITY elem "">
]>
<svg onload="alert(document.domain);" height="16" width="16">
  &elem;
</svg>
```
After saving changes the XSS payload will fire on [partners.shopify.com](https://partners.shopify.com). To fire the payload on `$shop$.myshopify.com/admin/` you'll need to authorize the application on your shop:
I've created an example malicious application associated with my partner account `shopify-whitehat-2+hackerone@bored.engineer` to help demonstrate the issue, you can authorize it by opening the following URL on `$your-shop$.myshopify.com`:
```
/admin/oauth/authorize?client_id=672a937d5eb24e10c756ea256c73bb8c&scope=read_products&redirect_uri=https://attackerdoma.in/93ba4bef-cff1-43b1-922d-0631bd387e2e.html&state=nonce
```
Immediately after authorizing the application (and all future admin panel loads) an alert should appear on the /admin window containing document.domain.

# Exploitability
This seems like a really odd issue, so it may good to see if there are other places this icon could surface (ex. the app store or internal admin panels) to full understand the impact. For the known exploitable use-case via OAuth authorization you do need to convince an administrator to authorize your malicious application, however the exploit does not require any specific permissions to trigger so an admin may be more willing to authorize the application. Once the administrator has loaded the application it will immediately fire without additional user-interaction. 

# Remediation
The application should not allow XML entities in uploaded SVGs (or at least fix the parsing so it handles them correctly).

## Attachments
No attachments
