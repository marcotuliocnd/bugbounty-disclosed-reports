# Potential IP revealing using UNC Path in Windows File Picker

## Report Details
- **Report ID**: 376004
- **URL**: https://hackerone.com/reports/376004
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-03T12:09:11.404Z
- **Disclosed**: 2023-11-28T09:09:48.364Z

## Reporter
- **Username**: newfunction
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
This report is inspired by #294364. The release note says that after fixing [Bug 26424](https://trac.torproject.org/projects/tor/ticket/26424), UNC path is disabled in Tor. But I found that I can still type UNC path in Windows file picker dialog box, and that sends requests to remote servers without Tor proxy.

Some social engineering is required to exploit this trick though. Attackers can use <input type="file"> on their website, and trick users to click "Browse" and type an attacker-controlled IP address into file picker in UNC format.

Is it possible to disable UNC path in the Windows file picker? If not, how about showing a warning message?

## Impact

With some social engineering, attackers can know user's real IP address with <input type="file">.

## Attachments
- UNC_Path_in_File_Picker.png
