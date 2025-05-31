# [Critical] Possibility to takeover any user account #2 without interaction on the https://██████████

## Report Details
- **Report ID**: 544334
- **URL**: https://hackerone.com/reports/544334
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-04-20T18:59:34.866Z
- **Disclosed**: 2019-10-04T15:16:48.305Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
Hello. This time I discovered a way to tekeover any user's account via unsafe password reset.
This time it's much easier than #1 way in the #543678 report.
When users requests the password reset, the next link is come to the email:
```
https://█████/resetpassword.aspx?ru=[user_id]&op=[token]
```
The [user_id] is numeric, always same for same emaill, and incremental for every new user.
The [token] parameter is random and used to protect the link from hijacking.
But, I discovered that Reset password endpoint accepts empty token!

So all the attacker needs, it's to initiate password reset for the victim's email, and request the
```
https://██████████/resetpassword.aspx?ru=[user_id]&op=
```
Since `[user_id]` is numeric and static for same account, it can be easily guessed by the attacker.

##POC
1) Go to the https://█████/ForgotPassword.aspx
2) Initiate reset password for the `██████` (it's my test account)
3) Use this link:
```
https://███/resetpassword.aspx?ru=7655&op=
```
where 7655 - it's my user numeric ID (as we know, it's incremental, and be easily guessed for other accounts).
██████████
4) Set the new password and confirm it. You can set something as `111111111aA!!!!` to pass the password requirements.
5) You will be logged into my organization as admin.

##Suggested fix
Fix the `op` tooken validation - it should be checked properly.

## Impact

Severity: Critical
Immediate account Individual/Cprporate account takeover via password reset. Attacker needs to know only email.

## Attachments
No attachments
