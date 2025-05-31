# Read-only administrator can change agent update settings

## Report Details
- **Report ID**: 1538004
- **URL**: https://hackerone.com/reports/1538004
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-11T20:34:31.027Z
- **Disclosed**: 2022-08-10T09:38:40.191Z

## Reporter
- **Username**: mega7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hello Gents,
+ While testing `eu2-cloud.acronis.com` I found that read-only administrators are able to update agents just by editing the HTML!

### Steps to reproduce:
1. Please login at https://eu2-cloud.acronis.com/mc/
2. From Users, invite a new user with Read-only administrator role.
3. From Read-only administrator account navigate to "Agents Update" https://eu2-cloud.acronis.com/mc/app;group_id=*******/settings/agents-update
4. Inspect element -> search for `readonly`.
5. Change the value from `readonly="true"` to `readonly="false"`.
6. Edit, update and save.
7. Now open the "Agents Update" page from the company administrator account, you will be able to see the changes!

### Proof of concept:
+ {F1688988}

## Impact

Read-only administrator is able to edit and "Agents Update"

## Attachments
- simplescreenrecorder-2022-04-09_22.17.41.mp4
