# DLL Hijacking when sending feedback and crash report leading to Privilege Escalation

## Report Details
- **Report ID**: 1008427
- **URL**: https://hackerone.com/reports/1008427
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-14T13:17:52.515Z
- **Disclosed**: 2024-08-27T13:46:49.676Z

## Reporter
- **Username**: z3ron3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Acronis True Image 2021 has a feature to send user feedback or application crash report to Acronis Support staff. ```report_sender.exe``` is the binary which manages such functionalities. The application is vulnerable to DLL hijacking attack because it searches for non-existing DLL files in locations which can be controlled by the attacker or normal user thus placing a malicious DLL in one of the folder will result it getting loaded by ```report_sender.exe``` with Administrator privileges which can be escalated to SYSTEM privileges thus resulting in a Privilege Escalation.

```report_sender.exe``` looks for the following DLL files and name of any file can be used to exploit the vulnerability.

+ CSUNSAPI.dll
+ swift.dll
+ nfhwcrhk.exe
+ SureWareHook.dll
+ aep.dll
+ atasi.dll
+ nusonsll.dll
+ ubsec.dll

Every Windows system contains ```%USERPROFILE%\AppData\Local\Microsoft\WindowsApps``` folder as a value in the User PATH environment variable where ```report_sender.exe``` will search for the DLL if not found in the preceding Search order folders. The malicious DLL file can be placed in this folder as normal user has Full control over this folder.

{F1035152}

Even if ```%USERPROFILE%\AppData\Local\Microsoft\WindowsApps``` folder is not in User PATH environment variable, attacker can add any folder of his choice to the User PATH environment variable as this does not require Administrative permissions.

## Steps To Reproduce
I created a DLL file which when loaded spawns ```cmd.exe``` while giving information as to which application loaded the DLL, path from where the file was loaded, and user privilege. I have attached the DLL file as well as the C++ code to build the DLL below if any necessary changes are to be made.

[ 1 ] - Copy or write the DLL file with any name from the above specified DLL file names in ```%USERPROFILE%\AppData\Local\Microsoft\WindowsApps``` folder. I chose ```ubsec.dll``` in this example.

{F1035153}

[ 2 ] - Go to the **Help** tab in Acronis True Image and click on **Send feedback**.

{F1035539}

[ 3 ] - Fill in the details of the feedback and click on **Send**.

{F1035561}

A ```cmd.exe``` window will open when ```report_sender.exe``` loads the DLL file.
We can see in the title of the ```cmd.exe``` window that it was started with **Administrator** privileges. To confirm, I ran ```net session``` command which gives **There are no entries in this list** output if executed with Administrator privileges and **Access denied** if executed as a normal user.

{F1035584}

## Escalating from Administrator privileges to NT AUTHORITY\SYSTEM.
[ 1 ] - From the Command Prompt that was executed after the DLL was loaded, create a scheduled task by using the Windows built-in schtasks.exe utility.

```schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR C:\Windows\System32\winver.exe /IT /RL HIGHEST```

{F1035585}

[ 2 ] - Run the task created in above step from the elevated Command Prompt.

```schtasks /run /I /TN EOP```

{F1035586}

```winver.exe``` can be seen executed as **NT AUTHORITY\SYSTEM** resulting in SYSTEM privileged code execution.

## Impact

Attackers gaining privilege to execute commands as Administrator or NT AUTHORITY\SYSTEM.

This attack can also work without any user interaction when ```report_sender.exe``` automatically sends crash report.

## Attachments
- 1.png
- 2.png
- 3.png
- 4.png
- 5.png
- 6.png
- 7.png
- ubsec.cpp
- ubsec.dll
