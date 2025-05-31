# Use of uninitialized memory in unserialize()

## Report Details
- **Report ID**: 195950
- **URL**: https://hackerone.com/reports/195950
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-05T11:24:39.937Z
- **Disclosed**: 2017-06-01T18:41:51.251Z

## Reporter
- **Username**: rc0r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The following is a copy of the bug report at https://bugs.php.net/bug.php?id=73832

# Description

There was found a bug showing that PHP uses uninitialized memory during
calls to `unserialize()`. As the following report shows, the payload supplied
to `unserialize()` may control this uninitialized memory region and thus may
be used to trick PHP into operating on faked objects and calling attacker
controlled destructor function pointers. The supplied proof of concept exploit
practically demonstrates the issue by executing arbitrary code solely by
passing a specially crafted string to `unserialize()`. Even though this
particular demo exploit only works locally this flaw is very likely to also
allow for remote code execution.

This bug was found using `afl-fuzz` / `afl-utils`.


# Analysis

The following shows a short gdb dump of the flaw in a custom-built PHP (git
master on 40727d7ce9) with debugging symbols ([1], [2]):

    $ gdb ./sapi/cli/php
    gdb> r test.php payload.master
    [...]
    Fatal error: Possible integer overflow in memory allocation (2736264714 * 32 + 32) in test.php on line 6

    Program received signal SIGSEGV, Segmentation fault.
    gdb> i r
    rax            0x7ffff7fb673c	140737353836348
    rbx            0x3030303030303030	3472328296227680304
    rcx            0xf6d9	63193
    rdx            0x1cb8c30	30116912
    rsi            0x0	0
    rdi            0x3030303030303030	3472328296227680304
    rbp            0x30303030	0x30303030
    rsp            0x7fffffffc080	0x7fffffffc080
    r8             0x7ffff7fb6740	140737353836352
    r9             0x1cb4d00	30100736
    r10            0xeb	235
    r11            0x206	518
    r12            0x1c96ad8	29977304
    r13            0x30303030	808464432
    r14            0x7ffff167be00	140737243495936
    r15            0x3030303030303030	3472328296227680304         << !!!
    rip            0x10b63d7	0x10b63d7 <zend_hash_destroy+327>
    eflags         0x10202	[ IF RF ]
    cs             0x33	51
    ss             0x2b	43
    ds             0x0	0
    es             0x0	0
    fs             0x0	0
    gs             0x0	0
    gdb> x/i $rip
    => 0x10b63d7 <zend_hash_destroy+327>:	callq  *%r15
    gdb> bt
    #0  0x00000000010b63d7 in zend_hash_destroy (ht=<optimized out>) at Zend/zend_hash.c:1233
    #1  0x00000000010b7914 in zend_array_destroy (ht=0x7ffff167be00) at Zend/zend_hash.c:1293
    #2  0x000000000106f59e in _zval_dtor_func (p=0x7ffff167be00) at Zend/zend_variables.c:43
    #3  0x00000000010b708e in i_zval_ptr_dtor (zval_ptr=<optimized out>) at Zend/zend_variables.h:49
    #4  zend_array_destroy (ht=<optimized out>) at Zend/zend_hash.c:1303
    #5  0x000000000106f59e in _zval_dtor_func (p=0x7ffff167bce8) at Zend/zend_variables.c:43
    #6  0x00000000010b708e in i_zval_ptr_dtor (zval_ptr=<optimized out>) at Zend/zend_variables.h:49
    #7  zend_array_destroy (ht=<optimized out>) at Zend/zend_hash.c:1303
    [...]
    #83 0x000000000106f59e in _zval_dtor_func (p=0x7ffff1656540) at Zend/zend_variables.c:43
    #84 0x00000000010b708e in i_zval_ptr_dtor (zval_ptr=<optimized out>) at Zend/zend_variables.h:49
    #85 zend_array_destroy (ht=<optimized out>) at Zend/zend_hash.c:1303
    #86 0x000000000106f59e in _zval_dtor_func (p=0x7ffff1656428) at Zend/zend_variables.c:43
    #87 0x00000000010b7323 in i_zval_ptr_dtor (zval_ptr=<optimized out>) at Zend/zend_variables.h:49
    #88 zend_array_destroy (ht=<optimized out>) at Zend/zend_hash.c:1307
    #89 0x0000000001137a3d in zend_object_std_dtor (object=0x7ffff165c960) at Zend/zend_objects.c:60
    #90 0x0000000001147fdf in zend_objects_store_free_object_storage (objects=<optimized out>) at Zend/zend_objects_API.c:99
    #91 0x000000000103ce3b in shutdown_executor () at Zend/zend_execute_API.c:359
    #92 0x0000000001073599 in zend_deactivate () at Zend/zend.c:997
    #93 0x0000000000f27ff1 in php_request_shutdown (dummy=<optimized out>) at main/main.c:1873
    #94 0x0000000001355e25 in do_cli (argc=<optimized out>, argv=<optimized out>) at sapi/cli/php_cli.c:1161
    #95 0x00000000013533d5 in main (argc=<optimized out>, argv=<optimized out>) at sapi/cli/php_cli.c:1387

