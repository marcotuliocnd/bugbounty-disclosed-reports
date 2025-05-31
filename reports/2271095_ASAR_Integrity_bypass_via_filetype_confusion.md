# ASAR Integrity bypass via filetype confusion

## Report Details
- **Report ID**: 2271095
- **URL**: https://hackerone.com/reports/2271095
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-12-04T06:02:02.260Z
- **Disclosed**: 2024-01-20T16:43:37.361Z

## Reporter
- **Username**: marshallofsound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Maliciously crafted directories mirroring an ASAR file structure could be used to trick apps with ASAR integrity enabled into loading non-validated code.

## Impact

This only impacts apps that have the embeddedAsarIntegrityValidation and onlyLoadAppFromAsar fuses enabled. Apps without these fuses enabled are not impacted. This issue is specific to macOS as these fuses are only currently supported on macOS.

Specifically this issue can only be exploited if your app is launched from a filesystem the attacker has write access too. i.e. the ability to edit files inside the .app bundle on macOS which these fuses are supposed to protect against.

There are no app side workarounds, you must update to a patched version of Electron.

**Fixed Versions**
* `27.0.0-alpha.7`
* `26.2.1`
* `25.8.1`
* `24.8.3`
* `22.3.24`

## Attachments
No attachments
