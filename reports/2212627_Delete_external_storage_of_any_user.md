# Delete external storage of any user

## Report Details
- **Report ID**: 2212627
- **URL**: https://hackerone.com/reports/2212627
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-10-17T00:08:29.709Z
- **Disclosed**: 2023-11-21T09:22:22.998Z

## Reporter
- **Username**: cx75fa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
A security vulnerability was uncovered that allowed standard users to remove external storage resources from any user account in the application. This flaw was particularly concerning because it enabled unauthorized users to delete these resources based on a system-generated ID, which automatically incremented, without requiring any special privileges. This issue didn't grant access to the data but allowed for the indiscriminate removal of external storage associated with user accounts, potentially leading to data loss and disruption of service for affected users.

Reproduction Steps:
1.Begin by logging in with a standard user account and establish an external storage connection.
2. Afterward, update the storage configuration. Observe that the following request is generated:
```
PUT /apps/files_external/userstorages/<storage_id> HTTP/1.1
Host: 127.0.0.1:9090
[REDACTED]

{"mountPoint":"simpleuser","backend":"owncloud","authMechanism":"password::logincredentials","backendOptions":{"host":"cq6xxrdnw1941wu9jk4gcyfuglmfa4.oastify.com","root":"","secure":true},"testOnly":true,"id":<storage_id>,"mountOptions":{"enable_sharing":true,"encoding_compatibility":false,"encrypt":true,"filesystem_check_changes":1,"previews":true,"readonly":false}}
```
3.Next, log in to the application with an administrative user account or any other role and establish a storage connection.
4.Observe that each new storage created increments the ID automatically. For instance, it could become 28.
5. Using the standard user role, issue the request once more to modify the ID linked to the administrative storage. Observe that this action leads to the removal of the storage from the administrator's account.

VIDEO POC:
{F2778950}

## Impact

This finding has a huge impact on the application, including data loss, service disruption, unauthorized actions, data privacy concerns, security risks, and potential reputation damage.

## Attachments
- delete_storage.mp4