Some more in-depth debugging walk through follows:
 
    $ gdb ./sapi/cli/php
    gdb> b zend_hash_destroy
    gdb> ign 1 2
    gdb> r test.php payload.master
    gdb> p ht
    $6 = (HashTable *) 0x7ffff167be00
    gdb> p *ht
    $7 = {
      gc = {
        refcount = 0, 
        u = {
          v = {
            type = 1 '\001', 
            flags = 0 '\000', 
            gc_info = 32768
          }, 
          type_info = 2147483649
        }
      }, 
      u = {
        v = {
          flags = 18 '\022', 
          nApplyCount = 0 '\000', 
          nIteratorsCount = 0 '\000', 
          consistency = 0 '\000'
        }, 
        flags = 18
      }, 
      nTableMask = 808464432, 
      arData = 0x3030303030303030, 
      nNumUsed = 808464432, 
      nNumOfElements = 808464432, 
      nTableSize = 808464432, 
      nInternalPointer = 808464432, 
      nNextFreeElement = 3472328296227680304, 
      pDestructor = 0x3030303030303030
    }
    gdb> awatch *0x7ffff167be00
    gdb> dis 1
    gdb> r
    Hardware access (read/write) watchpoint 2: *0x7ffff167be00
    Value = 808464432
    0x00007ffff5103d44 in __memmove_sse2_unaligned_erms () from /usr/lib/libc.so.6
    gdb> x/20x 0x00007ffff167be00
    0x7ffff167be00:	0x30303030	0x30303030	0x30303030	0x30303030
    0x7ffff167be10:	0x30303030	0x30303030	0x30303030	0x30303030
    0x7ffff167be20:	0x30303030	0x30303030	0x30303030	0x30303030
    0x7ffff167be30:	0x30303030	0x30303030	0x30303030	0x30303030
    0x7ffff167be40:	0x30303030	0x30303030	0x30303030	0x30303030
    gdb> c // (multiple times)
    [...]
    Hardware access (read/write) watchpoint 2: *0x7ffff167be00

    Value = -244859336
    0x0000000000fdcacb in zend_mm_alloc_small (size=<optimized out>, heap=<optimized out>, bin_num=<optimized out>) at Zend/zend_alloc.c:1261
    1261			heap->free_slot[bin_num] = p->next_free_slot;
    >>> bt
    #0  0x0000000000fdcacb in zend_mm_alloc_small (size=<optimized out>, heap=<optimized out>, bin_num=<optimized out>) at Zend/zend_alloc.c:1261
    #1  _emalloc_56 () at Zend/zend_alloc.c:2336
    #2  0x000000000107f6f7 in _array_init (arg=0x7ffff16673c0, size=2736264714) at Zend/zend_API.c:1060
    #3  0x0000000000e23888 in php_var_unserialize_internal (rval=<optimized out>, p=<optimized out>, max=<optimized out>, var_hash=<optimized out>) at ext/standard/var_unserializer.re:788

