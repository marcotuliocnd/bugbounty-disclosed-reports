# [h1-2102] Information disclosure - ShopifyPlus add user displays existing Shopify ID fullname

## Report Details
- **Report ID**: 1083922
- **URL**: https://hackerone.com/reports/1083922
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-22T02:34:04.236Z
- **Disclosed**: 2022-02-10T19:45:42.206Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I am not sure if this by design but it came to my attention that the **Add users** functionality located at `https://shopify.plus/[id]/users/invite` allow a Shopify Plus user with the **User management** access to retrieve any existing Shopify ID full name.

## Steps to reproduce
1. Log in into **ShopifyPlus**
1. Go to **Users > Add users**
1. Within the email field, enter an email address of any existing Shopify Account ID (i.e: francisbeaudoin+h1-2101@wearehackerone.com)
1. Select any role and click **Send invite**

As a result, if the entered email does have a Shopify ID, its fullname will be displayed within the user page.

## Screenshot of a pending invite
██████████

**Note:** I've a feeling that this is expected but still reporting it as the standard invite flow (non ShopifyPlus) doesn't display that kind of informations unless the user accepts the invite.

## Impact

A **ShopifyPlus** user with **User management** can retrieve the firstname and lastname of any existing ShopifyID account (by email lookup).

## Attachments
No attachments
