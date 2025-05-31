# Ability to verify any email address you don't own - accounts.shopify.com

## Report Details
- **Report ID**: 229619
- **URL**: https://hackerone.com/reports/229619
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-18T13:26:49.722Z
- **Disclosed**: 2019-11-08T11:03:38.432Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary: 
During testing it's been found that in `accounts.shopify.com` it's possible to change your email address to any email address that you don't own and confirm that email due to the confirmation token being leaked.

## Steps to reproduce: 
1. Login to `https://accounts.shopify.com/account`
2. Click **Change** Next to email
3. Enter any new email address
4. You'll see a message saying:
 
```
Verification email sent
We sent you an email to verify that you own "email@example.com". We'll change your email once you verify that you own it.
```
with a link to resend the verification email or cancel the change.
5.- Copy the resend link, it will look like this: `https://accounts.shopify.com/email-change/<Confirmation-TOKEN>/resend`
6.- Go to `https://accounts.shopify.com/email-change/<Confirmation-TOKEN>/` and the email will be verified even though you don't own it.

Thanks!

## Attachments
No attachments
