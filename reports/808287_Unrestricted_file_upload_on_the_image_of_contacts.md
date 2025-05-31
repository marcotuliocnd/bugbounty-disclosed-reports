# Unrestricted file upload on the image of contacts

## Report Details
- **Report ID**: 808287
- **URL**: https://hackerone.com/reports/808287
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-01T23:44:39.282Z
- **Disclosed**: 2020-07-08T15:15:35.627Z

## Reporter
- **Username**: hitman_47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
When uploading an image for a contact, on the file upload pop up window it shows that it can accept all files of any data type. For my testing I uploaded a sample executable, named 'SimpleCrackMe.exe' which doesn't do really do anything without passing parameters to it on a terminal when running it. The file was uploaded successfully.

## Impact

An attacker could upload a dangerous executable file like a virus, malware, etc.. If you don't think this is a vulnerability, please let me close the report myself so that I don't lose points

## Attachments
No attachments
