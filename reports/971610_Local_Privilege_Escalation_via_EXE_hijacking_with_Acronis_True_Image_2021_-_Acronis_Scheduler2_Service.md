# Local Privilege Escalation via EXE hijacking with Acronis True Image 2021 - Acronis Scheduler2 Service

## Report Details
- **Report ID**: 971610
- **URL**: https://hackerone.com/reports/971610
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-31T21:20:38.507Z
- **Disclosed**: 2024-08-27T13:46:27.864Z

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
Upon the Acronis Scheduler2 Service start/restart , the malicious code will be run with SYSTEM rights.

-Impact:
If a local attacker has modifying rights, or is chaining the attack with an arbitrary move/write vulnerability, and be able to store the file in the path from where the EXE is called, allowing to execute code with SYSTEM rights.

-How to Reproduce:
1.Download the latest version of Acronis True Image 2021 installer

URL: https://download.acronis.com/AcronisTrueImage2021.exe

2.Start a procmon utility, from Sysinternal, and monitor "schedul2.exe".

3.Finish the installation
4.During the  Acronis Scheduler2 Service start/restart the executable is looking for C:\program.exe
Below is an output:

NT AUTHORITY\SYSTEM	schedul2.exe	2976	CreateFile	C:\Program.exe	NAME NOT FOUND	

The test was perform on my Windows 10 Pro Version 1909 (OS Build 18363.1016).

I have attached a sample exe file, that when executed will display a pop-up with the message "EXE Loaded". 
This need to be stored in the C:\ just to demonstrate this behavior, before the installation process begins.

I have attached a print-screen that shows the  schedul2.exe is running the sample executable.

## Impact

This could potentially allow an authorized low privileged local account to execute arbitrary code in order to perform horizontal and/or vertical privilege escalation.

## Attachments
- Schedul2-Insecure-call.png
- Program.7z
