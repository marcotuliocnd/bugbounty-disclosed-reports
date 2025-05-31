# Password reset tokens sent to CSP reporting endpoints

## Report Details
- **Report ID**: 1626281
- **URL**: https://hackerone.com/reports/1626281
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-07-05T14:20:34.320Z
- **Disclosed**: 2022-08-31T23:53:18.606Z

## Reporter
- **Username**: mahfujwhh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Description:
It has been identified that the application is leaking referrer token to third party sites. In this case it was found that the password reset token is being leaked to third party sites which is a issue knowing the fact that it can allow any malicious users to use the token and reset the passwords of the victim.

Steps To Reproduce:-
1) Request a password reset link for a valid account
2) Click on the reset link
3) Before resetting the password, go burp suite and search the Reset token
4) Now, you see in the third party site leakage reset token.

Similler resource Bug :
https://hackerone.com/reports/272379
https://hackerone.com/reports/1177287

## Impact

Password reset token leak on third party website.

Thanks

## Attachments
No attachments
