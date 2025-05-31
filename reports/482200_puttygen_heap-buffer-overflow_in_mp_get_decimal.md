# puttygen: heap-buffer-overflow in mp_get_decimal()

## Report Details
- **Report ID**: 482200
- **URL**: https://hackerone.com/reports/482200
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-18T14:24:06.666Z
- **Disclosed**: 2019-11-03T16:42:58.785Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: putty_h1c

## Vulnerability Information
**Summary:** 
After downloading `putty-0.70-2019-01-17.53747ad.tar.gz`, I compiled it on Debian 9 with Clang-8.0.0 and AddressSanitizer and while trying to extract a public key from a crafted key file, I triggered a heap-buffer-overflow in mp_get_decimal().

**Description:**
A buffer overflow condition exists when a program attempts to put more data in a buffer than it can hold or when a program attempts to put data in a memory area past a buffer. In this case, a buffer is a sequential section of memory allocated to contain anything from a character string to an array of integers. Writing outside the bounds of a block of allocated memory can corrupt data, crash the program, or cause the execution of malicious code.

## Steps To Reproduce:

1) Compile putty with Clang and ASan:
`CC=clang CXX=clang++ CFLAGS=-fsanitize=address CXXFLAGS=-fsanitize=address ./configure --without-gtk && make --j2`

2) Run puttygen and attempt to extract a public key from the crafted key file:
`./puttygen -L test0013.ppk`
```
==20118==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x602000000160 at pc 0x000000523b65 bp 0x7ffcaacb32f0 sp 0x7ffcaacb32e8
READ of size 8 at 0x602000000160 thread T0
    #0 0x523b64 in mp_get_decimal /root/putty-0.70-2019-01-17.53747ad/mpint.c:412:15
    #1 0x58c162 in ssh1_pubkey_str /root/putty-0.70-2019-01-17.53747ad/sshpubk.c:1363:12
    #2 0x58c162 in ssh1_write_pubkey /root/putty-0.70-2019-01-17.53747ad/sshpubk.c:1375
    #3 0x4f845d in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:970:17
    #4 0x7f39a807d2e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)
    #5 0x41db89 in _start (/root/putty-0.70-2019-01-17.53747ad/puttygen+0x41db89)

0x602000000160 is located 0 bytes to the right of 16-byte region [0x602000000150,0x602000000160)
allocated by thread T0 here:
    #0 0x4c6333 in malloc /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/compiler-rt/lib/asan/asan_malloc_linux.cc:146:3
    #1 0x51971d in safemalloc /root/putty-0.70-2019-01-17.53747ad/memory.c:23:6
    #2 0x521ebf in mp_make_sized /root/putty-0.70-2019-01-17.53747ad/mpint.c:38:17
    #3 0x521ebf in mp_get_decimal /root/putty-0.70-2019-01-17.53747ad/mpint.c:408
    #4 0x58c162 in ssh1_pubkey_str /root/putty-0.70-2019-01-17.53747ad/sshpubk.c:1363:12
    #5 0x58c162 in ssh1_write_pubkey /root/putty-0.70-2019-01-17.53747ad/sshpubk.c:1375
    #6 0x4f845d in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:970:17
    #7 0x7f39a807d2e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)

SUMMARY: AddressSanitizer: heap-buffer-overflow /root/putty-0.70-2019-01-17.53747ad/mpint.c:412:15 in mp_get_decimal
```

