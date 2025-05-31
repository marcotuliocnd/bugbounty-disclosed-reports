# Takeover of an account via reset password options after removing the account

## Report Details
- **Report ID**: 230076
- **URL**: https://hackerone.com/reports/230076
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-20T06:53:22.466Z
- **Disclosed**: 2017-06-13T15:41:17.436Z

## Reporter
- **Username**: imran_hadid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi, 

The Reset password mechanism can't validate or authenticate an user properly. After removing a user account it's possible to takeover the user account by using reset password option. which is turn into takeover an account. 

##Step to Reproduce: 

1. Go to [weblate](https://demo.weblate.org)
2. Remove your account from [weblate](https://demo.weblate.org)
3. Now go to for [login](https://demo.weblate.org/accounts/login/)
4. Enter username or email and password, try to login. you are failed to login because email and password is removed
5. Now click on [reset it](https://demo.weblate.org/accounts/reset/)
6. Enter email and captcha and hit `Reset my password`
{F186309}
7. Open mail and click on reset password link 
{F186311}
8. Now enter Password twice and login to the account 

After doing all the steps you are successfully able to change the password.
{F186313}

Thanks 


## Attachments
- account_takeover_1.PNG
- account_takeover_2.PNG
- account_takeover_3.PNG
- account_takeover_4.PNG
- account_takeover_5.PNG
