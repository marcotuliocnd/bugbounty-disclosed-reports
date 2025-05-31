# Linux Desktop application "sifnoded" executable does not use Pie / no ASLR

## Report Details
- **Report ID**: 1188633
- **URL**: https://hackerone.com/reports/1188633
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-05-07T20:30:08.141Z
- **Disclosed**: 2021-12-09T19:48:57.448Z

## Reporter
- **Username**: dantt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hello Sifchain,
sifnoded binary from the Linux application is no position independent executable
PoC;
**$file sifnoded
Output will be like ;
███████

Position independent executables are required for full ASLR support on Linux. Non-pie-binaries are loaded to a fixed location, thus allowing ROP attacks.
Reference for this report; #415272
Thanks.

## Impact

A simple memory corruption bug like a buffer overflow can easily lead to a remote code execution bug. With ASLR these bugs are much harder and sometimes impossible to exploit.

LSB executable should be "LSB shared object" or "LSB pie executable"

## Attachments
No attachments
