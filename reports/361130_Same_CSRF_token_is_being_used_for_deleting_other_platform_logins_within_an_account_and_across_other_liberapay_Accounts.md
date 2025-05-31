# Same CSRF token is being used for deleting other platform login’s within an account and across other liberapay Account’s

## Report Details
- **Report ID**: 361130
- **URL**: https://hackerone.com/reports/361130
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-06-02T16:52:29.297Z
- **Disclosed**: 2018-06-04T08:13:00.725Z

## Reporter
- **Username**: mah1ndra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
>We’ve got  “Accounts Elsewhere” option in the profile section. where we can connect our liberapay account with multiple other platform accounts.

>While deleting those Multiple other platform accounts same CSRF token is being used.

>I’ve signed up with a couple of liberapay accounts. Where I found the using of same CSRF token within the account and across other accounts.

## Impact

In the first account in "Accounts ElseWhere" section, I've logged in with Google+ account successfully and while deleting the account I got CSRF token = J0Lk5iXTpp40iDN5KNcrI24bulPcF0PV
Next, I found the same CSRF token is being during deleting all other available other platform logins.

I've created another liberapay account and in "Account ElseWhere" section. I've logged in with my Facebook account and while deleting it I came across same CSRF token used in other account = J0Lk5iXTpp40iDN5KNcrI24bulPcF0PV.

So, I'Ve found same CSRF token is being used for deleting other platform accounts within a liberapay account and across liberapay accounts.

I'm dropping the POC video below.

## Attachments
No attachments
