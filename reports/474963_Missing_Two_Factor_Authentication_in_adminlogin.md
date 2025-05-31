# Missing Two Factor Authentication in /admin/login

## Report Details
- **Report ID**: 474963
- **URL**: https://hackerone.com/reports/474963
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-01-05T09:04:11.284Z
- **Disclosed**: 2019-01-07T12:50:52.913Z

## Reporter
- **Username**: notexist
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cfptime

## Vulnerability Information
Hello Team,
>First of all this report is just mainly concern for `Suggested security improvements` based on your policy page.
>If and only if not mean possible, please do let me know. Thanks!

#### INTRODUCTION
Administrative panel is one of the main entry point for the website owner to manage their web apps from outside, making it expose not only to website owner but to public as well.

#### DESCRIPTION
It have found out that `https://www.cfptime.org/` has an endpoint of `admin/login`  which was a written django web application python framework (i should say based on the login page UI). 

Though the web application looks okay, i do suggests that you'll need to setup an additional Two Factor Authentication on the login page to ensure that only the website owner can access the site internally and nothing else.

#### RECOMMENDATIONS

>###Things To Look For
> - Suggested security improvements

I highly recommend to install 2FA from the following modules in python `django-otp`,`qrcode` which uses otp token for verification since csrf token are mean to use only on public, while otp can only be received by the website owner itself only.

#### REFERENCES
Finally the references i used for this report, you might consider checking this also for even more ways to fortify your web application.
https://hackernoon.com/5-ways-to-make-django-admin-safer-eb7753698ac8

## Impact

Prone to password guessing attacks/brute force attacks.

## Attachments
No attachments
