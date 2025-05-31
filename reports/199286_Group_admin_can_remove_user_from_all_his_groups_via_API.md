# Group admin can remove user from all his groups via API

## Report Details
- **Report ID**: 199286
- **URL**: https://hackerone.com/reports/199286
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-01-18T08:30:23.166Z
- **Disclosed**: 2017-02-23T12:23:06.457Z

## Reporter
- **Username**: nickvergessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
### Steps
1. As admin make user1 group admin for group1 and group2
2. As user1 create a new user user2
3. As user1 try to remove the user from both groups via the UI
4. Take the first `togglegroup.php` request and replay it with `group2` on curl

### Expected
Should not work

### Actual
The group-admin can escape his groups and create users that are not part of his groups.

Also possible via the provisioning_api.

Either the restriction should be enforced on the api endpoints (not only in the UI), or the restriction in the UI should be removed.


## Attachments
No attachments
