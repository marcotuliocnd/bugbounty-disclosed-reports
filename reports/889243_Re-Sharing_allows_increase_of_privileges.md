# Re-Sharing allows increase of privileges

## Report Details
- **Report ID**: 889243
- **URL**: https://hackerone.com/reports/889243
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-02T11:23:03.692Z
- **Disclosed**: 2020-09-28T09:19:36.857Z

## Reporter
- **Username**: alx_il
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
- User A shares a file/folder to user B with re-sharing permission, but readonly
- User B shares this file/folder to User C (Needs the shareapi_default_permissions set to 1 (all checkmarks off in admin panel))
- User B can add write permissions for the share to User C (User C may also be anonymous using a link)
- User C gets write access and can edit existing files

## Impact

User can get write permission on read-only shared files/folders.

## Attachments
No attachments
