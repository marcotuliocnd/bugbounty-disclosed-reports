# Ability to bypass partner email confirmation to take over any store given an employee email

## Report Details
- **Report ID**: 300305
- **URL**: https://hackerone.com/reports/300305
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-12-24T08:47:29.068Z
- **Disclosed**: 2018-02-07T13:28:31.959Z

## Reporter
- **Username**: cache-money
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I told Pete I would take a look at Spotify, hi Pete.

**Summary**
It's possible to take over any store account through partners given an employee email address. This is possible because I found a way to confirm arbitrary emails. I don't know the Shopify ecosystem well enough to know the other ramifications of such a bug.

On #270981 you wrote:
> The intention was that, when a partner already had a valid user account on the store, their collaborator account request could be accepted automatically, with the user account converted into a collaborator account.

I tested that functionality and confirmed how it works. I realized that if you can somehow create a partner account with a business email that matched that of an employee, you would be able to take over their employee account, then convert it to a collaborator. The problem is that business accounts need emails to be validated, but this can be bypassed with a race condition.

The bug works by hitting the email validation endpoint for an email you own, at the same time as changing your email to a victim's. It might take a few tries, but eventually your email will be changed and be validated due to not (properly) using a DB transaction.

**Steps to reproduce**
1. Create a store account and invite an employee.
2. Accept the employee invite (maybe not necessary I didn't test).
3. Login to or create a partner account as the attacker.
4. Go to your partner settings page `https://partners.shopify.com/[ID]/settings` and change your email to something you own.
5. Check your email and grab the confirmation link, but don't visit it yet.
6. Go back to your partner account and change your email to that of the store employee from step 2, but intercept the request to not let it through yet.
7. Now the tricky part. The "change email" takes anywhere from 1,100 - 2,500 ms to load so you need to take that into account. But let the request go through, wait for some milliseconds, then in another tab visit that email confirmation link from step 5.
8. If done correctly you will now have confirmed an email you do not own.
9. Visit `https://partners.shopify.com/[ID]/managed_stores`, add the store, and you now have access.

As proof, look at the email for partner account `698396`. It will be confirmed `cache@hackerone.com`, which I obviously would never be able to validate otherwise.

Thanks,
-- Tanner

## Impact

Ability to take over stores, and possibly perform any other action that relies on a validated email as a security measure.

## Attachments
No attachments
