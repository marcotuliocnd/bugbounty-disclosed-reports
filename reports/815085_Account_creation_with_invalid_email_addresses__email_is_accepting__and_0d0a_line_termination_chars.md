# Account creation with invalid email addresses / email is accepting % and %0d%0a line termination chars

## Report Details
- **Report ID**: 815085
- **URL**: https://hackerone.com/reports/815085
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-09T13:56:00.538Z
- **Disclosed**: 2024-02-04T16:58:28.007Z

## Reporter
- **Username**: resett3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hackerone SignUp feature is misconfigured with email parameter. Email address parameter is accepting % and %0d%0a character along with genuine email address. Using this technique hackerone user account can be created but cannot be verified as there is not possible to verify those invalid email accounts. Basically random use of invalid email address, attacker can create multiple accounts.

**Description:**
As email address field always being verified with any special character (except @ and .) but here email is accepting % and line termination char %0d%0a

### Steps To Reproduce

1. SignUp with new hacker account 
2. Use email address adding with character like % or %0d%0a, account will be created and you will get a account creation message
████ ███████
{F742080}
3. Even if you try now to login using same above email and password then you will get same message for account is already created and need to verify email
█████
4. You can not use the same invalid email again, as it will show an error of reuse of that invalid email address

## Impact

>>Garbage value can be stored in database using user account signup form
>>Multiple account can be created, just like if any use has real account with his email address, then also account can be created by adding %0d%0a or % char
>>Account is created using invalid email address, but can not be used

## Attachments
- email_verification_message.png
