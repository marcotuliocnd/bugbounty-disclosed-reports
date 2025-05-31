# Local Privilege Escalation via DLL Search-Order Hijacking with Cyber Protection Agent - tibxread.exe utility

## Report Details
- **Report ID**: 963103
- **URL**: https://hackerone.com/reports/963103
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-20T11:16:45.441Z
- **Disclosed**: 2024-08-26T15:24:36.903Z

## Reporter
- **Username**: mmg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Using the latest version of Cyber Protection Agent (Version 12.5.23130) is possible to perform DLL Search-Order Hijacking.
The only requirement is to have modify rights to one folder defined in the PATH system variable, due to the order in which the DLL is loaded.

-Impact:
If a local attacker has modifying rights to one of the folders defined in the PATH system variable, will be able to load his malicious DLL when the tibxread.exe starts, allowing a low privileged  attacker to perform horizontal and/or vertical privilege escalation.

-How to Reproduce:
1.Download the latest version for the Windows Agent
URL: https://mc-beta-cloud.acronis.com/download/u/baas/4.0/12.5.23130/Cyber_Protection_Agent_for_Windows_web.exe

2.Start a procmon utility, from Sysinternal, and monitor "tibxread.exe"
As part of my PATH system variables, I have the Python's location, which was installed in the C:\Python27 folder.

After the installation is complete, you can run the following utility "C:\Program Files\BackupClient\BackupAndRecovery\tibxread.exe" executable.
Below is an output of the process is which is looking for tcmalloc.dll:

tibxread.exe	1336	CreateFile	C:\python27\tcmalloc.dll	NAME NOT FOUND


The test was perform on my Windows 10 Pro Version 1909 (OS Build 18363.1016).

I have attached a sample DLL, when loaded this will call C:\attacker\mmg.bat file.
You will need to create the c:\attcker folder and you can add in the mmg.bat file any command you want.
For validation i usually append in the file "whoami /all >> c:\attacker\who.txt" to confirm the security context in which my code was executed.

## Impact

This could potentially allow an authorized low privileged local account to execute arbitrary code in order to perform horizontal and/or vertical privilege escalation.

## Attachments
- mmg.bat.txt
- tcmalloc.dll
