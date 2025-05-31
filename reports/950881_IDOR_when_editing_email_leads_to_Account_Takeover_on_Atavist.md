# IDOR when editing email leads to Account Takeover on Atavist

## Report Details
- **Report ID**: 950881
- **URL**: https://hackerone.com/reports/950881
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-08-04T14:08:42.754Z
- **Disclosed**: 2020-11-18T14:21:14.912Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
I created an account on Atavist and checked my settings page.
I can change my email at https://magazine.atavist.com/cms/reader/account with this request :

{F936117}

And as you can see, there is a `id` parameter on request data. It's our user ID, and it's vulnerable for IDOR. So we can change any user's email address.

Also user IDs are sequential so an attacker can change all accounts' email.

## Steps To Reproduce:

  1.Go to https://magazine.atavist.com/login and Login to your account
  1. Go to https://magazine.atavist.com/cms/reader/account and open your proxy program 
  1. Change the email and click `Save`
  1. In request, change the ID to your test account's ID
  1. Forward the request
  1. Now you can reset victim's password via https://magazine.atavist.com/forgot

## Impact

Account Takeover without user interaction

Thanks,
Bugra

## Attachments
- request.PNG
