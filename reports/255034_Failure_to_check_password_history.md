# Failure to check password history

## Report Details
- **Report ID**: 255034
- **URL**: https://hackerone.com/reports/255034
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-30T19:19:06.917Z
- **Disclosed**: 2017-07-30T19:36:37.471Z

## Reporter
- **Username**: c0d3fire
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
I discovered that old passwords could be reused and believe that wakatime.com could benefit if there was a check for old passwords in your database.

Because password reuse is an important concern in any organization. Many users want to reuse the same password for their account over a long period of time. The longer the same password is used for a particular account, the greater the chance that an attacker will be able to determine the password through brute force attacks. If users are required to change their password, but they can reuse an old password, the effectiveness of a good password policy is greatly reduced. 

*POC*
1. Create a account in wakatime.com or use a existed one.
2. Go to settings "Change Password" where the password settings are located.
3. Change the password with your previous password
4. Password is changed to same password as before. 

*Criticality*
This impacts every user that has an account with wakatime.com. 

*Suggested fix*
- Set Enforce password history to 24. This will help mitigate vulnerabilities that are caused by password reuse.
- Set Maximum password age to 60 days. Try to expire the passwords between major business cycles to prevent work loss.
- Configure Minimum password age so that you do not allow passwords to be changed immediately.

## Attachments
No attachments
