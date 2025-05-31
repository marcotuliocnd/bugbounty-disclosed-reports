# Email Confirmation Bypass in myshop.myshopify.com that Leads to Full Privilege Escalation to Any Shop Owner by Taking Advantage of the Shopify SSO

## Report Details
- **Report ID**: 791775
- **URL**: https://hackerone.com/reports/791775
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-02-09T23:25:28.933Z
- **Disclosed**: 2020-04-01T21:01:33.551Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I told Pete I would take a look at Spotify, hi Pete.

## Summary
It's possible to take over any store account through bypassing the email confirmation step in *.myshopify.com. I found a way to confirm arbitrary emails, and after confirming arbitrary email in *.myshopify.com, user is able to **integrate** with other Shopify store that shares the same email address by setting a master password for all of the stores(if the owner hasn't integrated before), effectively taking over every Shopify stores by knowing just the owner's email address.

After signing up a new Shopify instance in https://www.shopify.com/pricing and start the free trial, user can change their email address to a new email address before confirming the one they used to sign up.

The bug is that Shopify email system mistakenly send the confirmation link of the new email address, to the one that is used to signed up.

And the result is user can confirm arbitrary email address. And the next step is taking over other user's Shopify instance by taking advantage of the SSO.

## Quick check
If you check https://h31ngalog.myshopify.com/ and see the email address of the owner, it is ngalog@hackerone.com, which I obviously would never be able to validate otherwise
{F711349}

## steps to reproduce
- Visit https://www.shopify.com/pricing and signup a free trial with an email address, say attacker@gmail.com that you can receive emails
- after entering the fields to enter the store, on top right corner, click your name and go to **Your Profile**
- change your email to someone that you want to takeover, for example yaworsk@hackerone.com and click save
- All done now, grab a coffee, sit back and relax, watch some YouTube videos and wait for an email to go to your email attacker@gmail.com
- The email that you are waiting for is from mailer@shopify.com, and the format should look like this {F711348}
- Click the link and you should see your email has been updated to yaworsk@hackerone.com

## Reason?
Email system mistakenly send the confirmation link of yaworsk@hackerone.com to attacker@gmail.com because attacker@gmail.com is the one that is saved on system, and the email system didn't notice the confirmation link has been updated to yaworsk@gmail.com, and should not be sent to attacker@gmail.com

## SSO account takeover
- now we have the ability to confirm arbitrary email, then we can takeover other stores
- On top right corner of you-shop.myshopify.com click your name then click profile, you should see a box that says, you have other two accounts in Shopify, want to integrate them together
- click yes, then just follow the instructions then you will be able to takeover all other stores by changing the master password for all of the stores under that email address.

## Impact

Ability to confirm arbitrary email on *.myshopify.com and leverage SSO to set master password for all other stores under the same password

## Attachments
- Screenshot_2020-02-10_at_12.18.01_PM.png
- Screenshot_2020-02-10_at_12.13.19_PM.png
