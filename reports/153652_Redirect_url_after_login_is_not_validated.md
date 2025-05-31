# Redirect url after login is not validated

## Report Details
- **Report ID**: 153652
- **URL**: https://hackerone.com/reports/153652
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-25T09:46:50.564Z
- **Disclosed**: 2016-07-28T17:14:12.540Z

## Reporter
- **Username**: capripio
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hey,

I have noticed and redirect hidden field in admin/staff login page so I though give it a little shot! 

What happened another user create a Shopify page with bad javascript code in it.

and when any user or owner login with following traversal URL he/she will be redirected to bad js containing a page with any intentional.

"https://capripio.myshopify.com/admin/auth/login?redirect=../pages/about-us"

I am well aware of the following description on your bug bounty page.
"Any issue where a store administrator is able to insert javascript in the storefront area of their own store, including the checkout pages."

But I think security issue is greater here as you were aware of above statement so it might be dangerous to redirect someone to a bad page on a front store, so I submitted.

Please see POC video for more demo. available at private dropbox folder follow link below:
https://www.dropbox.com/s/49odz7owp1oj53t/poc.zip?dl=0

Sorry for my bad English!

## Attachments
No attachments
