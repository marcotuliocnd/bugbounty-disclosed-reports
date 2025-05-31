# Any authenticated user can download full list of users, including email

## Report Details
- **Report ID**: 228399
- **URL**: https://hackerone.com/reports/228399
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-15T01:08:49.796Z
- **Disclosed**: 2017-06-17T03:51:44.105Z

## Reporter
- **Username**: arkadiyt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: discourse

## Vulnerability Information
The `ExportCsvController` allows users to export different types of entities, if one has guardian access:
https://github.com/discourse/discourse/blob/master/app/controllers/export_csv_controller.rb#L6

However, the guardian check only checks that the entity type is not "admin":
https://github.com/discourse/discourse/blob/master/lib/guardian.rb#L296

But the entity type "admin" does not exist anyway, so the check boils down to whether or not a user has made an export on that day. This means that once a day a user can export any of the entity types in the `ExportCsvFile` job:
https://github.com/discourse/discourse/blob/master/app/jobs/regular/export_csv_file.rb

Including:
A full user list export (names, email addresses, admin status, etc)
Staff actions
etc

As a proof of concept I was able to download a full list of users on https://try.discourse.org

## Attachments
- Screen_Shot_2017-05-14_at_6.04.04_PM.png
- Screen_Shot_2017-05-14_at_6.06.00_PM.png
