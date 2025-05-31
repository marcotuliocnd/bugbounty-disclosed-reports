# Login CSRF : Login Authentication Flaw

## Report Details
- **Report ID**: 229528
- **URL**: https://hackerone.com/reports/229528
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-18T06:50:42.729Z
- **Disclosed**: 2017-06-02T09:51:04.678Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi Team,

Domain: `demo.weblate.org`

In this bug, i have found a way to login any person to the attackers account, therefor when any user login to attackers account, the attacker can see the victims activity inside attackers account such as sensitive information. The issue relies on __registration confirmation together with the password reset__.

### Steps to reproduce:

  1. Attacker create account
  2. Account confirmation will send to the attackers email 
  3. Attackers will send the confirmation link to the victim
  4. Victim clicks the link and will automatically logged in to the attackers account.
  5. Done, victim will think that he/she is in his own account.

Now, how the attackers can view the information that the victim supplied to the account ? (let say the victim provided a password that the attackers do not know ? , this is where the flaw of the password reset will use, because password reset also automatically logged in the person who have the password reset link even without supplying the password.

### Attackers steps to access the fake account on where the victim was logged-in

  1. Attacker go to reset password and perform reset since attacker originated the email address of the fake account.
  2. Password reset link will sent to attackers email.
  3. Attacker will click the reset link and will automatically logged in even did not supply the password.
  4. Done. Attacker and Victim now logged in in the same account.
  5. Attacker can now see all activities of the victim including all sensitive information that the victim supplied to the account.

### Mitigation:

I have observed that the password creation was not enforced on the registration form and this will causes the issue on the 2 endpoints (registration and reset password).

__Fix: PASSWORD should be enforced to create upon registration.__

__1. Regisration Endoiunt Fix:__ Now when the password is created upon registration, the confirmation link sent to email should be redirected to the login page, then the user should input the username and password first before continue logged in to the account.

__2. Password Reset Fix:__ Now when anyone request password reset, the url link of reset password should redirect to the page that will require `current, newpass, and confirm newpass`, __BUT do not directly logged-in the account, after successfully changing the password it should also redirect to login page, then the user will input username and password before continue logged in to the account.

Let me know if you need more information.

Regards
Japz

## Attachments
No attachments
