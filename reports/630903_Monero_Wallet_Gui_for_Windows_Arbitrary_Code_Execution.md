# Monero Wallet Gui for Windows (Arbitrary Code Execution)

## Report Details
- **Report ID**: 630903
- **URL**: https://hackerone.com/reports/630903
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-06-27T19:10:51.047Z
- **Disclosed**: 2019-11-18T21:33:55.252Z

## Reporter
- **Username**: l00ph0le
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
Summary:
The windows version of the monero-wallet-gui.exe application allows for code injection. The monero-wallet-gui.exe utilizes a precompiled OpenSSL library called libeay32.dll. This OpenSSL library is trying to read a configuration file that doesn’t exist. By default, on windows systems, authenticated users can create under the c:\ drive. A user with low privileges can create the folder structure and copy a malicious openssl config and .dll files into their path. When the monero-wallet-gui.exe application is executed, the malicious .dll file is also executed. 

Description: 
If you download Microsoft sys internals process monitor and execute it. Then open the monero-wallet-gui.exe application, you can see the “monero-wallet-gui.exe” binary trying to read a file called openssl.cnf and getting the result “PATH NOT FOUND”. See attached screenshot (FileNotFound.png).

I believe the issue can be resolved by compiling the OpenSSL library using –openssldir parameter and specifying a directory that can only be written too by administrators (i.e. C:\Program Files, C:\ProgramData). Currently it looks for the “ssl” directory in the parent directory of the Monero install path. For example, if I download the monero-gui-win-x64-v0.14.0.0.zip file and save it to the c: drive, then extract the file, the install path becomes “C:\monero-gui-win-x64-v0.14.0.0\monero-gui-v0.14.0.0”. When monero-wallet-gui.exe is executed, it looks for the openssl.cnf file in “C:\monero-gui-win-x64-v0.14.0.0\ssl”, which doesn’t exist.

I’ve included two example exploits for this;

Exploit example 1
calc.c – source code of my .dll file to execute calc.exe
calc.dll – compiled version of the calc.exe library
openssl-calc.cnf – example malicious openssl config

Exploit example 2
backdoor.c – source code my .dll file to create a local administrator, this uses a known uac bypass
backdoor.dll – compiled version of the local admin backdoor library
openssl-backdoor.cnf - example malicious openssl config

Steps To Reproduce:
Download and extract monero-gui-win-x64-v0.14.0.0.zip to c: drive.

Exploit 1 – calc.exe – See attached video calc.mp4
1.	Login with a low privileged user (part of Users group)
2.	Open a cmd.exe and issue command: mkdir C:\monero-gui-win-x64-v0.14.0.0\ssl
3.	Copy calc.dll C:\monero-gui-win-x64-v0.14.0.0\ssl
4.	Copy openssl-calc.cnf to C:\monero-gui-win-x64-v0.14.0.0\ssl
5.	Rename openssl-calc.cnf to openssl.cnf
6.	Logout of low privileged user.
7.	Login with local administrator.
8.	Launch monero-wallet-gui.exe application.
9.	Calc.exe with execute.

Exploit 2 – create a local admin user (uac bypass) – See attached video backdoor.mp4
1.	Login with a low privileged user (part of Users group)
2.	Open a cmd.exe and issue command: mkdir C:\monero-gui-win-x64-v0.14.0.0\ssl
3.	Copy backdoor.dll to C:\monero-gui-win-x64-v0.14.0.0\ssl 
4.	Copy openssl-backdoor.cnf .dll to C:\monero-gui-win-x64-v0.14.0.0\ssl 
5.	Rename openssl-backdoor.cnf to openssl.cnf
6.	Logout of low privileged user.
7.	Login with local administrator.
8.	Launch monero-wallet-gui.exe application.
9.	Open “Computer Management”
10.	Navigate to “System Tools” -> “Local Users and Groups” -> “Users”
11.	A new user of “backdoor” with a password of “backdoor” was added.
12.	Right click on “backdoor” and click “Properties”, then click “Member Of”.
13.	The “backdoor” user is part of the local administrator group.

How can the system be exploited with this bug?
DLL Hi-jacking can be used for many nefarious purposes. It can be used by malware to propagate and establish persistence on a workstation. It can be used to privilege escalation in the post exploitation phases of an attack.

## Impact

The impact is high. Successful exploitation leads to arbitrary code execution on the windows system. There are many actions a nefarious individual could accomplish with this vulnerability. In addition to post-exploitation privilege escalation, another example could be ransomware, or other malware.

## Attachments
- backdoor-uac.c
- backdoor-uac.dll
- calc.c
- calc.dll
- backdoor.mp4
- calc.mp4
- FileNotFound.png
- openssl-backdoor.cnf
- openssl-calc.cnf
