# Running 2 accounts with a single email [Part 2]

## Report Details
- **Report ID**: 241608
- **URL**: https://hackerone.com/reports/241608
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-20T08:28:57.327Z
- **Disclosed**: 2017-10-07T14:44:59.575Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Following the fix on #224072, I decided to try this in another way and it worked!

##Reproduction Steps
1. Login with Github on Browser1 and set a password to it.
- With another email, signup on Weblate on Browser2
- In the new account on  Browser2, do the following:
> Confirm email and Set a Password
Add a Google Account with the same email used to signup Github
Now, disconnect the email used to signup
So, it the email is default to same email on the other account

4. Reload both browsers to confirm, https://hosted.weblate.org/accounts/profile/#account
- Logout any of the browsers
- Trying to login with the email and any of the set passwords pops an **Internal Server Error**

Accompanying screenshots are attached below.

## Attachments
No attachments
