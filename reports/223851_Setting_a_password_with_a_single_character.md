# Setting a password with a single character

## Report Details
- **Report ID**: 223851
- **URL**: https://hackerone.com/reports/223851
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-25T17:54:24.566Z
- **Disclosed**: 2017-05-18T07:58:16.660Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi!,

Following my previous report, #223618, I could see that you made a change to the site which https://demo.weblate.org/accounts/password/ says

>Your password can't be too similar to your other personal information.
>Your password must contain at least 6 characters.
>Your password can't be a commonly used password.
>Your password can't be entirely numeric.
>**Your password can't consist of single character or whitespace only.**

I found that it is possible to create a password with a single character

###Reproduction Steps
- Create a new account
- Load the link sent to your mail
- Now, set password to six spaces(tapping the space bar 6 times) and a letter included
- You'll get a success message.

##Screenshot
{F179412}
{F179413}

Regards,
Shuaib

## Attachments
- Weblate_req1.png
- Weblate_res1.png
