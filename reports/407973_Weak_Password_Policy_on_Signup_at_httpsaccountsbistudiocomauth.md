# Weak Password Policy on Signup at https://accounts.bistudio.com/auth

## Report Details
- **Report ID**: 407973
- **URL**: https://hackerone.com/reports/407973
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-09-10T16:28:06.402Z
- **Disclosed**: 2018-09-18T14:10:18.024Z

## Reporter
- **Username**: hack2684
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bohemia

## Vulnerability Information
Hi,
I found that you are using a weak password policy! Because user can set his password same as Email address!

Steps To reproduce:

1. Register an account with Email address "xyz@gmail.com"
2. Also password "xyz@gmail.com". 

You can see both values are same. You will become successfully register with these information which can easily guessable by anyone. Kindly restrict user that password should be same as Email address!

Thanks,

## Impact

Password should not match with Email address because if password is same as Email address then account can be compromise easily!

## Attachments
No attachments
