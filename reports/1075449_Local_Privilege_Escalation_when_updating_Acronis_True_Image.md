# Local Privilege Escalation when updating Acronis True Image

## Report Details
- **Report ID**: 1075449
- **URL**: https://hackerone.com/reports/1075449
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-10T08:50:24.670Z
- **Disclosed**: 2024-08-27T14:04:02.438Z

## Reporter
- **Username**: z3ron3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Acronis True Image has a feature that updates itself with its newer version automatically or manually depending on the user choice. When updating, the software writes log file named ```%temp%\Acronis\DriverSetup\inst.log``` with **SYSYEM** privileges accessible to normal user . This can be escalated to privileged write vulnerability by an attacker to write to files that he does not have permission to leading to Privilege Escalation.

## Steps To Reproduce
I'm using **Acronis True Image Version 2021, Build 32010** and will update it to latest build for demonstration.
{F1151730}
In this example, I will overwrite ```C:\Windows\System32\drivers\pci.sys``` file which cannot be modified by normal user.

[ 1 ] - Delete ```%temp%\Acronis\DriverSetup``` if it already exists.
```rmdir /S /Q %temp%\Acronis\DriverSetup```

{F1151731}

[ 2 ] - Create empty ```%temp%\Acronis``` folder.
```mkdir %temp%\Acronis```

{F1151732}

[ 3 ] - Create a symlink from ```%temp%\Acronis\DriverSetup\inst.log``` file to ```C:\Windows\System32\drivers\pci.sys``` file.
```CreateSymlink %temp%\Acronis\DriverSetup\inst.log C:\Windows\System32\drivers\pci.sys```

{F1151733}

[ 4 ] - Go to Account tab in Acronis True Image and click on **A new version is available**. True Image will begin to download the latest version.
{F1151734}

Wait for True Image to download new build.
{F1151735}

[ 5 ] - The installer will open after the download is complete, click on **Update** in the installer.
{F1151736}

While installing the new build, **setupapp_amd64.exe** will write to the log file in ```%temp%\Acronis\DriverSetup\inst.log``` with **SYSTEM** privileges and because of the symlink, pci.sys file will get overwritten.

{F1151737}

This is the MD5 hash of **pci.sys** file before the attack.
{F1151738}

This is the MD5 hash of **pci.sys** file after the attack.
{F1151739}

This proves that the content of **pci.sys** file was overwritten with the content of **inst.log** file


## Tested on:
Windows 10 Home Version 20H2 (OS Build 19042.685)
Acronis True Image Version 2021, Build 32010

## Impact

Attacker can overwrite any file of his choice without permission. Further, the vulnerability can be escalated to SYSTEM privileged code execution if the content of the file can be controlled.

## Attachments
- 1.png
- 2.png
- 3.png
- 4.png
- 5.png
- 6.png
- 7.png
- 8.png
- 9.png
- 10.png
