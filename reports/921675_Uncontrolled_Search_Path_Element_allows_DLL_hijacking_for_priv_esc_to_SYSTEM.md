# Uncontrolled Search Path Element allows DLL hijacking for priv esc to SYSTEM

## Report Details
- **Report ID**: 921675
- **URL**: https://hackerone.com/reports/921675
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-12T19:45:31.302Z
- **Disclosed**: 2021-06-04T13:56:55.896Z

## Reporter
- **Username**: dawouw
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glasswire

## Vulnerability Information
GlassWire contains a DLL hijacking vulnerability that could allow an authenticated attacker to execute arbitrary code on the targeted system. The vulnerability exists due to GlassWire loading DLL files from the PATH environment variable without verification. The machine should have at least one writable PATH directory for the privilege escalation to work (e.g. having Python, Java, etc. installed).
Nine different DLL's are loaded by the GlassWire Service (GWCtlSrv.exe) as SYSTEM. 
One DLL is loaded by the GUI (GlassWire.exe) as the currently logged in user.

Class: Privilege Escalation [CAPEC-233]
Class: Uncontrolled Search Path Element [CWE-427]

**Affected Product**
GlassWire 2.2.210.0

**Proof of Concept**
Usually, Python is prepended to the PATH environment (Path=C:\Python38\Scripts\;C:\Python38\;..). For my ease and workflow, I prepended my folder to it (C:\Dima\;). Place the [x86 DLL](https://secret.club/2020/04/23/directory-deletion-shell.html) in one of the writable folder paths.


*C:\Program Files (x86)\GlassWire\GWCtlSrv.exe*
GlassWire (32bit) loads the following DLLs during boot as SYSTEM:
- swift.dll
- CSUNSAPI.dll
- nfhwcrhk.dll
- SureWareHook.dll
- aep.dll
- nfhwcrhk.dll
- atasi.dll
- nuronssl.dll
- ubsec.dll

{F904704}
{F904728}


*C:\Program Files (x86)\GlassWire\GlassWire.exe*
Glasswire GUI (32bit) loads the following DLL after user logon as the current user:
- Wtsapi32.dll.dll

{F904730}


I hope this helps. Please let me know if you require more information.

Kind regards,
Dima van de Wouw
[Outflank](https://outflank.nl/)

## Impact

Successful exploitation of the GlassWire service allows an attacker to gain SYSTEM privileges and inject into the GlassWire service process at boot.
Successful exploitation of the GlassWire GUI allows a user to gain persistence. On shared machines, this would allow a user to move laterally to sessions of other users.

## Attachments
- GlassWire1.png
- GlassWire2.png
- GlassWireU.png
