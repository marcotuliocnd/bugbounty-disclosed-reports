# Local Privilege Escalation using System Clean-up functionality

## Report Details
- **Report ID**: 996576
- **URL**: https://hackerone.com/reports/996576
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-02T14:54:45.708Z
- **Disclosed**: 2024-08-27T14:03:37.140Z

## Reporter
- **Username**: z3ron3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Acronis True Image 2021 contains a **System Clean-up** functionality which allows the user to wipe Recycle Bin, Temp folder, recent usage history including passwords and other information. The software has protections against symlink attack but it is vulnerable to Directory junction attack and it is possible for an attacker to delete all the files and subfolders of a folder using this vulnerability even if he does not have the permission to do so resulting in Privilege Escalation.

## Steps To Reproduce
I will demonstrate the vulnerability with two examples. In 1st example, I will show how to delete all the contents (files and subfolders) of a folder at once and in 2nd example I will show how to delete just one specific file from a folder using some Python code (flock.py) I wrote which is attached to the report.

**Example No.1:**
In this example, I will try to delete all the files inside **C:\Windows\System32\drivers\etc** which contain network mapping and port information for Windows. Normal user does not have permission to delete these files.

[ 1 ] - Create an empty folder inside **%userprofile%\AppData\Local\Temp** folder. Normal user has full access to this folder.
I created a folder named 'deleteme' on my system. %userprofile% is a Windows environment variable for the user folder which is 'C:\Users\Gr33n' in my case.

```mkdir %userprofile%\AppData\Local\Temp\deleteme```

{F1011626}

[ 2 ] - Open **System Clean-up** tool.

{F1011636}

[ 3 ] - Select the **deleteme** folder under **Temporary file**. It is not mandatory to only select the newly created folder in Step [ 1 ]. Selecting the whole **Temporary file** or **System Clean-up** option will also work.

{F1011647}

[ 4 ] - Delete the **deleteme** folder as it a prerequisite for creating Directory junction.

```rmdir /S /Q %userprofile%\AppData\Local\Temp\deleteme```

{F1011672}

[ 5 ] - Create a Directory junction from **%userprofile%\AppData\Local\Temp\deleteme** to **C:\Windows\System32\drivers\etc** folder.

```mklink /J %userprofile%\AppData\Local\Temp\deleteme C:\Windows\System32\drivers\etc```

{F1011683}

[ 6 ] - Click on the **Clean-up** option in the System Clean-up window.

{F1011685}

**TrueImageTools.exe** tool will attempt to delete the **deleteme** folder and all the contents inside it but because of the Directory junction, the operations will be performed on **C:\Windows\System32\drivers\etc** folder.

{F1011689}


  **Example No.2**
In this example, I will try to delete the **hosts** file inside **C:\Windows\System32\drivers\etc** which contains the mappings of IP addresses to host names for Windows. Normal user does not have permission to delete these files.

[ 1 ] - Create an empty folder inside **%userprofile%\AppData\Local\Temp** folder. Normal user has full access to this folder.
I created a folder named 'deleteme' on my system. %userprofile% is a Windows environment variable for the user folder which is 'C:\Users\Gr33n' in my case.

```mkdir %userprofile%\AppData\Local\Temp\deleteme```

{F1011626}

[ 2 ] -  In the **deleteme** folder, create a file with the name of the the file you want to delete from the target folder. **hosts** file in this case.

```echo|set /p="" > %userprofile%\AppData\Local\Temp\deleteme\hosts```

{F1011847}

[ 3 ] - Open **System Clean-up** tool.

{F1011636}

[ 4 ] - Select the **hosts** file under **Temporary file**. It is not mandatory to only select the newly created file in Step [ 2 ]. Selecting the whole **Temporary file** or **System Clean-up** option will also work.

{F1011771}

[ 5 ] - Delete the **deleteme** folder as it a prerequisite for creating Directory junction.

```rmdir /S /Q %userprofile%\AppData\Local\Temp\deleteme```

{F1011672}

[ 6 ] - Create a Directory junction from **%userprofile%\AppData\Local\Temp\deleteme** to **C:\Windows\System32\drivers\etc** folder.

```mklink /J %userprofile%\AppData\Local\Temp\deleteme C:\Windows\System32\drivers\etc```

{F1011683}

[ 7 ] - Run the Python program with the file to be deleted as an argument. **hosts** file in this example.

```python flock.py C:\Windows\System32\drivers\etc\hosts```

{F1011787}

The python program will open a handle to all files except the target file and keep it open until user input is given which will prevent them from getting deleted.

[ 8 ] - Click on the **Clean-up** option in the System Clean-up window.

{F1011685}

[ 9 ] - The **System Clean-up** window will show a prompt asking what to do since it cannot delete other files in the folder as they are opened by the python program. Click on **Ignore All**.

{F1011812}

**TrueImageTools.exe** will attempt to delete the **deleteme** folder and all the contents inside it but because of the Directory junction, the operations will be performed on **C:\Windows\System32\drivers\etc** folder and since all files except  the **hosts** file is opened by the python program, **TrueImageTools.exe** tool will fail to delete those opened files and only delete the **hosts** file.

**hosts** file does not exist in **C:\Windows\System32\drivers\etc** folder anymore.

{F1011814}


## Recommendations
Detect Directory junction and stop the deletion process.

## Impact

Attacker can delete all the files and subfolders from a folder or just a specific file or folder of his choice even when he does not have the permissions to do so.

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
- 12.png
- flock.py
