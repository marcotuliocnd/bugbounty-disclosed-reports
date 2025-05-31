# Send Empty CSRF leads to log out user on [https://hosted.weblate.org/accounts/profile]

## Report Details
- **Report ID**: 1003468
- **URL**: https://hackerone.com/reports/1003468
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-10-09T13:35:36.772Z
- **Disclosed**: 2020-10-12T11:30:29.239Z

## Reporter
- **Username**: homaa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi 
There is a CSRF bug on your [Website](https://hosted.weblate.org/) leads to logout user from the dashboard.
If the user click on the attached file (CSRF.html) redirect to another page and see the following error and the user log out immediately:

{F1029146}

## Steps to reproduce:
1- Login to your account via [Login page](https://hosted.weblate.org/accounts/login/)
2- Click on CSRF.html that attached. 
After that, you will redirect to a new page an see the error, the user after clicking on this file log out from account.

You can see in the CSRF file there isn't any token, but if you place a vaid CSRF token from the source page, this attack will be successful too.

{F1029164}

If you have any questions, please let me know.

Best.

## Impact

An attacker can send the CSRF file to the victim or host it on a website. Whenever the user login in to your website click on file or link will be logged out.

## Attachments
- weblate_CSRF.png
- CSRF.html
- source.png
