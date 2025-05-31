# Local Privilege Escalation via DLL Search-Order Hijacking with Cyber Protection Agent - systeminfo.exe utility

## Report Details
- **Report ID**: 959608
- **URL**: https://hackerone.com/reports/959608
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-15T20:12:54.621Z
- **Disclosed**: 2024-08-27T14:05:57.437Z

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
If a local attacker has modifying rights to one of the folders defined in the PATH system variable, will be able to load his malicious DLL, when the systeminfo.exe  starts, and execute his code with elevated privileges.

-How to Reproduce:
1.Download the latest version for the Windows Agent
URL: https://mc-beta-cloud.acronis.com/download/u/baas/4.0/12.5.23130/Cyber_Protection_Agent_for_Windows_web.exe

2.Start a procmon utility, from Sysinternal, and monitor "systeminfo.exe"
As part of my PATH system variables, I have the Python's location, which was installed in the C:\Python27 folder.

After the installation is complete, manually start the systeminfo.exe, which in my case is pointing to "C:\Program Files\Common Files\Acronis\AdvReport\systeminfo.exe" executable.
Below is an output of the process is which is looking for snapapi.dll:

systeminfo.exe	2132	CreateFile	C:\python27\snapapi.dll	NAME NOT FOUND

The test was perform on my Windows 10 Pro Version 1909 (OS Build 18363.1016).

I have attached a sample DLL, when loaded this will call C:\attacker\mmg.bat file.
You will need to create the c:\attcker folder and you can add in the mmg.bat file any command you want.
For validation i usually append in the file "whoami /all >> c:\attacker\who.txt" to confirm the security context in which my code was executed.

## Impact

The software executable is not verifying the authenticity of the DLL files, or the Search-Order before loading, thus an attacker may leverage this vulnerability to execute arbitrary code on the victim's machine, with the highest privileges.

## Attachments
- mmg.bat.txt
- snapapi.dll
