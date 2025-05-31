#  Application allowing old password to be set as new password | hosted.weblate.org

## Report Details
- **Report ID**: 264934
- **URL**: https://hackerone.com/reports/264934
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-31T09:46:56.320Z
- **Disclosed**: 2017-10-05T14:22:17.624Z

## Reporter
- **Username**: sadhu16
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi Team,

I found an issue that your application is allowing user to set new password same as that of the old password.

Steps to reproduce the defect

-Firstly logged into the application with existing password (refer screenshot named : Original Password login Request)-Old password highlighted in screenshot

-secondly now go to change password link and tried to set the new password with same value set in old password (refer screenshot named : Change Password Request Old and new password are same )

-thirdly now as a result of the above step you can see the new password same as old password (refer screenshot named : Change Password Request and Response- Old and new password are same)


Issue Description

As per secure password policy application should not allow same old password value to be used in setting new password value cos there might be possibility that old password might be exposed or leaked to an adversary so its advisable on application end to enforce strong password policy and should implement check to not to allow user to set old password value in new password value.

See the attached screenshots for issue details.

Please also refer the below mentioned link for reference:

https://www.owasp.org/index.php/Testing_for_Weak_password_policy_(OTG-AUTHN-007)

## Attachments
- Change_Password_Request_and_Response-_Old_and_new_password_are_same.png
- Change_Password_Request_Old_and_new_password_are_same.png
- Original_Password_login_Request.png
