# H1514 [*.(my)shopify.com] - Viewing Password Protected Content

## Report Details
- **Report ID**: 421859
- **URL**: https://hackerone.com/reports/421859
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-10-09T23:29:59.524Z
- **Disclosed**: 2019-05-22T18:30:53.737Z

## Reporter
- **Username**: corb3nik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi guys!

When administering a shop, the owner has the ability to preview his shop with various themes. When previewing, a unique link is generated, which the owner can share with various people without any authentication.

The generation of that unique link does not require authentication, which means any user can generate a preview link and view the contents of the shop.

Previewing isn't affected by password protection, so a user who has managed to obtain a preview link can successfully view the shop's content without knowing the password.

## Steps to Reproduce

1. Visit the following shop : https://mycorb3nikshop.myshopify.com.
2. Notice that it is protected by a password.
3. Visit https://mycorb3nikshop.myshopify.com/preview_bar and view the page's source code.
4. Search for a shopifypreview.com URL. This is the preview link generated for `mycorb3nikshop`.
5. Visit the preview URL.

You should now see the contents of the shop. Note that we've successfully viewed the content without any authentication.

{F358126}

## Impact

The impact of this bug is pretty straightforward. Because of the `/preview_bar`, the password protection is rendered useless.

Depending on the confidentiality of a shop's content, I would set the severity to either high or medium here :)

## Attachments
- Screen_Shot_2018-10-09_at_7.25.21_PM.png
