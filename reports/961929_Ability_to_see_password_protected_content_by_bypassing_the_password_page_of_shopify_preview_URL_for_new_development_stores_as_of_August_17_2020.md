# Ability to see password protected content by bypassing the password page of shopify preview URL for new development stores (as of August 17, 2020)

## Report Details
- **Report ID**: 961929
- **URL**: https://hackerone.com/reports/961929
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-18T22:55:44.494Z
- **Disclosed**: 2020-08-25T15:55:25.920Z

## Reporter
- **Username**: saltymermaid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

## Description
I have found a way to bypass the password page of a shopify preview URL for new development stores created  as of August 17, 2020. Currenty, with older development stores, when we share a preview url with someone, we are able to see the content of the store without having to enter a password even if the password protectection is on. For newly created development stores, if you share a preview url with someone, you are asked to enter a password before you can go any further, so I believe that as of august 17, 2020, when sharing a preview url of a development store, we also have to provide the store password for someone to preview the content. 

As cited in https://help.shopify.com/en/partners/dashboard/managing-stores/development-stores#the-development-store-password-page :

```
 All newly created development stores are password protected. This means that visitors to development stores can access your development store in the following ways only:

    1. By entering a password on the development store password page
    2. By logging into the development store's admin
    3. Through a Shopify Theme Store or Shopify App Store demo link
       Unlike the customizable password page for a store that's on a free trial or paid plan, the development store password page isn't linked to the online 
       store's theme and can't be customized.

 You can remove the password page only after you transfer the store to a merchant or switch the store to a paid plan.
```

## Steps to reproduce
1. Create a new development store that meets the new standard (August 17, 2020)
2. Go to `Sales channels > Online Store > Themes`
3. At the top of the page, under the **Themes** title, click the **View your store** link button
4. Look at the url in the address bar and copy the `?_bt=<some-long-token>` query parameter
5. Open a preview url that was generated from another store and that also meets the new standard (August 17, 2020).
6. Paste the `?_bt=<some-long-token>` query parameter you copied from step #4 at the end of the preview url in the address bar and send it
7. You should have bypassed the password authentication and be able to see the store content

I will be attaching a POC video, but if you need extra details just let me know.

## Impact

Even if unlikely to happen, if someone had the preview url in hand, but did not have the store password, this method could be used to bypass the password authentication and have access to the store content. This would lead to information disclosure.

## Attachments
No attachments
