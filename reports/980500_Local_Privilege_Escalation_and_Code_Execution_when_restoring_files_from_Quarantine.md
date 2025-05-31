# Local Privilege Escalation and Code Execution when restoring files from Quarantine

## Report Details
- **Report ID**: 980500
- **URL**: https://hackerone.com/reports/980500
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-12T06:36:40.711Z
- **Disclosed**: 2024-08-27T14:05:38.170Z

## Reporter
- **Username**: z3ron3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Acronis True Image has an Antivirus functionality which provides real-time protection and signature-based defenses against viruses and malwares. The Quarantine  has a Restore feature which can be used to restore quarantined files back to their original location if the user is sure that the file is not a threat. 
The Restore file feature makes sure to stop Symlink attack successfully but it is vulnerable to Directory junction attack.
After more testing, I was able to create or modify any file on the system with attacker controlled data that a normal user does not have access to thus resulting in a Local Privilege Escalation vulnerability.


## Steps To Reproduce
[ 1 ] - Create a new folder anywhere on the system.
I created a folder named 'eicar' on my system.  %userprofile% is a Windows environment variable for the user folder which is '**C:\Users\Gr33n**' in my case.
`mkdir %userprofile%\Desktop\eicar`

{F985003}


[ 2 ] - Write the EICAR test string to a file you want to replace or write as the target file as a fake virus for Acronis AV to detect. (eicar.bat in this case)
`echo|set /p="X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*" > %userprofile%\Desktop\eicar\eicar.bat`

{F985007}

After writing EICAR string to a file in 'eicar' folder, Acronis AV will detect it as a threat and will await for instructions wheather to trust the file or quarantine it.

{F985009}


[ 3 ] - Before choosing the Quarantine option, we must change the contents of the detected eicar.bat file.
I will change the contents of eicar.bat file with a simple 'calc' command which opens Microsoft Calculator when executed in a batch file.
`echo calc > %userprofile%\Desktop\eicar\eicar.bat`

{F985012}

[ 4 ] - Click on Quarantine option in the Acronis AV threat detected overlay.

{F985019}

The edited eicar.bat will be moved into Acronis AV's Quarantine folder.

[ 5 ] - Delete the whole eicar folder as it a prerequisite for creating Directory Junction.
`rmdir /S /Q %userprofile%\Desktop\eicar`

{F985021}

[ 6 ] - Create a Directory Junction from the 'eicar' folder to any target folder you want to write to but don't have permission for.
I chose '**C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp**' folder in Windows which executes any programs in it on system start as the logged in user. This means logging in as SYSTEM will execute the program from SYSTEM privileges.

{F985022}

[ 7 ] - Restore the quarantined 'eicar.bat' file from Acronis AV Quarantine.

{F985025}

Acronis AV will restore the 'eicar.bat' to its original location but due to the Directory Junction from that folder to 'Startup' folder, the 'eicar.bat' file will be restored in 'Startup' folder.

{F985030}


## Note

{F985065}

From Acronis AV's settings, I chose 'Block and notify' as Action on detection so that I could easily get screenshots for the demonstration of this report and it is the option that most people prefer.
The vulnerability will also work when 'Quarantine' option is selected if attacker controlled data is written in detected file (eicar.bat) in a short time frame before Acronis AV moves the file into Quarantine which requires a little bit of trial an error.


## Recommendations
Detect Directory Junction on file's origin folder and stop the restore process.

## Impact

##Denial of Service (DoS)
Using the above demonstrated vulnerability, an attacker can corrupt important files which are necessary for the working of the Acronis AV thus denying user from using its protection.

An attacker can also corrupt important files which are necessary for Windows to boot such as '**C:\Windows\System32\drivers\pci.sys**' file. User won't be able to boot into Windows if this file gets corrupted resulting into a DoS attack.

##SYSTEM level Code execution
 [ 1 ] - I saw that Acronis AV users a 'schedul2.exe' application which executes '**C:\Program Files (x86)\Acronis\Agent\bin\adp-rest-util.exe**' with SYSTEM privileges so I tried the above demonstrated attack on 'adp-rest-util.exe' and was able to execute attacker controlled command as SYSTEM as it can seen in the Process Monitor.

{F985043}

[ 2 ] - Attacker can plant malicious DLL files for applications running as SYSTEM or Acronis components itself in directories of DLL search order and the malicious DLL will be loaded when the application is launched resulting in SYSTEM level code execution.

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
- note.png
