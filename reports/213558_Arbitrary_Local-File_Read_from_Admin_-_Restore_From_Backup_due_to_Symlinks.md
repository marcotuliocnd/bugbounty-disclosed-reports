# Arbitrary Local-File Read from Admin - Restore From Backup due to Symlinks

## Report Details
- **Report ID**: 213558
- **URL**: https://hackerone.com/reports/213558
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-03-15T02:26:12.640Z
- **Disclosed**: 2017-05-13T21:25:53.261Z

## Reporter
- **Username**: ziot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: discourse

## Vulnerability Information
As an Admin user on Discourse there is a feature to create, upload, and restore backups. Generating a backup creates a tar file consisting of the database as a SQL file and uploaded files from /public/upload/*. Having the ability to upload these tar files and restore from them, you can add any file that you wish. 

Manually modifying the tar archive and adding a symlink, you are able to read any arbitrary file that the user has permission to including files outside of the Discourse application directory.

## Steps

1. Load http://try.discourse.org
2. Login as an Admin user.
3. Go to the Backups page:
 * http://try.discourse.org/admin/backups/
4. Create a new backup including files.
5. Extract the backup files to a folder on your server.
6. Create a symlink to `/etc/passwd` In the /uploads/ folder of the backup, e.g. `/uploads/default/original/1X/[file].jpg`.
 * example: `ln -s /etc/passwd /home/symlink/files/uploads/default/original/1X/7ad2e8f5fe02890f20503044b604e29e6f3718fd.png`
7. Create a .tar.gz from the extracted files.
8. Upload the newly crafted tar to the server.
9. Enable `Restore from Backups` in settings if it's not enabled.
10. Restore from the backup that uploaded.
11. Go to the uploaded file in your browser after it uploads, e.g.
 * http://try.discourse.org/uploads/default/original/1X/[file].jpg
12. ---> You were able to read file contents of `/etc/passwd` due to the symlink being extracted from the tar.



## Attachments
- symlink.png
