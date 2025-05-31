# Forgot password link doesn't expire after used, only after some hours

## Report Details
- **Report ID**: 244642
- **URL**: https://hackerone.com/reports/244642
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-30T05:32:22.026Z
- **Disclosed**: 2017-07-03T06:42:58.087Z

## Reporter
- **Username**: mohammad_obaid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi, Hope you guys are doing great. I want to report couple of issues regarding forgot password mechanism. 
##1st ISSUE:
One thing I noticed that when password rest link is requested and user change its password, that reset link should expire immediately but in your case , used reset link can be reused again and again. This will cause an attacker to take over victim account if he somehow gain victim email account access and found password reset token in emails.
##POC:
1- Go to https://wakatime.com/reset_password
2- Enter your email address and you will get one password reset token in your email.
3- Now change password using that link and you will be successfully log in from your new password.
4- Now log out and change password again using reset token which is sent in step2.
5- You will see your password will again changed.

##2nd ISSUE:
Second issue I want to report is that when multiple token is requested , previous one should be expired immediately which in your case is not.
This will cause an attacker to take over victim account if he somehow gain victim email account access and found unused password reset token in emails.

##POC:
1- Go to https://wakatime.com/reset_password
2- Enter your email address and you will get one password reset token in your email. Call this token1.
3- No repeat step 1 and 2 and you will get another rest token. Call this token2
3- Now change password using token2 and you will be successfully log in from your new password.
4- Now log out and change password again using  token1 which is sent in step2.
5- You will see your password will again changed.

##POSSIBLE FIX:
All used password reset link should be expired immediately.
All unused password reset token should be expired immediately with the issue of new token .



## Attachments
No attachments
