# UI flaw allows unauthorized users to add documents to restricted folders

## Report Details
- **Report ID**: 3101986
- **URL**: https://hackerone.com/reports/3101986
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-04-20T22:18:35.268Z
- **Disclosed**: 2025-04-23T19:26:44.276Z

## Reporter
- **Username**: qatada
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dust

## Vulnerability Information
hey team
A UI issue allows a user to upload or add documents to a folder they should not have access to. This bypasses intended permissions and could lead to unauthorized access or data integrity issues.

steps to reproduce: 
1- login in account a which is the admin, add any document to the folder
2-login as account b which is member and go to the same folder then click on add multiple documents and choose any document
3-the document will be uploaded successfully, the button of adding looks disabled but it works fine, the member is not supposed to do this function

█████████

## Impact

This issue constitutes an Insecure Direct Object Reference (IDOR) vulnerability. Although the UI is intended to restrict access, users can manipulate the client-side behavior to perform unauthorized actions — in this case, uploading documents to folders they shouldn't have access to. This breaks access control at the object level and could allow:

Unauthorized insertion of documents into restricted folders

## Attachments
No attachments
