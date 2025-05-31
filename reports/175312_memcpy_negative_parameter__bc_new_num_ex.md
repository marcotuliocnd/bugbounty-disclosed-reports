# memcpy negative parameter _bc_new_num_ex

## Report Details
- **Report ID**: 175312
- **URL**: https://hackerone.com/reports/175312
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-12T06:52:52.217Z
- **Disclosed**: 2017-02-07T17:56:49.047Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
https://bugs.php.net/bug.php?id=73190

Summary
--
When *scale* parameter value in \_bc_new_num_ex is large enough ( 0x7fffffff), memset function receive negative size parameter. 

Affected functions: *bcsub, bcadd , bcsqrt* ...

Source code:
https://github.com/php/php-src/blob/master/ext/bcmath/libbcmath/src/init.c#L47

```
bc_num _bc_new_num_ex (length, scale, persistent)
     int length, scale, persistent;
{
...
  temp->n_ptr = (char *) safe_pemalloc (1, length, scale, persistent);
  if (temp->n_ptr == NULL) bc_out_of_memory();
  temp->n_value = temp->n_ptr;
  memset (temp->n_ptr, 0, length+scale);     # 1 + 0x7fffffff = -2147483648
  return temp;
}
```

GDB output:
```
gdb -q --args /home/operac/build4/bin/php -n poc.php
No symbol table is loaded.  Use the "file" command.
Breakpoint 1 (__asan_report_error) pending.
Reading symbols from /home/operac/build4/bin/php...done.
gdb-peda$ b _bc_new_num_ex
Breakpoint 2 at 0x7de0a0: _bc_new_num_ex. (4 locations)
gdb-peda$ r
...
Breakpoint 3, _bc_new_num_ex (length=length@entry=0x1, scale=scale@entry=0x7fffffff, persistent=persistent@entry=0x0)
    at /home/operac/build4/php-src/ext/bcmath/libbcmath/src/init.c:72
72	  memset (temp->n_ptr, 0, length+scale);
gdb-peda$ p length
$1 = 0x1
gdb-peda$ p scale
$2 = 0x7fffffff
gdb-peda$ p length+scale
$3 = 0x80000000
gdb-peda$ p/d length+scale
$4 = -2147483648
gdb-peda$ b memset
...
Breakpoint 3, 0x00007ffff6ef6d10 in memset () from /usr/lib/x86_64-linux-gnu/libasan.so.2
gdb-peda$ p/d $rdx
$6 = -2147483648
gdb-peda$ p $rdx
$7 = 0xffffffff80000000
```

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=40e7baab3c90001beee4c8f0ed0ef79ad18ee0d6
```

Fixed for PHP 5.6.27, PHP 7.0.12
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php#7.0.12


## Attachments
No attachments
