# Information can be changed without a password

## Report Details
- **Report ID**: 721341
- **URL**: https://hackerone.com/reports/721341
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-10-23T20:11:46.579Z
- **Disclosed**: 2020-03-14T01:41:03.427Z

## Reporter
- **Username**: jamesconnor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
If a user has access to a logged in session on Khan Academy, they are able to conduct a full account takeover. This is due to the fact that a new email address can be added to an account without a method of re-authentication. Once this email address has been added, the attacker can simply logout and follow the "Forgot Password" dialogue on the login page to send a password reset email to the email address they added. This allows them to change the password and completely take over the account. While this could arguably be the user's fault for not logging out, Khan Academy specifically targets an audience of students and educators, many of whom may use their accounts on shared computers in school. As a result, it's necessary to require re-authentication before allowing modifications to certain user settings, such as the account's email addresses.

**Steps to reproduce**

1. Open a browser in which a user has previously logged into an account, but hasn't logged out.
2. Go to https://www.khanacademy.com/settings (the user settings)
3. Scroll down to "Connect an email", click the button, and type in any email address that you control. This simulates the attacker's email address. Finally, click "Send a Confirmation Email". 
4. Open the attacker's inbox and follow the instructions to reset the password. Change the password to whatever you want.
5. Click "Reset and Log In". The account has now been successfully taken over.

## Impact

An attacker can take over an account and lock a user out by resetting the password.

## Attachments
- User_settings.png
- Connect_an_email.PNG
- Link_confirmation.PNG
- Confirm_email.PNG
- Success.PNG
- Forgot_password.PNG
- Reset_password_email.PNG
