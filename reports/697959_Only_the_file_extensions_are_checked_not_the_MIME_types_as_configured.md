# Only the file extensions are checked, not the MIME types as configured

## Report Details
- **Report ID**: 697959
- **URL**: https://hackerone.com/reports/697959
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-19T16:29:18.610Z
- **Disclosed**: 2020-03-14T10:10:41.596Z

## Reporter
- **Username**: teaport
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The tool is not working as hoped. File access control speaks of MIME types that are blocked or not blocked. In fact, only the file extensions are checked. If a user renames an unauthorized file to an allowed file, he can upload and download it. The MIME type of the current file is insignificant, only the file extension is checked. 

A company administrator prohibits the upload of exe files using file access control and MIME types. One user 
copies his remote access application as a txt file to Nextcloud and downloads it in his professional environment.

A user on github has created a patch that has not yet found its way into the public repository.

## Impact

An attacker could upload malicious files that have been blocked by the administrator.

## Attachments
No attachments
