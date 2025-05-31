# Verify any unused email address

## Report Details
- **Report ID**: 574962
- **URL**: https://hackerone.com/reports/574962
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-05-09T06:33:08.310Z
- **Disclosed**: 2019-06-24T01:58:35.031Z

## Reporter
- **Username**: seifelsallamy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** 
Verify any unused email address in twitter account

**Description:** 
After signing up on twitter it's recommended for a user to verify his/her email address to avoid spam and impersonation, I was able to verify the email without having access to the email itself.

## Steps To Reproduce:
It's a bit complex I'll write and make a video
Requirments:
1.Telerik Fiddler (setuped for using https)
2.A Twitter account that you have access to it's Email address

Steps:
1. Open Fiddler then click `file` and enable `capture traffic` then go to https://twitter.com/signup
2. Stop capturing once this URL is captured https://api.twitter.com/1.1/onboarding/task.json?flow_name=signup
3. In fiddler click on the url and in the response click raw and copy all the response then paste and save them in a new file make sure to save them in UTF-8 encoding (ansi won't work)
4. In fiddler click on Autoresponder and click "Add rule" in "rule editor" first field enter `EXACT:https://api.twitter.com/1.1/onboarding/task.json?flow_name=signup` in second field open dropdown menu and click `find a file` and select the file that you saved and click `save` and finally check 'Enable rules' then click `file` > `Capture traffic`
5. go to https://twitter.com/login then login with your twitter account
6. then go to https://twitter.com/signup enter name and `Use email instead` then enter any email address to verify then click next then click `sign up`
7. login to your email address attached to your Twitter account that you logged in with you will find that the verification code is sent to you copy it and enter it to verify the other email that you signed up with then enter a password and continue and now you got an email verified twitter account 

## Supporting Material/References:
I uploaded a video

## Impact

1) Authenticating attackers to users accounts with Twitter oauth in third parties applications
suppose that a website (www.example.com) have 2 methods for login 
- Login with email address
- Login with Twitter account (in case that the website requires user email to authenticate users)
If the user is using an email address that is not signed up on twitter, an attacker is able to signup and verify the email address then login with twitter and access all victim data in third parties applications 
2) Impersonate a user by verifying his/her email address on a twitter account and making crimes using this account.
3) spam, creating a huge amount of verified twitter accounts and spam

## Attachments
No attachments
