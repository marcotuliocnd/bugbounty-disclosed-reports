# DLL hijacking in Monero GUI for Windows 0.17.3.0 would allow an attacker to perform remote command execution

## Report Details
- **Report ID**: 1437942
- **URL**: https://hackerone.com/reports/1437942
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-12-30T00:49:01.644Z
- **Disclosed**: 2021-12-30T17:08:50.250Z

## Reporter
- **Username**: fukuyama
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
Summary:
Monero for windows contains a DLL hijacking vulnerability that allows to get a meterpreter command (metasploit remote shell), The moment the victim runs the program it will execute our payload (malicious .dll) that will give an attacker a meterpreter console. This will allow the attacker obtain a remote command execution console and If the victim runs the program frequently this will give the attacker permanent access to the it's computer.

The moment the user or the attacker runs the program it will execute our malicious.dll. If the attacker has a low-privileged shell or a basic shell that does not allow him to perform too many actions beyond the basic ones, then he can upgrade his shell and use all the advantages that the meterpreter has, which will allow him to perform more actions than a basic shell and also the opportunity to escalate privileges using post exploitation modules.

If for any reason the user runs the program as an administrator user, it is 100% sure that the attacker will obtain administrator privileges.

Observation
I used my own local IP and a normal .dll malicious file creator (maybe your antivirus will detect it, remember to disable it temporarily or add an exception) just for the PoC. In real situation an attacker will use a public IP (real or faked), and the malicious .dll would be encoded.

Releases Affected:
monero-gui-install-win-x64-v0.17.3.0.exe ( https://downloads.getmonero.org/gui/win64install )

Steps To Reproduce:

1. Create the malicious .DLL file named as: perf.dll (Screenshot_1.png)
2. Drop perf.dll in the install folder location ( C:\Users\<Your username here>\AppData\Local\Microsoft\WindowsApps)  (Screenshot_2.png)
3. In the attacker's computer , using metasploit configure a multi/handler meterpreter. (Screenshot_3.png)
4. Execute the program
5. Now the attacker will have a meterpreter connection (Remote Code Execution). (Screenshot_4.png)

Supporting Material/References:
https://attack.mitre.org/techniques/T1574/001/

## Impact

An attacker can exploit this vulnerability to load a DLL file of the attacker's choosing that could execute arbitrary code which will give an opportunity for the attacker to escalate privileges if he uses the post-exploitation modules or post-exploitation techniques.

If for any reason the user runs the program as an administrator user, it is 100% sure that the attacker will obtain administrator privileges.

## Attachments
- Screenshot_1.PNG
- Screenshot_2.PNG
- Screenshot_3.PNG
- Screenshot_4.PNG
