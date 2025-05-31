# Administrator can create user without entering high security mode

## Report Details
- **Report ID**: 351361
- **URL**: https://hackerone.com/reports/351361
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-05-14T09:56:08.683Z
- **Disclosed**: 2018-05-22T09:27:26.906Z

## Reporter
- **Username**: ivh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
When an administrator wants to create a user, he can go to https://phabricator.example.com/people/create/ and will be required to enter his MFA token in order to enter high security mode.

However, if an administrator goes to https://phabricator.example.com/people/new/standard/ he will bypass the choice of user type and go straight to the new standard user form. This form allows the administrator to create a new user without entering high security mode.

mongoose

## Impact

The attacker could create a user account for someone that is not supposed to have access to Phabricator, or for himself in order to keep his access to Phabricator after losing access to the (compromised) administrator account.

## Attachments
No attachments
