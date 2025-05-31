# DLL Hijacking when creating Rescue Media Builder leading to Privilege Escalation

## Report Details
- **Report ID**: 1010552
- **URL**: https://hackerone.com/reports/1010552
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-17T09:59:28.671Z
- **Disclosed**: 2024-08-27T13:48:12.272Z

## Reporter
- **Username**: z3ron3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Acronis True Image 2021 provides a **Rescue Media Builder** tool which lets the user create a bootable media to recover system if it becomes unbootable. 
```MediaBuilder.exe``` is the binary which manages such functionalities. The application is vulnerable to DLL hijacking attack because it searches for a non-existing DLL file named ```tcmalloc.dll``` (Google's custom implementation of dynamic memory allocation) in locations which can be controlled by the attacker or normal user thus placing a malicious DLL in one of the folder will result it getting loaded by ```MediaBuilder.exe``` with Administrator privileges which can be escalated to SYSTEM privileges thus resulting in Privilege Escalation.

Every Windows system contains ```%USERPROFILE%\AppData\Local\Microsoft\WindowsApps``` folder as a value in the User PATH environment variable where ```MediaBuilder.exe``` will search for the DLL if not found in the preceding Search order folders. The malicious DLL file can be placed in this folder as normal user has Full control over this folder.

{F1039832}

Even if ```%USERPROFILE%\AppData\Local\Microsoft\WindowsApps``` folder is not in User PATH environment variable, attacker can add any folder of his choice to the User PATH environment variable as this does not require Administrative permissions.

## Steps To Reproduce
I created a DLL file which when loaded spawns ```cmd.exe``` while giving information as to which application loaded the DLL, path from where the file was loaded, and user privilege. I have attached the DLL file as well as the C++ code to build the DLL below if any necessary changes are to be made.

[ 1 ] - Copy or write the DLL file named ```tcmalloc.dll```  which is to be executed in ```%USERPROFILE%\AppData\Local\Microsoft\WindowsApps``` folder.

{F1039839}

[ 2 ] - Got to Tools tab of True Image and open **Rescue Media Builder**.

{F1039840}

A ```cmd.exe``` window will open when ```MediaBuilder.exe``` loads the DLL file.
We can see in the title of the ```cmd.exe``` window that it was started with Administrator privileges. To confirm, I ran ```net session``` command which gives **There are no entries in this list** output if executed with Administrator privileges and **Access denied** if executed as a normal user.

{F1039842}

## Escalating from Administrator privileges to NT AUTHORITY\SYSTEM
[ 1 ] - From the Command Prompt that was executed after the DLL was loaded, create a scheduled task by using the Windows built-in schtasks.exe utility.

```schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR C:\Windows\System32\winver.exe /IT /RL HIGHEST```

{F1039843}

[ 2 ] - Run the task created in above step from the elevated Command Prompt.

```schtasks /run /I /TN EOP```

{F1039844}

```winver.exe``` can be seen executed as **NT AUTHORITY\SYSTEM** resulting in **SYSTEM** privileged code execution.

## Impact

Attackers gaining privilege to execute commands as Administrator or NT AUTHORITY\SYSTEM.

## Attachments
- 1.png
- 2.png
- 3.png
- 4.png
- 5.png
- 6.png
