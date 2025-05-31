# Add me email address Authentication bypass

## Report Details
- **Report ID**: 1607645
- **URL**: https://hackerone.com/reports/1607645
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-06-20T14:37:18.046Z
- **Disclosed**: 2022-07-15T16:33:19.782Z

## Reporter
- **Username**: raajeevrathnam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
hi, this vulnerability can able to access user account without email verification in linkedins' add me email address function page. user add mail2 email address. without mail2 email address verification user can fully access mail1 linkedin account using mail2 email address. 

In linkedin mobile application, we can add second email address, and its display "We can't use this email for your account until you verify it." so, it'll play authentication logic error.

TO REPRODUCE :
1. have account mail1 & mail2.
2. login to mail1 linkedin account.
3. go to https://www.linkedin.com/psettings/email , add mail2 email address.
4. then remove mail2 email address.
5. linkedin sent verification link to mail2s' gmail.
6. copy this link, open private tab and paste it.
7. click signin button and type  mail1s' password.
8. will login successfully.

ATTACHED Detailed Reproduce Video below

## Impact

User/attacker can login successfully without email verification and also, authentication logic error happened. login using unverified email address, can't notify login successful message in the primary email address. email2 login n-no. of time without verification, and also can't notify login message to mail1(primary email) gmail account.

## Attachments
No attachments
