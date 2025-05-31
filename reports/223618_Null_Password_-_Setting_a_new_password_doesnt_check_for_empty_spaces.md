# Null Password - Setting a new password doesn't check for empty spaces

## Report Details
- **Report ID**: 223618
- **URL**: https://hackerone.com/reports/223618
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-25T00:25:42.408Z
- **Disclosed**: 2017-05-18T07:58:33.022Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi Again!

As seen your website at https://demo.weblate.org/accounts/password/
>Your password can't be too similar to your other personal information.
>Your password must contain at least 6 characters.
>Your password can't be a commonly used password.
>Your password can't be entirely numeric.

I found that it is possible to create a password with `empty spaces`, not useful anyway but renders the password security weak.

##Reproduction Steps
- Create a new account
- Load the link sent to your mail
- Now, set password to six spaces (tapping the space bar 6 times)
- You'll get a success message

##Screenshots
Here are screenshots confirming the vulnerability
{F179097}
{F179097}

Regards,
Shuaib

## Attachments
- Weblate_req.png
- Weblate_res.png
