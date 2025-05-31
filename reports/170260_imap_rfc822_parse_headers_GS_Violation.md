# imap_rfc822_parse_headers GS Violation

## Report Details
- **Report ID**: 170260
- **URL**: https://hackerone.com/reports/170260
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-18T18:04:04.324Z
- **Disclosed**: 2019-10-31T06:16:25.047Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream issue
----
https://bugs.php.net/bug.php?id=72968

Description
-----
Exception when processing a long header string causes GS violation on Windows platform.

```
0:000:x86> r;!exploitable -v
eax=00000001 ebx=08a13020 ecx=00000007 edx=00000000 esi=00000003 edi=08a6116c
eip=5221468b esp=0712e408 ebp=0712e418 iopl=0         nv up ei pl nz na po nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000202
ucrtbase!abort+0x4b:
5221468b cd29            int     29h

!exploitable 1.6.0.0
HostMachine\HostUser
Executing Processor Architecture is x86
Debuggee is in User Mode
Debuggee is a live user mode debugging session on the local machine
Event Type: Exception
*** ERROR: Symbol file could not be found.  Defaulted to export symbols for C:\WINDOWS\SysWOW64\KERNEL32.DLL - 
*** ERROR: Symbol file could not be found.  Defaulted to export symbols for ntdll.dll - 
Exception Faulting Address: 0x5221468b
Second Chance Exception Type: STATUS_STACK_BUFFER_OVERRUN (0xC0000409)

Exception Hash (Major/Minor): 0x3eec876b.0x85eecc65

 Hash Usage : Stack Trace:
Major+Minor : ucrtbase!abort+0x4b
Major+Minor : php_imap!rfc822_parse_msg_full+0x14
Major+Minor : php_imap!zif_imap_rfc822_parse_headers+0x62
Major+Minor : php7!execute_ex+0xfb
Major+Minor : php7!zend_execute+0x124
Minor       : php7!zend_execute_scripts+0xe7
Minor       : php7!php_execute_script+0x372
Minor       : php!do_cli+0x3d3
Minor       : php!main+0x2cb
Minor       : php!__scrt_common_main_seh+0xf9
Minor       : KERNEL32!BaseThreadInitThunk+0x24
Excluded    : ntdll_776f0000!RtlInitializeExceptionChain+0x8f
Excluded    : ntdll_776f0000!RtlInitializeExceptionChain+0x5a
Instruction Address: 0x000000005221468b

Description: Stack Buffer Overrun (/GS Exception)
Short Description: GSViolation
Exploitability Classification: EXPLOITABLE
Recommended Bug Title: Exploitable - Stack Buffer Overrun (/GS Exception) starting at ucrtbase!abort+0x000000000000004b (Hash=0x3eec876b.0x85eecc65)

An overrun of a protected stack buffer has been detected. This is considered exploitable, and must be fixed.
```

Fixed in PHP 7.0.11 and PHP 5.6.26
---
https://gist.github.com/anonymous/39b697c75a0502e091a1191f83029034
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php

## Attachments
No attachments
