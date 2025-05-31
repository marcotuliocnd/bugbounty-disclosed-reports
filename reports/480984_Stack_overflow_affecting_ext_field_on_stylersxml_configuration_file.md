# Stack overflow affecting "ext" field on stylers.xml configuration file

## Report Details
- **Report ID**: 480984
- **URL**: https://hackerone.com/reports/480984
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-01-16T15:55:52.607Z
- **Disclosed**: 2019-08-25T12:51:14.728Z

## Reporter
- **Username**: ammm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: notepad-plus-plus

## Vulnerability Information
**Summary:**

A stack buffer overflow vulnerability affects "ext" field into "stylers.xml" configuration file.

"isInList" function doesn't check boundaries on word[64] array.

**Description:**
Vulnerability src file: notepad-plus-plus/PowerEditor/src/MISC/Common/Common.cpp
Vulnerability line: line 329
Variable affected: TCHAR word[64];

## Steps To Reproduce:

Notice: All this steps have been tested on 32-bits version of Notepad++.

  1. Open "stylers.xml" configuration file (C:\Users\%USERPROFILE%\AppData\Roaming\Notepad++)
  2. Modify "ext" field with a long string, such as "123456789012346789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789" (see ExploitationExample.png)
  3. Close Notepad++ application and re-open it.
  4. Application should crash

## Supporting Material/References:

- ExploitationExample.png -> Exploitation example
- CrashEvidence.png -> Evidence of vulnerability exploitation

## Impact

A local attacker could modify this configuration file to trigger a stack buffer overflow. When the victim re-open Notepad++ vulnerability will be exploited.

It's not a remote vulnerability. Local access to stylers.xml is required.

## Attachments
- CrashEvidence.png
- ExploitationExample.png
