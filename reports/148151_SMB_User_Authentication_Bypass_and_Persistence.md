# SMB User Authentication Bypass and Persistence

## Report Details
- **Report ID**: 148151
- **URL**: https://hackerone.com/reports/148151
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-29T06:53:24.816Z
- **Disclosed**: 2016-11-26T15:29:24.618Z

## Reporter
- **Username**: rhinosecuritylabs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
Authentication Bypass
==================

The external user authentication app in OwnCloud does not properly authenticate against an SMB server. In it's current implementation, the file (owncloud/apps/user_external/lib/smb.php, line 46-47) uses the command `smbclient -L //host/dummy -Uuser%pass`, where the variables `user` and `pass` are escaped for shell characters. However, default Samba SMB servers set "map to guest" to the value "bad user". This allows for the listing of shares regardless of user, but not further information. 

The image shows the command `smbclient -L //localhost/dummy -Utest%test` succeeding with an invalid user "test" using password "test", yet the user does not exist as shown by the second command `smbclient //localhost/dummy -Utest%test`.

{F102413}

When the default "map to guest" parameter is changed to "never" in the smb.conf for the SMB server, both commands fail as required.

{F102414}

To properly validate the user the command should simply be `smbclient //host -Uuser%pass`. This properly authenticates the user and returns a valid error message the the script can interpret. In it's current implementation, providing any username to the application will log you in as that user - even creating a new one if necessary.

To Replicate
------------------
1. Set up a Samba SMB server like detailed on this page:

https://help.ubuntu.com/community/How%20to%20Create%20a%20Network%20Share%20Via%20Samba%20Via%20CLI%20(Command-line%20interface/Linux%20Terminal)%20-%20Uncomplicated,%20Simple%20and%20Brief%20Way!

2. Login to the OwnCloud application and enable the external user authentication app.

3. Edit the config and add:
'user_backends' => 
  array (
    0 => 
    array (
      'class' => 'OC_User_SMB',
      'arguments' => 
      array (
        0 => 'SMBHOST',
      ),
    ),
  ),

3. If a user already exists and you have the username, you can login using any password (including the administrator account!). If user doesn't exist, it will create said user and log you in.


Untrusted Parameter Host
======================

In the same php file (owncloud/apps/user_external/lib/smb.php, line 46-47) the parameter `host` is not properly escaped. This allows for code execution every time a user logs into the application if they were able to edit the owncloud/config/config.php file. This could allow for a valid persistence mechanism within the application.

## Attachments
- Screen_Shot_2016-06-28_at_11.45.08_PM.png
- Screen_Shot_2016-06-28_at_11.46.11_PM.png
