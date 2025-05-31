# Bypass GlassWire's monitoring of Hosts file

## Report Details
- **Report ID**: 141700
- **URL**: https://hackerone.com/reports/141700
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-28T14:20:21.804Z
- **Disclosed**: 2016-07-23T21:18:11.898Z

## Reporter
- **Username**: newfunction
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glasswire

## Vulnerability Information
Product version: 1.2.64beta
OS version: Windows 8.1 Enterprise x86

If a program modifies the Hosts file (C:\Windows\System32\drivers\etc\hosts), GlassWire notifies the user that "system file changed" with the path of the hosts file (see attachment "screenshot_hosts_changed.png"). I discover that a malware (running with admin privilege) can change the content of hosts file without triggering this notification. The method is to use hardlink.

To reproduce:
Step 1: Open cmd.exe as administrator
Step 2: execute "fsutil hardlink create c:\ProgramData\hosts.txt c:\windows\system32\drivers\etc\hosts" in cmd.exe
Step 3: execute "echo ::1 example.local>>c:\ProgramData\hosts.txt" in cmd.exe
You can see that the notification is not triggered after step3. See "screenshot_modified_via_hardlink_no_notification.png".

Now execute "echo ::1 example2.local>>c:\windows\system32\drivers\etc\hosts" in cmd.exe. You receive a notification that hosts file is modified, prompted by GlassWire. See "screenshot_modified_directly_have_notification.png".

## Attachments
- screenshot_hosts_changed.png
- screenshot_modified_directly_have_notification.png
- screenshot_modified_via_hardlink_no_notification.png