From the above backtrace one can see PHP tries to allocate memory for a
`zend_array` of very large length corresponding to `a:9000111000000010:{...`
in `payload.master` ([2]).
This allocation fails a bit later because of an integer overflow in the size
parameter that is detected in `zend_hash_check_size()` called from
`_zend_hash_init()`. As soon as this overflow is detected, PHP starts to
shut down. At this point the contents of the partially initialized `zend_array`
look as follows:

    gdb> c
    Fatal error: Possible integer overflow in memory allocation (2736264714 * 32 + 32) in test.php on line 6
    Hardware access (read/write) watchpoint 2: *0x7ffff167be00

    Value = 1
    0x00000000010b6f6e in i_zval_ptr_dtor (zval_ptr=<optimized out>) at Zend/zend_variables.h:48
    48			if (!--GC_REFCOUNT(ref)) {
    gdb> x/16x 0x00007ffff167be00
    0x7ffff167be00:	0x00000001	0x00008007	0x00000012	0x30303030
    0x7ffff167be10:	0x30303030	0x30303030	0x30303030	0x30303030
    0x7ffff167be20:	0x30303030	0x30303030	0x30303030	0x30303030
    0x7ffff167be30:	0x30303030	0x30303030	0xf167be70	0x00007fff 

During shutdown PHP attempts to destroy its internal objects as well as the
corrupted array shown above. Therefore at some point the arrays own destructor
gets called from `zend_hash_destroy()` which was overwritten with user supplied
contents:
 
```c
ZEND_API void ZEND_FASTCALL zend_hash_destroy(HashTable *ht)
{
// ...
1231 				if (HT_IS_WITHOUT_HOLES(ht)) {
1232 					do {
1233 						ht->pDestructor(&p->val);
1234 					} while (++p != end);
1235 				} else {
// ...
```


# PoC

The following PoC exploit was developed for PHP 7.0.14 shipped with the
Archlinux (x64) distribution:

    $ uname -a
    Linux box01 4.8.13-1-ARCH #1 SMP PREEMPT Fri Dec 9 07:24:34 CET 2016 x86_64 GNU/Linux
    $ php --version
    PHP 7.0.14 (cli) (built: Dec  7 2016 17:11:27) ( NTS )
    Copyright (c) 1997-2016 The PHP Group
    Zend Engine v3.0.0, Copyright (c) 1998-2016 Zend Technologies

For the PoC `exploit.py` ([3]) to work you'll need the PHP test script
`test.php` ([1]) as well as the master payload file `payload.master` ([2])
to be placed in the same directory.
The PoC contains ROP gadgets for php-7.0.13-* and php-7.0.14 of Arch linux.
Uncomment them as needed.

    $ python exploit.py
    [............... <gnome-calculator pops open!> ......]

Upon success `gnome-calculator` should be executed. You may want to replace
`gnome-calculator` with sth. else like, f.e. `touch a` in `epxloit.py` in case
you want to test this without `gnome-calculator` present.


# References

[1](http://hlt99.blinkenshell.org/php/gfhd8763lkjdg3149nop1qyt/test.php)
[2](http://hlt99.blinkenshell.org/php/gfhd8763lkjdg3149nop1qyt/payload.master)
[3](http://hlt99.blinkenshell.org/php/gfhd8763lkjdg3149nop1qyt/exploit.py)


# PHP versions known to be affected

7.0.13 (Arch Linux)
7.0.13-* (Arch Linux)
7.0.14 (Arch Linux)
master on Github (as of commit 40727d7ce9)

Versions prior to 7.0.13 have not been tested.



# Reporters

rc0r <hlt99@blinkenshell.org>
Henri Salo from Nixu Corporation


# Thanks

A very big thank you goes to Kapsi internet-käyttäjät ry for providing
valuable fuzzing resources!

## Attachments
No attachments
