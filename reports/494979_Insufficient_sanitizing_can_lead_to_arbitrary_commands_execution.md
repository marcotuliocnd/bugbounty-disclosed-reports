# Insufficient sanitizing can lead to arbitrary commands execution

## Report Details
- **Report ID**: 494979
- **URL**: https://hackerone.com/reports/494979
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-13T01:31:54.418Z
- **Disclosed**: 2019-06-06T00:46:57.283Z

## Reporter
- **Username**: mrnbayoh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: notepad-plus-plus

## Vulnerability Information
##Information:

**Summary:**
Notepad++ is vulnerable to a command injection attack.

**Debug Info:**
Notepad++ v7.6.3 (32-bit)
Build time : Jan 27 2019 - 17:20:30
Path : C:\Program Files (x86)\Notepad++\notepad++.exe
Admin mode : ON
Local Conf mode : OFF
OS : Windows 10 (64-bit)
Plugins : none

**Description:** 

Let's look at this command execution for example in `NppCommand.cpp`:
```
case IDM_FILE_OPEN_CMD:
		{
			Command cmd(TEXT("cmd /K cd /d \"$(CURRENT_DIRECTORY)\""));
			cmd.run(_pPublicInterface->getHSelf());
		}
break;
```

`\"` have been introduced with commit [0f93670](https://github.com/notepad-plus-plus/notepad-plus-plus/commit/0f936707a2457eb4611d7d42a68a3e066614f8e4#diff-48044e0078aaf1c5ab452bd9c8f0bcf3) to prevent RCE. 
However it is still possible to inject arbitrary commands using environment variables. For example trying to open a folder named `%TEST%` will result in the expansion of the environment variable, if it contains a `"` then its possible to inject arbitrary commands after that `"` in the directory name.

## Steps To Reproduce:

  1. Create a new environment variable (or a temporary one), let's name it `TEST` and set its value: `"`
  2. Create a new folder named `%TEST%  && mkdir boom` and create a text file in it, let's name that file `test.txt`
  3. Open `test.txt` with Notepad++ and click on `File->Open Containing Folder->cmd`
  4. The command in the folder name gets executed and the `boom` folder is created

## Fix:

Escape `%`characters before executing the command: `%` -> `^%`.

## Impact

A successful attack can lead to arbitrary commands execution.

## Attachments
No attachments
