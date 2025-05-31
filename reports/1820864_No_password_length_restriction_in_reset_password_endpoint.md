# No password length restriction in reset password endpoint

## Report Details
- **Report ID**: 1820864
- **URL**: https://hackerone.com/reports/1820864
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-01-03T08:44:39.654Z
- **Disclosed**: 2023-02-09T13:57:52.319Z

## Reporter
- **Username**: aditya404
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi, 

##Summary:
There is no password length restriction in reset password endpoint at https://efss.qloud.my/index.php/login when resetting for new password.


##Steps To Reproduce:
1. Visit https://nextcloud.com/sign-up/ and Sign up.

2. Logout and reset your password.

 3.Go to your email and click on reset password link.
4.Enter 150 characters or more as a password and confirm the characters.
5.You will successfully logged in.

## Impact

Attacker can do denial of service to your server since there is no restriction in the length of password.
Example when he enter like 2500 character, your server will crash for some time 
Below Image is the impact of entering 2500 characters.

##Mitigation :

Restrict user to use less than 40 character as a password, while the restriction should be both on back-end and front-end (with javascript ).

##THANK YOU

## Attachments
- Screenshot_2023-01-03_14_09_52.png
