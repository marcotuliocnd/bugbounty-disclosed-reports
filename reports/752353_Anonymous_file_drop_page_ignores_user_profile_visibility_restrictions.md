# Anonymous file drop page ignores user profile visibility restrictions

## Report Details
- **Report ID**: 752353
- **URL**: https://hackerone.com/reports/752353
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-12-06T00:32:20.074Z
- **Disclosed**: 2020-08-03T08:27:43.603Z

## Reporter
- **Username**: pshknst
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
User profile on Nextcloud server by url like https://<server.domain>/index.php/settings/user includes personal information: photo, name, email address. For each listed fields user can select the visibility settings: local, contacts, public. It is expected that these settings will work in all places of the Nextcloud server.

But if you use an anonymous download folder as written in documentation
https://docs.nextcloud.com/server/stable/user_manual/files/file_drop.html
then the profile visibility settings on upload page are ignored.
For example, if you specify the photo and fullname to be shown only for local or contacts Nextcloud server users, they will still be displayed on the upload page available publicly by the link.
Even in the documentation itself, the name is covered with black mask because it refers to a specific user.

This is not the behavior of the application that is expected when the settings for visibility of photo and fullname only to local users are selected. In order to not disclose this information to anonymous public users, it is better to use the profile parameter on the file upload page too: hide non-public user info; show, for example, only the name of the folder without a photo and name of owner of folder.
Disclosure of personal data can occur even without knowledge of owner of folder, because if he provided access to his folder for other registered Nextcloud users of the same server, they can next share folder for upload by share link without his participation and knowledge. No too good for enterprise uses where Nextcloud can sync user profiles with company's directory services which usually should be restricted for public access.

## Impact

Information disclosure of user profile data

## Attachments
No attachments
