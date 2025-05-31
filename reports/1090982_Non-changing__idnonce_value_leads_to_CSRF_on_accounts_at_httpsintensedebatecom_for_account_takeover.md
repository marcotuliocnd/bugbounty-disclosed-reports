# Non-changing "_idnonce" value leads to CSRF on accounts at https://intensedebate.com for account takeover

## Report Details
- **Report ID**: 1090982
- **URL**: https://hackerone.com/reports/1090982
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-30T21:00:39.248Z
- **Disclosed**: 2021-02-17T09:35:50.873Z

## Reporter
- **Username**: hackxsd_rootx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
The "_idnonce" value on https://intensedebate.com protects victims from CSRF attacks. However, this value is not changing with changed user ids of same account (_idnonce value is same in request from user id 'X' and user id 'Y' when 'X' is changed to 'Y'). It leads to CSRF on victim's account (prospective user who is going to signup on https://intensedebate.com for legitimate account). I demonstrate that account takeover is possible due to this vulnerability of knowing the secret token i.e. "_idnonce" value.

An attacker will create account with own email address. Considering that he's targeting account takeover, the attacker will note the value of "_idnonce" while making the request to change email to the victim's email (prospective user who is going to signup on https://intensedebate.com for legitimate account).

When the victim tries to signup on https://intensedebate.com, he's denied by the system since the email already exists. The victim obtains the password reset link on his email to change the password, verifies his email id, and operates the account. Both email id and password have been changed, however, any new request of changing email id will have the same "_idnonce" value. It will be exploited by the attacker for CSRF to change victim's email id to attacker's email id.

## Platform(s) Affected:
User accounts at https://intensedebate.com

## Steps To Reproduce:

  1. Sign up on https://intensedebate.com as attacker with own email address and verify it to operate the account.
  2. Change email id on Account section of https://intensedebate.com/edit-user-account page to the victim's email (prospective user who is going to signup on https://intensedebate.com for legitimate account). Note down the "_idnonce" value by observing the request in Burp. You are logged out from the account by application when you change email id.
  3. As a victim, try to sign up on https://intensedebate.com using different browser. The system will tell that email already exists.
  4. Since the victim can't sign up, the way to claim this account is resetting the password using Forgot Password feature. Do so as the victim and verify the account to operate it.
  5. On the same (victim's) browser, load the following HTML page as PoC of CSRF. Before loading the page, change xyz123 to the _idnonce value noted down by attacker in Step 2 and also change attacker@email.com to the attacker's email id. [Keep the double quotes in both values].

<html><form enctype="application/x-www-form-urlencoded" method="POST" action="https://intensedebate.com/edit-user-account"><table><tr><td>_idnonce</td><td><input type="text" value="xyz123" name="_idnonce"></td></tr>
<tr><td>txt_email</td><td><input type="text" value="attacker@email.com" name="txt_email"></td></tr>
<tr><td>txt_old_pass</td><td><input type="text" value="" name="txt_old_pass"></td></tr>
<tr><td>txt_new_pass</td><td><input type="text" value="" name="txt_new_pass"></td></tr>
<tr><td>txt_new_pass_repeat</td><td><input type="text" value="" name="txt_new_pass_repeat"></td></tr>
<tr><td>chk_email_reply</td><td><input type="text" value="T" name="chk_email_reply"></td></tr>
</table><input type="submit" value="https://intensedebate.com/edit-user-account"></form></html>

Both email id and password have been taken by the victim, however, the request of changing email id will work with the same "_idnonce" value. As the attacker, reset the password of target account using Forgot Password feature and verify the account to operate it i.e. account takeover.

## Impact

Non-changing "_idnonce" value leads to CSRF on accounts at https://intensedebate.com for account takeover.

## Attachments
No attachments
