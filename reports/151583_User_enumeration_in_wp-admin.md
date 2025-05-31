# User enumeration in wp-admin

## Report Details
- **Report ID**: 151583
- **URL**: https://hackerone.com/reports/151583
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-15T19:45:32.488Z
- **Disclosed**: 2016-07-16T09:21:08.425Z

## Reporter
- **Username**: hacklikeapro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hi, I have found that in the page  wp-admin possible to perform user enumeration though differences in error massages:
if user exist the site will return :" ERROR: The password you entered for the username admin is incorrect."
if user not exit: Invalid username.


## Attachments
- userExist.png
- userNotExist.jpg
