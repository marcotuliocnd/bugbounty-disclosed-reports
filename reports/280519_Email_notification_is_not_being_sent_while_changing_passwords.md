# Email notification is not being sent while changing passwords

## Report Details
- **Report ID**: 280519
- **URL**: https://hackerone.com/reports/280519
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-19T14:35:56.082Z
- **Disclosed**: 2018-01-29T14:25:10.935Z

## Reporter
- **Username**: saikiran-10099
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Vulnerabilities:-
1.Use of old passwords is possible(current password can be used as new password).
2.Email notification is not being sent to linked mail account while changing passwords.

Impact:-

Case-1:-
->whenever a user requests a reset token for recovery of his account,a reset token is being to his linked mail account.so,he can set a new password in next step.
->but,here the bug is that infogram is again accepting the current password(that is,forgotten password by the user).
->the problem is that,today attackers are accessing particular user account by knowing his other account passwords in other sites and also by knowing the old passwords used by him.
->so,allowing users to set old password is some what a typical issue.

Case-3:-
-> If an attacker reset the password of user account by any other method(e.g. by using password reset token hijacking method or by accessing user gmail account),then the email(e.g. your password has been reset) is not being sent to user mail id.
->So,finally by using other method if an attacker hijacks/access the password reset token/user gmail account and reset the password,in that case missing of this protection will also leads to privilege escalation of the attacker.

Necessity for implementing this security practice:-
->for security purpose,if these emails are been sent to user,then it will help user to know immediately that his account is in danger.so,that an immediate remediation step can be taken by the user to protect his account.

NOTE:-
->I think in general 90% of all sites with users definitely have this protection implemented for the sake of users,because the main aim is that users should not be fall into trouble.

Conclusion:-
->Finally,do not implementing mail server configuration is leading to these many issues and also failing to implement this practice in turn leads to further impact.
->At the end,atleast users should have one chance to take remedy step immediately if their accounts are hacked.

->I hope that you will consider this report and resolve it.And also i am ready to give any more info if you want regarding this issue.

Thank you

## Attachments
No attachments
