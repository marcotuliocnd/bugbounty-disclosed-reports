# User password left in memory in plain text after GUI launch

## Report Details
- **Report ID**: 761480
- **URL**: https://hackerone.com/reports/761480
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-19T08:14:23.075Z
- **Disclosed**: 2021-01-24T08:52:01.747Z

## Reporter
- **Username**: kaimi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
## Summary
When NordVPN GUI has sensitive data in memory and has no further need for it, it should wipe the data out of its memory, in case malware later gains access to the NordVPN process or the memory is swapped out to disk or written into a crash dump file. An obvious example of this is the user password in plain text.

## Steps to reproduce
1. Install NordVPN client
2. Authorize with your account
3. Close application
4. Relaunch application and create a memory dump (for example using Windows Task Manager)
5. Search password in resulting dump with any hex editor.
{F663532}

## Why bother
NordVPN desktop application is designed as VPN client, not as a management software for the user account. Currently application stores user credentials by the following path: `C:\Users\%USER%\AppData\Local\NordVPN\NordVPN.exe_Url_htakemwyuyjotcmrvjkhtpa53zxkjlky\6.26.6.0\user.config` in encrypted state. But it is clear, that VPN client should rely only on authentication and refresh tokens which should be unvalidated upon password change from user control panel on NordVPN web site. Those tokens actions should be limited only to activities required for establishing a VPN connection. Thus there's no purpose in storing user credentials (even in encrypted form) in the user configuration file and therefore in process memory.

## Mitigation
Consider wiping plain text password for memory and do no load it in memory after startup. Consider using tokens instead of user credentials.

## Impact

A plain text password from memory may be exposed to the malicious actor.

## Attachments
- dump.png
