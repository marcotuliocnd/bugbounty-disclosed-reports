# Able to Takeover Merchants Accounts Even They Have Already Setup SSO, After Bypassing the Email Confirmation

## Report Details
- **Report ID**: 796956
- **URL**: https://hackerone.com/reports/796956
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-14T22:33:04.887Z
- **Disclosed**: 2020-04-01T21:01:12.321Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Able to Takeover Merchants Accounts  Even They Have Already Setup SSO, After Bypassing the Email Confirmation

## Summary
This report is based on the scenario that email confirmation has been bypassed already, like shown in #791775.

What happened in #791775 was, I was too excited and didn't take a step further to try to takeover merchant's account even they have SSO setup, and after reading the comment `An important mitigating factor was that this bug only affected user accounts which had not yet adopted our single login system. `, I know I have to find a way to bypass that to prove my point.

## Description
For merchant that have accounts already setup SSO, even attacker has bypassed the email confirmation, they would have no ways to takeover the rest of the accounts of the merchant, because they will need to enter the master password of the merchant in the process of merging accounts.

Let me illustrate this in graphs, in this example, the merchant that has SSO already setup is `ngalog+1@wearehackerone.com`, the attacker sign-up a store h48ngalog.myshopify.com, with email `ngalog+1@wearehackeorne.com`

Stage 1. First, for whatever reason, maybe a new feature appeared that allows attacker to bypass email confirmation again or an old bug bypass, that as an attacker with ngalog+1@wearehackerone.com confirmed, he should see this in the shop

{F716958}

Stage 2. Then, when attacker clicks Review accounts, attacker needs to put in the store password first, which is fine cause attacker signup this store account himself, so it should have no problem

{F716957}

Stage 3. After authenticating, here is the real obstacle, Shopify asks attacker for the main shop's password, for sure the attacker doesn't know the password, otherwise he could just go on and takeover the store without these steps.

{F716959}

Stage 4. Here's the magic step, note that the url path is `/login` now at stage3, change the path to `/accounts_merge/new-password` while keeping the query part the same

{F716960}

Stage 5. The victim `ngalog+1@wearehackerone.com `account has no 2FA configured, after submitting this report I'll try again with the 2FA enabled victim account and see if this still works, for now stay with me, enter a new password of attackers choice, and click do not enable 2FA etc.., and finally you'll be redirected to this page, asking you to confirm the change of password, click the button

{F716961}

And now we are done, you should be redirected to your old store, and feel free to change stores on the upper left switch store tab, or use your new password to login victim's store.

## Steps to reproduce
- Create a store, and confirm your email with victim's email, and this victim should not have 2FA setup, and should have SSO setup already
- Click the button shown in {F716958}
- enter your store's own password
- the url should now be accounts.shopify.com/login?xxxxxx, change `/login` to `/accounts_merge/new-password` while keeping the query part xxx the same {F716960}
- Enter your new password and continue without setting up the 2FA, you can try to setup the 2FA for victim, I never tried, guess it is not important, since the impact would just be locking victim out of their account
- Finally, click confirm button on the password change {F716961}

## Impact

Able to takeover merchant's account even they have SSO enabled after email confirmation bypass

## Attachments
- stage2.png
- stage1.png
- stage3.png
- stage4.png
- stage5.png
