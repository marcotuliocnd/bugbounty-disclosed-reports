# Local Privilege Escalation via EXE hijacking with Acronis True Image 2021 installer

## Report Details
- **Report ID**: 970739
- **URL**: https://hackerone.com/reports/970739
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-30T14:33:07.528Z
- **Disclosed**: 2024-08-27T13:39:03.021Z

## Reporter
- **Username**: mmg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Using the latest version of Acronis True Image 2021 (25.4.30480) is possible to perform EXE Hijacking.
This could potentially allow an authorized but privileged local user to execute arbitrary code with elevated privileges on the system.

A successful attempt would require the local attacker must insert an executable file in the path of the EXE that is called.
Upon the software installation or possibly upgrade, the malicious code will be run with elevated privileges.

-Impact:
If a local attacker has modifying rights, or is chaining the attack with an arbitrary move/write vulnerability, and be able to store the file in the path from where the EXE is called, allowing to perform horizontal and/or vertical privilege escalation.

-How to Reproduce:
1.Download the latest version of  Acronis True Image 2021 installer

URL: https://download.acronis.com/AcronisTrueImage2021.exe

2.Start a procmon utility, from Sysinternal, and monitor "atih_installer_shell_standard.exe".

Start the installation
4.During the installation process the atih_installer_shell_standard.exe is looking for C:\program.exe
Below is an output:

atih_installer_shell_standard.exe	19792	CreateFile	C:\Program.exe	NAME NOT FOUND

The test was perform on my Windows 10 Pro Version 1909 (OS Build 18363.1016).

I have attached a sample exe file, that when executed will display a pop-up with the message "EXE Loaded".
This need to be stored in the C:\ just to demonstrate this behavior, before the installation process begins.

## Impact

This could potentially allow an authorized low privileged local account to execute arbitrary code in order to perform horizontal and/or vertical privilege escalation.

## Attachments
- Program.7z
- Insecure-execution-True-01.png
- Insecure-execution-True-02.png
