# Local privilege escalation via insecure MSI file

## Report Details
- **Report ID**: 1071832
- **URL**: https://hackerone.com/reports/1071832
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-01-05T10:38:03.082Z
- **Disclosed**: 2021-08-07T19:11:30.813Z

## Reporter
- **Username**: twvyy3vyaw8k
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
I've found a vulnerability which leads to a local privilege escalation starting from a non-admin user.

When `True Image` client installs it drops 2 MSI files into `C:\Windows\Installer` folder.
Since this folder (by default) is readable by anyone, a non-admin user can execute commands like `msiexec /fa installer_name.msi`, which forces `installer_name.msi` to "repair" the program.

One of these 2 MSIs (i can't named it because MSI file names are random and unique for every installation) when forced to repair it creates a dll in `%TEMP%\random_name` and then, after some time, `MsiExec.exe` loads it. Since `MsiExec.exe` auto-escalate privileges when executed and `%TEMP%` is writable by anyone, this behavior could be abused to gain `nt authority\system` privileges.

## Steps To Reproduce
  1.  Open `%TEMP%` and `C:\Windows\Installer`
  2.  Locate the MSI file in the installer folder: it's 1.3 GB large and has `Acronis` as author 
  3.  Open `cmd.exe` and execute `msiexec /fa C:\Windows\Installer\installer_name.msi`.  After few seconds a new folder will appear in `%TEMP%`
  4.  Replace `schedule.dll` inside that folder with the `schedule.dll` attachment  in this report
  5.  Wait until the process finishes. After some time a UAC should prompt, just select "no"
  6.  A new cmd should pop up. Type `whoami` to confirm the new privileges


I've also recorded a PoC video in case something it's not clear.

## Recommendations
Do not use local `%TEMP%` to create `schedule.dll`, use `C:\Windows\TEMP`.

## Impact

LPEs like this one are often used by malwares to evade antivirus engines, install rootkits, spread over the network, etc...
A malware author could use this exploit to target Acronis end users.

## Attachments
- true_image_LPE_PoC.mp4
- schedule.dll
