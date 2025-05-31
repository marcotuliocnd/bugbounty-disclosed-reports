# Folder architecture and Filesizes of private file drop shares can be getten

## Report Details
- **Report ID**: 1337422
- **URL**: https://hackerone.com/reports/1337422
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-12T10:40:41.355Z
- **Disclosed**: 2022-04-09T13:08:38.397Z

## Reporter
- **Username**: shakierbellows
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Steps To Reproduce:

1. Create a new Folder "TestABC"
2. Share a password protected link of this folder
3. Create a file "README.md" and a file "README.md" in the Subfolder "Subfolder".

==> curl -H "OCS-APIREQUEST: true" "http://localhost/ocs/v2.php/apps/text/public/workspace?shareToken=ABCDE12345"

==> curl -H "OCS-APIREQUEST: true" "http://localhost/ocs/v2.php/apps/text/public/workspace?shareToken=ABCDE12345&folder=subfolder"

## Impact

Folder architecture and Filesizes of private file drop shares can be getten

## Attachments
No attachments
