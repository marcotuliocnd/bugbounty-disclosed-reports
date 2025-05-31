# Group admins can remove arbitrary data from "data" directory (including admin data)

## Report Details
- **Report ID**: 508493
- **URL**: https://hackerone.com/reports/508493
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-12T15:48:46.756Z
- **Disclosed**: 2019-08-12T15:15:22.336Z

## Reporter
- **Username**: leonklingele
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Steps to reproduce:

1. Create a new user and make him an admin of an arbitrary group
2. Log in as this new user
3. Create a new user "files_external", "appdata_{random-data}", ..
4. Delete this user

Result: The data/files_external / data/appdata{..} folder is removed.

Solution: Prevent creation of users if data/{new-user-uid} is either
a file or a folder. In addition, prevent deletion of users where the
user data directory (data/{user}) contains other files and folders
than "files" (where the user data is stored).

## Impact

Group admin can remove arbitrary data from "data" directory

## Attachments
No attachments
