# Local Privilege Escalation when deleting a file from Quarantine

## Report Details
- **Report ID**: 983363
- **URL**: https://hackerone.com/reports/983363
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-16T11:27:10.424Z
- **Disclosed**: 2024-08-26T15:31:34.261Z

## Reporter
- **Username**: z3ron3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Acronis True Image has an Antivirus functionality which provides real-time protection and signature-based defenses against viruses and malwares.
When a file is put in Quarantine by Acronis AV it is not completely deleted from the original location, but rather the original file is emptied and reduced to 0 byte size and then made hidden.
The Quarantine has a **Delete from PC** feature which can be used to delete the selected file from Acronis AV's Quarantine folder as well as the hidden empty file from the original path. The delete operation that gets performed on Acronis AV's Quarantine folder is safe as normal user does not have access to it but the delete operation on the hidden empty file is vulnerable to a symlink attack.

## Steps To Reproduce
In this example I will try to delete ```C:\Windows\System32\drivers\pci.sys``` file which is a Windows driver file that a normal user does not have the permissions to delete.

{F989876}

[ 1 ] - Create a new folder anywhere on the system.
I created a folder named 'eicar' on my system. %userprofile% is a Windows environment variable for the user folder which is 'C:\Users\Gr33n' in my case.
```mkdir %userprofile%\Desktop\eicar```

{F989879}

[ 2 ] - Write the EICAR string in the folder created above so that Acronis's AV detects it as a threat and puts the file in Quarantine.
```echo|set /p="X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*" > %userprofile%\Desktop\eicar\eicar.exe```

{F989887}

Acronis AV will put eicar.exe into its Quarantine and make the original eicar.exe file empty and hidden.

{F989894}

[ 3 ] - Delete the 'eicar' folder which contains the hidden and empty 'eicar.exe' file as it is a prerequisite for creating a symlink.
```rmdir /S /Q %userprofile%\Desktop\eicar\eicar.exe```

{F989911}

[ 4 ] - Create a symlink from 'eicar.exe' file to the target file which is to be deleted.
To create a symlink without administrator rights, we first need to create a Mount Point such that "%userprofile%\Desktop\eicar" directory points to the "\RPC Control\" object directory and then create a symlink such that "\RPC Control\eicar.exe" file points to the target file (pci.sys in this example).

A simple way to perform this is by using James Forshaw's symboliclink-testing-tools. The tools can be built with Visual Studio 2013 or higher.
https://github.com/googleprojectzero/symboliclink-testing-tools

I have used CreateSymlink tool from symboliclink-testing-tools in this example.

```CreateSymlink.exe %userprofile%\Desktop\eicar\eicar.exe C:\Windows\System32\drivers\pci.sys```

{F989916}

[  5 ] - Open Acronis AV's Quarantine, select the file and choose the option Delete from PC.

{F989920}

Acronis AV will delete the file from its Quarantine and it will also try to delete the empty and hidden 'eicar.exe' file but because of the symlink, the delete operation will be performed on ```C:\Windows\Systen32\drivers\pci.sys``` file resulting in its deletion.

{F989937}

To delete a folder, append "::$index_allocation" to the target folder when creating symlink.
For example, ```CreateSymlink.exe %userprofile%\Desktop\eicar\eicar.exe C:\Temp::$index_allocation``` will create a symlink from 'eicar.exe' file to ```C:\Temp``` folder because of the way files are stored in NTFS and 'Temp' folder will be deleted after the attack.


## Recommendations
Impersonate as normal user when deleting the hidden and empty file.

## Escalating this vulnerability further to privileged write
I think I may have found a way to escalate this privileged delete vulnerability to privileged write to increase the severity of the issue but I will need some time to verify that.

## Impact

Attacker can delete any file or folder of his choice even when he does not have the permissions to do so.

## Attachments
- 1.png
- 2.png
- 3.png
- 4.png
- 5.png
- 6.png
- 7.png
- 8.png