Valgrind reports the same on a non-ASan build:
```
==23803== Memcheck, a memory error detector
==23803== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==23803== Using Valgrind-3.12.0.SVN and LibVEX; rerun with -h for copyright info
==23803== Command: ./puttygen -L ../../putty-0.70-2019-01-17.53747ad/tmp/out/crashes/test0013.ppk
==23803==
==23803== Invalid read of size 8
==23803==    at 0x118B3F: mp_get_decimal (mpint.c:412)
==23803==    by 0x12C05A: ssh1_pubkey_str (sshpubk.c:1363)
==23803==    by 0x12C0E0: ssh1_write_pubkey (sshpubk.c:1375)
==23803==    by 0x10DFFB: main (cmdgen.c:970)
==23803==  Address 0x53de1b0 is 0 bytes after a block of size 16 alloc'd
==23803==    at 0x4C2BBAF: malloc (vg_replace_malloc.c:299)
==23803==    by 0x116727: safemalloc (memory.c:23)
==23803==    by 0x11725B: mp_make_sized (mpint.c:38)
==23803==    by 0x118B0F: mp_get_decimal (mpint.c:408)
==23803==    by 0x12C05A: ssh1_pubkey_str (sshpubk.c:1363)
==23803==    by 0x12C0E0: ssh1_write_pubkey (sshpubk.c:1375)
==23803==    by 0x10DFFB: main (cmdgen.c:970)
==23803==
==23803== Invalid read of size 8
==23803==    at 0x118B3F: mp_get_decimal (mpint.c:412)
==23803==    by 0x12C066: ssh1_pubkey_str (sshpubk.c:1364)
==23803==    by 0x12C0E0: ssh1_write_pubkey (sshpubk.c:1375)
==23803==    by 0x10DFFB: main (cmdgen.c:970)
==23803==  Address 0x53de390 is 0 bytes after a block of size 16 alloc'd
==23803==    at 0x4C2BBAF: malloc (vg_replace_malloc.c:299)
==23803==    by 0x116727: safemalloc (memory.c:23)
==23803==    by 0x11725B: mp_make_sized (mpint.c:38)
==23803==    by 0x118B0F: mp_get_decimal (mpint.c:408)
==23803==    by 0x12C066: ssh1_pubkey_str (sshpubk.c:1364)
==23803==    by 0x12C0E0: ssh1_write_pubkey (sshpubk.c:1375)
==23803==    by 0x10DFFB: main (cmdgen.c:970)
==23803==
0 0 0   -<-    >
==23803== Invalid free() / delete / delete[] / realloc()
==23803==    at 0x4C2CDDB: free (vg_replace_malloc.c:530)
==23803==    by 0x12DCE2: freersakey (sshrsa.c:379)
==23803==    by 0x10D62D: main (cmdgen.c:1068)
==23803==  Address 0x53de010 is 0 bytes inside a block of size 11 free'd
==23803==    at 0x4C2CDDB: free (vg_replace_malloc.c:530)
==23803==    by 0x10D625: main (cmdgen.c:1067)
==23803==  Block was alloc'd at
==23803==    at 0x4C2BBAF: malloc (vg_replace_malloc.c:299)
==23803==    by 0x116727: safemalloc (memory.c:23)
==23803==    by 0x1365FD: dupstr (utils.c:235)
==23803==    by 0x10DBBF: main (cmdgen.c:790)
==23803==
==23803==
==23803== HEAP SUMMARY:
==23803==     in use at exit: 156 bytes in 4 blocks
==23803==   total heap usage: 33 allocs, 30 frees, 12,856 bytes allocated
==23803==
==23803== LEAK SUMMARY:
==23803==    definitely lost: 91 bytes in 3 blocks
==23803==    indirectly lost: 65 bytes in 1 blocks
==23803==      possibly lost: 0 bytes in 0 blocks
==23803==    still reachable: 0 bytes in 0 blocks
==23803==         suppressed: 0 bytes in 0 blocks
==23803== Rerun with --leak-check=full to see details of leaked memory
==23803==
==23803== For counts of detected and suppressed errors, rerun with: -v
==23803== ERROR SUMMARY: 5 errors from 3 contexts (suppressed: 0 from 0)
```

## Impact

1) Buffer overflows generally lead to crashes. Other attacks leading to lack of availability are possible, including putting the program into an infinite loop.

2) Buffer overflows often can be used to execute arbitrary code, which is usually outside the scope of a program’s implicit security policy.

3) When the consequence is arbitrary code execution, this can often be used to subvert any other security service.

## Attachments
- test0013.ppk.gz
