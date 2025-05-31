# Node.js - DLL Hijacking on Windows

## Report Details
- **Report ID**: 1636566
- **URL**: https://hackerone.com/reports/1636566
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-07-14T08:46:21.726Z
- **Disclosed**: 2022-07-25T18:30:17.800Z

## Reporter
- **Username**: yakirka
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Full Node.js Security Releases  - summarizing the issue is here:https://nodejs.org/en/blog/vulnerability/july-2022-security-releases/
The original Node.js HackerOne report is here: https://hackerone.com/bugs?report_id=1447455

-----

Node.js versions earlier than 16.16.0 (LTS) and 14.20.0 are vulnerable to dynamic link library (DLL) hijacking.
Attackers can exploit this vulnerability to escalate their privileges and establish persistence in a target environment.
The vulnerability can also provide another way to embed malicious code into packages.

This vulnerability can be exploited if the victim has the following dependencies on Windows machine:
* OpenSSL has been installed or “C:\Program Files\Common Files\SSL\openssl.cnf” exists.

Whenever the above conditions are present, node.exe will search for providers.dll in the current user directory.
After that, node.exe will try to search for providers.dll by the DLL Search Order in Windows.

It is possible for an attacker to place the malicious file providers.dll under a variety of paths and exploit this vulnerability.
This was fixed in Node.js 16.16.0 and 14.20.0 versions.

## Impact

A locally unprivileged attacker could perform a local privilege escalation, also It is possible for an attacker to place the malicious file "providers.dll" under a variety of paths (or under any other custom name via changing "Providers=provider_sect" providers filed to other package name(
In addition, the attackers may upload packages containing malicious dlls which run on the victim's windows machine after they download them.
The victim will not see any interaction with the dll in package code, so if he doesn't analyze the dll and decides to install the package, then the code will run.

## Attachments
No attachments
