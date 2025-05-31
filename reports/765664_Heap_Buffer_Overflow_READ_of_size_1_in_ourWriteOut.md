# Heap Buffer Overflow (READ of size 1) in ourWriteOut

## Report Details
- **Report ID**: 765664
- **URL**: https://hackerone.com/reports/765664
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-29T05:53:26.416Z
- **Disclosed**: 2021-01-08T15:08:01.810Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Whilst fuzzing the curl command line tool (built from commit 779b415) with AFL, ASAN and libdislocator, a heap buffer overflow was triggered when a crafted curl configuration file was loaded.

## Steps To Reproduce:
`echo "LXdAAAou" | base64 -d > test0070.conf`
`./curl -q -K test0070.conf file:///dev/null`

```
==1162==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x615000000a00 at pc 0x00000058fa99 bp 0x7ffd004d37d0 sp 0x7ffd004d37c8
READ of size 1 at 0x615000000a00 thread T0
    #0 0x58fa98 in ourWriteOut /root/curl/build-afl/src/../../src/tool_writeout.c:119:16
    #1 0x527643 in post_per_transfer /root/curl/build-afl/src/../../src/tool_operate.c:620:5
    #2 0x5233a2 in serial_transfers /root/curl/build-afl/src/../../src/tool_operate.c:2201:14
    #3 0x5233a2 in run_all_transfers /root/curl/build-afl/src/../../src/tool_operate.c:2372:16
    #4 0x521e67 in operate /root/curl/build-afl/src/../../src/tool_operate.c:2484:18
    #5 0x51eb29 in main /root/curl/build-afl/src/../../src/tool_main.c:314:14
    #6 0x7f3103a021e2 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x271e2)
    #7 0x41c61d in _start (/root/curl/build-afl/src/curl+0x41c61d)

0x615000000a00 is located 0 bytes to the right of 512-byte region [0x615000000800,0x615000000a00)
allocated by thread T0 here:
    #0 0x49451d in malloc (/root/curl/build-afl/src/curl+0x49451d)
    #1 0x55557b in file2string /root/curl/build-afl/src/../../src/tool_paramhlp.c:68:14
    #2 0x4fb6df in getparameter /root/curl/build-afl/src/../../src/tool_getparam.c:2112:15
    #3 0x5620b2 in parseconfig /root/curl/build-afl/src/../../src/tool_parsecfg.c:235:13
    #4 0x4f87b1 in getparameter /root/curl/build-afl/src/../../src/tool_getparam.c:1826:10
    #5 0x514890 in parse_args /root/curl/build-afl/src/../../src/tool_getparam.c:2245:18
    #6 0x5218bb in operate /root/curl/build-afl/src/../../src/tool_operate.c:2423:26

SUMMARY: AddressSanitizer: heap-buffer-overflow /root/curl/build-afl/src/../../src/tool_writeout.c:119:16 in ourWriteOut
```

## Supporting Material/References:
```
curl 7.68.0-DEV (x86_64-pc-linux-gnu) libcurl/7.68.0-DEV zlib/1.2.11
Release-Date: [unreleased]
Protocols: dict file ftp gopher http imap pop3 rtsp smtp telnet tftp
Features: AsynchDNS IPv6 Largefile libz UnixSockets
```

## Impact

Application crash plus other as yet undetermined consequences

## Attachments
No attachments
