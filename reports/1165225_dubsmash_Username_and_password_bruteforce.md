# [dubsmash] Username and password bruteforce

## Report Details
- **Report ID**: 1165225
- **URL**: https://hackerone.com/reports/1165225
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-14T20:04:50.410Z
- **Disclosed**: 2021-12-13T22:48:54.994Z

## Reporter
- **Username**: asce21
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Due to less complexity of password and no rate limiting attacker can bruteforce user name and password and takeover the victim account

Login Page- No rate limits
Password length is minimum five character with no variations. Plain  password are easy to bruteforce 
Reset Password page- No rate limits

Attacker can send as many request with no restrictions

## Impact:
Account takeover

## Steps To Reproduce:


  1. To get the username attacker bruteforce through reset password page with selecting email parameter
 2. It shows 200 status for every request but 

for valid user it respond with {status :true}

{"data":{"resetPassword":{"status":true,"__typename":"ResetPasswordOutput"}}}

For invalid user

{"data":{"resetPassword":{"status":false,"__typename":"ResetPasswordOutput"}}}

 3.Login with victim email and any password.
4.Intercept request with burp and send to intruder with selecting password parameter
6.Load the desired password list and start attack
7.It shows status 200 for every request but for valid password it gives jwt token in response
  

## Supporting Material/References:

f_user.jpg: Username is invalid
r_user.jpg: Right username is found.
r_pass.jpg: Valid password is found.

  * [attachment / reference]

## Impact

Account take over even if the user password is  long but not complex.

## Attachments
No attachments
