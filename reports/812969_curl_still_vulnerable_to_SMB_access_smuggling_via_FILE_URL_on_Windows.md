# curl still vulnerable to SMB access smuggling via FILE URL on Windows

## Report Details
- **Report ID**: 812969
- **URL**: https://hackerone.com/reports/812969
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-03-08T01:06:41.661Z
- **Disclosed**: 2021-01-08T14:16:03.527Z

## Reporter
- **Username**: tsedlmeyer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
The released fix for CVE-2019-15601, SMB access smuggling via FILE URL on Windows, leaves curl still vulnerable to SMB access smuggling via FILE URLs.
 - FILE URLs formatted as `file:////smb_server/smb_share/file` are not filtered.
 - FILE URLs which point to the global DOS name space, \??\, and formatted as `file:///%3f%3f/UNC/smb_server/smb_share/file_name` or `file:///%3f%3f/GLOBAL/UNC/smb_server/smb_share/file` are not filtered.

## Steps To Reproduce:

  1. `curl file:////localhost/c$/windows/win.ini`
  2. `curl file:///%3f%3f/UNC/localhost/c$/windows/win.ini`
  3. `curl file:///%3f%3f/GLOBAL/UNC/localhost/c$/windows/win.ini`

The above examples will return the contents of C:\Windows\win.ini utilizing SMB to fetch the file via the local administrative share for the C drive. This will also work with remote shares.

## Impact

A properly crafted URL could cause a user to unknowingly access a remote file.

## Attachments
No attachments
