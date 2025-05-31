# Invalid read in `str_replace_partial`

## Report Details
- **Report ID**: 633607
- **URL**: https://hackerone.com/reports/633607
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-07-02T06:34:49.653Z
- **Disclosed**: 2019-09-04T13:34:59.341Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
===
The attached POC shows an invalid read.

Debug info
==========
The issue happens when `memmove` is called inside `str_replace_partial`.

valgrind report:

```
0==27051== Invalid read of size 1
==27051==    at 0x483FA10: memmove (vg_replace_strmem.c:1270)
==27051==    by 0x135D60: str_replace_partial (string.c:1193)
==27051==    by 0x1359CB: mrb_str_aset (string.c:1226)
==27051==    by 0x131AE8: mrb_str_aset_m (string.c:1255)
==27051==    by 0x1656FE: mrb_f_send (vm.c:633)
==27051==    by 0x169C3E: mrb_vm_exec (vm.c:1441)
==27051==    by 0x166540: mrb_vm_run (vm.c:949)
==27051==    by 0x17A5C7: mrb_top_run (vm.c:2837)
==27051==    by 0x153113: mrb_load_exec (parse.y:6318)
==27051==    by 0x1533E6: mrb_load_file_cxt (parse.y:6327)
==27051==    by 0x10DC3C: main (mruby.c:270)
==27051==  Address 0x4da9370 is 176 bytes inside an unallocated block of size 2,796,832 in arena "client"
```

git bisect shows the issue was introduced in [0d452073](https://github.com/mruby/mruby/commit/0d452073f46fc46496200db610ce785e514cdb65).

Test platform
=============
* Arch Linux

Thank you,
Dinko Galetic
Denis Kasak

## Impact

Potential information disclosure.

## Attachments
- poc
