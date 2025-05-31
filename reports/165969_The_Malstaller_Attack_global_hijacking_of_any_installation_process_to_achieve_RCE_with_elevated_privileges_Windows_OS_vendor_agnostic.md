# The “Malstaller” Attack, global hijacking of any installation process to achieve RCE with elevated privileges, Windows OS (vendor agnostic) 

## Report Details
- **Report ID**: 165969
- **URL**: https://hackerone.com/reports/165969
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-05T19:24:46.125Z
- **Disclosed**: 2019-11-12T23:53:30.371Z

## Reporter
- **Username**: penrose
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Malstaller is a severe vulnerability that affects the installation process of an unknown number of software including many top-100 download software. The vulnerability affects Windows OS (WIN 7 verified vulnerable) users and variations of the attack can affect already installed software and native Windows OS tools.
Malstaller allows attackers to perform RCE and elevate privileges on the affected system corrupting or patching installations of various software with malicious code, blocking AV solutions, leaving a system unprotected or stealing sensitive information via URL sniffing. 

What can the attackers gain?

Malstaller allows attackers to perform RCE and elevate privileges on the affected system. An attacker with low privilege access to a Windows System (user) can intercept the installation/uninstallation process ( triggered by an elevated user) of software and execute his own code. Depending on the elevation level gained he can execute code as administrator, ultimately tampering the installation folder/files of the system or other system folders content. Of course he can execute any other malicious actions with his elevated privileges.

Variations of the same attack can hijack the use of native windows administrative tools like for example “perfmon.exe” or “mmc.exe”. The specific scenario exploits the fact that tools that need administrative level authority in order to execute, rely on resources accessible/editable by simple users under the HKEY_CURRENT_USER hive. The attacker hijacks the execution of an administrative level tool and injects his code which runs with elevated privileges.

Who is vulnerable and when?

Windows 7 OS users are vulnerable to this attack. Other versions of Windows OS seem to be vulnerable. 
The attack can take place during:
•	Installation of software
•	Execution of software (if run as admin)
•	Uninstallation of software 
The attack can take place without user interaction. These are the cases where an installation of uninstallation process automatically redirect user to a URL thus activating automatically the injected code with elevated privileges.

Replication of the attack

It is possible for an attacker that has limited user privileges (not admin) to hijack the installation process of your executable via tampering registry keys belonging to HKCU Hive. Typically installers require admin privileges (UAC) to install the tool properly but "unfortunately" trust registry keys that can be tampered by underprivileged users in order to perform certain actions. The specific registry keys targetted in this exploit are mainly used to identify the default browser (path of the browser) chosen by the user.
An attacker can tamper these registry keys and replace them, pointing to malicious software, triggering a code execution with elevated privileges during the installation/uninstallation or elevated execution of software. This can lead to attacker escalating privileges and at the same time tampering the installation itself opening a window to more dangerous attacks.

Here are the steps to replicate the attack:
On Windows 7 OS install Firefox Browser (set as default browser) (The attack is also possible with other browsers. This parameter is needed in order to know which registry key to tamper)

Step 1: Tempering Registry Keys
Attacker (with low privileges) tampers the content of the following registry keys:
•	[HKEY_CURRENT_USER\Software\Classes\https\shell\open\command]
•	[HKEY_CURRENT_USER\Software\Classes\http\shell\open\command]
•	[HKEY_CURRENT_USER\Software\Classes\FirefoxHTML\shell\open\command]
•	[HKEY_CURRENT_USER\Software\Classes\FirefoxURL\shell\open\command]

With value:
"C:\Users\{CURRENTUSERNAME_EDIT_HERE}\Desktop\malstaller.bat" "%1"
The value above points to the code the attacker wants to be executed with elevated privileges and can be of any file type including .exe, .vbs, .bat etc. 

Step 2: Attack script
Create a simple .bat file named malstaller.bat on the Desktop folder of the user. This script will perform the RCE with elevated privileges. (In reality these files would have been hidden on a different folder). 
Example content of malstaller.bat:

REM Malstaller Attack 2016
set arg1=%1
REM RCE with ELEVATION (Capturing URLs and saving to admin space)
echo %date% : %1 >> C:\mal_log.txt
REM Opening URL not to raise suspicion
"C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -osint -url "%1"

Step 3: Attack replication
Victim administrator: 
•	Installs software
•	Executes software (as admin)
•	Uninstalls software 

UAC window pops up asking for privileged access which the admin provides.
At this point the user (victim) is navigated through various panels with installation/uninstallation options. In case he clicks on any of the external links like for example the Privacy policy he unconsciously triggers the attacker’s script (malstaller.bat) with elevated privileges (RCE & Privilege Escalation). 
In our case the script will create a file named mal_log.txt under C:\, a protected admin folder.
The file will contain the Date and URL that was clicked to trigger the attack in order to easily identify the vulnerable program.

Examples of Vulnerable Software 

The following software are just some indicative examples of popular software vulnerable to this attack. The full list is unknown. Links that trigger the attack scripts are highlighted with red squares.

Verified List (RCE with Elevated Privileges)
AV: AVG, Avira, MalwareBytes, Microsoft Security Essentials, McAfee
Readers: Foxit
WEB: Wamp Server, TeamViewer
General Purpose: Winrar, Winzip, VLC
Windows Native: perfmon, mmc

Check the Annex Section attached for a collection of PoC images of vulnerable software.

Disclaimer: All tests were made using the latest versions of the tools depicted above. Downloads were made using direct links from the official websites of each tool.

How can I check if my installer or software is vulnerable?

Follow the “Replication of attack guide” and while installing/uninstalling or running any software try to click on all possible links that would trigger a browser to open. If the script is activated, check mal_log.txt to find the newly created log. If a new entry is present that the installer/uninstaller or software is vulnerable to this type of attack.

Mitigation

Never trust/rely on resources (registry keys) that can be tampered by underprivileged users when executing a privileged action like the installation/uninstallation of software.
Use HKEY_LOCAL_MACHINE Hive instead to identify browsers and navigate to URLs.
If you need to link your installer app to an external link (ex. privacy policy page) use a non-elevated executable first and only when real installation/uninstallation starts ask to elevate privileges.

Who else can be affected?

The number of software/tools that are vulnerable to this attack are unknown. The number of users impacted by this attack is also hard to define.

## Attachments
- Malstaller_Whitepaper_v.10.docx
- malstaller.bat
