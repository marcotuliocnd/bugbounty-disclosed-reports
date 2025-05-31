# A stack buffer overflow in BabyGrid.cpp can lead to program crashes via a malicious localization file

## Report Details
- **Report ID**: 497255
- **URL**: https://hackerone.com/reports/497255
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-17T11:52:01.984Z
- **Disclosed**: 2019-05-07T22:45:59.211Z

## Reporter
- **Username**: peter_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: notepad-plus-plus

## Vulnerability Information
**Summary:** A stack buffer overflow in BabyGrid.cpp can lead to program crashes via a malicious localization file, when opening the Shortcut Mapper sub-menu

**Description:** Setting a very long `name` attribute for specific xml tags in the `nativeLang.xml` will trigger a stack buffer overflow, due to missing bound checks.

The `nativeLang.xml` file is an optional configuration file, as described in [http://docs.notepad-plus-plus.org/index.php/Configuration_Files](http://docs.notepad-plus-plus.org/index.php/Configuration_Files), [http://docs.notepad-plus-plus.org/index.php/Localisation](http://docs.notepad-plus-plus.org/index.php/Localisation), [https://notepad-plus-plus.org/contribute/binary-translation-howto.html](https://notepad-plus-plus.org/contribute/binary-translation-howto.html). `nativeLang.xml` lets users change the localization language of Notepad++, by providing alternative translations for every visible string in the GUI.

In the `nativeLang.xml` file, in the `ShortcutMapper` tag,
the `name` attribute of any of the following children is vulnerable:

* `ColumnName`
* `ColumnShortcut`
* `ColumnCategory`
* `ColumnPlugin`

The overflow is triggered with:

* a `name` with more than ~1000 characters on the 32-bit program
* a `name` with more than ~2000 characters on the 64-bit program

See the attached proofs of concept as an example.

The cause of the overflow is the usage of the unsafe `lstrcat` and `lstrcpy` functions without any bounds checks.

## Vulnerability #1
In `PowerEditor/src/WinControls/Grid/BabyGrid.cpp`, line 1671:

```
    lstrcat(buffer, (TCHAR*)lParam);
```

`lstrcat` introduces an unbounded stack buffer overflow, by overrunning the 1000 bytes long buffer `buffer`.

`lParam` can be controlled and can be of arbitrary length, for example when loading localization strings.

Example of an execution trace triggering the vulnerability:

1. In `ShortcutMapper.cpp`, `ShortcutMapper::run_dlgProc`
2. In `ShortcutMapper.cpp`, `ShortcutMapper::fillOutBabyGrid`
	* `generic_string nameStr = nativeLangSpeaker->getShortcutMapperLangStr("ColumnName", TEXT("Name"));`
	* `_babygrid.setText(0, 1, nameStr.c_str());`
3. In `BabyGridWrapper.h`, `setText`
	* `		::SendMessage(_hSelf, BGM_SETCELLDATA, reinterpret_cast<WPARAM>(&cell), reinterpret_cast<LPARAM>(text));`
4. In `BabyGrid.cpp`, `GridProc`
	* `lstrcat(buffer, (TCHAR*)lParam);` (line 1669)

## Vulnerability #2
If vulnerability #1 is fixed, a second vulnerability will still allow a very similar stack buffer overflow.

In `PowerEditor/src/WinControls/Grid/BabyGrid.cpp`, line 1308:

```
    lstrcpy(temptext,text);
```

`lstrcpy` introduces an unbounded stack buffer overflow, by overrunning the 1000 bytes long buffer `temptext`.

`text` can be controlled and can be of arbitrary length, for example when loading localization strings.

Example of an execution trace triggering the vulnerability:

1. In `ShortcutMapper.cpp`, `ShortcutMapper::run_dlgProc`
2. In `ShortcutMapper.cpp`, `ShortcutMapper::fillOutBabyGrid`
	* `generic_string nameStr = nativeLangSpeaker->getShortcutMapperLangStr("ColumnName", TEXT("Name"));`
	* `_babygrid.setText(0, 1, nameStr.c_str());`
3. In `BabyGridWrapper.h`, `setText`
	* `		::SendMessage(_hSelf, BGM_SETCELLDATA, reinterpret_cast<WPARAM>(&cell), reinterpret_cast<LPARAM>(text));`
4. In `BabyGrid.cpp`, `GridProc`
	* `longestline=FindLongestLine(hdc,(TCHAR*)lParam,&size);` (line 1726)
5. In `BabyGrid.cpp`, `FindLongestLine`
	* `lstrcpy(temptext,text);` (line 1306)


## Steps To Reproduce:

1. Install the 32-bit version of Notepad++
2. Copy `nativeLang.xml` to the `%APPDATA%\Notepad++` folder (or to the Notepad++ installation folder)
3. Run Notepad++
4. Open the "Settings" > "Shortcut Mapper" menu

Notepad++ will crash.

### Alternative steps
The PoC can be reproduced in the same way on the 64-bit version by using one of the provided .xml files ending with `-64` (remember to rename them to `nativeLang.xml`).

All of the attached files, when renamed to `nativeLang.xml` and moved to the `%APPDATA%\Notepad++` folder, will trigger a crash.

The `nativeLang-4` version of the PoC needs an additional step: after opening the Shortcut Mapper, move to the "Plugin" tab.

## Suggested fix

* Add `strsafe.h` as header

* In `PowerEditor/src/WinControls/Grid/BabyGrid.cpp`, line 1671

```diff
-    lstrcat(buffer, (TCHAR*)lParam);
+    StringCchCat(buffer, 1000, (TCHAR*)lParam);
```

* In `PowerEditor/src/WinControls/Grid/BabyGrid.cpp`, line 1308

```diff
-    lstrcpy(temptext,text);
+    StringCchCopy(temptext, 1000, text);
```

`strcat` and `strcpy` are fundamentally unsafe, due to the lack of bounds checking. Consider replacing all occurrences with safer alternatives like `StringCchCat` and `StringCchCopy`.

## Supporting Material/References:

### Debug info of tested executables
The executables were downloaded from the nightly build at https://ci.appveyor.com/project/donho/notepad-plus-plus

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

Any user who is using one of these malicious localization files will experience crashes when using the "Shortcut Mapper" menu.

This may cause:

* Loss of unsaved data when the program crashes (if the interval between automatic file backups is too long or automatic backups are disabled)
* No access to the Shortcut Mapper, making it impossible to change shortcuts

Users may be persuaded to install a custom localization file, for instance by looking for a translation for a language that is not supported yet, or by believing that a particular translation is better than the official one.

Moreover, a malicious program running with the user's permission may directly write to %APPDATA% and trigger the vulnerability.

Since this exploit is read from a file and therefore not dynamic, exploitation to code execution looks impossible due to the presence of the stack cookie and ASLR.

## Attachments
- nativeLang-1.xml
- nativeLang.xml
- nativeLang-1-64.xml
- nativeLang-2-64.xml
- nativeLang-2.xml
- nativeLang-3-64.xml
- nativeLang-3.xml
- nativeLang-4.xml
- nativeLang-4-64.xml
