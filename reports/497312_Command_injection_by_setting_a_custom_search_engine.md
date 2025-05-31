# Command injection by setting a custom search engine

## Report Details
- **Report ID**: 497312
- **URL**: https://hackerone.com/reports/497312
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-17T16:00:52.893Z
- **Disclosed**: 2019-05-07T22:46:18.602Z

## Reporter
- **Username**: peter_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: notepad-plus-plus

## Vulnerability Information
**Summary:** Arbitrary commands can be injected when using the "Search on Internet" function with a malicious custom search engine. The custom search engine can be set through the GUI or the config files, with different attack scenarios.

**Description:** The "Search on Internet" context menu functionality calls the `ShellExecute` function with the current search engine as argument. This can lead to arbitrary command execution.

By setting a command or a program (e.g. `cmd.exe /c "your_command_here"`) the command will be passed to `ShellExecute` and will be run. After the malicious search engine is set, the command will be executed *every time* the "Search on Internet" context menu functionality is used, instead of opening a web page in a browser.

The consequence is that any actor that can succesfully set the custom search engine can make the user execute any command.

There are two ways to set the custom search engine:

* in the GUI, from "Settings" > "Preferences" > "Search Engine"
* from the `config.xml` file, by editing the following fields in the `GuiConfig` tag with `name="searchEngine"`:
	* set `searchEngineCustom` to the command to execute
	* set `searchEngineChoice=0` to use the custom search engine

## The vulnerability

In `PowerEditor\src\NppCommands.cpp`, line 452:

```
    case IDM_EDIT_SEARCHONINTERNET:
    {
[...]
      if (nppGui._searchEngineChoice == nppGui.se_custom)
      {
[...]
        {
          url = nppGui._searchEngineCustom.c_str();
        }
      }
[...]
      Command cmd(url.c_str());
      cmd.run(_pPublicInterface->getHSelf());  
```

In `PowerEditor\src\WinControls\StaticDialog\RunDlg\RunDlg.cpp`, line 169:

```
HINSTANCE Command::run(HWND hWnd)
{
[...]
    HINSTANCE res = ::ShellExecute(hWnd, TEXT("open"), cmd2Exec, args2Exec, TEXT("."), SW_SHOW);
```

`::ShellExecute` is called on arguments that can be controlled by malicious users, without any validation.

When a HTTP url is used as search engine, `ShellExecute` will see that the argument starts with "http://" or "https://" and open the default web browser. This is not guaranteed if the argument does not start with one of these two prefixes.

The `IDM_EDIT_SEARCHONINTERNET` code assumes that `url` is a well-formed HTTP url, but no checks are made to verify this. This makes it possible to pass arbitrary strings to `ShellExecute` and execute arbitrary commands for any actor that can modify the custom search engine.


## Steps To Reproduce:
In our proof of concept, we chose to open a calculator by providing `cmd.exe /c calc.exe` as custom search engine.

  1. Copy the provided `config.xml` file to `%APPDATA%\Notepad++`
  2. Run Notepad++
  3. Right-click anywhere in the text field
  4. Select "Search on Internet"

The default Windows calculator will open.

## Suggested fix
A possible fix is to check if the url actually starts with "http://" or "https://" when executing the "Search on Internet" function, before the `cmd.run` call.

This should guarantee that the default web browser will be opened instead of running arbitrary commands (NB: no filename can contain `:` or `/` on Windows).

## Supporting Material/References:

### Debug info of tested executables
The executables were downloaded from the nightly build at [https://ci.appveyor.com/project/donho/notepad-plus-plus](https://ci.appveyor.com/project/donho/notepad-plus-plus)

```
Notepad++ v7.6.3   (32-bit)
Build time : Feb 16 2019 - 23:07:35
Path : C:\Users\Pietro\Downloads\npp.7.6.3.bin.minimalist\notepad++.exe
Admin mode : OFF
Local Conf mode : ON
OS : Windows 10 (64-bit)
Plugins : none
```

```
Notepad++ v7.6.3   (64-bit)
Build time : Feb 17 2019 - 02:47:42
Path : C:\Users\Pietro\Downloads\npp.7.6.3.bin.minimalist64\notepad++.exe
Admin mode : OFF
Local Conf mode : ON
OS : Windows 10 (64-bit)
Plugins : none
```

## Impact

Since this is vulnerability can lead to arbitrary command execution, users risk complete loss of integrity, confidentiality and availability. An attacker may read, delete and modify any files that are accessible with the program's permission, and execute arbitrary code.

Users may be persuaded to use a custom config file, for instance if provided as a example config file on the Internet, or if the user believes it would solve a problem with the config they have.

Moreover, a malicious program running with the user's permissions may directly write to %APPDATA% and trigger the vulnerability.

## Attachments
- config.xml
