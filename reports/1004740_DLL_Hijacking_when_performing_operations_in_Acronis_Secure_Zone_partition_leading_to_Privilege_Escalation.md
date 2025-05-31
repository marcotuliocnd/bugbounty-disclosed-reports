# DLL Hijacking when performing operations in Acronis Secure Zone partition leading to Privilege Escalation

## Report Details
- **Report ID**: 1004740
- **URL**: https://hackerone.com/reports/1004740
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-10T18:24:45.008Z
- **Disclosed**: 2024-08-26T15:26:41.791Z

## Reporter
- **Username**: z3ron3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Acronis True Image 2021 lets user create a special protected partition for storing backups. ```aszbrowsehelper.exe``` process enables browsing contents of the Acronis Secure Zone partition but every time any kind of operation gets performed in Secure Zone, ```aszbrowsehelper.exe``` looks for for ```tcmalloc.dll``` (Google's custom implementation of dynamic memory allocation) DLL file according to the untrusted search order.
1) C:\Program Files (x86)\Acronis\TrueImageHome
2) Application's current working directory
3) System directory
4) 16-bit System directory
5) Windows directory
6) Directories in System PATH environment variable
7) Directories in User PATH environment variable

Every Windows system contains ```%USERPROFILE%\AppData\Local\Microsoft\WindowsApps``` folder as a value in the User PATH environment variable where ```aszbrowsehelper.exe``` will search for the DLL if not found in other Search order folders.

{F1030633}

Normal user has Full control over ```WindowsApps``` folder so anyone can place a malicious DLL file in the folder and ```aszbrowsehelper.exe``` will load that malicious DLL file resulting in its execution with **Administrative** privileges which can be escalated to **NT/AUTHORITY SYSTEM** privileges resulting in Privilege Escalation.

Even if ```%USERPROFILE%\AppData\Local\Microsoft\WindowsApps``` folder is not in User PATH environment variable, attacker can add any folder of his choice to the User PATH environment variable as this does not require Administrative permissions.

## Steps To Reproduce
An Acronis Secure Zone partition is required for this vulnerability to work.
To create a secure partition,
1) Open Acronis Secure Zone tool from Tools tab.
2) Select a partition from the disk of your choice and click Next.
3) Select how much size you want to give the secure partition and click Next.
4) Click Proceed and True Image will prompt you to reboot the system to complete the operation.

After rebooting, the Secure Zone partition will be created.

I'm assuming the partition is already created in this example.

I created a DLL file which when loaded spawns ```cmd.exe``` while giving information as to which application loaded the DLL, path from where the file was loaded, and user privilege. I have attached the DLL file as well as the C++ code to build the DLL below if any necessary changes are to be made.

[ 1 ] - Copy or write the DLL file named ```tcmalloc.dll``` in ```%USERPROFILE%\AppData\Local\Microsoft\WindowsApps``` folder.

{F1030634}

[ 2 ] - In this example, I chose to execute the DLL by opening the **Manage Acronis Secure Zone Wizard** from Tools tab in Acronis True Image but the DLL will also get loaded when  browsing the secure partition in Windows Explorer.

{F1030635}

We can see in the title of the cmd.exe window that it was started with Administrator privileges. To confirm, I ran ```net session``` command which gives **There are no entries in this list** output if executed with Administrator privileges and **Access denied** if executed as a normal user.

## Escalating from Administrator privileges to NT AUTHORITY\SYSTEM.

[ 1 ] - From the Command Prompt that was executed after the DLL was loaded, create a scheduled task by using the Windows built-in schtasks.exe utility.

```schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR C:\Windows\System32\winver.exe /IT /RL HIGHEST```

{F1030636}

[ 2 ] - Run the task created in above step from the elevated Command Prompt.

```schtasks /run /I /TN EOP```

{F1030637}

```winver.exe``` can be seen executed as NT AUTHORITY\SYSTEM after the task is started thus resulting in SYSTEM privileged code execution.

## Impact

Granting attackers privilege to execute commands as Administrator or NT AUTHORITY\SYSTEM.

## Attachments
- 1.png
- 2.png
- 3.png
- 4.png
- 5.png
- tcmalloc.cpp
- tcmalloc.dll
