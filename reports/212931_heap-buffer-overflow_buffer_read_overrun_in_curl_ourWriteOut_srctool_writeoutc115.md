# heap-buffer-overflow (buffer read overrun) in curl: ourWriteOut() src/tool_writeout.c:115

## Report Details
- **Report ID**: 212931
- **URL**: https://hackerone.com/reports/212931
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-03-12T20:54:30.887Z
- **Disclosed**: 2018-05-16T15:37:54.688Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Curl is a ubiquitous tool in use by millions of people around the world. I reported this flaw to the curl security mailing list on 10 March 2017:

```
./curl -q -K test000
==21754==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200000dbb2 at pc 0x0000004fcd39 bp 0x7ffcd27dc250 sp 0x7ffcd27dc248
READ of size 1 at 0x60200000dbb2 thread T0
    #0 0x4fcd38 in ourWriteOut /root/curl/src/tool_writeout.c:115:3
    #1 0x4ec947 in operate_do /root/curl/src/tool_operate.c:1669:11
    #2 0x4e053e in operate /root/curl/src/tool_operate.c:2024:20
    #3 0x4de5a6 in main /root/curl/src/tool_main.c:252:14
    #4 0x7fad0a96fb44 in __libc_start_main /build/glibc-qK83Be/glibc-2.19/csu/libc-start.c:287
    #5 0x4c407c in _start (/root/curl/src/curl+0x4c407c)

0x60200000dbb2 is located 0 bytes to the right of 2-byte region [0x60200000dbb0,0x60200000dbb2)
allocated by thread T0 here:
    #0 0x4a69fb in malloc (/root/curl/src/curl+0x4a69fb)
    #1 0x7fad0a9cf989 in __strdup /build/glibc-qK83Be/glibc-2.19/string/strdup.c:42

SUMMARY: AddressSanitizer: heap-buffer-overflow /root/curl/src/tool_writeout.c:115 ourWriteOut
```

Fixed by the developers on 12 March 2017:
https://github.com/curl/curl/commit/1890d59905414ab84a35892b2e45833654aa5c13

From the git commit:
```
If a % ended the statement, the string's trailing NUL would be skipped
and memory past the end of the buffer would be accessed and potentially
displayed as part of the --write-out output.
```
From the curl security mailing list:
```
It's possible that the data past the end of the buffer could get displayed as
part of the --write-out output (up to the first nul character, anyway), so
theoretically, it could write out a password or secret key or something.
```

## Attachments
No attachments
