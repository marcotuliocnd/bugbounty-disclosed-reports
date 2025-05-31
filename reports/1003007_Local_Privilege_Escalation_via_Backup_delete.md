# Local Privilege Escalation via Backup delete

## Report Details
- **Report ID**: 1003007
- **URL**: https://hackerone.com/reports/1003007
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-08T21:30:53.257Z
- **Disclosed**: 2024-08-27T14:03:18.385Z

## Reporter
- **Username**: z3ron3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Acronis True Image 2021 is famous for its seamless Backup and Restore feature which lets users backup any data to any place of their choice and restore it back in case of accidental loss. I found a serious bug/bypass in Acronis AntiRansomware Service when it comes to accessing backup files which when combined with symlink attack can let an attacker modify AntiRansomware protected backup files and delete any file on the system without permissions leading to Privilege Escalation.


## Issue
Acronis True Image  saves information about backups in ```.tib``` files. The ```.tib``` file itself as well as the folder it is in is monitored by Acronis AntiRansomware Protection to block any kind of modification unless an exclusion is created. The issue is that it monitors all modification operations on the file and folder except **Rename** operation on the folder containing the ```.tib``` file.


## Steps To Reproduce
We need to have a backup first to be able to delete it. The **Preparation** part contains the steps to create a backup and **Exploitation** part contains the steps to exploit the vulnerability. If you already have a backup, skip **Preparation** part.


Preparation:
------------
[ 1 ] - Create a file in a folder which is to be backed up. I chose to create a file named ```poc.exe``` in ```data_acronis``` folder on my Desktop.

```mkdir %userprofile%\Desktop\data_acronis & echo PoC > %userprofile%\Desktop\data_acronis\poc.exe```

{F1028123}

[ 2 ] - In Backup tab of Acronis True Image, click on **Change source** then click on **Files and folders** and select ```poc.exe``` file from ```data_acronis``` folder.

{F1028125}

[ 3 ] - Create a folder to save the backup .tib files in. I chose to create a folder named ```backup_acronis``` on my Desktop.

```mkdir %userprofile%\Desktop\backup_acronis```

{F1028127}

[ 4 ] - Click on **Select destination**, then click on **Browse** and select the ```backup_acronis``` folder.

{F1028128}

[ 5 ] - Click on **Back up now**.

{F1028129}

```poc.exe``` file from ```data_acronis``` folder will be backed up by Acronis True Image and the .tib files will be saved in ```backup_folder``` folder.

{F1028130}

Exploitation:
------------
The name pattern for the .tib files is ```[backup_name]_[backup_scheme]_b1_s1_v1.tib``` so after the backup, a file named ```poc_full_b1_s1_v1.tib``` will be created in ```backup_acronis``` folder.

Normally, the backup ```.tib``` files and folder are protected by Acronis AntiRansomware Protection from any kind of modification.

{F1028131}

But the issue is that it does not monitor and block **Rename** operation on the folder where the ```.tib``` files are stored which is ```%userprofile%\Desktop\backup_acronis``` in this case.

[ 1 ] - Rename ```backup_acronis``` to any other name.

```rename %userprofile%\Desktop\backup_acronis not_backup_acronis```

{F1028132}

[ 2 ] - Create a symlink from ```%userprofile%\Desktop\acronis_backup\poc_full_b1_s1_v1.tib``` file to the target file which is to be deleted. I will try to delete ```C:\Windows\System32\drivers\pci.sys``` file.
I've used CreateSymlink tool from [symboliclink-testing-tools](https://github.com/googleprojectzero/symboliclink-testing-tools) in this example.

```CreateSymlink %userprofile%\Desktop\backup_acronis\poc_full_b1_s1_v1.tib C:\Windows\System32\drivers\pci.sys```

{F1028133}

[ 3 ] - Go to Backup tab, right click on the backup and click on **Delete**, then click on **Delete entirely** option.

{F1028134}

Acronis True Image will try to delete the ```poc_full_b1_s1_v1.tib``` file from ```%userprofile%\Desktop\backup_acronis``` folder but because of the symlink the operation will be performed on ```C:\Windows\System32\drivers\pci.sys``` resulting in its deletion.

{F1028135}


## Tested on
Windows 10 Home, Version 2004 (OS Build 19041.450)
Acronis True Image 2021, Build 32010

Regards,
Saurabh Patil  ( @z3ron3 )

## Impact

If we rename the folder which contains the ```.tib``` file and create new folder of same name, we are able to write into the new folder without AntiRansomware protection blocking the write and Acronis True Image will assume its the same folder and read content from it which totally breaks the aim of Actve AntiRansomware protection as anyone is able to change contents of the ```.tib``` file.

Being able to change contents of AntiRansomware protected backup files without permission is a big issue in itself for True Image so I think this issue should be considered with greater severity. Privileged delete was just an application of the issue .

## Attachments
- 1.png
- 2.png
- 3.png
- 4.png
- 5.png
- 6.png
- 7.png
- 8.png
- 9.png
- 10.png
- 11.png
