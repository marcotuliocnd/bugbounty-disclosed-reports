# Email Verification Bypass And Get access to user's private invitation.

## Report Details
- **Report ID**: 1350401
- **URL**: https://hackerone.com/reports/1350401
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-24T11:53:38.349Z
- **Disclosed**: 2021-10-21T19:51:53.477Z

## Reporter
- **Username**: manish_prajapat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
Part 2 of my previous report : https://hackerone.com/reports/1225499
I am sending this report again because you closed my previous report. i posed new impact of this vulnerability in my previous report but i didn't get any reply. So i reported it again.

First Vulnerability : Email verification Bypass-
Summary:
In this vulnerability you can verify any email without verification link. (reddit.com and ads.reddit.com)

Steps To Reproduce:
Email that i wants to verify example : security12345@reddit.com
1. Signup an account with direct “continue with google” with your own email.
2. Go to User Settings and click on "Change" in email section.  it will send you a password reset link before changing email because you signed up an account with google without giving a password. So first you need to reset your account password. (now you can disconnect the google accountif you wants.)
3. After changing password change the email to any other random email like 12332newtestemail@sstestmail.com.
4. After it You will get an email message on your email ‘[reddit] your email address has been changed‘ with account recovery link.
5. Open the link in new incognito tab and enter all details. on email field enter victim’s email that you wants to verify, enter any ramdom password in  current password field and then set new password that you wants to use for this account.
6. Click on Submit button 4 Times because it will give error on 3 attempt.
7. You can see your entered email has been verified.

In Previous report you said its just UI bug but its not only UI bug beacuse  i can use that account(created from above steps) in ads.reddit.com. Normally ads.reddit.com not working with unverified account. But here i can use that account for all of your services as a verified account.

--------------------------------------------------------------------------------------------------------------------------------------------

Second Vulnerability : Get access to user's private invitations
Description :
in ad account if you invites someone as with admin or other permissions. it will send invite to user in https://ads.reddit.com/account/userid/accounts. it can be access by another account that have same verified email.
Steps to reproduce :
1. Make an account and then add victim's email and verify it by using above method.
2. Then create an ad account with this account.
3. Open Switch User page(https://ads.reddit.com/account/userid/accounts) and here you can access victim's private invitation. Everytime victim receives an invitation your account also notified.
Here you can add your account to "invitation sender's account" by clicking Accept button.

Thanks

## Impact

First Bug :
It can be used by an attacker to create verified accounts with any Victim's email on ads.reddit.com and reddit.com.

Second Bug :
It can be used to steal user's private invitation and also react on it.

## Attachments
- Poc_video_email_bypass.mov
