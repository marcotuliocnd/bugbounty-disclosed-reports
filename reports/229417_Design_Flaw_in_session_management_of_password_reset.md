# Design Flaw in session management of password reset 

## Report Details
- **Report ID**: 229417
- **URL**: https://hackerone.com/reports/229417
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-17T20:50:48.187Z
- **Disclosed**: 2017-06-02T11:00:00.435Z

## Reporter
- **Username**: asaxena2190
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi team,

I found that there is some design flaw in the website in Password reset functionality.

This report is basically combination of two reports ( #223329 & #223339) those are already resolved but i bypass the fixes provided for.

Issue 1: Bypass the Logout CSRF fix.

**Steps to reproduce/POC:**

1. Login with user A.
2. Request for password reset token from user B.
3. Use this reset password link on the same browser where user A is already logged in.
4. User A will be logged out.

**Scenario for Logout CSRF:**
1. Victim is already logged in his account.
2. Attacker request the password reset token on his account.
3. Attacker will send the password reset link encapsulated in other link to victim.
4. Victim will click on the link and will get logged out.

**Impact:**
1. In general there are very less imppact of logout CSRF but using the bypass method explained by me impacting the whole account of the user.
2. If an attacker gets successful to do logout the Victim. Victim will never log in with his/her current password. He have to change the password unintentionally. 

**Issue 2:** User is getting logged in just by clicking on the reset password token or link as described in the report #223339. It is marked resolved.

As you are well aware the above Issue : 2, so i am not explaining but i will explain the impact of the combination of the both issues.

#Combination of both Issues (Scenario):

1. Attacker will generate the two password reset token back to back.
2. Attacker will not use the tokens.
3. He will encapsulate the password reset link in a html file with some javascript. 
4. Attacker will upload the the above script on the serer which will execute the both password reset token one by one with the sleep of 3 or 4 seconds.
5. So when first password reset token will be executed on the victim's browser he will get logged out from his account.
6. and when second password reset token will be executed on the victim's browser he will be automatically logged in the attacker's account.
7. So attacker will easily do logout the victim from his account and logged in his account for his malicious purpose.
8. As weblate is project and development based site. Attacker could be interested in the code written by victim or his idea of project, So attacker can use the above attack to login victim to his account and victim will do the changes unknowingly in the attacker's account as victim is considering that account his account.

Please look into this.

Thanks,
Akash Saxena.


## Attachments
No attachments
