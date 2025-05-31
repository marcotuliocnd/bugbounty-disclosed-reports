# Uploading files to a folder where invited user don't have any EDIT privilege

## Report Details
- **Report ID**: 145950
- **URL**: https://hackerone.com/reports/145950
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-19T23:33:59.213Z
- **Disclosed**: 2016-07-19T13:06:41.966Z

## Reporter
- **Username**: detroitsmash
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi,

Any invited user to a shared folder with no edit privilege can create files in it through copy feature of ``Nextclod`` android app.

### Steps to reproduce it

+ Create any folder and invite a user in it without any edit privilege.
+ Now login from invited user account through android app.
+ Copy any file from your ``nextcloud`` root folder to shared folder.
+ Check nextcloud web app!! Copied file will show in shared folder

Thanks

## Attachments
No attachments
