# nordvpn Linux Desktop executable application does not use pie / no ASLR

## Report Details
- **Report ID**: 771977
- **URL**: https://hackerone.com/reports/771977
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-01-10T23:31:23.866Z
- **Disclosed**: 2020-02-21T11:20:31.572Z

## Reporter
- **Username**: x54xc3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
Summary:
The nordvpn Linux binary application is not compiled as position independent code or position independent Executable.

Steps To Reproduce:
POC:

$file /usr/bin/nordvpn 
/usr/bin/nordvpn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, Go BuildID=i37gHO0n9oYRfAq4FjCD/_uGbyIw1UD66CPoD8bU0/KLu22bljColDqQZw59EI/NXGrqgSqoGfuHTYig0f9, stripped

Note : PIE excutable show as "LSB shared object" or "LSB pie executable"

Position independent executables are required for full ASLR support on Linux. Non-pie-binaries are loaded to a fixed location, thus allowing ROP attacks.ASLR is generally considered standard practice these days and that lack of it can mean very simple bugs can directly lead to code execution.

## Impact

If malicious user can get to execute buffer overflow in the Nordvpn linux binary can result in remote code execution die to the lack of PIE, with ASLR in place these bugs are much harder and sometimes impossible to exploit.

## Attachments
- POC.png
