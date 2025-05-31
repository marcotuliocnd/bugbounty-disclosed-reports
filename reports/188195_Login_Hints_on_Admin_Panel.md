# Login Hints on Admin Panel

## Report Details
- **Report ID**: 188195
- **URL**: https://hackerone.com/reports/188195
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-04T11:40:18.448Z
- **Disclosed**: 2016-12-05T10:27:00.336Z

## Reporter
- **Username**: madhur_bhargava
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi,

Hope you are doing fine.
I wanted to inform you regarding the enabling of the login hints on your wp-admin panel(https://nextcloud.com/wp-login.php).

Vulnerability: The admin panel shows very "specific" hint information if a hacker tries for a bruteforcing attack.

Steps to reproduce:
1. Navigate to: https://nextcloud.com/wp-login.php 

2. Enter username: "charlietango" 
    Enter password: "charlietango"
    A specific error message is shown stating "Invalid Username".(See attachment: xnc_user_err.png)

3. Now enter the following credentials:
    Enter username: "frank" 
    Enter password: "charlietango"
   A specific error message is shown stating "The password you entered for username frank is incorrect".   (See attachment: xnc_user_exist.png)

Why is this important:
As per step 3, Now the attacker knows that "frank" is an existing user in the system and multitude of attacks can be launched. At the very least, the attacker can spam the user's mailbox with several lost password requests. I believe this is not good and should be fixed.

Please do let me know your thoughts on this or if you need any more information.

Thank You,
Madhur 

## Attachments
- xnc_user_err.png
- xnc_user_exist.png
