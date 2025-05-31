# Race condition (TOCTOU) in NordVPN can result in local privilege escalation

## Report Details
- **Report ID**: 768110
- **URL**: https://hackerone.com/reports/768110
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-04T14:03:38.368Z
- **Disclosed**: 2020-02-21T11:37:04.545Z

## Reporter
- **Username**: hexgold
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
## Summary:
A vulnerability exists in the NordVPN service, which is installed as part of the NordVPN Windows app. By exploiting a race condition in the NordVPN service it is possible to launch OpenVPN with a user-supplied configuration file. By setting an OpenSSL engine name within this configuration file, it is possible to cause OpenVPN to load an arbitrary DLL. The NordVPN service is running with SYSTEM privileges and is responsible for starting the OpenVPN process. Consequently, the code in the attacker's DLL will also run with SYSTEM privileges.

This issue exists because it is possible to pass the NordVPN service an arbitrary path via the `DomainName` parameter. The service will use the domain name to construct a path to the location of a OpenVPN configuration file. The configuration file is validated before starting OpenVPN. If the path is controlled by a local attacker it is possible to trigger a race condition. In the time after the validation of the NordVPN service and before starting OpenVPN, it is possible to switch the validated configuration with a different one containing configuration options that are normally not allowed.

## Steps To Reproduce:
Attached PowerShell Module can be used to exploit this issue. Example usage:

```
Import-Module .\Invoke-ExploitNordVPNConfigLPE.psd1
Invoke-ExploitNordVPNConfigLPE "net user backdoor P@ssword /add" "net localgroup administrators backdoor /add"## Supporting 
```

## Vulnerability details:
NordVPN 6.26.8.0 mitigates a different local privilege escalation vulnerability by removing the `engine` option from the whitelist with allowed OpenVPN options. No validation of the `ServerDomain` parameter of the `VpnConnectionProxy` WCF model was added to prevent the loading of OpenVPN configuration files from arbitrary locations.

A time-of-check-time-of-use (TOCTOU) race condition exists in the way OpenVPN configuration files are validated/used. First the NordVPN service will validate the OpenVPN configuration that is located at the path that is constructed using the `ServerDomain` parameter. If the configuration file is valid, OpenVPN is launched with the same path. In the time between the validation and launching, the configuration file can be swapped for another one, and OpenVPN will used that file instead of the one that was validated by the NordVPN service.

NTFS [opportunistic locks](https://docs.microsoft.com/en-us/windows/win32/fileio/opportunistic-locks) can be used to exploit this issue by detecting that a process is accessing a certain file. When this occurs, the file can be swapped for another file. The second read will thus return different content. The [BaitAndSwitch](https://github.com/googleprojectzero/symboliclink-testing-tools/releases) from [James Forshaw](https://twitter.com/tiraniddo) does exactly this and can be used to exploit this issue.

## Possible fix(es):
- Perform strict validation of the `ServerDomain` parameter.
- Copy the OpenVPN configuration file to a folder that is only accessible by the SYSTEM user. Give the configuration file a unique (random) name and validate it after the file has been copied. Start OpenVPN with the configuration file from this path.
- After constructing the path  with `Path.Combine()` validate if the path starts with the value of `PrebundledOpenVpnConfig.BundleDirectory()`.

## Impact

A local low privileged user can exploit this issue to run arbitrary code with LocalSystem privileges.

## Attachments
- Invoke-ExploitNordVPNConfigLPE.psd1
- Invoke-ExploitNordVPNConfigLPE.psm1
