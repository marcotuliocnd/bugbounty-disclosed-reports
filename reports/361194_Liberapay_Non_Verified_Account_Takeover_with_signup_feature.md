# Liberapay Non Verified Account Takeover with signup feature

## Report Details
- **Report ID**: 361194
- **URL**: https://hackerone.com/reports/361194
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-02T21:35:04.040Z
- **Disclosed**: 2018-06-03T10:20:31.937Z

## Reporter
- **Username**: khizer47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hi,

So i saw a strange behaviour of your web on signup feature when that can be escalated to Account Takeover but for limited timeline, 

#Issue:
When a New user signup for an account on https://en.liberapay.com/ he have to enter his email address only and it doesn't say anything about sending a confirmation/verification email to the user. and thus user gets login to his account, and also as there is an option for user to chose not to use a password for his account user account can be compromised 

#POC:
1) Go to https://en.liberapay.com/sign-in?back_to=/
2) in "Create Your account" Field add your email address 
3) You will be logged into your account
4) You will also receive a Verification email ( But no need to open it or use that link ) 
5) Now if you go again to https://en.liberapay.com/sign-in?back_to=/ and in login field enter your email ( No password needed as your account don't have a Password yet ) 
6) after you press login you will see a message saying 
`We've sent you a single-use login link. Check your inbox, open the provided link in a new tab, then come back to this page and click on the button below to carry on with what you wanted to do.`
7) Now this means that you will have to get the URL send to the email but this can be bypassed
8) go to https://en.liberapay.com/sign-up and enter the email Address of that account 
9) You will see that you will be in that account 

#Fix Maybe: 
This can be fixed by not letting user login without Verification 
and also make sure again the same email can't be used 

#NOTE:
this will not work with verified accounts 
also if someone signup for your email after you did for 1st time he will get access to your account but if he tried 2nd time he will get an error saying `A verification email has already been sent to test@gmail.com recently.` But this can be bypassed by waiting for like 2-3 hours i have tried  like 3 times and if a user is verified the error will be like `test1@gmail.com is already connected to a different Liberapay account.`

#Video POC:

https://www.youtube.com/watch?v=P-76XHx-GkE&feature=youtu.be

## Impact

unauthorized person can get access to user account by knowing their email if user account is not verified and have no password set by using signup feature

## Attachments
No attachments
