# Disavowing an account doesn't disable it

## Report Details
- **Report ID**: 1165015
- **URL**: https://hackerone.com/reports/1165015
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-14T14:03:39.469Z
- **Disclosed**: 2021-05-07T07:43:28.971Z

## Reporter
- **Username**: raven_in_matrix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hello security team, while I testing your website, I found improper email verification while sign-up 
liberapay.com. 

Steps to reproduce:
1) Go to https://liberapay.com.
2) Create new account with any email.
3) You will receive  an email verification to the given email.
4) Open that email and click "No, it wasn't me". There will be a message "You have successfully disavowed having connected your email address to this Liberapay account.".
5) Now come to the liberapay.com in browser and reload the page. (It should not allow the user to continue with that account)

But you can see, there is no changes with the site and you can continue with that account.

## Impact

Attacker can create an account with anyone's email without verifying.

## Attachments
No attachments
