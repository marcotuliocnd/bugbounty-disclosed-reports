# No password length restriction in reset password endpoint at http://suppliers.mtn.cm

## Report Details
- **Report ID**: 1285694
- **URL**: https://hackerone.com/reports/1285694
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-07-31T21:13:32.807Z
- **Disclosed**: 2022-09-05T23:00:44.261Z

## Reporter
- **Username**: aliyugombe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hello

## Summary:
I found no password length restriction in reset password endpoint at http://suppliers.mtn.cm when resetting new password

## Steps To Reproduce:
1. Visit https://suppliers.mtn.cm/ and register.
2. logout and reset your password
3. go to your email and click on reset password link
4. enter 150 characters as a password and confirm the characters
5. you will successfully logged in.

## Impact

Attacker can do denial of service to your server since there is no restriction in the length of password.
Example when he enter like 2500 character, your server will crash for some time,

I did not attempt to ddos your server,  because you exclude any activity related to denial of service to your assets, I only test for 150 character and its working.

##Mitigation :
Restrict user to use less than 40 character as a password, while the restriction should be both on back-end and front-end (with javascript ).

##Thank you

## Attachments
No attachments
