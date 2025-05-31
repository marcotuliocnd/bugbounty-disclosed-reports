# A user with only [MODIFY_SETTINGS] permmision could takeover any user accounts

## Report Details
- **Report ID**: 2279010
- **URL**: https://hackerone.com/reports/2279010
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-12-09T05:30:55.990Z
- **Disclosed**: 2024-05-20T09:06:47.723Z

## Reporter
- **Username**: osama-hamad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
a user with modify_settings permission only is not allowed to view team, edit users or groups or manage extensions which allows code execution. 
{F2912067}

however, modifying settings allows to configure email settings therefore, the attacker could submit a public SMTP that can view its logs, and whenever an administrator or a user with a permssion to edit or add user ask a reset password for a user or add a user via its account , the attacker will capture the added / existed edited user email and password reset link. 

### Proof of Concept

- Create a user with Modify settings permission only. 
- Login into the account you created. 
- Navigate to email from settings , change SMTP information to a public one , you can create a free smtp from here 
https://elasticemail.com/
- Set up the info from your account and save it. 
{F2912082}
- Login to an administrator account and to users , press reset password for any user and observe logs in https://elasticemail.com/ dashboard. 
You will get that user : username , email and password reset link .

{F2912084}
{F2912085}

it will be similar case in case of an administrator in the dashboard or someone with similar role try to add a user + attacker could read any message for any action that sends email from enterprise burp dashboard.

## Impact

any user with modify_settings permission is able to takeover other users account ( needs interaction either by reset password or user addition functionalities )

## Attachments
- image.png
- image.png
- image.png
- image.png
