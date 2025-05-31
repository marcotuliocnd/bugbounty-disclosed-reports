# Linux Desktop application slack executable does not use pie / no ASLR

## Report Details
- **Report ID**: 415272
- **URL**: https://hackerone.com/reports/415272
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-27T12:33:08.436Z
- **Disclosed**: 2019-11-17T12:44:47.022Z

## Reporter
- **Username**: hanno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
The slack binary from the Linux desktop application is no position independent executable:

$ file usr/lib/slack/slack 
usr/lib/slack/slack: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, stripped

(pie executables report either "LSB shared object" or "LSB pie executable".)

Position independent executables are required for full ASLR support on Linux. Non-pie-binaries are loaded to a fixed location, thus allowing ROP attacks.

I'm aware that technically this is not a vulnerability, but a lack of a hardening feature. However given that ASLR is generally considered standard practice these days and that lack of it can mean very simple bugs can directly lead to code execution I think it deserves to be fixed.

## Impact

A simple memory corruption bug like a buffer overflow can easily lead to a remote code execution bug. With ASLR these bugs are much harder and sometimes impossible to exploit.

## Attachments
No attachments
